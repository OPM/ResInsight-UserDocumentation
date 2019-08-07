---
layout: docs
title: Python API - rips
permalink: /docs/python/
published: true
---

ResInsight has a [gRPC Remote Procedure Call](https://www.grpc.io/) interface with a Python Client interface. This interface, called rips, allows you to interact with a running ResInsight instance from a Python script.

The Python client package is available for install via the Python PIP package system with `pip install rips` as admin user, or `pip install --user rips` as a regular user. On some systems the `pip` command may have to be replaced by `python -m pip`. See the [rips page on pypi.org](https://test.pypi.org/project/rips/) for more information about releases of the rips package.

In order for the Python-gRPC connection to be available, ResInsight needs to be built with the `RESINSIGHT_ENABLE_GRPC` option set. A valid gRPC build will show a message in the About dialog confirming gRPC is available:



![image](../images/AboutGrpc.png)

Furthermore, gRPC needs to be enabled in the Scripting tab of the Preference dialog:



![image](../images/PrefGrpc.png)

It is actually possible to interact with ResInsight using a number of other programming languages, C++, C#, Web Javascript, Go, Node.js, PHP, Java, etc. This requires familiarity with gRPC and Protocol Buffers and is currently undocumented and unsupported from a ResInsight point of view.

# Instance Module


#### class rips.Instance(port=50051)
The ResInsight Instance class. Use to launch or find existing ResInsight instances


#### launched()
Tells us whether the application was launched as a new process.
If the application was launched we may need to close it when exiting the script.


* **Type**

    bool



#### app()
Application information object. Set when creating an instance.


* **Type**

    App



#### commands()
Command executor. Set when creating an instance.


* **Type**

    Commands



#### project()
Current project in ResInsight.
Set when creating an instance and updated when opening/closing projects.


* **Type**

    Project



#### static find(startPort=50051, endPort=50071)
Search for an existing Instance of ResInsight by testing ports.

By default we search from port 50051 to 50071 or if the environment
variable RESINSIGHT_GRPC_PORT is set we search
RESINSIGHT_GRPC_PORT to RESINSIGHT_GRPC_PORT+20


* **Parameters**

    * **startPort** (*int*) -- start searching from this port

    * **endPort** (*int*) -- search up to but not including this port



#### static launch(resInsightExecutable='', console=False)
Launch a new Instance of ResInsight. This requires the environment variable
RESINSIGHT_EXECUTABLE to be set or the parameter resInsightExecutable to be provided.
The RESINSIGHT_GRPC_PORT environment variable can be set to an alternative port number.


* **Parameters**

    * **resInsightExecutable** (*str*) -- Path to a valid ResInsight executable. If set
      will take precedence over what is provided in the RESINSIGHT_EXECUTABLE
      environment variable.

    * **console** (*bool*) -- If True, launch as console application, without GUI.



* **Returns**

    an instance object if it worked. None if not.



* **Return type**

    Instance


## Example

```python
import rips

resInsight  = rips.Instance.find()

if resInsight is None:
    print('ERROR: could not find ResInsight')
```

# App Module


#### class rips.App(channel)
ResInsight application information and control.
Allows retrieving of information and controlling the running instance
Not meant to be constructed manually, but exists as part of the Instance method


#### exit()
Tell ResInsight instance to quit


#### isConsole()
Returns true if the connected ResInsight instance is a console app


#### isGui()
Returns true if the connected ResInsight instance is a GUI app


#### majorVersion()
Get an integer with the major version number


#### minorVersion()
Get an integer with the minor version number


#### patchVersion()
Get an integer with the patch version number


#### versionString()
Get a full version string, i.e. 2019.04.01

## Example

```python
import rips

resInsight  = rips.Instance.find()
if resInsight is not None:
    print(resInsight.app.versionString())
    print("Is this a console run?", resInsight.app.isConsole())
```

# Case Module


#### class rips.Case(channel, id)
ResInsight case class

Operate on a ResInsight case specified by a Case Id integer.
Not meant to be constructed separately but created by one of the following
methods in Project: loadCase, case, allCases, selectedCases


#### id()
Case Id corresponding to case Id in ResInsight project.


* **Type**

    int



#### name()
Case name


* **Type**

    str



#### groupId()
Case Group id


* **Type**

    int



#### cellCount(porosityModel='MATRIX_MODEL')
Get a cell count object containing number of active cells and
total number of cells


* **Parameters**

    **porosityModel** (*str*) -- String representing an enum.
    must be 'MATRIX_MODEL' or 'FRACTURE_MODEL'.



* **Returns**

    active_cell_count: number of active cells
    reservoir_cell_count: total number of reservoir cells



* **Return type**

    Cell Count object with the following integer attributes



#### cellInfoForActiveCells(porosityModel='MATRIX_MODEL')
Get Stream of cell info objects for current case


* **Parameters**

    **porosityModel** (*str*) -- String representing an enum.
    must be 'MATRIX_MODEL' or 'FRACTURE_MODEL'.



* **Returns**

    grid_index(int): grid the cell belongs to
    parent_grid_index(int): parent of the grid the cell belongs to
    coarsening_box_index(int): the coarsening box index
    local_ijk(Vec3i: i(int), j(int), k(int)): local cell index in i, j, k directions.
    parent_ijk(Vec3i: i(int), j(int), k(int)): cell index in parent grid in i, j, k.



* **Return type**

    Stream of cell info objects with the following attributes



#### daysSinceStart()
Get a list of decimal values representing days since the start of the simulation


#### grid(index)
Get Grid of a given index. Returns a rips Grid object


* **Parameters**

    **index** (*int*) -- The grid index


Returns: Grid object


#### gridCount()
Get number of grids in the case


#### grids()
Get a list of all rips Grid objects in the case


#### timeSteps()
Get a list containing time step strings for all time steps

## Example

```python
import rips

resInsight  = rips.Instance.find()
if resInsight is not None:
    cases = resInsight.project.cases()

    print ("Got " + str(len(cases)) + " cases: ")
    for case in cases:
        print(case.name)
```

# Commands Module


#### class rips.Commands(channel)
Command executor which can run ResInsight Command File commands nearly verbatim

Documentation Command File Interface:

    [https://resinsight.org/docs/commandfile/](https://resinsight.org/docs/commandfile/)

The differences are:

    * Enum values have to be provided as strings. I.e. "ALL" instead of ALL.

    * Booleans have to be specified as correct Python. True instead of true.


#### closeProject()
Close the current project (and reopen empty one)


#### computeCaseGroupStatistics(caseIds)

#### createLgrForCompletions(caseId, timeStep, wellPathNames, refinementI, refinementJ, refinementK, splitType)

#### createMultipleFractures(caseId, templateId, wellPathNames, minDistFromWellTd, maxFracturesPerWell, topLayer, baseLayer, spacing, action)

#### createSaturationPressurePlots(caseIds)

#### exportMsw(caseId, wellPath)

#### exportMultiCaseSnapshots(gridListFile)
Export snapshots for a set of cases


* **Parameters**

    **gridListFile** (*str*) -- Path to a file containing a list of grids to export snapshot for



#### exportProperty(caseId, timeStep, property, eclipseKeyword=<class 'property'>, undefinedValue=0.0, exportFile=<class 'property'>)
Export an Eclipse property


* **Parameters**

    * **caseId** (*int*) -- case id

    * **timeStep** (*int*) -- time step index

    * **property** (*str*) -- property to export

    * **eclipseKeyword** (*str*) -- Eclipse keyword used as text in export header. Defaults to the value of property parameter.

    * **undefinedValue** (*double*) -- Value to use for undefined values. Defaults to 0.0

    * **exportFile** (*str*) -- Filename for export. Defaults to the value of property parameter



#### exportPropertyInViews(caseId, viewNames, undefinedValue)

#### exportSimWellFractureCompletions(caseId, viewName, timeStep, simulationWellNames, fileSplit, compdatExport)

#### exportSnapshots(type='ALL', prefix='')
Export snapshots of a given type


* **Parameters**

    * **type** (*str*) -- Enum string ('ALL', 'VIEWS' or 'PLOTS')

    * **prefix** (*str*) -- Exported file name prefix



#### exportVisibleCells(caseId, viewName, exportKeyword='FLUXNUM', visibleActiveCellsValue=1, hiddenActiveCellsValue=0, inactiveCellsValue=0)

#### exportWellPathCompletions(caseId, timeStep, wellPathNames, fileSplit, compdatExport, includePerforations, includeFishbones, excludeMainBoreForFishbones, combinationMode)

#### exportWellPaths(wellPaths=[], mdStepSize=5.0)

#### loadCase(path)
Load a case


* **Parameters**

    **path** (*str*) -- path to EGRID file



* **Returns**

    A Case object



#### openProject(path)
Open a project


* **Parameters**

    **path** (*str*) -- path to project file



#### replaceCase(newGridFile, caseId=0)
Replace the given case with a new case loaded from file


* **Parameters**

    * **newGridFile** (*str*) -- path to EGRID file

    * **caseId** (*int*) -- case Id to replace



#### replaceSourceCases(gridListFile, caseGroupId=0)
Replace all source cases within a case group


* **Parameters**

    * **gridListFile** (*str*) -- path to file containing a list of cases

    * **caseGroupId** (*int*) -- id of the case group to replace



#### runOctaveScript(path, cases)

#### scaleFractureTemplate(id, halfLength, height, dFactor, conductivity)

#### setExportFolder(type, path, createFolder=False)

#### setFractureContainment(id, topLayer, baseLayer)

#### setMainWindowSize(width, height)

#### setStartDir(path)
Set current start directory


* **Parameters**

    **path** (*str*) -- path to directory



#### setTimeStep(caseId, timeStep)
## Example

```python
import rips

# Load instance
resInsight = rips.Instance.find()

# Run a couple of commands
resInsight.commands.setTimeStep(caseId=0, timeStep=3)
resInsight.commands.setMainWindowSize(width=800, height=500)
#resInsight.commands.exportWellPaths()
with tempfile.TemporaryDirectory(prefix="rips") as tmpdirname:
    print("Temporary folder: ", tmpdirname)
    resInsight.commands.setExportFolder(type='SNAPSHOTS', path=tmpdirname)
    resInsight.commands.setExportFolder(type='PROPERTIES', path=tmpdirname)
    resInsight.commands.exportSnapshots()
    print(os.listdir(tmpdirname))
    assert(len(os.listdir(tmpdirname)) > 0)
    case = resInsight.project.case(id=0)
    resInsight.commands.exportPropertyInViews(0, "3D View", 0)
    expectedFileName = case.name + "-" + str("3D_View") + "-" + "T3" + "-SOIL"
    fullPath = tmpdirname + "/" + expectedFileName
    assert(os.path.exists(fullPath))

```

# Grid Module


#### class rips.Grid(index, case)
Grid Information. Not meant to be constructed separately

Create Grid objects using mathods on Case: Grid() and Grids()


#### dimensions()
The dimensions in i, j, k direction


* **Returns**

    class with integer attributes i, j, k representing the extent in all three dimensions.



* **Return type**

    Vec3i


## Example

```python
    case = rips_instance.project.loadCase(path=casePath)
print (case.gridCount())
    if case.gridCount() > 0:
            grid = case.grid(index=0)
            dimensions = grid.dimensions()
            print(dimensions.i)
            print(dimensions.j)
            print(dimensions.k)
```

# Project Module


#### class rips.Project(channel)
ResInsight project. Not intended to be created separately.

Automatically created and assigned to Instance.


#### case(id)
Get a specific case from the provided case Id


* **Parameters**

    **id** (*int*) -- case id



* **Returns**

    A rips Case object



#### cases()
Get a list of all cases in the project


* **Returns**

    A list of rips Case objects



#### close()
Close the current project (and open new blank project)


#### loadCase(path)
Load a new case from the given file path


* **Parameters**

    **path** (*str*) -- file path to case



* **Returns**

    A rips Case object



#### open(path)
Open a new project from the given path


* **Parameters**

    **path** (*str*) -- path to project file



#### selectedCases()
Get a list of all cases selected in the project tree


* **Returns**

    A list of rips Case objects


# Properties Module


#### class rips.Properties(case)
Class for streaming properties to and from ResInsight


#### activeCellProperty(propertyType, propertyName, timeStep, porosityModel='MATRIX_MODEL')
Get a cell property for all active cells. Async, so returns an iterator


* **Parameters**

    * **propertyType** (*str*) -- string enum. See available()

    * **propertyName** (*str*) -- name of an Eclipse property

    * **timeStep** (*int*) -- the time step for which to get the property for

    * **porosityModel** (*str*) -- string enum. See available()



* **Returns**

    An iterator to a chunk object containing an array of double values
    You first loop through the chunks and then the values within the chunk to get all values.



#### available(propertyType, porosityModel='MATRIX_MODEL')
Get a list of available properties


* **Parameters**

    * **propertyType** (*str*) -- string corresponding to propertyType enum.

      Can be one of the following:

      'DYNAMIC_NATIVE'

          'STATIC_NATIVE'
          'SOURSIMRL'
          'GENERATED'
          'INPUT_PROPERTY'
          'FORMATION_NAMES'
          'FLOW_DIAGNOSTICS'
          'INJECTION_FLOODING'


    * **porosityModel** (*str*) -- 'MATRIX_MODEL' or 'FRACTURE_MODEL'.



#### gridProperty(propertyType, propertyName, timeStep, gridIndex=0, porosityModel='MATRIX_MODEL')
Get a cell property for all grid cells. Async, so returns an iterator


* **Parameters**

    * **propertyType** (*str*) -- string enum. See available()

    * **propertyName** (*str*) -- name of an Eclipse property

    * **timeStep** (*int*) -- the time step for which to get the property for

    * **gridIndex** (*int*) -- index to the grid we're getting values for

    * **porosityModel** (*str*) -- string enum. See available()



* **Returns**

    An iterator to a chunk object containing an array of double values
    You first loop through the chunks and then the values within the chunk to get all values.



#### setActiveCellProperty(values, propertyType, propertyName, timeStep, porosityModel='MATRIX_MODEL')
Set a cell property for all active cells.


* **Parameters**

    * **values** (*list*) -- a list of double precision floating point numbers

    * **propertyType** (*str*) -- string enum. See available()

    * **propertyName** (*str*) -- name of an Eclipse property

    * **timeStep** (*int*) -- the time step for which to get the property for

    * **porosityModel** (*str*) -- string enum. See available()



#### setActiveCellPropertyAsync(values_iterator, propertyType, propertyName, timeStep, porosityModel='MATRIX_MODEL')
Set a cell property for all active cells. Async, and so takes an iterator to the input values


* **Parameters**

    * **values_iterator** (*iterator*) -- an iterator to the properties to be set

    * **propertyType** (*str*) -- string enum. See available()

    * **propertyName** (*str*) -- name of an Eclipse property

    * **timeStep** (*int*) -- the time step for which to get the property for

    * **porosityModel** (*str*) -- string enum. See available()



#### setGridProperty(values, propertyType, propertyName, timeStep, gridIndex=0, porosityModel='MATRIX_MODEL')
Set a cell property for all grid cells.


* **Parameters**

    * **values** (*list*) -- a list of double precision floating point numbers

    * **propertyType** (*str*) -- string enum. See available()

    * **propertyName** (*str*) -- name of an Eclipse property

    * **timeStep** (*int*) -- the time step for which to get the property for

    * **gridIndex** (*int*) -- index to the grid we're setting values for

    * **porosityModel** (*str*) -- string enum. See available()


## Synchronous Example

Read two properties, multiply them together and push the results back to ResInsight in a naïve way, by reading PORO into a list, then reading PERMX into a list, then multiplying them both in a resulting list and finally transferring back the list.

This is slow and inefficient, but works.

```python
import rips
import time

resInsight     = rips.Instance.find()
start = time.time()
case = resInsight.project.case(id=0)

poroChunks = case.properties.activeCellProperty('STATIC_NATIVE', 'PORO', 0)
poroResults = []
for poroChunk in poroChunks:
    for poro in poroChunk.values:
        poroResults.append(poro)

permxChunks = case.properties.activeCellProperty('STATIC_NATIVE', 'PERMX', 0)
permxResults = []
for permxChunk in permxChunks:
    for permx in permxChunk.values:
        permxResults.append(permx)

results = []
for (poro, permx) in zip(poroResults, permxResults):
    results.append(poro * permx)

case.properties.setActiveCellProperty(results, 'GENERATED', 'POROPERMXSY', 0)

end = time.time()
print("Time elapsed: ", end - start)

print("Transferred all results back")
```

## Asynchronous Example

Read two properties at the same time chunk by chunk, multiply each chunk together and start transferring the result back to ResInsight as soon as the chunk is finished.

This is far more efficient.

```python
import rips
import time

def createResult(poroChunks, permxChunks):
    for (poroChunk, permxChunk) in zip(poroChunks, permxChunks):
        resultChunk = []
        for (poro, permx) in zip(poroChunk.values, permxChunk.values):
            resultChunk.append(poro * permx)
        yield resultChunk

resInsight     = rips.Instance.find()
start = time.time()
case = resInsight.project.case(id=0)

poroChunks = case.properties.activeCellProperty('STATIC_NATIVE', 'PORO', 0)
permxChunks = case.properties.activeCellProperty('STATIC_NATIVE', 'PERMX', 0)

case.properties.setActiveCellPropertyAsync(createResult(poroChunks, permxChunks),
                                           'GENERATED', 'POROPERMXAS', 0)

end = time.time()
print("Time elapsed: ", end - start)

print("Transferred all results back")
```
