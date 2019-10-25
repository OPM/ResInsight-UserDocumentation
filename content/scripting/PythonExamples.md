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
resinsight  = rips.Instance.find()
if resinsight is not None:
    # Get a list of all cases
    cases = resinsight.project.cases()

    print ("Got " + str(len(cases)) + " cases: ")
    for case in cases:
        print("Case id: " + str(case.case_id))
        print("Case name: " + case.name)
        print("Case type: " + case.type)
        print("Case grid path: " + case.grid_path())
        
        timesteps = case.time_steps()
        for t in timesteps:
            print("Year: " + str(t.year))
            print("Month: " + str(t.month))
        
    

```

# CaseGridGroup

```
import os
import rips

resinsight  = rips.Instance.find()

case_paths = []
case_paths.append("C:/Users/lindk/source/repos/ResInsight/TestModels/Case_with_10_timesteps/Real0/BRUGGE_0000.EGRID")
case_paths.append("C:/Users/lindk/source/repos/ResInsight/TestModels/Case_with_10_timesteps/Real10/BRUGGE_0010.EGRID")
for case_path in case_paths:
    assert os.path.exists(case_path), "You need to set valid case paths for this script to work"

case_group = resinsight.project.create_grid_case_group(case_paths=case_paths)

case_group.print_object_info()
    
#stat_cases = caseGroup.statistics_cases()
#case_ids = []
#for stat_case in stat_cases:
#    stat_case.set_value("DynamicPropertiesToCalculate", ["SWAT"])
#    stat_case.update()
#    case_ids.append(stat_case.get_value("CaseId"))

case_group.compute_statistics()

view = case_group.views()[0]
cell_result = view.set_cell_result()
cell_result.set_value("ResultVariable", "PRESSURE_DEV")
cell_result.update()
        
```

# CaseInfoStreamingExample

```
###############################################################################
# This example will get the cell info for the active cells for the first case
###############################################################################

# Import the ResInsight Processing Server Module
import rips

# Connect to ResInsight
resinsight  = rips.Instance.find()

# Get the case with id == 0. This will fail if your project doesn't have a case with id == 0
case = resinsight.project.case(case_id=0)

# Get the cell count object
cell_counts = case.cell_count()
print("Number of active cells: " + str(cell_counts.active_cell_count))
print("Total number of reservoir cells: " + str(cell_counts.reservoir_cell_count))

# Get information for all active cells
active_cell_infos = case.cell_info_for_active_cells()

# A simple check on the size of the cell info
assert(cell_counts.active_cell_count == len(active_cell_infos))

# Print information for the first active cell
print("First active cell: ")
print(active_cell_infos[0])
```

# CommandExample

```
###############################################################################
# This example will show setting time step, window size and export snapshots and properties
###############################################################################
import os
import tempfile
import rips

# Load instance
resinsight = rips.Instance.find()

# Set window sizes
resinsight.set_main_window_size(width=800, height=500)
resinsight.set_plot_window_size(width=1000, height=1000)


# Retrieve first case
case = resinsight.project.cases()[0]

# Get a view
view1 = case.view(view_id=0)

# Clone the view
view2 = view1.clone()

# Set the time step for view1 only
view1.set_time_step(time_step=2)

# Set cell result to SOIL
view1.apply_cell_result(result_type='DYNAMIC_NATIVE', result_variable='SOIL')


# Create a temporary directory which will disappear at the end of this script
# If you want to keep the files, provide a good path name instead of tmpdirname
with tempfile.TemporaryDirectory(prefix="rips") as tmpdirname:
    print("Temporary folder: ", tmpdirname)
    
    # Set export folder for snapshots and properties
    resinsight.set_export_folder(export_type='SNAPSHOTS', path=tmpdirname)
    resinsight.set_export_folder(export_type='PROPERTIES', path=tmpdirname)
    
    # Export all snapshots
    resinsight.project.export_snapshots()
        
    assert(len(os.listdir(tmpdirname)) > 0)
    
    # Export properties in the view
    view1.export_property()

    # Check that the exported file exists
    expected_file_name = case.name + "-" + str("3D_View") + "-" + "T2" + "-SOIL"
    full_path = tmpdirname + "/" + expected_file_name

    # Print contents of temporary folder
    print(os.listdir(tmpdirname))

    assert(os.path.exists(full_path))

```

# Create WBS Plot

```
import os
# Load ResInsight Processing Server Client Library
import rips
# Connect to ResInsight instance
resInsight = rips.Instance.find()

cases = resInsight.project.cases()

well_paths = resInsight.project.import_well_paths(well_path_folder='D:/Projects/ResInsight-regression-test/ModelData/Norne_LessWellPaths')
well_log_files = resInsight.project.import_well_log_files(well_log_folder='D:/Projects/ResInsight-regression-test/ModelData/Norne_PLT_LAS')

if len(well_paths) < 1:
    print("No well paths in project")
    exit(1)
print(well_paths)

for case in cases:
    if case.type == "GeoMechCase":
        print (case.case_id)
        case_path = case.grid_path()
        folder_name = os.path.dirname(case_path)
        case.import_formation_names(formation_files=['D:/Projects/ResInsight-regression-test/ModelData/norne/Norne_ATW2013.lyr'])

        # create a folder to hold the snapshots
        dirname = os.path.join(folder_name, 'snapshots')
        print("Exporting to: " + dirname)

        for well_path in well_paths:
            wbsplot = case.create_well_bore_stability_plot(well_path=well_path, time_step=0)
            wbsplot.export_snapshot(export_folder=dirname)
```

# ErrorHandling

```
###################################################################
# This example demonstrates the use of ResInsight exceptions 
# for proper error handling
###################################################################

import rips
import grpc
import tempfile

resinsight     = rips.Instance.find()

case = None

# Try loading a non-existing case. We should get a grpc.RpcError exception from the server
try:
    case = resinsight.project.load_case("Nonsense")
except grpc.RpcError as e:
    print("Expected Server Exception Received while loading case: ", e)

# Try loading well paths from a non-existing folder.  We should get a grpc.RpcError exception from the server
try:
    well_path_files = resinsight.project.import_well_paths(well_path_folder="NONSENSE/NONSENSE")
except grpc.RpcError as e:
    print("Expected Server Exception Received while loading wellpaths: ", e)

# Try loading well paths from an existing but empty folder. We should get a warning.
try:
    with tempfile.TemporaryDirectory() as tmpdirname:
        well_path_files = resinsight.project.import_well_paths(well_path_folder=tmpdirname)
        assert(len(well_path_files) == 0)
        assert(resinsight.project.has_warnings())
        print("Should get warnings below")
        for warning in resinsight.project.warnings():
            print (warning)
except grpc.RpcError as e:
    print("Unexpected Server Exception caught!!!", e)

case = resinsight.project.case(case_id=0)
if case is not None:
    results = case.active_cell_property('STATIC_NATIVE', 'PORO', 0)
    active_cell_count = len(results)

    # Send the results back to ResInsight inside try / except construct
    try:        
        case.set_active_cell_property(results, 'GENERATED', 'POROAPPENDED', 0)
        print("Everything went well as expected")
    except: # Match any exception, but it should not happen
        print("Ooops!")

    # Add another value, so this is outside the bounds of the active cell result storage
    results.append(1.0)

    # This time we should get a grpc.RpcError exception, which is a server side error.
    try:        
        case.set_active_cell_property(results, 'GENERATED', 'POROAPPENDED', 0)
        print("Everything went well??")
    except grpc.RpcError as e:
        print("Expected Server Exception Received: ", e)
    except IndexError:
        print ("Got index out of bounds error. This shouldn't happen here")

    # With a chunk size exactly matching the active cell count the server will not
    # be able to see any error as it will successfully close the stream after receiving
    # the correct number of values, even if the python client has more chunks to send
    case.chunk_size = active_cell_count

    try:        
        case.set_active_cell_property(results, 'GENERATED', 'POROAPPENDED', 0)
        print("Everything went well??")
    except grpc.RpcError as e:
        print("Got unexpected server exception", e, "This should not happen now")
    except IndexError:
        print ("Got expected index out of bounds error on client side")



```

# ExportPlots

```
# Import the tempfile module
import tempfile
# Load ResInsight Processing Server Client Library
import rips
# Connect to ResInsight instance
resInsight = rips.Instance.find()

# Get a list of all plots
plots = resInsight.project.plots()

export_folder = tempfile.mkdtemp()

print("Exporting to: " + export_folder)

for plot in plots:
	plot.export_snapshot(export_folder=export_folder)
	plot.export_data_as_las(export_folder=export_folder)
	plot.export_data_as_ascii(export_folder=export_folder)
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
resinsight = rips.Instance.find()
cases = resinsight.project.cases()

# Set main window size
resinsight.set_main_window_size(width=800, height=500)

n = 5                            # every n-th time_step for snapshot
property_list = ['SOIL', 'PRESSURE'] # list of parameter for snapshot

print ("Looping through cases")
for case in cases:
    print("Case name: ", case.name)
    print("Case id: ", case.case_id)
    # Get grid path and its folder name
    case_path = case.grid_path()
    folder_name = os.path.dirname(case_path)
    
    # create a folder to hold the snapshots
    dirname = os.path.join(folder_name, 'snapshots')
        
    if os.path.exists(dirname) is False:
        os.mkdir(dirname)
    
    print ("Exporting to folder: " + dirname)
    resinsight.set_export_folder(export_type='SNAPSHOTS', path=dirname)
   
    time_steps = case.time_steps()
    print('Number of time_steps: ' + str(len(time_steps)))
        
    view = case.views()[0]
    for property in property_list:
        view.apply_cell_result(result_type='DYNAMIC_NATIVE', result_variable=property)
        for time_step in range(0, len(time_steps), 10):
            view.set_time_step(time_step = time_step)
            view.export_snapshot()
```

# GridInformation

```
######################################################################################
# This example prints information about the grids of all cases in the current project
######################################################################################

import rips

resinsight  = rips.Instance.find()

cases = resinsight.project.cases()
print("Number of cases found: ", len(cases))
for case in cases:
    print(case.name)
    grids = case.grids()
    print("Number of grids: ", len(grids))
    for grid in grids:
        print("Grid dimensions: ", grid.dimensions())



```

# Import Well Paths

```
# Load ResInsight Processing Server Client Library
import rips
# Connect to ResInsight instance
resInsight = rips.Instance.find()

well_path_names = resInsight.project.import_well_paths(well_path_folder='D:/Projects/ResInsight-regression-test/ModelData/norne/wellpaths')
if resInsight.project.has_warnings():
    for warning in resInsight.project.warnings():
        print(warning)


for well_path_name in well_path_names:
    print("Imported from folder: " + well_path_name)

well_path_names = resInsight.project.import_well_paths(well_path_files=['D:/Projects/ResInsight-regression-test/ModelData/Norne_WellPaths/E-3H.json',
                                                                        'D:/Projects/ResInsight-regression-test/ModelData/Norne_WellPaths/C-1H.json'])
if resInsight.project.has_warnings():
    for warning in resInsight.project.warnings():
        print(warning)


for well_path_name in well_path_names:
    print("Imported from indivdual files: " + well_path_name)


well_path_names = resInsight.project.import_well_log_files(well_log_folder='D:/Projects/ResInsight-regression-test/ModelData/Norne_PLT_LAS')
if resInsight.project.has_warnings():
    for warning in resInsight.project.warnings():
        print(warning)

for well_path_name in well_path_names:
    print("Imported well log file for: " + well_path_name)
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
def create_result(poro_chunks, permx_chunks):
    # Loop through all the chunks of poro and permx in order
    for (poroChunk, permxChunk) in zip(poro_chunks, permx_chunks):
        resultChunk = []
        # Loop through all the values inside the chunks, in order
        for (poro, permx) in zip(poroChunk.values, permxChunk.values):
            resultChunk.append(poro * permx)
        # Return a generator object that behaves like a Python iterator
        yield resultChunk

resinsight     = rips.Instance.find()
start = time.time()
case = resinsight.project.case(case_id=0)

# Get a generator for the poro results. The generator will provide a chunk each time it is iterated
poro_chunks = case.active_cell_property_async('STATIC_NATIVE', 'PORO', 0)
# Get a generator for the permx results. The generator will provide a chunk each time it is iterated
permx_chunks = case.active_cell_property_async('STATIC_NATIVE', 'PERMX', 0)

# Send back the result with the result provided by a generator object.
# Iterating the result generator will cause the script to read from the poro and permx generators
# And return the result of each iteration
case.set_active_cell_property_async(create_result(poro_chunks, permx_chunks),
                                           'GENERATED', 'POROPERMXAS', 0)

end = time.time()
print("Time elapsed: ", end - start)
print("Transferred all results back")
view = case.views()[0].apply_cell_result('GENERATED', 'POROPERMXAS')
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

resinsight     = rips.Instance.find()
start = time.time()
case = resinsight.project.case(case_id=0)

# Read poro result into list
poro_results = case.active_cell_property('STATIC_NATIVE', 'PORO', 0)
# Read permx result into list
permx_results = case.active_cell_property('STATIC_NATIVE', 'PERMX', 0)

# Generate output result
results = []
for (poro, permx) in zip(poro_results, permx_results):
    results.append(poro * permx)

try:
    # Send back output result
    case.set_active_cell_property(results, 'GENERATED', 'POROPERMXSY', 0)
except grpc.RpcError as e:
    print("Exception Received: ", e)


end = time.time()
print("Time elapsed: ", end - start)
print("Transferred all results back")

view = case.views()[0].apply_cell_result('GENERATED', 'POROPERMXSY')
```

# InstanceExample

```
#######################################
# This example connects to ResInsight
#######################################
import rips

resinsight  = rips.Instance.find()

if resinsight is None:
    print('ERROR: could not find ResInsight')
else:
	print('Successfully connected to ResInsight')
```

# LaunchWithCommandLineOptions

```
# Load ResInsight Processing Server Client Library
import rips
# Launch ResInsight with last project file and a Window size of 600x1000 pixels
resinsight = rips.Instance.launch(command_line_parameters=['--last', '--size', 600, 1000])
# Get a list of all cases
cases = resinsight.project.cases()

print ("Got " + str(len(cases)) + " cases: ")
for case in cases:
    print("Case name: " + case.name)
    print("Case grid path: " + case.grid_path())
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

resinsight  = rips.Instance.find()
if resinsight is not None:
    cases = resinsight.project.selected_cases()

    print ("Got " + str(len(cases)) + " cases: ")
    for case in cases:
        print(case.name)
        for property in case.available_properties('DYNAMIC_NATIVE'):
            print(property)


```

# SetCellResult

```
######################################################################
# This script applies a cell result to the first view in the project
######################################################################
import rips

resinsight  = rips.Instance.find()

view = resinsight.project.view(view_id=0)
view.apply_cell_result(result_type='STATIC_NATIVE', result_variable='DX')
```

# SetFlowDiagnosticsResult

```
######################################################################
# This script applies a flow diagnostics cell result to the first view in the project
######################################################################

# Load ResInsight Processing Server Client Library
import rips
# Connect to ResInsight instance
resinsight = rips.Instance.find()

view = resinsight.project.view(view_id=0)
#view.apply_flow_diagnostics_cell_result(result_variable='Fraction',
#                                    selection_mode='FLOW_TR_INJ_AND_PROD')
                                    
# Example of setting individual wells. Commented out because well names are case specific.
view.apply_flow_diagnostics_cell_result(result_variable='Fraction',
                                    selection_mode='FLOW_TR_BY_SELECTION',
                                    injectors = ['C-1H', 'C-2H', 'F-2H'],
                                    producers = ['B-1AH', 'B-3H', 'D-1H'])
```

# SetGridProperties

```
######################################################################
# This script sets values for SOIL for all grid cells in the first case in the project
######################################################################
import rips

resinsight     = rips.Instance.find()

case = resinsight.project.case(case_id=0)
total_cell_count = case.cell_count().reservoir_cell_count

values = []
for i in range(0, total_cell_count):
    values.append(i % 2 * 0.75);

print("Applying values to full grid")
case.set_grid_property(values, 'DYNAMIC_NATIVE', 'SOIL', 0)

```

# SoilAverageAsync

```
###########################################################################################
# This example will asynchronously calculate the average value for SOIL for all time steps
###########################################################################################

import rips
import itertools
import time

resinsight     = rips.Instance.find()

start          = time.time()

# Get the case with case id 0
case           = resinsight.project.case(case_id=0)

# Get a list of all time steps
timeSteps      = case.time_steps()

averages = []
for i in range(0, len(timeSteps)):
    # Get the results from time step i asynchronously
    # It actually returns a generator object almost immediately
	result_chunks = case.active_cell_property_async('DYNAMIC_NATIVE', 'SOIL', i)
	mysum = 0.0
	count = 0
    # Loop through and append the average. each time we loop resultChunks
    # We will trigger a read of the input data, meaning the script will start
    # Calculating averages before the whole resultValue for this time step has been received
	for chunk in result_chunks:
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

resinsight     = rips.Instance.find()

start          = time.time()

# Get the case with case id 0
case           = resinsight.project.case(case_id=0)

# Get a list of all time steps
time_steps      = case.time_steps()

averages = []
for i in range(0, len(time_steps)):
    # Get a list of all the results for time step i
	results = case.active_cell_property('DYNAMIC_NATIVE', 'SOIL', i)
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
def create_result(soil_chunks, porv_chunks):
    for (soil_chunk, porv_chunk) in zip(soil_chunks, porv_chunks):
        resultChunk = []
        number = 0
        for (soil_value, porv_value) in zip(soil_chunk.values, porv_chunk.values):
            resultChunk.append(soil_value * porv_value)
        # Return a Python generator
        yield resultChunk

resinsight   = rips.Instance.find()
start        = time.time()
case         = resinsight.project.case(case_id=0)
timeStepInfo = case.time_steps()

# Get a generator for the porv results. The generator will provide a chunk each time it is iterated
porv_chunks   = case.active_cell_property_async('STATIC_NATIVE', 'PORV', 0)

# Read the static result into an array, so we don't have to transfer it for each iteration
# Note we use the async method even if we synchronise here, because we need the values chunked
# ... to match the soil chunks
porv_array = []
for porv_chunk in porv_chunks:
    porv_array.append(porv_chunk)

for i in range (0, len(timeStepInfo)):
    # Get a generator object for the SOIL property for time step i
    soil_chunks = case.active_cell_property_async('DYNAMIC_NATIVE', 'SOIL', i)
    # Create the generator object for the SOIL * PORV derived result
    result_generator = create_result(soil_chunks, iter(porv_array))
    # Send back the result asynchronously with a generator object
    case.set_active_cell_property_async(result_generator, 'GENERATED', 'SOILPORVAsync', i)

end = time.time()
print("Time elapsed: ", end - start)
        
print("Transferred all results back")

view = case.views()[0].apply_cell_result('GENERATED', 'SOILPORVAsync')
```

# SoilPorvSync

```
##############################################################################
# This example will create a derived result for each time step synchronously
##############################################################################

import rips
import time

resinsight = rips.Instance.find()
start = time.time()
case       = resinsight.project.case(case_id=0)

# Read the full porv result
porv_results = case.active_cell_property('STATIC_NATIVE', 'PORV', 0)
time_step_info = case.time_steps()

for i in range (0, len(time_step_info)):
    # Read the full SOIl result for time step i
    soil_results = case.active_cell_property('DYNAMIC_NATIVE', 'SOIL', i)
    
    # Generate the result by looping through both lists in order
    results = []
    for (soil, porv) in zip(soil_results, porv_results):
        results.append(soil * porv)

    # Send back result
    case.set_active_cell_property(results, 'GENERATED', 'SOILPORVSync', i)

end = time.time()
print("Time elapsed: ", end - start)

print("Transferred all results back")

view = case.views()[0].apply_cell_result('GENERATED', 'SOILPORVSync')
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
resinsight = rips.Instance.find()

# Check if connection worked
if resinsight is not None:
    # Get a list of all cases
    cases = resinsight.project.cases()
    for case in cases:
        # Get a list of all views
        views = case.views()
        for view in views:
            # Set some parameters for the view
            view.set_show_grid_box(not view.show_grid_box())
            view.set_background_color("#3388AA")            
            # Update the view in ResInsight
            view.update()
        # Clone the first view
        new_view = views[0].clone()
        view.set_show_grid_box(False)
        new_view.set_background_color("#FFAA33")
        new_view.update()
```
