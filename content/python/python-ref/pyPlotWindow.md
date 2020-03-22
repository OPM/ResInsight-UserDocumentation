+++
title = "PlotWindow"
published = true
+++


# PlotWindow
```python
PlotWindow(self, pb2_object=None, channel=None)
```

The Abstract base class for all MDI Windows in the Plot Window

**Attributes**:

- `id` _int_ - View ID
  

## export_snapshot
```python
PlotWindow.export_snapshot(export_folder='',
file_prefix='',
output_format='PNG')
```
Export snapshot for the current plot

**Arguments**:

- `export_folder(str)` - The path to export to. By default will use the global export folder
- `prefix` _str_ - Exported file name prefix
- `output_format(str)` - Enum string. Can be 'PNG' or 'PDF'.
  
  
