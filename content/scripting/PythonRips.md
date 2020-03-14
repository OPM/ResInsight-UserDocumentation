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


#### set_plot_window_size(width, height)
Set the plot window size in pixels

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


#### class rips.case.Case(pb2_object=None, channel=None)
The ResInsight base class for Cases


#### file_path()
Case File Name


* **Type**

    str



#### id()
Case ID


* **Type**

    int



#### name()
Case Name


* **Type**

    str



#### active_cell_centers(porosity_model='MATRIX_MODEL')
Get a cell centers for all active cells. Synchronous, so returns a list.


* **Parameters**

    **porosity_model** (*str*) -- string enum. See available()



* **Returns**

    A list of Vec3d



#### active_cell_centers_async(porosity_model='MATRIX_MODEL')
Get a cell centers for all active cells. Async, so returns an iterator


* **Parameters**

    **porosity_model** (*str*) -- string enum. See available()



* **Returns**

    An iterator to a chunk object containing an array of Vec3d values.
    Loop through the chunks and then the values within the chunk to get all values.



#### active_cell_corners(porosity_model='MATRIX_MODEL')
Get a cell corners for all active cells. Synchronous, so returns a list.


* **Parameters**

    **porosity_model** (*str*) -- string enum. See available()



* **Returns**

    A list of CellCorners



#### active_cell_corners_async(porosity_model='MATRIX_MODEL')
Get a cell corners for all active cells. Async, so returns an iterator


* **Parameters**

    **porosity_model** (*str*) -- string enum. See available()



* **Returns**

    An iterator to a chunk object containing an array of CellCorners (which is eight Vec3d values).
    Loop through the chunks and then the values within the chunk to get all values.



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



#### available_nnc_properties()
Get a list of available NNC properties


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


#### coarsening_info()
Get a coarsening information for all grids in the case.


* **Returns**

    A list of CoarseningInfo objects with two Vec3i min and max objects
    for each entry.



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


#### create_well_bore_stability_plot(well_path, time_step, parameters=None)
Create a new well bore stability plot


* **Parameters**

    * **well_path** (*str*) -- well path name

    * **time_step** (*int*) -- time step



* **Returns**

    A new plot object



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



#### export_snapshots_of_all_views(prefix='', export_folder='')
Export snapshots for all views in the case


* **Parameters**

    * **prefix** (*str*) -- Exported file name prefix

    * **export_folder** (*str*) -- The path to export to. By default will use the global export folder



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


#### import_formation_names(formation_files=None)
Import formation names into project and apply it to the current case


* **Parameters**

    **formation_files** (*list*) -- list of files to import



#### nnc_connections()
Get the NNC connection. Synchronous, so returns a list.


* **Returns**

    A list of NNCConnection objects.



#### nnc_connections_async()
Get the NNC connections. Async, so returns an iterator.


* **Returns**

    An iterator to a chunk object containing an array NNCConnection objects.
    Loop through the chunks and then the connection within the chunk to get all connections.



#### nnc_connections_dynamic_values(property_name, time_step)
Get the dynamic NNC values.


* **Returns**

    A list of doubles. The order of the list matches the list from
    nnc_connections, i.e. the nth object of nnc_connections() refers to nth
    value in this list.



#### nnc_connections_dynamic_values_async(property_name, time_step)
Get the dynamic NNC values. Async, so returns an iterator.


* **Returns**

    An iterator to a chunk object containing an list of doubles.
    Loop through the chunks and then the values within the chunk to get values
    for all the connections. The order of the list matches the list from
    nnc_connections, i.e. the nth object of nnc_connections() refers to nth
    value in this list.



#### nnc_connections_generated_values(property_name, time_step)
Get the generated NNC values.


* **Returns**

    A list of doubles. The order of the list matches the list from
    nnc_connections, i.e. the nth object of nnc_connections() refers to nth
    value in this list.



#### nnc_connections_generated_values_async(property_name, time_step)
Get the generated NNC values. Async, so returns an iterator.


* **Returns**

    An iterator to a chunk object containing an list of doubles.
    Loop through the chunks and then the values within the chunk to get values
    for all the connections. The order of the list matches the list from
    nnc_connections, i.e. the nth object of nnc_connections() refers to nth
    value in this list.



#### nnc_connections_static_values(property_name)
Get the static NNC values.


* **Returns**

    A list of doubles. The order of the list matches the list from
    nnc_connections, i.e. the nth object of nnc_connections() refers to nth
    value in this list.



#### nnc_connections_static_values_async(property_name)
Get the static NNC values. Async, so returns an iterator.


* **Returns**

    An iterator to a chunk object containing an list of doubles.
    Loop through the chunks and then the values within the chunk to get values
    for all the connections. The order of the list matches the list from
    nnc_connections, i.e. the nth object of nnc_connections() refers to nth
    value in this list.



#### replace(new_grid_file)
Replace the current case grid with a new grid loaded from file


* **Parameters**

    **new_egrid_file** (*str*) -- path to EGRID file



#### reservoir_boundingbox()
Get the reservoir bounding box

Returns: A class with six double members: min_x, max_x, min_y, max_y, min_z, max_z


#### reservoir_depth_range()
Get the reservoir depth range

Returns: A tuple with two members. The first is the minimum depth, the second is the maximum depth


#### selected_cell_property(property_type, property_name, time_step, porosity_model='MATRIX_MODEL')
Get a cell property for all selected cells. Sync, so returns a list


* **Parameters**

    * **property_type** (*str*) -- string enum. See available()

    * **property_name** (*str*) -- name of an Eclipse property

    * **time_step** (*int*) -- the time step for which to get the property for

    * **porosity_model** (*str*) -- string enum. See available()



* **Returns**

    A list containing double values
    Loop through the chunks and then the values within the chunk to get all values.



#### selected_cell_property_async(property_type, property_name, time_step, porosity_model='MATRIX_MODEL')
Get a cell property for all selected cells. Async, so returns an iterator


* **Parameters**

    * **property_type** (*str*) -- string enum. See available()

    * **property_name** (*str*) -- name of an Eclipse property

    * **time_step** (*int*) -- the time step for which to get the property for

    * **porosity_model** (*str*) -- string enum. See available()



* **Returns**

    An iterator to a chunk object containing an array of double values
    Loop through the chunks and then the values within the chunk to get all values.



#### selected_cells()
Get the selected cells. Synchronous, so returns a list.


* **Returns**

    A list of Cells.



#### selected_cells_async()
Get the selected cells. Async, so returns an iterator.


* **Returns**

    An iterator to a chunk object containing an array of cells.
    Loop through the chunks and then the cells within the chunk to get all cells.



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



#### set_nnc_connections_values(values, property_name, time_step, porosity_model='MATRIX_MODEL')
Set nnc connection values for all connections..


* **Parameters**

    * **values** (*list*) -- a list of double precision floating point numbers

    * **property_name** (*str*) -- name of an Eclipse property

    * **time_step** (*int*) -- the time step for which to get the property for

    * **porosity_model** (*str*) -- string enum. See available()



#### simulation_wells()
Get a list of all simulation wells for a case


* **Returns**

    A list of rips **SimulationWell** objects



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
        print("Case id: " + str(case.id))
        print("Case name: " + case.name)
        print("Case type: " + case.__class__.__name__)
        print("Case file name: " + case.file_path)
        print("Case reservoir bounding box:", case.reservoir_boundingbox())

        timesteps = case.time_steps()
        for t in timesteps:
            print("Year: " + str(t.year))
            print("Month: " + str(t.month))

        if isinstance(case, rips.EclipseCase):
            print ("Getting coarsening info for case: ", case.name, case.id)
            coarsening_info = case.coarsening_info()
            if coarsening_info:
                print("Coarsening information:")

            for c in coarsening_info:
                print("[{}, {}, {}] - [{}, {}, {}]".format(c.min.x, c.min.y, c.min.z,
                                                           c.max.x, c.max.y, c.max.z))
```

# Contour Map Module


#### class rips.contour_map.EclipseContourMap(pb2_object=None, channel=None)
A contour map for Eclipse cases


#### export_to_text(export_file_name='', export_local_coordinates=False, undefined_value_label='NaN', exclude_undefined_values=False)
Export snapshot for the current view


* **Parameters**

    * **export_file_name** (*str*) -- The file location to store results in.

    * **export_local_coordinates** (*bool*) -- Should we export local coordinates, or UTM.

    * **undefined_value_label** (*str*) -- Replace undefined values with this label.

    * **exclude_undefined_values** (*bool*) -- Skip undefined values.



#### class rips.contour_map.GeoMechContourMap(pb2_object=None, channel=None)
A contour map for GeoMech cases


#### export_to_text(export_file_name='', export_local_coordinates=False, undefined_value_label='NaN', exclude_undefined_values=False)
Export snapshot for the current view


* **Parameters**

    * **export_file_name** (*str*) -- The file location to store results in.

    * **export_local_coordinates** (*bool*) -- Should we export local coordinates, or UTM.

    * **undefined_value_label** (*str*) -- Replace undefined values with this label.

    * **exclude_undefined_values** (*bool*) -- Skip undefined values.


# Grid Module


#### class rips.grid.Grid(index, case, channel)
Grid Information. Not meant to be constructed separately

Create Grid objects using methods on Case: Grid() and Grids()


#### cell_centers()
The cell center for all cells in given grid


* **Returns**

    class with double attributes x, y, x giving cell centers



* **Return type**

    List of Vec3d



#### cell_centers_async()
The cells center for all cells in given grid async.


* **Returns**

    class with double attributes x, y, x giving cell centers



* **Return type**

    Iterator to a list of Vec3d



#### cell_corners()
The cell corners for all cells in given grid


* **Returns**

    a class with Vec3d for each corner (c0, c1.., c7)



* **Return type**

    list of CellCorners



#### cell_corners_async()
The cell corners for all cells in given grid, async.


* **Returns**

    a class with Vec3d for each corner (c0, c1.., c7)



* **Return type**

    iterator to a list of CellCorners



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


#### class rips.gridcasegroup.GridCaseGroup(pb2_object=None, channel=None)
A statistics case group


#### group_id()
Case Group ID


* **Type**

    int



#### user_description()
Name


* **Type**

    str



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

# Plot Module


#### class rips.project.Plot(pb2_object=None, channel=None)
The Abstract Base Class for all Plot Objects

# Project Module


#### class rips.project.Project(pb2_object=None, channel=None)
The ResInsight Project


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



#### export_snapshots(snapshot_type='ALL', prefix='', plot_format='PNG')
Export all snapshots of a given type


* **Parameters**

    * **snapshot_type** (*str*) -- Enum string ('ALL', 'VIEWS' or 'PLOTS')

    * **prefix** (*str*) -- Exported file name prefix

    * **plot_format** (*str*) -- Enum string, 'PNG' or 'PDF'



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


#### import_formation_names(formation_files=None)
Import formation names into project


* **Parameters**

    **formation_files** (*list*) -- list of files to import



#### import_well_log_files(well_log_files=None, well_log_folder='')
Import well log files into project


* **Parameters**

    * **well_log_files** (*list*) -- List of file paths to import

    * **well_log_folder** (*str*) -- A folder path containing files to import



* **Returns**

    A list of well path names (strings) that had logs imported



#### import_well_paths(well_path_files=None, well_path_folder='')
Import well paths into project


* **Parameters**

    * **well_path_files** (*list*) -- List of file paths to import

    * **well_path_folder** (*str*) -- A folder path containing files to import



* **Returns**

    A list of WellPath objects



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



#### plot(view_id)
Get a particular plot by providing view id
:param view_id: view id
:type view_id: int

Returns: a plot object


#### plots()
Get a list of all plots belonging to a project


#### replace_source_cases(grid_list_file, case_group_id=0)
Replace all source cases within a case group


* **Parameters**

    * **grid_list_file** (*str*) -- path to file containing a list of cases

    * **case_group_id** (*int*) -- id of the case group to replace



#### save(path='')
Save the project to the existing project file, or to a new file
:param path: File path to the file to save the project to. If empty, saves to the active project file
:type path: str


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

    **view_id** (*int*) -- view id


Returns: a view object


#### views()
Get a list of views belonging to a project


#### well_path_by_name(well_path_name)
Get a specific well path by name from the project


* **Returns**

    A WellPath object



#### well_paths()
Get a list of all well paths in the project


* **Returns**

    A list of rips WellPath objects


# Simulation Well Module


#### class rips.simulation_well.SimulationWell(pb2_object=None, channel=None)
An Eclipse Simulation Well


#### name()
Name


* **Type**

    str


# View Module


#### class rips.view.View(pb2_object=None, channel=None)

#### background_color()
Background


* **Type**

    str



#### current_time_step()
Current Time Step


* **Type**

    int



#### disable_lighting()
Disable Results Lighting


* **Type**

    str



#### grid_z_scale()
Z Scale


* **Type**

    float



#### id()
View ID


* **Type**

    int



#### perspective_projection()
Perspective Projection


* **Type**

    str



#### show_grid_box()
Show Grid Box


* **Type**

    str



#### show_z_scale()
Show Z Scale Label


* **Type**

    str



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


#### export_visible_cells(export_keyword='FLUXNUM', visible_active_cells_value=1, hidden_active_cells_value=0, inactive_cells_value=0)
Export special properties for all visible cells.


* **Parameters**

    * **export_keyword** (*string*) -- The keyword to export.

    * **Choices** -- 'FLUXNUM' or 'MULTNUM'. Default: 'FLUXNUM'

    * **visible_active_cells_value** (*int*) -- Value to export forvisible active cells. Default: 1

    * **hidden_active_cells_value** (*int*) -- Value to export for hidden active cells. Default: 0

    * **inactive_cells_value** (*int*) -- Value to export for inactive cells. Default: 0



#### set_time_step(time_step)
Set the time step for current view

# Well Log Plot Module


#### class rips.well_log_plot.WellLogPlot(pb2_object=None, channel=None)
A Well Log Plot With a shared Depth Axis and Multiple Tracks


#### auto_scale_depth_enabled()
Auto Scale


* **Type**

    str



#### depth_type()
Type


* **Type**

    str



#### depth_unit()
Unit


* **Type**

    str



#### maximum_depth()
Max


* **Type**

    float



#### minimum_depth()
Min


* **Type**

    float



#### show_depth_grid_lines()
Show Grid Lines


* **Type**

    str



#### show_title_in_plot()
Show Title


* **Type**

    str



#### export_data_as_ascii(export_folder, file_prefix='', capitalize_file_names=False)
Export LAS file(s) for the current plot


* **Parameters**

    * **export_folder** (*str*) -- The path to export to. By default will use the global export folder

    * **file_prefix** (*str*) -- Exported file name prefix

    * **capitalize_file_names** (*bool*) -- Make all file names upper case



* **Returns**

    A list of files exported



#### export_data_as_las(export_folder, file_prefix='', export_tvdrkb=False, capitalize_file_names=False, resample_interval=0.0, convert_to_standard_units=False)
Export LAS file(s) for the current plot


* **Parameters**

    * **export_folder** (*str*) -- The path to export to. By default will use the global export folder

    * **file_prefix** (*str*) -- Exported file name prefix

    * **export_tvdrkb** (*bool*) -- Export in TVD-RKB format

    * **capitalize_file_names** (*bool*) -- Make all file names upper case

    * **resample_interval** (*double*) -- if > 0.0 the files will be resampled



* **Returns**

    A list of files exported


## Synchronous Example

Read two properties, multiply them together and push the results back to ResInsight in a naïve way, by reading PORO into a list, then reading PERMX into a list, then multiplying them both in a resulting list and finally transferring back the list.

This is slow and inefficient, but works.

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
case = resinsight.project.cases()[0]

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

## Asynchronous Example

Read two properties at the same time chunk by chunk, multiply each chunk together and start transferring the result back to ResInsight as soon as the chunk is finished.

This is far more efficient.

```
########################################################################################
import rips
import time
import grpc

resinsight     = rips.Instance.find()
start = time.time()
case = resinsight.project.cases()[0]

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
