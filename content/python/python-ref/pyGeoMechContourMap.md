+++
title = "GeoMechContourMap"
published = true
+++


# GeoMechContourMap
```python
GeoMechContourMap(self, pb2_object=None, channel=None)
```

A contour map for GeoMech cases



## export_to_text
```python
GeoMechContourMap.export_to_text(export_file_name='',
export_local_coordinates=False,
undefined_value_label='NaN',
exclude_undefined_values=False)
```
Export snapshot for the current view

**Arguments**:

- `export_file_name(str)` - The file location to store results in.
- `export_local_coordinates(bool)` - Should we export local coordinates, or UTM.
- `undefined_value_label(str)` - Replace undefined values with this label.
- `exclude_undefined_values(bool)` - Skip undefined values.
  
