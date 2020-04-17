+++
title = "What's New in 2020.04"
published = true
weight = 10
hidden = true
+++

ResInsight 2020.04 is the latest version of ResInsight, the professional quality, open source 3D visualization, curve plotting and post-processing tool for reservoir models and simulations. Version 2020.04 is a major update bringing a range of significant new and enhanced features.

## Well Bore Stability Plot
![]({{< relref "" >}}images/plot-window/WellBoreStability.png)

ResInsight can create [Well Bore Stability Plot]({{< relref "plot-window/wellborestabilityplots" >}}) plots for Geomechanical cases. These plots are specialized [Well Log Plots]({{< relref "welllogsandplots" >}}) to visualize [Formations]({{< relref "formations" >}}), [Well Path Attributes]({{< relref "wellpaths" >}}#well-path-attributes) as well as a set of well path derived curves in different tracks. 

## Delta Summary Case

## Well Disks
![]({{< relref "" >}}images/3d-main-window/WellDisks.png)

[Well Disks]({{< relref "wells-and-completions/simulationwells" >}}#disks) may be used to visualize production and injection rates and cumulative production and injection with oil, gas, and water phases shown in green, red, and blue, respectively. Optionally, the quantity of production and injection can be displayed.

## Cumulative Phase Distribution Plots
![]({{< relref "" >}}images/plot-window/FlowDiagnosticsCumulativePhaseDistributionPlot.png)

A [Cumulative Phase Distribution Plot]({{< relref "plot-window/flowdiagnosticsplots" >}}#cumulative-phase-distribution-plot) shows the volumetric oil, gas, and water distribution from contributing wells to a target well.

## Allen Diagrams

![]({{< relref "" >}}images/3d-main-window/AllenDiagram.png)

[Allen Diagrams]({{< relref "3d-main-window/allendiagrams" >}}) displays the overlap of formations and layers across fault faces.

## Combine Multi Case Results in one View

In a view displaying result values from one case, ResInsight also supports display of results from other cases. This feature is available for [ Faults ]({{< relref "3d-main-window/faults" >}}#separate-fault-result), [ Intersections ]({{< relref "3d-main-window/intersections" >}}#intersection-results), and [ Surfaces ]({{< relref "3d-main-window/surfaces" >}}#surface-results)

## Surfaces
![]({{< relref "" >}}images/3d-main-window/SurfacesOverview.png)

ResInsight is capable of mapping properties and simulation results onto [ 3D Surfaces ]({{< relref "3d-main-window/surfaces" >}})

## Python Documentation
The Python documentation is now available on a separate site.

Here is a highlight of new featres available for Python

- Summary data
- Simulation well data - status and active connection for given time step
- Grid and cell geometry
- NNC data

[ Python Documentation ](https://api.resinsight.org)

## Bugfixes

[Release info on GitHub](https://github.com/OPM/ResInsight/releases/tag/v2020.04)
