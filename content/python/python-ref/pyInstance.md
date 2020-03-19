+++
title = "Instance"
published = true
+++


# Instance
```python
Instance(self, port=50051, launched=False)
```
The ResInsight Instance class. Use to launch or find existing ResInsight instances

**Attributes**:

- `launched` _bool_ - Tells us whether the application was launched as a new process.
  If the application was launched we may need to close it when exiting the script.
- `commands` _Commands_ - Command executor. Set when creating an instance.
- `project` _Project_ - Current project in ResInsight.
  Set when creating an instance and updated when opening/closing projects.
  

## launch
```python
Instance.launch(resinsight_executable='',
console=False,
launch_port=-1,
command_line_parameters=None)
```
Launch a new Instance of ResInsight. This requires the environment variable
RESINSIGHT_EXECUTABLE to be set or the parameter resinsight_executable to be provided.
The RESINSIGHT_GRPC_PORT environment variable can be set to an alternative port number.

**Arguments**:

- `resinsight_executable` _str_ - Path to a valid ResInsight executable. If set
  will take precedence over what is provided in the RESINSIGHT_EXECUTABLE
  environment variable.
- `console` _bool_ - If True, launch as console application, without GUI.
- `launch_port(int)` - If -1 will use the default port 50051 or RESINSIGHT_GRPC_PORT
  if anything else, ResInsight will try to launch with this port
- `command_line_parameters(list)` - Additional parameters as string entries in the list.

**Returns**:

- `Instance` - an instance object if it worked. None if not.
  

## find
```python
Instance.find(start_port=50051, end_port=50071)
```
Search for an existing Instance of ResInsight by testing ports.

By default we search from port 50051 to 50071 or if the environment
variable RESINSIGHT_GRPC_PORT is set we search
RESINSIGHT_GRPC_PORT to RESINSIGHT_GRPC_PORT+20

**Arguments**:

- `start_port` _int_ - start searching from this port
- `end_port` _int_ - search up to but not including this port
  

## set_start_dir
```python
Instance.set_start_dir(path)
```
Set current start directory

**Arguments**:

- `path` _str_ - path to directory
  
  

## set_export_folder
```python
Instance.set_export_folder(export_type, path, create_folder=False)
```

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



## set_main_window_size
```python
Instance.set_main_window_size(width, height)
```

Set the main window size in pixels

Parameter | Description      | Type
--------- | ---------------- | -----
width     | Width in pixels  | Integer
height    | Height in pixels | Integer


## set_plot_window_size
```python
Instance.set_plot_window_size(width, height)
```

Set the plot window size in pixels

Parameter | Description      | Type
--------- | ---------------- | -----
width     | Width in pixels  | Integer
height    | Height in pixels | Integer


## major_version
```python
Instance.major_version()
```
Get an integer with the major version number

## minor_version
```python
Instance.minor_version()
```
Get an integer with the minor version number

## patch_version
```python
Instance.patch_version()
```
Get an integer with the patch version number

## version_string
```python
Instance.version_string()
```
Get a full version string, i.e. 2019.04.01

## client_version_string
```python
Instance.client_version_string()
```
Get a full version string, i.e. 2019.04.01

## exit
```python
Instance.exit()
```
Tell ResInsight instance to quit

## is_console
```python
Instance.is_console()
```
Returns true if the connected ResInsight instance is a console app

## is_gui
```python
Instance.is_gui()
```
Returns true if the connected ResInsight instance is a GUI app
