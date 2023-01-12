+++
title = "What's New in 2023.01"
published = true
weight = 10
hidden = true
+++

## Summary Plotting
![]({{< relref "" >}}images/plot-window/SummaryPlotsMain.png)

[Summary Plotting]({{< relref "summaryplots.md" >}}) is updated with new features and improved workflows:
- Improved logarithmic legend and default ranges
- Visual appearance of curves is stable when doing **Source Stepping**
- Curve name and plot name improvements 

## Change Data Source by Clicking in 3D
If data is extracted along a well path and displayed as curves in a plot, the data source for multiple plots can be updated by clicking on a well path in 3D. This feature can be useful for large fields with many wells and you want to investigate a small subset of wells.

[Source Stepping]({{< relref "summarysourcestepping" >}}#change-well-data-source-from-3d-view) 



## Linked Views Improvements
It is now possible to get the result property values from all linked views when left-clicking on a cell in a view. Text is displayed in [Result Info]({{< relref "resultinfo" >}}), and values from other properties can also be appended. Property filters can now be linked between views, and will also work between multiple cases. 

[Linked Views]({{< relref "linkedviews" >}}) 


## Calculator Improvements
![]({{< relref "" >}}images/3d-main-window/GridPropertyCalculatorMain.png)

The grid calculator and summary curve calculator is updated with more help and improved usability. The grid property calculations will now always calculate values for active cells and do nothing for other inactive cells.

[Grid Calculator]({{< relref "GridPropertyCalculator" >}}) 

[Summary Calculator]({{< relref "CurveCalculator" >}}) 

[Calculator Expressions]({{< relref "CalculatorExpressions" >}}) 


## Breaking changes for user defined well paths

The calculation of the geometry for a user defined well path had some defects in some cases. These issues are now fixed, and will affect the generated geometry of a user-defined well path. If the ResInsight project file was stored with a version < 2023.01, loading the project in version 2023.01 can potentially generate a slightly different well path geometry (the location of well targets are unchanged). The location of perforation intervals and completions are specified by measured depth, and could be shifted to a different location due to this change of behaviour.

Thanks to https://github.com/EdmundStephens for reporting this [issue](https://github.com/OPM/ResInsight/issues/9439).

[User defined well paths]({{< relref "createnewwellpaths" >}})


## Display of RFT segment curves
![]({{< relref "" >}}images/plot-window/RFTSegmentPlot.png)

**RFT Segment Data** can be plotted as horizontal **Well Log Plots**. This feature is now improved with more tracks and improved visual quality.

[RFT Segment plots]({{< relref "rftsegmentplot" >}})


## Import of ROFF files (Preview)
ROFF files with properties can be imported, both in ASCII and binary form. Grid geometry and properties per cell can be imported.

[ROFF grid models]({{< relref "RoffGridModels" >}})


## High Priority Issues Fixed

[Wrong area for scaled fractures](https://github.com/OPM/ResInsight/issues/9473)





See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.