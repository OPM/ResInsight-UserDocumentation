+++
title = "What's New in 2023.12"

weight = 10
hidden = true
[build]
  list = 'never'
+++

## Grid Calculations

- [Grid Property Calculations]({{% relref "gridpropertycalculator" %}}) can now be applied to multiple grid cases.
- A grid calculation can be used as data source for [Grid Case Statistics]({{% relref "casegroupsandstatistics" %}}). The data source for statistics computations can either be a cell property or a grid calculation expression.
- Time step selection is added to the **Grid Case Statistics** settings to reduce computation demand.
- Expressions can be stored to a file and loaded from a file. This makes it possible to reuse expressions in multiple projects.
 
## Aggregated Grid Calculations
When using a aggregation expression like **sum** the resulting value will be available as a cell result (the single value is duplicated and displayed for all cells used in the calculation). If the calculation is applied to multiple grids, the aggregated value for each realization will be displayed in the **Messages** dialog. For each time step, the statistical values are also computed and displayed as text.

[Aggregation of Grid Cell Values Example]({{% relref "aggregationofgridcellvalues" %}})

## Summary Improvements
- The summary plot editor has been reworked to make it easier to use and to make it more consistent with the generated plots. The preview plot title is removed, and preview curves are using multiple axes similar to other plots.
- Space between curve icon and text in legend is increased to make it easier to read
- Fixed missing curve legend when clicking on curves (Happens on some Linux distributions)
- Added flag to optionally distribute a summary calculation to all cases
- Summary expressions can be stored to a file and loaded from a file. This makes it possible to reuse expressions in multiple projects.

## Automation of RFT PLots
Multiple RFT plots can now be created using the **Create Multiple RFT Plots** menu item. The operation will create one plot for each RFT well.

## Other improvements
- Fixed a crash issue when using the summary toolbar
- Fixed a crash when toggling on [Well Allocation Over Time]({{% relref "wellallocationovertimeplot" %}}) plot
- Regression Analysis: Fixed crash after modifying the expression
- Completion export: Exclude COMPDAT for deactivated laterals


See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.