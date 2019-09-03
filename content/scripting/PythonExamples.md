+++
title = "Python Examples"
published = true
weight = 40
+++

![]({{< relref "" >}}images/scripting/python-logo-master-v3-TM.png)

This pages is created based on the content in the **PythonExamples** folder located inside the **rips** module, made available online for convenience.

# AllCases

```
###################################################################################
# This example will connect to ResInsight, retrieve a list of cases and print info
# 
###################################################################################

# Import the ResInsight Processing Server Module
import rips

# Connect to ResInsight
resInsight  = rips.Instance.find()
if resInsight is not None:
    # Get a list of all cases
    cases = resInsight.project.cases()

    print ("Got " + str(len(cases)) + " cases: ")
    for case in cases:
        print("Case name: " + case.name)
        print("Case grid path: " + case.gridPath())
        
        timesteps = case.timeSteps()
        for t in timesteps:
            print("Year: " + str(t.year))
            print("Month: " + str(t.month))
        
    

```

# AppInfo

```
import rips

resInsight  = rips.Instance.find()
if resInsight is not None:
    print(resInsight.versionString())
    print("Is this a console run?", resInsight.isConsole())
```

# CaseGridGroup

```
import os
import rips

resInsight  = rips.Instance.find()

casePaths = []
casePaths.append("C:/Users/lindk/source/repos/ResInsight/TestModels/Case_with_10_timesteps/Real0/BRUGGE_0000.EGRID")
casePaths.append("C:/Users/lindk/source/repos/ResInsight/TestModels/Case_with_10_timesteps/Real10/BRUGGE_0010.EGRID")
for casePath in casePaths:
    assert os.path.exists(casePath), "You need to set valid case paths for this script to work"

caseGroup = resInsight.project.createGridCaseGroup(casePaths=casePaths)

caseGroup.printObjectInfo()
    
#statCases = caseGroup.statisticsCases()
#caseIds = []
#for statCase in statCases:
#    statCase.setValue("DynamicPropertiesToCalculate", ["SWAT"])
#    statCase.update()
#    caseIds.append(statCase.getValue("CaseId"))

resInsight.commands.computeCaseGroupStatistics(caseGroupId=caseGroup.groupId)

view = caseGroup.views()[0]
cellResult = view.cellResult()
cellResult.setValue("ResultVariable", "PRESSURE_DEV")
cellResult.update()
        
```

# CaseInfoStreamingExample

```
###############################################################################
# This example will get the cell info for the active cells for the first case
###############################################################################

# Import the ResInsight Processing Server Module
import rips

# Connect to ResInsight
resInsight  = rips.Instance.find()

# Get the case with id == 0. This will fail if your project doesn't have a case with id == 0
case = resInsight.project.case(id = 0)

# Get the cell count object
cellCounts = case.cellCount()
print("Number of active cells: " + str(cellCounts.active_cell_count))
print("Total number of reservoir cells: " + str(cellCounts.reservoir_cell_count))

# Get information for all active cells
activeCellInfos = case.cellInfoForActiveCells()

# A simple check on the size of the cell info
assert(cellCounts.active_cell_count == len(activeCellInfos))

# Print information for the first active cell
print("First active cell: ")
print(activeCellInfos[0])
```

# CommandExample

```
###############################################################################
# This example will run a few ResInsight command file commands
# .. which are exposed in the Python interface.
# Including setting time step, window size and export snapshots and properties
###############################################################################
import os
import tempfile
import rips

# Load instance
resInsight = rips.Instance.find()

# Run a couple of commands
resInsight.commands.setTimeStep(caseId=0, timeStep=3)
resInsight.commands.setMainWindowSize(width=800, height=500)

# Create a temporary directory which will disappear at the end of this script
# If you want to keep the files, provide a good path name instead of tmpdirname
with tempfile.TemporaryDirectory(prefix="rips") as tmpdirname:
    print("Temporary folder: ", tmpdirname)
    
    # Set export folder for snapshots and properties
    resInsight.commands.setExportFolder(type='SNAPSHOTS', path=tmpdirname)
    resInsight.commands.setExportFolder(type='PROPERTIES', path=tmpdirname)
    
    # Export snapshots
    resInsight.commands.exportSnapshots()
    
    # Print contents of temporary folder
    print(os.listdir(tmpdirname))
    
    assert(len(os.listdir(tmpdirname)) > 0)
    case = resInsight.project.case(id=0)
    
    # Export properties in the view
    resInsight.commands.exportPropertyInViews(0, "3D View", 0)
    
    # Check that the exported file exists
    expectedFileName = case.name + "-" + str("3D_View") + "-" + "T3" + "-SOIL"
    fullPath = tmpdirname + "/" + expectedFileName
    assert(os.path.exists(fullPath))

```

# ErrorHandling

```
###################################################################
# This example demonstrates the use of ResInsight exceptions 
# for proper error handling
###################################################################

import rips
import grpc

resInsight     = rips.Instance.find()

case = None

# Try loading a non-existing case. We should get a grpc.RpcError exception from the server
try:
    case = resInsight.project.loadCase("Nonsense")
except grpc.RpcError as e:
    print("Expected Server Exception Received: ", e)

case = resInsight.project.case(id=0)
if case is not None:
    results = case.properties.activeCellProperty('STATIC_NATIVE', 'PORO', 0)
    activeCellCount = len(results)

    # Send the results back to ResInsight inside try / except construct
    try:        
        case.properties.setActiveCellProperty(results, 'GENERATED', 'POROAPPENDED', 0)
        print("Everything went well as expected")
    except: # Match any exception, but it should not happen
        print("Ooops!")

    # Add another value, so this is outside the bounds of the active cell result storage
    results.append(1.0)

    # This time we should get a grpc.RpcError exception, which is a server side error.
    try:        
        case.properties.setActiveCellProperty(results, 'GENERATED', 'POROAPPENDED', 0)
        print("Everything went well??")
    except grpc.RpcError as e:
        print("Expected Server Exception Received: ", e)
    except IndexError:
        print ("Got index out of bounds error. This shouldn't happen here")

    # With a chunk size exactly matching the active cell count the server will not
    # be able to see any error as it will successfully close the stream after receiving
    # the correct number of values, even if the python client has more chunks to send
    case.properties.chunkSize = activeCellCount

    try:        
        case.properties.setActiveCellProperty(results, 'GENERATED', 'POROAPPENDED', 0)
        print("Everything went well??")
    except grpc.RpcError as e:
        print("Got unexpected server exception", e, "This should not happen now")
    except IndexError:
        print ("Got expected index out of bounds error on client side")

        

```

# ExportSnapshots

```
############################################################################
# This script will export snapshots for two properties in every loaded case
# And put them in a snapshots folder in the same folder as the case grid
############################################################################
import os
import rips

# Load instance
resInsight = rips.Instance.find()
cases = resInsight.project.cases()

# Set main window size
resInsight.commands.setMainWindowSize(width=800, height=500)

n = 5                            # every n-th timestep for snapshot
property_list = ['SOIL', 'PRESSURE'] # list of parameter for snapshot

print ("Looping through cases")
for case in cases:
    # Get grid path and its folder name
    casepath = case.gridPath()
    foldername = os.path.dirname(casepath)
    
    # create a folder to hold the snapshots
    dirname = os.path.join(foldername, 'snapshots')
        
    if os.path.exists(dirname) is False:
        os.mkdir(dirname)
    
    print ("Exporting to folder: " + dirname)
    resInsight.commands.setExportFolder(type='SNAPSHOTS', path=dirname)
   
    timeSteps = case.timeSteps()
    tss_snapshot = range(0, len(timeSteps), n)
    print(case.name, case.id, 'Number of timesteps: ' + str(len(timeSteps)))
    print('Number of timesteps for snapshoting: ' + str(len(tss_snapshot)))
        
    view = case.views()[0]
    for property in property_list:
        view.applyCellResult(resultType='DYNAMIC_NATIVE', resultVariable=property)
        for ts_snapshot in tss_snapshot:
            resInsight.commands.setTimeStep(caseId = case.id, timeStep = ts_snapshot)        
            resInsight.commands.exportSnapshots(type='VIEWS', caseId=case.id)  # ‘ALL’, ‘VIEWS’ or ‘PLOTS’ default is 'ALL'
```

# GridInformation

```
######################################################################################
# This example prints information about the grids of all cases in the current project
######################################################################################

import rips

resInsight  = rips.Instance.find()

cases = resInsight.project.cases()
print("Number of cases found: ", len(cases))
for case in cases:
    print(case.name)
    grids = case.grids()
    print("Number of grids: ", len(grids))
    for grid in grids:
        print("Grid dimensions: ", grid.dimensions())



```

# InputPropTestAsync

```
########################################################################################
# This example generates a derived property in an asynchronous manner
# Meaning it does not wait for all the data for each stage to be read before proceeding
########################################################################################
import rips
import time

# Internal function for creating a result from a small chunk of poro and permx results
# The return value of the function is a generator for the results rather than the result itself.
def createResult(poroChunks, permxChunks):
    # Loop through all the chunks of poro and permx in order
    for (poroChunk, permxChunk) in zip(poroChunks, permxChunks):
        resultChunk = []
        # Loop through all the values inside the chunks, in order
        for (poro, permx) in zip(poroChunk.values, permxChunk.values):
            resultChunk.append(poro * permx)
        # Return a generator object that behaves like a Python iterator
        yield resultChunk

resInsight     = rips.Instance.find()
start = time.time()
case = resInsight.project.case(id=0)

# Get a generator for the poro results. The generator will provide a chunk each time it is iterated
poroChunks = case.properties.activeCellPropertyAsync('STATIC_NATIVE', 'PORO', 0)
# Get a generator for the permx results. The generator will provide a chunk each time it is iterated
permxChunks = case.properties.activeCellPropertyAsync('STATIC_NATIVE', 'PERMX', 0)

# Send back the result with the result provided by a generator object.
# Iterating the result generator will cause the script to read from the poro and permx generators
# And return the result of each iteration
case.properties.setActiveCellPropertyAsync(createResult(poroChunks, permxChunks),
                                           'GENERATED', 'POROPERMXAS', 0)

end = time.time()
print("Time elapsed: ", end - start)
print("Transferred all results back")
view = case.views()[0].applyCellResult('GENERATED', 'POROPERMXAS')
```

# InputPropTestSync

```
########################################################################################
# This example generates a derived property in an synchronous manner
# Meaning it completes reading each result before calculating the derived result
# See InputPropTestAsync for how to do this asynchronously instead.
########################################################################################
import rips
import time
import grpc

resInsight     = rips.Instance.find()
start = time.time()
case = resInsight.project.case(id=0)

# Read poro result into list
poroResults = case.properties.activeCellProperty('STATIC_NATIVE', 'PORO', 0)
# Read permx result into list
permxResults = case.properties.activeCellProperty('STATIC_NATIVE', 'PERMX', 0)

# Generate output result
results = []
for (poro, permx) in zip(poroResults, permxResults):
    results.append(poro * permx)

try:
    # Send back output result
    case.properties.setActiveCellProperty(results, 'GENERATED', 'POROPERMXSY', 0)
except grpc.RpcError as e:
    print("Exception Received: ", e)


end = time.time()
print("Time elapsed: ", end - start)
print("Transferred all results back")

view = case.views()[0].applyCellResult('GENERATED', 'POROPERMXSY')
```

# InstanceExample

```
#######################################
# This example connects to ResInsight
#######################################
import rips

resInsight  = rips.Instance.find()

if resInsight is None:
    print('ERROR: could not find ResInsight')
else:
	print('Successfully connected to ResInsight')
```

# LaunchWithCommandLineOptions

```
# Load ResInsight Processing Server Client Library
import rips
# Launch ResInsight with last project file and a Window size of 600x1000 pixels
resInsight = rips.Instance.launch(commandLineParameters=['--last', '--size', 600, 1000])
# Get a list of all cases
cases = resInsight.project.cases()

print ("Got " + str(len(cases)) + " cases: ")
for case in cases:
    print("Case name: " + case.name)
    print("Case grid path: " + case.gridPath())
```

# SelectedCases

```
############################################################################
# This example returns the currently selected cases in ResInsight
# Because running this script in the GUI takes away the selection
# This script does not run successfully from within the ResInsight GUI
# And will need to be run from the command line separately from ResInsight
############################################################################

import rips

resInsight  = rips.Instance.find()
if resInsight is not None:
    cases = resInsight.project.selectedCases()

    print ("Got " + str(len(cases)) + " cases: ")
    for case in cases:
        print(case.name)
        for property in case.properties.available('DYNAMIC_NATIVE'):
            print(property)


```

# SetCellResult

```
######################################################################
# This script applies a cell result to the first view in the project
######################################################################
import rips

resInsight  = rips.Instance.find()

view = resInsight.project.view(0)
view.applyCellResult(resultType='STATIC_NATIVE', resultVariable='DX')
```

# SetFlowDiagnosticsResult

```
######################################################################
# This script applies a flow diagnostics cell result to the first view in the project
######################################################################

# Load ResInsight Processing Server Client Library
import rips
# Connect to ResInsight instance
resInsight = rips.Instance.find()

view = resInsight.project.view(0)
#view.applyFlowDiagnosticsCellResult(resultVariable='Fraction',
#                                    selectionMode='FLOW_TR_INJ_AND_PROD')
                                    
# Example of setting individual wells. Commented out because well names are case specific.
view.applyFlowDiagnosticsCellResult(resultVariable='Fraction',
                                    selectionMode='FLOW_TR_BY_SELECTION',
                                    injectors = ['C-1H', 'C-2H', 'F-2H'],
                                    producers = ['B-1AH', 'B-3H', 'D-1H'])
```

# SetGridProperties

```
######################################################################
# This script sets values for SOIL for all grid cells in the first case in the project
######################################################################
import rips

resInsight     = rips.Instance.find()

case = resInsight.project.case(id=0)
totalCellCount = case.cellCount().reservoir_cell_count

values = []
for i in range(0, totalCellCount):
    values.append(i % 2 * 0.75);

print("Applying values to full grid")
case.properties.setGridProperty(values, 'DYNAMIC_NATIVE', 'SOIL', 0)

```

# SoilAverageAsync

```
###########################################################################################
# This example will asynchronously calculate the average value for SOIL for all time steps
###########################################################################################

import rips
import itertools
import time

resInsight     = rips.Instance.find()

start          = time.time()

# Get the case with case id 0
case           = resInsight.project.case(id=0)

# Get a list of all time steps
timeSteps      = case.timeSteps()

averages = []
for i in range(0, len(timeSteps)):
    # Get the results from time step i asynchronously
    # It actually returns a generator object almost immediately
	resultChunks = case.properties.activeCellPropertyAsync('DYNAMIC_NATIVE', 'SOIL', i)
	mysum = 0.0
	count = 0
    # Loop through and append the average. each time we loop resultChunks
    # We will trigger a read of the input data, meaning the script will start
    # Calculating averages before the whole resultValue for this time step has been received
	for chunk in resultChunks:
		mysum += sum(chunk.values)
		count += len(chunk.values)

	averages.append(mysum/count)

end = time.time()
print("Time elapsed: ", end - start)
print(averages)
```

# SoilAverageSync

```
###########################################################################################
# This example will synchronously calculate the average value for SOIL for all time steps
###########################################################################################
import rips
import itertools
import time

resInsight     = rips.Instance.find()

start          = time.time()
case           = resInsight.project.case(id=0)

# Get the case with case id 0
case           = resInsight.project.case(id=0)

# Get a list of all time steps
timeSteps      = case.timeSteps()

averages = []
for i in range(0, len(timeSteps)):
    # Get a list of all the results for time step i
	results = case.properties.activeCellProperty('DYNAMIC_NATIVE', 'SOIL', i)
	mysum = sum(results)
	averages.append(mysum/len(results))

end = time.time()
print("Time elapsed: ", end - start)
print(averages)
```

# SoilPorvAsync

```
##############################################################################
# This example will create a derived result for each time step asynchronously
##############################################################################

import rips
import time

# Internal function for creating a result from a small chunk of soil and porv results
# The return value of the function is a generator for the results rather than the result itself.
def createResult(soilChunks, porvChunks):
    for (soilChunk, porvChunk) in zip(soilChunks, porvChunks):
        resultChunk = []
        number = 0
        for (soilValue, porvValue) in zip(soilChunk.values, porvChunk.values):
            resultChunk.append(soilValue * porvValue)
        # Return a Python generator
        yield resultChunk

resInsight   = rips.Instance.find()
start        = time.time()
case         = resInsight.project.case(id=0)
timeStepInfo = case.timeSteps()

# Get a generator for the porv results. The generator will provide a chunk each time it is iterated
porvChunks   = case.properties.activeCellPropertyAsync('STATIC_NATIVE', 'PORV', 0)

# Read the static result into an array, so we don't have to transfer it for each iteration
# Note we use the async method even if we synchronise here, because we need the values chunked
# ... to match the soil chunks
porvArray = []
for porvChunk in porvChunks:
    porvArray.append(porvChunk)

for i in range (0, len(timeStepInfo)):
    # Get a generator object for the SOIL property for time step i
    soilChunks = case.properties.activeCellPropertyAsync('DYNAMIC_NATIVE', 'SOIL', i)
    # Create the generator object for the SOIL * PORV derived result
    result_generator = createResult(soilChunks, iter(porvArray))
    # Send back the result asynchronously with a generator object
    case.properties.setActiveCellPropertyAsync(result_generator, 'GENERATED', 'SOILPORVAsync', i)

end = time.time()
print("Time elapsed: ", end - start)
        
print("Transferred all results back")

view = case.views()[0].applyCellResult('GENERATED', 'SOILPORVAsync')
```

# SoilPorvSync

```
##############################################################################
# This example will create a derived result for each time step synchronously
##############################################################################

import rips
import time

resInsight = rips.Instance.find()
start = time.time()
case       = resInsight.project.case(id=0)

# Read the full porv result
porvResults = case.properties.activeCellProperty('STATIC_NATIVE', 'PORV', 0)
timeStepInfo = case.timeSteps()

for i in range (0, len(timeStepInfo)):
    # Read the full SOIl result for time step i
    soilResults = case.properties.activeCellProperty('DYNAMIC_NATIVE', 'SOIL', i)
    
    # Generate the result by looping through both lists in order
    results = []
    for (soil, porv) in zip(soilResults, porvResults):
        results.append(soil * porv)

    # Send back result
    case.properties.setActiveCellProperty(results, 'GENERATED', 'SOILPORVSync', i)

end = time.time()
print("Time elapsed: ", end - start)

print("Transferred all results back")

view = case.views()[0].applyCellResult('GENERATED', 'SOILPORVSync')
```

# ViewExample

```
#############################################################
# This example will alter the views of all cases
# By setting the background color and toggle the grid box
# Also clones the first view
#############################################################
import rips
# Connect to ResInsight instance
resInsight = rips.Instance.find()

# Check if connection worked
if resInsight is not None:
    # Get a list of all cases
    cases = resInsight.project.cases()
    for case in cases:
        # Get a list of all views
        views = case.views()
        for view in views:
            # Set some parameters for the view
            view.setShowGridBox(not view.showGridBox())
            view.setBackgroundColor("#3388AA")            
            # Update the view in ResInsight
            view.update()
        # Clone the first view
        newView = views[0].clone()
        view.setShowGridBox(False)
        newView.setBackgroundColor("#FFAA33")
        newView.update()
```
