+++
title = "Generic View"

weight = 111
+++

![](/images/3d-main-window/GenericView.png)

A generic view can display geometry like surfaces and polygons without a loaded grid model. Use it to look at well paths, surfaces, polygons and annotations before, or without, importing a grid.

## Creating a Generic View
Right-click the **Views** item or the **Surfaces** item in the project tree and select **New Generic View**.

A generic view is also created automatically when well paths or surfaces are imported into a project that has no 3D views.

## Content of a Generic View
The following objects can be displayed:

- **Wells** -- All visible well paths in the project
- **Surfaces** -- Toggle each surface on or off below **Surfaces** in the view, see [Surfaces]({{% relref "surfaces" %}})
- **Polygons** -- Toggle each polygon on or off below **Polygons** in the view, see [Polygons]({{% relref "polygons" %}})
- **Annotations** -- Text and reach circle annotations, see [Annotations]({{% relref "annotations" %}})

## Bounding Box
The extent of the grid box and the default zoom is computed from the visible objects when the view is created or the project is loaded. The bounding box is not changed when objects are toggled on or off. To recompute it from the currently visible objects, right-click the view in the project tree or the background of the 3D view and select **Update Bounding Box**.

The background right-click menu of the 3D view also contains **Link View** and **Zoom All**.

## Python Scripting
A generic view can be created with `project.create_generic_view()`. Surfaces and polygons are shown in the view with `view.set_surface_visible()` and `view.set_polygon_visible()`. See [Python Interface]({{% relref "pythoninterface" %}}).
