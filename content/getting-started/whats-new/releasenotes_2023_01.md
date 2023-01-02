+++
title = "What's New in 2023.01"
published = true
weight = 10
hidden = true
+++

## Summary Plotting
![]({{< relref "" >}}images/plot-window/SummaryPlotsMain.png)

[Summary Plotting]({{< relref "summaryplots.md" >}}) is updated with new features and improved workflows:
- improve logarithmic legend and default ranges
- visual appearance of curves is stable when doing Source Stepping
- curve name and plot name improvements 

## Change Data Source by Clicking in 3D
If data is extracted along a well path and displayed as curves in a plot, the data source for multiple plots can be updated by clicking on a well path in 3D. This feature can be useful for large fields with many wells and you want to investigate a small subset of wells.


## Linked View Improvements
It is now possible to get the result property values from all linked views when left-clicking on a cell in a view. Property filters can now be linked between views, and will also work between multiple cases.

[Linked Views]({{< relref "linkedviews" >}}) 

**Result Info** can now display values from additionaly selected properties.



## Calculator Improvements
![]({{< relref "" >}}images/3d-main-window/GridPropertyCalculatorMain.png)

The grid calculator and summary curve calculator is updated with more help and improved usability. The grid property calculations will now always calculate values for active cells and do nothing for other inactive cells.

[Grid Calculator]({{< relref "GridPropertyCalculator" >}}) 

[Summary Calculator]({{< relref "CurveCalculator" >}}) 

[Calculator Expressions]({{< relref "CalculatorExpressions" >}}) 


## Breaking changes for user defined well paths

The calculation of the geometry for a user defined well path was wrong in some cases. This is now fixed, and will affect the automatically generated geometry of a well path. If the ResInsight project file was stored with the wrong well path geometry, loading the project in version 2023.01 can potentially generate a different well path geometry (the location of well targets are unchanged). The location of perforation intervals and completions are specified in measured depth, and could be shifted to a different location.

Thanks to https://github.com/EdmundStephens for reporting this [issue](https://github.com/OPM/ResInsight/issues/9439).

[User defined well paths]({{< relref "createnewwellpaths" >}})


## Display of RFT segment curves
![]({{< relref "" >}}images/plot-window/RFTSegmentPlot.png)

RFT Segment Data can be plotted as horizontal Well Log Plots. This feature is now improved.


## Import of ROFF files (Preview)
ROFF files with properties can be imported, both in ASCII and binary form. Grid geometry and properties per cell can be imported.

[Import ROFF grid model]({{< relref "ROFFData" >}}).


## High Priority Issues Fixed

[Wrong area for scaled fractures](https://github.com/OPM/ResInsight/issues/9473)





See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.