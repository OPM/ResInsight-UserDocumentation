+++
title = "Case"
published = true
+++


# Case
```python
Case(self, pb2_object=None, channel=None)
```

The ResInsight base class for Cases

**Attributes**:

- `file_path` _str_ - Case File Name
- `id` _int_ - Case ID
- `name` _str_ - Case Name
  

## grid
```python
Case.grid(index)
```
Get Grid of a given index. Returns a rips Grid object

**Arguments**:

- `index` _int_ - The grid index
  
- `Returns` - Grid object
  

## grids
```python
Case.grids()
```
Get a list of all rips Grid objects in the case

## replace
```python
Case.replace(new_grid_file)
```
Replace the current case grid with a new grid loaded from file

**Arguments**:

- `new_egrid_file` _str_ - path to EGRID file
  

## cell_count
```python
Case.cell_count(porosity_model='MATRIX_MODEL')
```
Get a cell count object containing number of active cells and
total number of cells

**Arguments**:

- `porosity_model` _str_ - String representing an enum.
  must be 'MATRIX_MODEL' or 'FRACTURE_MODEL'.

**Returns**:

  Cell Count object with the following integer attributes:
- `active_cell_count` - number of active cells
- `reservoir_cell_count` - total number of reservoir cells
  

## cell_info_for_active_cells_async
```python
Case.cell_info_for_active_cells_async(porosity_model='MATRIX_MODEL')
```
Get Stream of cell info objects for current case

**Arguments**:

- `porosity_model(str)` - String representing an enum.
  must be 'MATRIX_MODEL' or 'FRACTURE_MODEL'.
  

**Returns**:

  Stream of **CellInfo** objects
  
  See cell_info_for_active_cells() for detalis on the **CellInfo** class.
  

## cell_info_for_active_cells
```python
Case.cell_info_for_active_cells(porosity_model='MATRIX_MODEL')
```
Get list of cell info objects for current case

**Arguments**:

- `porosity_model(str)` - String representing an enum.
  must be 'MATRIX_MODEL' or 'FRACTURE_MODEL'.
  

**Returns**:

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
  
  

## time_steps
```python
Case.time_steps()
```
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




## reservoir_boundingbox
```python
Case.reservoir_boundingbox()
```
Get the reservoir bounding box

Returns: A class with six double members: min_x, max_x, min_y, max_y, min_z, max_z


## reservoir_depth_range
```python
Case.reservoir_depth_range()
```
Get the reservoir depth range

Returns: A tuple with two members. The first is the minimum depth, the second is the maximum depth


## days_since_start
```python
Case.days_since_start()
```
Get a list of decimal values representing days since the start of the simulation

## view
```python
Case.view(view_id)
```
Get a particular view belonging to a case by providing view id

**Arguments**:

- `view_id(int)` - view id
  
- `Returns` - a view object
  
  

## create_view
```python
Case.create_view()
```
Create a new view in the current case

## export_snapshots_of_all_views
```python
Case.export_snapshots_of_all_views(prefix='', export_folder='')
```
Export snapshots for all views in the case

**Arguments**:

- `prefix` _str_ - Exported file name prefix
- `export_folder(str)` - The path to export to. By default will use the global export folder
  
  

## export_well_path_completions
```python
Case.export_well_path_completions(time_step,
well_path_names,
file_split,
compdat_export='TRANSMISSIBILITIES',
include_perforations=True,
include_fishbones=True,
fishbones_exclude_main_bore=True,
combination_mode='INDIVIDUALLY')
```

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



## export_msw
```python
Case.export_msw(well_path)
```

Export Eclipse Multi-segment-well model to file

**Arguments**:

- `well_path(str)` - Well path name
  

## create_multiple_fractures
```python
Case.create_multiple_fractures(template_id, well_path_names,
min_dist_from_well_td,
max_fractures_per_well, top_layer,
base_layer, spacing, action)
```

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


## create_lgr_for_completion
```python
Case.create_lgr_for_completion(time_step, well_path_names, refinement_i,
refinement_j, refinement_k, split_type)
```

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



## create_saturation_pressure_plots
```python
Case.create_saturation_pressure_plots()
```

Create saturation pressure plots for the current case


## export_flow_characteristics
```python
Case.export_flow_characteristics(time_steps,
injectors,
producers,
file_name,
minimum_communication=0.0,
aquifer_cell_threshold=0.1)
```
Export Flow Characteristics data to text file in CSV format

Parameter                 | Description                                   | Type
------------------------- | --------------------------------------------- | -----
time_steps                | Time step indices                             | List of Integer
injectors                 | Injector names                                | List of Strings
producers                 | Producer names                                | List of Strings
file_name                 | Export file name                              | Integer
minimum_communication     | Minimum Communication, defaults to 0.0        | Integer
aquifer_cell_threshold    | Aquifer Cell Threshold, defaults to 0.1       | Integer



## available_properties
```python
Case.available_properties(property_type, porosity_model='MATRIX_MODEL')
```
Get a list of available properties

**Arguments**:

- `property_type` _str_ - string corresponding to property_type enum. Choices:
  - DYNAMIC_NATIVE
  - STATIC_NATIVE
  - SOURSIMRL
  - GENERATED
  - INPUT_PROPERTY
  - FORMATION_NAMES
  - FLOW_DIAGNOSTICS
  - INJECTION_FLOODING
  
- `porosity_model(str)` - 'MATRIX_MODEL' or 'FRACTURE_MODEL'.
  

## active_cell_property_async
```python
Case.active_cell_property_async(property_type,
property_name,
time_step,
porosity_model='MATRIX_MODEL')
```
Get a cell property for all active cells. Async, so returns an iterator

**Arguments**:

- `property_type(str)` - string enum. See available()
- `property_name(str)` - name of an Eclipse property
- `time_step(int)` - the time step for which to get the property for
- `porosity_model(str)` - string enum. See available()
  

**Returns**:

  An iterator to a chunk object containing an array of double values
  Loop through the chunks and then the values within the chunk to get all values.
  

## active_cell_property
```python
Case.active_cell_property(property_type,
property_name,
time_step,
porosity_model='MATRIX_MODEL')
```
Get a cell property for all active cells. Sync, so returns a list

**Arguments**:

- `property_type(str)` - string enum. See available()
- `property_name(str)` - name of an Eclipse property
- `time_step(int)` - the time step for which to get the property for
- `porosity_model(str)` - string enum. See available()
  

**Returns**:

  A list containing double values
  Loop through the chunks and then the values within the chunk to get all values.
  

## selected_cell_property_async
```python
Case.selected_cell_property_async(property_type,
property_name,
time_step,
porosity_model='MATRIX_MODEL')
```
Get a cell property for all selected cells. Async, so returns an iterator

**Arguments**:

- `property_type(str)` - string enum. See available()
- `property_name(str)` - name of an Eclipse property
- `time_step(int)` - the time step for which to get the property for
- `porosity_model(str)` - string enum. See available()
  

**Returns**:

  An iterator to a chunk object containing an array of double values
  Loop through the chunks and then the values within the chunk to get all values.
  

## selected_cell_property
```python
Case.selected_cell_property(property_type,
property_name,
time_step,
porosity_model='MATRIX_MODEL')
```
Get a cell property for all selected cells. Sync, so returns a list

**Arguments**:

- `property_type(str)` - string enum. See available()
- `property_name(str)` - name of an Eclipse property
- `time_step(int)` - the time step for which to get the property for
- `porosity_model(str)` - string enum. See available()
  

**Returns**:

  A list containing double values
  Loop through the chunks and then the values within the chunk to get all values.
  

## grid_property_async
```python
Case.grid_property_async(property_type,
property_name,
time_step,
grid_index=0,
porosity_model='MATRIX_MODEL')
```
Get a cell property for all grid cells. Async, so returns an iterator

**Arguments**:

- `property_type(str)` - string enum. See available()
- `property_name(str)` - name of an Eclipse property
- `time_step(int)` - the time step for which to get the property for
- `gridIndex(int)` - index to the grid we're getting values for
- `porosity_model(str)` - string enum. See available()
  

**Returns**:

  An iterator to a chunk object containing an array of double values
  Loop through the chunks and then the values within the chunk to get all values.
  

## grid_property
```python
Case.grid_property(property_type,
property_name,
time_step,
grid_index=0,
porosity_model='MATRIX_MODEL')
```
Get a cell property for all grid cells. Synchronous, so returns a list

**Arguments**:

- `property_type(str)` - string enum. See available()
- `property_name(str)` - name of an Eclipse property
- `time_step(int)` - the time step for which to get the property for
- `grid_index(int)` - index to the grid we're getting values for
- `porosity_model(str)` - string enum. See available()
  

**Returns**:

  A list of double values
  

## set_active_cell_property_async
```python
Case.set_active_cell_property_async(values_iterator,
property_type,
property_name,
time_step,
porosity_model='MATRIX_MODEL')
```
Set cell property for all active cells Async. Takes an iterator to the input values

**Arguments**:

- `values_iterator(iterator)` - an iterator to the properties to be set
- `property_type(str)` - string enum. See available()
- `property_name(str)` - name of an Eclipse property
- `time_step(int)` - the time step for which to get the property for
- `porosity_model(str)` - string enum. See available()
  

## set_active_cell_property
```python
Case.set_active_cell_property(values,
property_type,
property_name,
time_step,
porosity_model='MATRIX_MODEL')
```
Set a cell property for all active cells.

**Arguments**:

- `values(list)` - a list of double precision floating point numbers
- `property_type(str)` - string enum. See available()
- `property_name(str)` - name of an Eclipse property
- `time_step(int)` - the time step for which to get the property for
- `porosity_model(str)` - string enum. See available()
  

## set_grid_property
```python
Case.set_grid_property(values,
property_type,
property_name,
time_step,
grid_index=0,
porosity_model='MATRIX_MODEL')
```
Set a cell property for all grid cells.

**Arguments**:

- `values(list)` - a list of double precision floating point numbers
- `property_type(str)` - string enum. See available()
- `property_name(str)` - name of an Eclipse property
- `time_step(int)` - the time step for which to get the property for
- `grid_index(int)` - index to the grid we're setting values for
- `porosity_model(str)` - string enum. See available()
  

## export_property
```python
Case.export_property(time_step,
property_name,
eclipse_keyword=property,
undefined_value=0.0,
export_file=property)
```
Export an Eclipse property

**Arguments**:

- `time_step` _int_ - time step index
- `property_name` _str_ - property to export
- `eclipse_keyword` _str_ - Keyword used in export header. Defaults: value of property
- `undefined_value` _double_ - Value to use for undefined values. Defaults to 0.0
- `export_file` _str_ - File name for export. Defaults to the value of property parameter
  

## create_well_bore_stability_plot
```python
Case.create_well_bore_stability_plot(well_path,
time_step,
parameters=None)
```
Create a new well bore stability plot

**Arguments**:

- `well_path(str)` - well path name
- `time_step(int)` - time step
  

**Returns**:

  A new plot object
  

## import_formation_names
```python
Case.import_formation_names(formation_files=None)
```
Import formation names into project and apply it to the current case

**Arguments**:

- `formation_files(list)` - list of files to import
  
  

## simulation_wells
```python
Case.simulation_wells()
```
Get a list of all simulation wells for a case

**Returns**:

  A list of rips **SimulationWell** objects
  

## active_cell_centers_async
```python
Case.active_cell_centers_async(porosity_model='MATRIX_MODEL')
```
Get a cell centers for all active cells. Async, so returns an iterator

**Arguments**:

- `porosity_model(str)` - string enum. See available()
  

**Returns**:

  An iterator to a chunk object containing an array of Vec3d values.
  Loop through the chunks and then the values within the chunk to get all values.
  

## active_cell_centers
```python
Case.active_cell_centers(porosity_model='MATRIX_MODEL')
```
Get a cell centers for all active cells. Synchronous, so returns a list.

**Arguments**:

- `porosity_model(str)` - string enum. See available()
  

**Returns**:

  A list of Vec3d
  

## active_cell_corners_async
```python
Case.active_cell_corners_async(porosity_model='MATRIX_MODEL')
```
Get a cell corners for all active cells. Async, so returns an iterator

**Arguments**:

- `porosity_model(str)` - string enum. See available()
  

**Returns**:

  An iterator to a chunk object containing an array of CellCorners (which is eight Vec3d values).
  Loop through the chunks and then the values within the chunk to get all values.
  

## active_cell_corners
```python
Case.active_cell_corners(porosity_model='MATRIX_MODEL')
```
Get a cell corners for all active cells. Synchronous, so returns a list.

**Arguments**:

- `porosity_model(str)` - string enum. See available()
  

**Returns**:

  A list of CellCorners
  

## selected_cells_async
```python
Case.selected_cells_async()
```
Get the selected cells. Async, so returns an iterator.

**Returns**:

  An iterator to a chunk object containing an array of cells.
  Loop through the chunks and then the cells within the chunk to get all cells.
  

## selected_cells
```python
Case.selected_cells()
```
Get the selected cells. Synchronous, so returns a list.

**Returns**:

  A list of Cells.
  

## coarsening_info
```python
Case.coarsening_info()
```
Get a coarsening information for all grids in the case.

**Returns**:

  A list of CoarseningInfo objects with two Vec3i min and max objects
  for each entry.
  

## available_nnc_properties
```python
Case.available_nnc_properties()
```
Get a list of available NNC properties


## nnc_connections_async
```python
Case.nnc_connections_async()
```
Get the NNC connections. Async, so returns an iterator.

**Returns**:

  An iterator to a chunk object containing an array NNCConnection objects.
  Loop through the chunks and then the connection within the chunk to get all connections.
  

## nnc_connections
```python
Case.nnc_connections()
```
Get the NNC connection. Synchronous, so returns a list.

**Returns**:

  A list of NNCConnection objects.
  

## nnc_connections_static_values_async
```python
Case.nnc_connections_static_values_async(property_name)
```
Get the static NNC values. Async, so returns an iterator.

**Returns**:

  An iterator to a chunk object containing an list of doubles.
  Loop through the chunks and then the values within the chunk to get values
  for all the connections. The order of the list matches the list from
  nnc_connections, i.e. the nth object of nnc_connections() refers to nth
  value in this list.
  

## nnc_connections_static_values
```python
Case.nnc_connections_static_values(property_name)
```
Get the static NNC values.

**Returns**:

  A list of doubles. The order of the list matches the list from
  nnc_connections, i.e. the nth object of nnc_connections() refers to nth
  value in this list.
  

## nnc_connections_dynamic_values_async
```python
Case.nnc_connections_dynamic_values_async(property_name, time_step)
```
Get the dynamic NNC values. Async, so returns an iterator.

**Returns**:

  An iterator to a chunk object containing an list of doubles.
  Loop through the chunks and then the values within the chunk to get values
  for all the connections. The order of the list matches the list from
  nnc_connections, i.e. the nth object of nnc_connections() refers to nth
  value in this list.
  

## nnc_connections_dynamic_values
```python
Case.nnc_connections_dynamic_values(property_name, time_step)
```
Get the dynamic NNC values.

**Returns**:

  A list of doubles. The order of the list matches the list from
  nnc_connections, i.e. the nth object of nnc_connections() refers to nth
  value in this list.
  

## nnc_connections_generated_values_async
```python
Case.nnc_connections_generated_values_async(property_name, time_step)
```
Get the generated NNC values. Async, so returns an iterator.

**Returns**:

  An iterator to a chunk object containing an list of doubles.
  Loop through the chunks and then the values within the chunk to get values
  for all the connections. The order of the list matches the list from
  nnc_connections, i.e. the nth object of nnc_connections() refers to nth
  value in this list.
  

## nnc_connections_generated_values
```python
Case.nnc_connections_generated_values(property_name, time_step)
```
Get the generated NNC values.

**Returns**:

  A list of doubles. The order of the list matches the list from
  nnc_connections, i.e. the nth object of nnc_connections() refers to nth
  value in this list.
  

## set_nnc_connections_values
```python
Case.set_nnc_connections_values(values,
property_name,
time_step,
porosity_model='MATRIX_MODEL')
```
Set nnc connection values for all connections..

**Arguments**:

- `values(list)` - a list of double precision floating point numbers
- `property_name(str)` - name of an Eclipse property
- `time_step(int)` - the time step for which to get the property for
- `porosity_model(str)` - string enum. See available()
  
