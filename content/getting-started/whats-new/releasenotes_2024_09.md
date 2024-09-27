+++
title = "What's New in 2024.09"
published = true
weight = 10
hidden = true
+++

## Cloud Services

![]({{< relref "" >}}images/cloud-services/osdu-well-path-3dview.png)

ResInsight has now support for import of data from two cloud services, ensemble summary data from **SUMO** and well path geometry from **OSDU**.

[Cloud Services]({{< relref "cloudservices" >}})

## Ensemble Grid Case

An ensemble of grid cases can be imported into a grid case ensemble. Creating a view in this ensemble will allow the user to quickly switch between realizations using a drop down menu.

[Import Grid Case Ensemble]({{< relref "eclipsecases" >}})

[Change Data Source for View]({{< relref "3dviews" >}}/#change-data-source-for-view)

If you have identical IJK for all grid cases, consider using [Grid Case Group]({{< relref "casegroupsandstatistics" >}})

## Improved VFP Plot
![]({{< relref "" >}}images/plot-window/VFP_Plot.png)

The import of VFP data is changed, and the management of VFP Plots is now improved.

[VFP Plots]({{< relref "vfpplot" >}})


## PFLOTRAN Faults
Import of faults defined in a PFLOTRAN simulation is now supported.

[Faults from PFLOTRAN]({{< relref "faults" >}}/#information-from-pflotran-simulations)

## Summary Curves
**Rate** or **Accumulated** summary curve type is automatically derived from the summary address. The type can also manually be set by the user, and is often useful for [Observed Data]({{< relref "observeddata" >}}).

[Summary Curve Type]({{< relref "summaryplots" >}}/#editing-a-summary-curve)

## Grid Import Improvements
Several improvements has been done related to the opm-common grid importer, especially simulation well data and LGR support. We recommend using opm-common for best performance.

[Performance Hints]({{< relref "performancehints" >}})

## Depth Surface
![]({{< relref "" >}}images/3d-main-window/SurfacesOverview.png)

A flat surface at a specified depth can be created, useful to indicate oil-water contact depth.

[Depth Surface]({{< relref "surfaces" >}}/#depth-surfaces)

## Other improvements
- Make sure summary ensemble statistics is calculated correctly if the first realization is partial
- Fix issue with display of connection results in RFT Segment plots
- Make sure regression curves works Observed Data
- Fixed issue with the layout system causing very thin dialogs at left and right side of screen
- Improved [Performance Hints]({{< relref "performancehints" >}})


## Python API
- Increased timeout when launching a process. When many processes are started at the same time, the launch time can increase significantly
- By default use the port number assigned by GRPC
- Look for the path to ResInsight executable in an optional JSON file


See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.