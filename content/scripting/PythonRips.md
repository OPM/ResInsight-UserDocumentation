+++
title = "Python API - rips"
published = true
weight = 42
+++

![]({{< relref "" >}}images/scripting/python-logo-master-v3-TM.png)

# Instance Module


#### class rips.instance.Instance(port=50051, launched=False)
The ResInsight Instance class. Use to launch or find existing ResInsight instances


#### launched()
Tells us whether the application was launched as a new process.
If the application was launched we may need to close it when exiting the script.


* **Type**

    bool



#### commands()
Command executor. Set when creating an instance.


* **Type**

    Commands



#### project()
Current project in ResInsight.
Set when creating an instance and updated when opening/closing projects.


* **Type**

    Project



#### client_version_string()
Get a full version string, i.e. 2019.04.01


#### exit()
Tell ResInsight instance to quit


#### static find(start_port=50051, end_port=50071)
Search for an existing Instance of ResInsight by testing ports.

By default we search from port 50051 to 50071 or if the environment
variable RESINSIGHT_GRPC_PORT is set we search
RESINSIGHT_GRPC_PORT to RESINSIGHT_GRPC_PORT+20


* **Parameters**

    * **start_port** (*int*) -- start searching from this port

    * **end_port** (*int*) -- search up to but not including this port



#### is_console()
Returns true if the connected ResInsight instance is a console app


#### is_gui()
Returns true if the connected ResInsight instance is a GUI app


#### static launch(resinsight_executable='', console=False, launch_port=-1, command_line_parameters=None)
Launch a new Instance of ResInsight. This requires the environment variable
RESINSIGHT_EXECUTABLE to be set or the parameter resinsight_executable to be provided.
The RESINSIGHT_GRPC_PORT environment variable can be set to an alternative port number.


* **Parameters**

    * **resinsight_executable** (*str*) -- Path to a valid ResInsight executable. If set
      will take precedence over what is provided in the RESINSIGHT_EXECUTABLE
      environment variable.

    * **console** (*bool*) -- If True, launch as console application, without GUI.

    * **launch_port** (*int*) -- If -1 will use the default port 50051 or RESINSIGHT_GRPC_PORT
      if anything else, ResInsight will try to launch with this port

    * **command_line_parameters** (*list*) -- Additional parameters as string entries in the list.



* **Returns**

    an instance object if it worked. None if not.



* **Return type**

    Instance



#### major_version()
Get an integer with the major version number


#### minor_version()
Get an integer with the minor version number


#### patch_version()
Get an integer with the patch version number


#### set_export_folder(export_type, path, create_folder=False)
Set the export folder used for all export functions

Parameter        | Description                                  | Type
---------------- | -------------------------------------------- | -----
export_type      | String specifying what to export             | String
path             | Path to folder                               | String
create_folder    | Create folder if it doesn't exist?           | Boolean

##### Enum export_type

Option          | Description
--------------- | ------------
"COMPLETIONS"   |
"SNAPSHOTS"     |
"PROPERTIES"    |
"STATISTICS"    |


#### set_main_window_size(width, height)
Set the main window size in pixels

Parameter | Description      | Type
--------- | ---------------- | -----
width     | Width in pixels  | Integer
height    | Height in pixels | Integer


#### set_start_dir(path)
Set current start directory


* **Parameters**

    **path** (*str*) -- path to directory



#### version_string()
Get a full version string, i.e. 2019.04.01

## Example

```

resinsight  = rips.Instance.find()

if resinsight is None:
    print('ERROR: could not find ResInsight')
else:
	print('Successfully connected to ResInsight')
```

# Case Module


#### class rips.case.Case(channel, case_id)
ResInsight case class

Operate on a ResInsight case specified by a Case Id integer.
Not meant to be constructed separately but created by one of the following
methods in Project: loadCase, case, allCases, selectedCasesq


#### id()
Case Id corresponding to case Id in ResInsight project.


* **Type**

    int



#### name()
Case name


* **Type**

    str



#### group_id()
Case Group id


* **Type**

    int



#### chunkSize()
The size of each chunk during value streaming.
A good chunk size is 64KiB = 65536B.
Meaning the ideal number of doubles would be 8192.
However we need overhead space, so the default is 8160.
This leaves 256B for overhead.


* **Type**

    int



#### active_cell_property(property_type, property_name, time_step, porosity_model='MATRIX_MODEL')
Get a cell property for all active cells. Sync, so returns a list


* **Parameters**

    * **property_type** (*str*) -- string enum. See available()

    * **property_name** (*str*) -- name of an Eclipse property

    * **time_step** (*int*) -- the time step for which to get the property for

    * **porosity_model** (*str*) -- string enum. See available()



* **Returns**

    A list containing double values
    Loop through the chunks and then the values within the chunk to get all values.



#### active_cell_property_async(property_type, property_name, time_step, porosity_model='MATRIX_MODEL')
Get a cell property for all active cells. Async, so returns an iterator


* **Parameters**

    * **property_type** (*str*) -- string enum. See available()

    * **property_name** (*str*) -- name of an Eclipse property

    * **time_step** (*int*) -- the time step for which to get the property for

    * **porosity_model** (*str*) -- string enum. See available()



* **Returns**

    An iterator to a chunk object containing an array of double values
    Loop through the chunks and then the values within the chunk to get all values.



#### available_properties(property_type, porosity_model='MATRIX_MODEL')
Get a list of available properties


* **Parameters**

    * **property_type** (*str*) -- string corresponding to property_type enum. Choices:
      - DYNAMIC_NATIVE
      - STATIC_NATIVE
      - SOURSIMRL
      - GENERATED
      - INPUT_PROPERTY
      - FORMATION_NAMES
      - FLOW_DIAGNOSTICS
      - INJECTION_FLOODING

    * **porosity_model** (*str*) -- 'MATRIX_MODEL' or 'FRACTURE_MODEL'.



#### cell_count(porosity_model='MATRIX_MODEL')
Get a cell count object containing number of active cells and
total number of cells


* **Parameters**

    **porosity_model** (*str*) -- String representing an enum.
    must be 'MATRIX_MODEL' or 'FRACTURE_MODEL'.



* **Returns**

    active_cell_count: number of active cells
    reservoir_cell_count: total number of reservoir cells



* **Return type**

    Cell Count object with the following integer attributes



#### cell_info_for_active_cells(porosity_model='MATRIX_MODEL')
Get list of cell info objects for current case


* **Parameters**

    **porosity_model** (*str*) -- String representing an enum.
    must be 'MATRIX_MODEL' or 'FRACTURE_MODEL'.



* **Returns**

    List of **CellInfo** objects


### CellInfo class description

Parameter                 | Description                                   | Type
------------------------- | --------------------------------------------- | -----
grid_index                | Index to grid                                 | Integer
parent_grid_index         | Index to parent grid                          | Integer
coarsening_box_index      | Index to coarsening box                       | Integer
local_ijk                 | Cell index in IJK directions of local grid    | Vec3i
parent_ijk                | Cell index in IJK directions of parent grid   | Vec3i

### Vec3i class description

Parameter        | Description                                  | Type
---------------- | -------------------------------------------- | -----
i                | I grid index                                 | Integer
j                | J grid index                                 | Integer
k                | K grid index                                 | Integer


#### cell_info_for_active_cells_async(porosity_model='MATRIX_MODEL')
Get Stream of cell info objects for current case


* **Parameters**

    **porosity_model** (*str*) -- String representing an enum.
    must be 'MATRIX_MODEL' or 'FRACTURE_MODEL'.



* **Returns**

    Stream of **CellInfo** objects


See cell_info_for_active_cells() for detalis on the **CellInfo** class.


#### create_lgr_for_completion(time_step, well_path_names, refinement_i, refinement_j, refinement_k, split_type)
Create a local grid refinement for the completions on the given well paths

Parameter       | Description                            | Type
--------------- | -------------------------------------- | -----
time_steps      | Time step index                        | Integer
well_path_names | List of well path names                | List of Strings
refinement_i    | Refinment in x-direction               | Integer
refinement_j    | Refinment in y-direction               | Integer
refinement_k    | Refinment in z-direction               | Integer
split_type      | Defines how to split LGRS              | String enum

##### Enum split_type

Option                  | Description
------------------------| ------------
"LGR_PER_CELL"          | One LGR for each completed cell
"LGR_PER_COMPLETION"    | One LGR for each completion (fracture, perforation, ...)
"LGR_PER_WELL"          | One LGR for each well


#### create_multiple_fractures(template_id, well_path_names, min_dist_from_well_td, max_fractures_per_well, top_layer, base_layer, spacing, action)
Create Multiple Fractures in one go

Parameter              | Description                               | Type
-----------------------| ----------------------------------------- | -----
template_id            | Id of the template                        | Integer
well_path_names        | List of well path names                   | List of Strings
min_dist_from_well_td  | Minimum distance from well TD             | Double
max_fractures_per_well | Max number of fractures per well          | Integer
top_layer              | Top grid k-level for fractures            | Integer
base_layer             | Base grid k-level for fractures           | Integer
spacing                | Spacing between fractures                 | Double
action                 | 'APPEND_FRACTURES' or 'REPLACE_FRACTURES' | String enum


#### create_saturation_pressure_plots()
Create saturation pressure plots for the current case


#### create_view()
Create a new view in the current case


#### days_since_start()
Get a list of decimal values representing days since the start of the simulation


#### export_flow_characteristics(time_steps, injectors, producers, file_name, minimum_communication=0.0, aquifer_cell_threshold=0.1)
Export Flow Characteristics data to text file in CSV format

Parameter                 | Description                                   | Type
------------------------- | --------------------------------------------- | -----
time_steps                | Time step indices                             | List of Integer
injectors                 | Injector names                                | List of Strings
producers                 | Producer names                                | List of Strings
file_name                 | Export file name                              | Integer
minimum_communication     | Minimum Communication, defaults to 0.0        | Integer
aquifer_cell_threshold    | Aquifer Cell Threshold, defaults to 0.1       | Integer


#### export_msw(well_path)
Export Eclipse Multi-segment-well model to file


* **Parameters**

    **well_path** (*str*) -- Well path name



#### export_property(time_step, property_name, eclipse_keyword=<class 'property'>, undefined_value=0.0, export_file=<class 'property'>)
Export an Eclipse property


* **Parameters**

    * **time_step** (*int*) -- time step index

    * **property_name** (*str*) -- property to export

    * **eclipse_keyword** (*str*) -- Keyword used in export header. Defaults: value of property

    * **undefined_value** (*double*) -- Value to use for undefined values. Defaults to 0.0

    * **export_file** (*str*) -- File name for export. Defaults to the value of property parameter



#### export_snapshots_of_all_views(prefix='')
Export snapshots for all views in the case


* **Parameters**

    **prefix** (*str*) -- Exported file name prefix



#### export_well_path_completions(time_step, well_path_names, file_split, compdat_export='TRANSMISSIBILITIES', include_perforations=True, include_fishbones=True, fishbones_exclude_main_bore=True, combination_mode='INDIVIDUALLY')
Export well path completions for the current case to file

Parameter                   | Description                                      | Type
----------------------------| ------------------------------------------------ | -----
time_step                   | Time step to export for                          | Integer
well_path_names             | List of well path names                          | List
file_split                  | Controls how export data is split into files     | String enum
compdat_export              | Compdat export type                              | String enum
include_perforations        | Export perforations?                             | bool
include_fishbones           | Export fishbones?                                | bool
fishbones_exclude_main_bore | Exclude main bore when exporting fishbones?      | bool
combination_mode            | Settings for multiple completions in same cell   | String Enum

##### Enum file_split

Option                              | Description
----------------------------------- | ------------
"UNIFIED_FILE"                      | A single file with all combined transmissibilities
"SPLIT_ON_WELL"                     | One file for each well with combined transmissibilities
"SPLIT_ON_WELL_AND_COMPLETION_TYPE" | One file for each completion type for each well

##### Enum compdat_export

Option                                      | Description
------------------------------------------- | ------------
"TRANSMISSIBILITIES"                        | Direct export of transmissibilities
"WPIMULT_AND_DEFAULT_CONNECTION_FACTORS"    | Include WPIMULT in addition to transmissibilities

##### Enum combination_mode

Option              | Description
------------------- | ------------
"INDIVIDUALLY"      | Exports the different completion types into separate sections
"COMBINED"          | Export one combined transmissibility for each cell


#### grid(index)
Get Grid of a given index. Returns a rips Grid object


* **Parameters**

    **index** (*int*) -- The grid index


Returns: Grid object


#### grid_path()
Get path of the current grid case

Returns: path string


#### grid_property(property_type, property_name, time_step, grid_index=0, porosity_model='MATRIX_MODEL')
Get a cell property for all grid cells. Synchronous, so returns a list


* **Parameters**

    * **property_type** (*str*) -- string enum. See available()

    * **property_name** (*str*) -- name of an Eclipse property

    * **time_step** (*int*) -- the time step for which to get the property for

    * **grid_index** (*int*) -- index to the grid we're getting values for

    * **porosity_model** (*str*) -- string enum. See available()



* **Returns**

    A list of double values



#### grid_property_async(property_type, property_name, time_step, grid_index=0, porosity_model='MATRIX_MODEL')
Get a cell property for all grid cells. Async, so returns an iterator


* **Parameters**

    * **property_type** (*str*) -- string enum. See available()

    * **property_name** (*str*) -- name of an Eclipse property

    * **time_step** (*int*) -- the time step for which to get the property for

    * **gridIndex** (*int*) -- index to the grid we're getting values for

    * **porosity_model** (*str*) -- string enum. See available()



* **Returns**

    An iterator to a chunk object containing an array of double values
    Loop through the chunks and then the values within the chunk to get all values.



#### grids()
Get a list of all rips Grid objects in the case


#### replace(new_grid_file)
Replace the current case grid with a new grid loaded from file


* **Parameters**

    **new_egrid_file** (*str*) -- path to EGRID file



#### set_active_cell_property(values, property_type, property_name, time_step, porosity_model='MATRIX_MODEL')
Set a cell property for all active cells.


* **Parameters**

    * **values** (*list*) -- a list of double precision floating point numbers

    * **property_type** (*str*) -- string enum. See available()

    * **property_name** (*str*) -- name of an Eclipse property

    * **time_step** (*int*) -- the time step for which to get the property for

    * **porosity_model** (*str*) -- string enum. See available()



#### set_active_cell_property_async(values_iterator, property_type, property_name, time_step, porosity_model='MATRIX_MODEL')
Set cell property for all active cells Async. Takes an iterator to the input values


* **Parameters**

    * **values_iterator** (*iterator*) -- an iterator to the properties to be set

    * **property_type** (*str*) -- string enum. See available()

    * **property_name** (*str*) -- name of an Eclipse property

    * **time_step** (*int*) -- the time step for which to get the property for

    * **porosity_model** (*str*) -- string enum. See available()



#### set_grid_property(values, property_type, property_name, time_step, grid_index=0, porosity_model='MATRIX_MODEL')
Set a cell property for all grid cells.


* **Parameters**

    * **values** (*list*) -- a list of double precision floating point numbers

    * **property_type** (*str*) -- string enum. See available()

    * **property_name** (*str*) -- name of an Eclipse property

    * **time_step** (*int*) -- the time step for which to get the property for

    * **grid_index** (*int*) -- index to the grid we're setting values for

    * **porosity_model** (*str*) -- string enum. See available()



#### time_steps()
Get a list containing all time steps

The time steps are defined by the class **TimeStepDate** :

Type      | Name
--------- | ----------
int       | year
int       | month
int       | day
int       | hour
int       | minute
int       | second


#### view(view_id)
Get a particular view belonging to a case by providing view id
:param view_id: view id
:type view_id: int

Returns: a view object


#### views()
Get a list of views belonging to a case

## Example

```

# Import the ResInsight Processing Server Module
import rips

# Connect to ResInsight
resinsight  = rips.Instance.find()
if resinsight is not None:
    # Get a list of all cases
    cases = resinsight.project.cases()

    print ("Got " + str(len(cases)) + " cases: ")
    for case in cases:
        print("Case name: " + case.name)
        print("Case grid path: " + case.grid_path())
        
        timesteps = case.time_steps()
        for t in timesteps:
            print("Year: " + str(t.year))
            print("Month: " + str(t.month))
        
    

```

# Grid Module


#### class rips.grid.Grid(index, case, channel)
Grid Information. Not meant to be constructed separately

Create Grid objects using mathods on Case: Grid() and Grids()


#### dimensions()
The dimensions in i, j, k direction


* **Returns**

    class with integer attributes i, j, k giving extent in all three dimensions.



* **Return type**

    Vec3i


## Example

```
    case = rips_instance.project.loadCase(path=casePath)
print (case.gridCount())
    if case.gridCount() > 0:
            grid = case.grid(index=0)
            dimensions = grid.dimensions()
            print(dimensions.i)
            print(dimensions.j)
            print(dimensions.k)
```

# GridCaseGroup Module


#### class rips.gridcasegroup.GridCaseGroup(pdm_object)
ResInsight Grid Case Group class

Operate on a ResInsight case group specified by a Case Group Id integer.


#### group_id()
Grid Case Group Id corresponding to case group Id in ResInsight project.


* **Type**

    int



#### compute_statistics(case_ids=None)
Compute statistics for the given case ids


* **Parameters**

    * **case_ids** (*list of integers*) -- list of case ids.

    * **this is None all cases in group are included** (*If*) -- 



#### create_statistics_case()
Create a Statistics case in the Grid Case Group


* **Returns**

    A new Case



#### statistics_cases()
Get a list of all statistics cases in the Grid Case Group


#### view(view_id)
Get a particular view belonging to a case group by providing view id
:param id: view id
:type id: int

Returns: a view object


#### views()
Get a list of views belonging to a grid case group

# Project Module


#### class rips.project.Project(channel)
ResInsight project. Not intended to be created separately.

Automatically created and assigned to Instance.


#### case(case_id)
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


#### create_grid_case_group(case_paths)
Create a Grid Case Group from a list of cases


* **Parameters**

    **case_paths** (*list*) -- list of file path strings



* **Returns**

    A case group id and name



#### export_multi_case_snapshots(grid_list_file)
Export snapshots for a set of cases


* **Parameters**

    **grid_list_file** (*str*) -- Path to a file containing a list of grids to export snapshot for



#### export_snapshots(snapshot_type='ALL', prefix='')
Export all snapshots of a given type


* **Parameters**

    * **snapshot_type** (*str*) -- Enum string ('ALL', 'VIEWS' or 'PLOTS')

    * **prefix** (*str*) -- Exported file name prefix



#### export_well_paths(well_paths=None, md_step_size=5.0)
Export a set of well paths


* **Parameters**

    * **well_paths** (*list*) -- List of strings of well paths. If none, export all.

    * **md_step_size** (*double*) -- resolution of the exported well path



#### grid_case_group(group_id)
Get a particular grid case group belonging to a project


* **Parameters**

    **groupId** (*int*) -- group id


Returns: a grid case group object


#### grid_case_groups()
Get a list of all grid case groups in the project


#### load_case(path)
Load a new case from the given file path


* **Parameters**

    **path** (*str*) -- file path to case



* **Returns**

    A rips Case object



#### open(path)
Open a new project from the given path


* **Parameters**

    **path** (*str*) -- path to project file



#### replace_source_cases(grid_list_file, case_group_id=0)
Replace all source cases within a case group


* **Parameters**

    * **grid_list_file** (*str*) -- path to file containing a list of cases

    * **case_group_id** (*int*) -- id of the case group to replace



#### scale_fracture_template(template_id, half_length, height, d_factor, conductivity)
Scale fracture template parameters


* **Parameters**

    * **template_id** (*int*) -- ID of fracture template

    * **half_length** (*double*) -- Half Length scale factor

    * **height** (*double*) -- Height scale factor

    * **d_factor** (*double*) -- D-factor scale factor

    * **conductivity** (*double*) -- Conductivity scale factor



#### selected_cases()
Get a list of all cases selected in the project tree


* **Returns**

    A list of rips Case objects



#### set_fracture_containment(template_id, top_layer, base_layer)
Set fracture template containment parameters


* **Parameters**

    * **template_id** (*int*) -- ID of fracture template

    * **top_layer** (*int*) -- Top layer containment

    * **base_layer** (*int*) -- Base layer containment



#### view(view_id)
Get a particular view belonging to a case by providing view id


* **Parameters**

    **id** (*int*) -- view id


Returns: a view object


#### views()
Get a list of views belonging to a project

# View Module


#### class rips.view.View(pdm_object)
ResInsight view class


#### id()
View Id corresponding to the View Id in ResInsight project.


* **Type**

    int



#### apply_cell_result(result_type, result_variable)
Apply a regular cell result


* **Parameters**

    * **result_type** (*str*) -- String representing the result category. The valid values are
      - DYNAMIC_NATIVE
      - STATIC_NATIVE
      - SOURSIMRL
      - GENERATED
      - INPUT_PROPERTY
      - FORMATION_NAMES
      - FLOW_DIAGNOSTICS
      - INJECTION_FLOODING

    * **result_variable** (*str*) -- String representing the result variable.



#### apply_flow_diagnostics_cell_result(result_variable='TOF', selection_mode='FLOW_TR_BY_SELECTION', injectors=None, producers=None)
Apply a flow diagnostics cell result

Parameter           | Description                                            | Type
------------------- | ------------------------------------------------------ | -----
result_variable     | String representing the result value                   | String
selection_mode      | String specifying which tracers to select              | String
injectors           | List of injector names, used by 'FLOW_TR_BY_SELECTION' | String List
producers           | List of injector names, used by 'FLOW_TR_BY_SELECTION' | String List

##### Enum compdat_export

Option                  | Description
------------------------| ------------
"TOF"                   | Time of flight
"Fraction"              | Fraction
"MaxFractionTracer"     | Max Fraction Tracer
"Communication"         | Communication


#### background_color()
Get the current background color in the view


#### case()
Get the case the view belongs to


#### clone()
Clone the current view


#### export_property(undefined_value=0.0)
Export the current Eclipse property from the view


* **Parameters**

    **undefined_value** (*double*) -- Value to use for undefined values. Defaults to 0.0



#### export_sim_well_fracture_completions(time_step, simulation_well_names, file_split, compdat_export)
Export fracture completions for simulation wells

Parameter                   | Description                                      | Type
----------------------------| ------------------------------------------------ | -----
time_step                   | Time step to export for                          | Integer
simulation_well_names       | List of simulation well names                    | List
file_split                  | Controls how export data is split into files     | String enum
compdat_export              | Compdat export type                              | String enum

##### Enum file_split

Option                              | Description
----------------------------------- | ------------
"UNIFIED_FILE" <b>Default Option</b>| A single file with all transmissibilities
"SPLIT_ON_WELL"                     | One file for each well transmissibilities
"SPLIT_ON_WELL_AND_COMPLETION_TYPE" | One file for each completion type for each well

##### Enum compdat_export

Option                                   | Description
-----------------------------------------| ------------
"TRANSMISSIBILITIES"<b>Default Option</b>| Direct export of transmissibilities
"WPIMULT_AND_DEFAULT_CONNECTION_FACTORS" | Include export of WPIMULT


#### export_snapshot(prefix='')
Export snapshot for the current view


* **Parameters**

    **prefix** (*str*) -- Exported file name prefix



#### export_visible_cells(export_keyword='FLUXNUM', visible_active_cells_value=1, hidden_active_cells_value=0, inactive_cells_value=0)
Export special properties for all visible cells.


* **Parameters**

    * **export_keyword** (*string*) -- The keyword to export.

    * **Choices** -- 'FLUXNUM' or 'MULTNUM'. Default: 'FLUXNUM'

    * **visible_active_cells_value** (*int*) -- Value to export forvisible active cells. Default: 1

    * **hidden_active_cells_value** (*int*) -- Value to export for hidden active cells. Default: 0

    * **inactive_cells_value** (*int*) -- Value to export for inactive cells. Default: 0



#### set_background_color(bgcolor)
Set the background color in the view


#### set_cell_result()
Retrieve the current cell results


#### set_show_grid_box(value)
Set if the grid box is meant to be shown in the view


#### set_time_step(time_step)
Set the time step for current view


#### show_grid_box()
Check if the grid box is meant to be shown in the view

## Synchronous Example

Read two properties, multiply them together and push the results back to ResInsight in a naïve way, by reading PORO into a list, then reading PERMX into a list, then multiplying them both in a resulting list and finally transferring back the list.

This is slow and inefficient, but works.

```
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

## Asynchronous Example

Read two properties at the same time chunk by chunk, multiply each chunk together and start transferring the result back to ResInsight as soon as the chunk is finished.

This is far more efficient.

```
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
