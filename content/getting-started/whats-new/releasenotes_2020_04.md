+++
title = "What's New in 2020.04"
published = true
weight = 10
hidden = true
+++

ResInsight 2020.04 is the latest version of ResInsight, the professional quality, open source 3D visualization, curve plotting and post-processing tool for reservoir models and simulations. Version 2020.04 is a major update bringing a range of significant new and enhanced features.

## Surfaces
![]({{< relref "" >}}images/3d-main-window/SurfacesOverview.png)

ResInsight supports import of [ 3D Surfaces ]({{< relref "3d-main-window/surfaces" >}}), and allows mapping properties and simulation results onto these surfaces.

## Allan Diagrams

![]({{< relref "" >}}images/3d-main-window/AllanDiagram.png)

[Allan Diagrams]({{< relref "/3d-main-window/allandiagrams" >}}) displays the overlap of formations and layers across fault faces.

## Cumulative Phase Distribution Plots
![]({{< relref "" >}}images/plot-window/FlowDiagnosticsCumulativePhaseDistributionPlot.png)

A [Cumulative Phase Distribution Plot]({{< relref "/plot-window/flow-diagnostics-plots" >}}#cumulative-phase-distribution-plot) shows the volumetric oil, gas, and water distribution from contributing wells to a target well.

## Delta Summary Case and Ensemble Case

The difference between two summary cases or two ensembles can be established using [Delta Ensemble]({{< ref "ensembleplotting" >}}#delta-ensemble) and [Delta Summary Case]({{< ref "summaryplots" >}}#delta-summary-case).

## Well Disks
![]({{< relref "" >}}images/3d-main-window/WellDisks.png)

[Well Disks]({{< relref "/wells-and-completions/simulationwells" >}}#disks) may be used to visualize production and injection rates and cumulative production and injection with oil, gas, and water phases shown in green, red, and blue, respectively. Optionally, the quantity of production and injection can be displayed.

## Python Documentation
The Python documentation is now available on a separate site.

![]({{< relref "" >}}images/scripting/apiResInsightOrg.png)

Here are the highlights of new features for Python

- Summary data
- Simulation well data - status and active connection for given time step
- Grid and cell geometry
- NNC data

[ Python Documentation ](https://api.resinsight.org)

## Multi Plot
![]({{< relref "" >}}images/plot-window/MultiPlotHeading.png)

A [ Multi Plot ]({{< relref "/plot-window/multiplots" >}}) allows the user to combine multiple plots in a grid layout. Plots from different types can be combined. This plot type is tailored for export to PDF.

## Well Measurements

![]({{< relref "" >}}images/3d-main-window/ResInsight_WellMeasurements.png)

ResInsight can import [ Well Measurements ]({{< relref "/wells-and-completions/wellmeasurements" >}}) and show the location of measurements by using symbols in the 3D view. 

## Additional News

**Well Bore Stability Plot**

More parameters are now available for [Well Bore Stability Plot]({{< relref "/plot-window/wellborestabilityplots" >}}), and it is now possible to create and modify these plots from Python. 

**Combine Multi Case Results in one View**

In a view displaying result values from one case, ResInsight also supports display of results from other cases. This feature is available for [ Faults ]({{< relref "/3d-main-window/faults" >}}#separate-fault-result), [ Intersections ]({{< relref "/3d-main-window/intersections" >}}#intersection-results), and [ Surfaces ]({{< relref "/3d-main-window/surfaces" >}}#surface-results)

**References to External Files**

All external file references are now located at the top of the [ Project File ]({{< relref "/misc/projectfile" >}}) enabling the user to efficiently change referenced data.

**Release Notes on GitHub**

[Release info on GitHub](https://github.com/OPM/ResInsight/releases/)
