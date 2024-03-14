+++
title = "What's New in 2024.03"
published = true
weight = 10
hidden = true
+++

## Grid Calculations

[Grid Property Calculations]({{< relref "gridpropertycalculator" >}}) perform better for multiple (large) grid models
 
## Polygons
![]({{< relref "" >}}images/3d-main-window/PolygonHeading.png)

- [Polygons]({{< relref "polygons" >}}) are now available as project objects, and a can be displayed in 3D views. A polygon can also be used to define an intersection and polygon cell filters. Polygons can be imported from a file, or created from a selection of cells in the 3D view. Polygons can be exported to file.
- A polygon cell filter can now be configured to use a polyline to define intersected cells in addition to a closed polygon.

## Performance Tools and Improvements
- When working with multiple large grid models, it is possible to run into low memory issues. The memory consumption of ResInsight can be monitored using the new [Memory Report Dialog]({{< relref "memorymanagement" >}}) . This will display the consumed memory for all cases in the project.

![]({{< relref "" >}}images/misc/MemoryUsage.png)

- Avoid allocation of formations data if no formations are present
- Added support for export of application [log messages to file]({{< relref "preferences" >}}#importexport) in addition to the **Messages Window**. 


## Other improvements
- Wrong unit conversion for field units made **Well Allocation Plot** unreadable [GitHub issue](https://github.com/OPM/ResInsight/issues/11231)
- Improved plot names and ordering of **Flow Diagnostics Plots**
- Improve curve legend names for calculated curves
- Improve MSW and short valve well visualization [GitHub issue](https://github.com/OPM/ResInsight/issues/11109)
- Fix windows tiling issue

## Python API
- Added completion export parameters and multi segment well options [GitHub issue](https://github.com/OPM/ResInsight/issues/10781)



See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.