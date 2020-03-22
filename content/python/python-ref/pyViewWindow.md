+++
title = "ViewWindow"
published = true
+++


# ViewWindow
```python
ViewWindow(self, pb2_object=None, channel=None)
```

The Base Class for all Views and Plots in ResInsight



## case
```python
ViewWindow.case()
```
Get the case the view belongs to

## export_snapshot
```python
ViewWindow.export_snapshot(prefix='', export_folder='')
```
Export snapshot for the current view

**Arguments**:

- `prefix` _str_ - Exported file name prefix
- `export_folder(str)` - The path to export to. By default will use the global export folder
  
