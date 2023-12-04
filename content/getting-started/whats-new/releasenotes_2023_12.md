+++
title = "What's New in 2023.12"
published = true
weight = 10
hidden = true
+++

## Grid Calculations

- Grid calculations can now be applied to multiple grid cases.
- A grid calculation can be used as data source for [Grid Case Statistics]({{< relref "casegroupsandstatistics" >}})  . The data source for statistics computations can either be a cell property or a grid calculation expression.
- Time step selection is added to the statistics dialog to make it possible to limit the resource usage.
- Expressions can be stored to a file and loaded from a file. This makes it possible to reuse expressions in multiple projects.
 
## Aggregated Grid Calculations
When using a aggregation expression like **sum** the resulting value will be available as a cell result(the single value is displayed in all cells used in the calculation). If this calculations is done on multiple grids, the statistics for the value for each realization will be displayed in the Message dialog. For each time step, the statistical values are displayed in the message dialog.

## Summery Improvements
- The summary plot editor has been reworked to make it easier to use and to make it more consistent with the generated plots. The preview plot title is removed, and preview curves are using multiple axes similar to other plots.
- Space between curve icon and text in legend is increased to make it easier to read
- Fixed missing curve legend when clicking on curves (Happens on some Linux distributions)
- Added flag to optionally distribute a summary calculation to all cases
- Summary expressions can be stored to a file and loaded from a file. This makes it possible to reuse expressions in multiple projects.

## Automation of RFT PLots
Multiple RFT plots can now be created using the **Create Multiple RFT Plots** menu item. The operation will create a plot for each RFT well.

## Other improvements
- Fixed a crash issue when using the summary toolbar
- Fixed a crash when toggling on Well Allocation over Time plot
- Regression Analysis: Fixed crash after modifying the polygon degree
- Completion export: Exclude COMPLDAT for deactivated laterals




OLD, to be removed:
- [Valve Import]({{< relref "completions" >}}#perforation-interval-valves) is now supported from Completor and Eclipse schedule files.
- Add text export using **Show Plot Data** for [Analysis Plots]({{< relref "analysisplots" >}}) and [Correlation Plots]({{< relref "correlationplots" >}}).
- Text labels can be visualized on surface intersection lines
- Ensemble RFT plots are improved to handle horizontal wells by using 3D grid model data
- Avoid setting curve color to full white when highlighting a curve
- Make sure summary data type **Network** is available in summary data source
- Duplicate a well path to a user-defined well path that can be manipulated - [Well Path Duplication]({{< relref "createnewwellpaths" >}}#well-path-duplication)


See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.