+++
title = "What's New in 2022.06"
published = true
weight = 10
hidden = true
+++

## Summary Plotting
![]({{< relref "" >}}images/plot-window/SummaryPlotsMain.png)

 Summary Plotting in now updated with new features and improved workflows.
- improved management of multiple subplots
- restructured organization of plot items in Property Editor
- improved data source stepping for multiple plots
- optionally color curves based on the summary vector phase

## Multiple Axes
![]({{< relref "" >}}images/plot-window/SummaryCurveHighlight.png)

Summary plots can now have [Multiple Axes]({{< relref "summaryplots.md" >}}#highlighting-a-curve-or-axis) on both left and right side. Clicking on a curve will highlight the curve and connected axis. Clicking on an axis will highlight the axis and all curves connected to this axis.

When a new curve is added to the plot, a new axis is created if needed.

## Restructure of Windows
- Data sources for summary data can be used to drag/drop operations and easy plot creation based on a summary vector
- Scripts are now available as a separate windows
- Templates are available as a separate window

## Plot Manager
The [Plot Manager]({{< relref "summaryplotmanager.md" >}}) can be used to create multiple plots based on a text filter.

## Plot Templates
[Plot Templates]({{< relref "summaryplottemplate.md" >}}) do now support multiplots. A set of templates can also automatically be created when a new case is loaded. 
 
 TODO: Update preferences

## Filter intersection by IJK
The visible parts of an intersection can now be filtered by a K-filter or by a user defined depth.
TODO: Add doc

## Grid Property Calculator
The [Grid Property Calculator]({{< relref "gridpropertycalculator.md" >}}) can be used to create derived results based on mathematical expressions.

## Display of RFT segments and connections

TODO

## Python API
Several improvements and more examples

- TODO

https://api.resinsight.org/en/stable/PythonExamples.html



## Additional New Features and Enhancements

- TODO

See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.
