+++
title = "Project"
published = true
+++


# Project
```python
Project(self, pb2_object=None, channel=None)
```

The ResInsight Project



## open
```python
Project.open(path)
```
Open a new project from the given path

**Arguments**:

- `path(str)` - path to project file
  
  

## save
```python
Project.save(path='')
```
Save the project to the existing project file, or to a new file

**Arguments**:

- `path(str)` - File path to the file to save the project to. If empty, saves to the active project file
  

## close
```python
Project.close()
```
Close the current project (and open new blank project)

## load_case
```python
Project.load_case(path)
```
Load a new case from the given file path

**Arguments**:

- `path(str)` - file path to case

**Returns**:

  A rips Case object
  

## selected_cases
```python
Project.selected_cases()
```
Get a list of all cases selected in the project tree

**Returns**:

  A list of rips Case objects
  

## cases
```python
Project.cases()
```
Get a list of all cases in the project

**Returns**:

  A list of rips Case objects
  

## case
```python
Project.case(case_id)
```
Get a specific case from the provided case Id

**Arguments**:

- `id(int)` - case id

**Returns**:

  A rips Case object
  

## replace_source_cases
```python
Project.replace_source_cases(grid_list_file, case_group_id=0)
```
Replace all source cases within a case group

**Arguments**:

- `grid_list_file` _str_ - path to file containing a list of cases
- `case_group_id` _int_ - id of the case group to replace
  

## create_grid_case_group
```python
Project.create_grid_case_group(case_paths)
```
Create a Grid Case Group from a list of cases

**Arguments**:

- `case_paths` _list_ - list of file path strings

**Returns**:

  A case group id and name
  

## views
```python
Project.views()
```
Get a list of views belonging to a project

## view
```python
Project.view(view_id)
```
Get a particular view belonging to a case by providing view id

**Arguments**:

- `view_id(int)` - view id
- `Returns` - a view object
  

## plots
```python
Project.plots()
```
Get a list of all plots belonging to a project

## plot
```python
Project.plot(view_id)
```
Get a particular plot by providing view id

**Arguments**:

- `view_id(int)` - view id
- `Returns` - a plot object
  

## grid_case_groups
```python
Project.grid_case_groups()
```
Get a list of all grid case groups in the project

## grid_case_group
```python
Project.grid_case_group(group_id)
```
Get a particular grid case group belonging to a project

**Arguments**:

- `groupId(int)` - group id
  
- `Returns` - a grid case group object
  

## export_multi_case_snapshots
```python
Project.export_multi_case_snapshots(grid_list_file)
```
Export snapshots for a set of cases

**Arguments**:

- `grid_list_file` _str_ - Path to a file containing a list of grids to export snapshot for
  

## export_snapshots
```python
Project.export_snapshots(snapshot_type='ALL',
prefix='',
plot_format='PNG')
```
Export all snapshots of a given type

**Arguments**:

- `snapshot_type` _str_ - Enum string ('ALL', 'VIEWS' or 'PLOTS')
- `prefix` _str_ - Exported file name prefix
- `plot_format(str)` - Enum string, 'PNG' or 'PDF'
  

## export_well_paths
```python
Project.export_well_paths(well_paths=None, md_step_size=5.0)
```
Export a set of well paths

**Arguments**:

- `well_paths(list)` - List of strings of well paths. If none, export all.
- `md_step_size(double)` - resolution of the exported well path
  

## scale_fracture_template
```python
Project.scale_fracture_template(template_id, half_length, height,
d_factor, conductivity)
```
Scale fracture template parameters

**Arguments**:

- `template_id(int)` - ID of fracture template
- `half_length` _double_ - Half Length scale factor
- `height` _double_ - Height scale factor
- `d_factor` _double_ - D-factor scale factor
- `conductivity` _double_ - Conductivity scale factor
  

## set_fracture_containment
```python
Project.set_fracture_containment(template_id, top_layer, base_layer)
```
Set fracture template containment parameters

**Arguments**:

- `template_id(int)` - ID of fracture template
- `top_layer` _int_ - Top layer containment
- `base_layer` _int_ - Base layer containment
  

## import_well_paths
```python
Project.import_well_paths(well_path_files=None, well_path_folder='')
```
Import well paths into project

**Arguments**:

- `well_path_files(list)` - List of file paths to import
- `well_path_folder(str)` - A folder path containing files to import
  

**Returns**:

  A list of WellPath objects
  

## well_paths
```python
Project.well_paths()
```
Get a list of all well paths in the project

**Returns**:

  A list of rips WellPath objects
  

## well_path_by_name
```python
Project.well_path_by_name(well_path_name)
```
Get a specific well path by name from the project

**Returns**:

  A WellPath object
  

## import_well_log_files
```python
Project.import_well_log_files(well_log_files=None, well_log_folder='')
```
Import well log files into project

**Arguments**:

- `well_log_files(list)` - List of file paths to import
- `well_log_folder(str)` - A folder path containing files to import
  

**Returns**:

  A list of well path names (strings) that had logs imported
  

## import_formation_names
```python
Project.import_formation_names(formation_files=None)
```
Import formation names into project

**Arguments**:

- `formation_files(list)` - list of files to import
  
  
