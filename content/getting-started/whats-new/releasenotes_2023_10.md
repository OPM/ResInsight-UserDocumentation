+++
title = "What's New in 2023.10"
published = true
weight = 10
hidden = true
+++



## Seismic View
![]({{< relref "" >}}images/3d-main-window/SeismicView.png)

When working with seismic data, it is no longer required to have a grid model open. Import a seismic cube and surfaces, add some well paths and interact with seismic data.

[Seismic View]({{< relref "seismicview" >}})

[Seismic Data]({{< relref "seismicdata" >}})

[Seismic Sections]({{< relref "seismicsections" >}})
 

## Summary Cross Plot Curves
![]({{< relref "" >}}images/plot-window/SummaryCrossPlot.png)

[Summary Cross Plot]({{< relref "summarycrossplots" >}}) curves are now easily available as part of a summary plot. Cross plot of ensemble curves is now supported, and [Regression Curves]({{< relref "regressionanalysis" >}}) can be created on both single cross plot curves and ensemble statistics curves.

## Performance improvements
- Huge performance improvements for summary cases with many objects (wells, groups, regions, ...)
- Using the [Polygon Cell Filter]({{< relref "filters" >}}#cell-filters) is now performing much better

## Stacking of Curves
- Fixed a crash when stacking was enabled
- Do a zoom all when stacking option is changed to make sure that all curves are visible
- Improve performance when selecting multiple curves and toggle stacking state of all curves in one operation

## Other improvements

- [Valve Import]({{< relref "completions" >}}#perforation-interval-valves) is now supported from Completor and Eclipse schedule files.
- Show plot data is not supported for [Analysis Plots]({{< relref "analysisplots" >}}) [Correlation Plots]({{< relref "correlationplots" >}}).
- Text labels can be visualized on surface intersection lines
- Ensemble RFT plots are improved to handle horizontal wells correctly
- Avoid setting curve color to full white when highlighting a curve
- Make sure summary data type **Network** is available in summary data source
- Duplicate a well path to a user-defined well path that can be manipulated - [Well Path Duplication]({{< relref "createnewwellpaths" >}}#well-path-duplication)


See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.