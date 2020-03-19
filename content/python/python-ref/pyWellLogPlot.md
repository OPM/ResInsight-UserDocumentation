+++
title = "WellLogPlot"
published = true
+++


# WellLogPlot
```python
WellLogPlot(self, pb2_object=None, channel=None)
```

A Well Log Plot With a shared Depth Axis and Multiple Tracks

**Attributes**:

- `auto_scale_depth_enabled` _str_ - Auto Scale
- `depth_type` _str_ - Type
- `depth_unit` _str_ - Unit
- `maximum_depth` _float_ - Max
- `minimum_depth` _float_ - Min
- `show_depth_grid_lines` _str_ - Show Grid Lines
- `show_title_in_plot` _str_ - Show Title
  

## export_data_as_las
```python
WellLogPlot.export_data_as_las(export_folder,
file_prefix='',
export_tvdrkb=False,
capitalize_file_names=False,
resample_interval=0.0,
convert_to_standard_units=False)
```
Export LAS file(s) for the current plot

**Arguments**:

- `export_folder(str)` - The path to export to. By default will use the global export folder
- `file_prefix` _str_ - Exported file name prefix
- `export_tvdrkb(bool)` - Export in TVD-RKB format
- `capitalize_file_names(bool)` - Make all file names upper case
- `resample_interval(double)` - if > 0.0 the files will be resampled
  

**Returns**:

  A list of files exported
  

## export_data_as_ascii
```python
WellLogPlot.export_data_as_ascii(export_folder,
file_prefix='',
capitalize_file_names=False)
```
Export LAS file(s) for the current plot

**Arguments**:

- `export_folder(str)` - The path to export to. By default will use the global export folder
- `file_prefix` _str_ - Exported file name prefix
- `capitalize_file_names(bool)` - Make all file names upper case
  

**Returns**:

  A list of files exported
  
