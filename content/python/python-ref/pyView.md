+++
title = "View"
published = true
+++


# View
```python
View(self, pb2_object=None, channel=None)
```

**Attributes**:

- `background_color` _str_ - Background
- `current_time_step` _int_ - Current Time Step
- `disable_lighting` _str_ - Disable Results Lighting
- `grid_z_scale` _float_ - Z Scale
- `id` _int_ - View ID
- `perspective_projection` _str_ - Perspective Projection
- `show_grid_box` _str_ - Show Grid Box
- `show_z_scale` _str_ - Show Z Scale Label
  

## apply_cell_result
```python
View.apply_cell_result(result_type, result_variable)
```
Apply a regular cell result

**Arguments**:

- `result_type` _str_ - String representing the result category. The valid values are
  - DYNAMIC_NATIVE
  - STATIC_NATIVE
  - SOURSIMRL
  - GENERATED
  - INPUT_PROPERTY
  - FORMATION_NAMES
  - FLOW_DIAGNOSTICS
  - INJECTION_FLOODING
- `result_variable` _str_ - String representing the result variable.
  

## apply_flow_diagnostics_cell_result
```python
View.apply_flow_diagnostics_cell_result(
result_variable='TOF',
selection_mode='FLOW_TR_BY_SELECTION',
injectors=None,
producers=None)
```
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



## clone
```python
View.clone()
```
Clone the current view

## set_time_step
```python
View.set_time_step(time_step)
```
Set the time step for current view

## export_sim_well_fracture_completions
```python
View.export_sim_well_fracture_completions(time_step,
simulation_well_names,
file_split, compdat_export)
```
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



## export_visible_cells
```python
View.export_visible_cells(export_keyword='FLUXNUM',
visible_active_cells_value=1,
hidden_active_cells_value=0,
inactive_cells_value=0)
```
Export special properties for all visible cells.

**Arguments**:

- `export_keyword` _string_ - The keyword to export.
- `Choices` - 'FLUXNUM' or 'MULTNUM'. Default: 'FLUXNUM'
- `visible_active_cells_value` _int_ - Value to export forvisible active cells. Default: 1
- `hidden_active_cells_value` _int_ - Value to export for hidden active cells. Default: 0
- `inactive_cells_value` _int_ - Value to export for inactive cells. Default: 0
  

## export_property
```python
View.export_property(undefined_value=0.0)
```
Export the current Eclipse property from the view

**Arguments**:

- `undefined_value` _double_ - Value to use for undefined values. Defaults to 0.0
  
