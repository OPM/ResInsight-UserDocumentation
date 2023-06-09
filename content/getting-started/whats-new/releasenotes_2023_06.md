+++
title = "What's New in 2023.06"
published = true
weight = 10
hidden = true
+++



## Seismic Data
![]({{< relref "" >}}images/3d-main-window/SeismicHeaderImage.png)

ResInsight supports the following seismic file formats:

- **SEGY**: file format developed by the **Society of Exploration Geophysicists** for storing geophysical data
- **VDS**: file format for fast random access to multi-dimensional volumetric data as supported by **OSDU OpenVDS**
- **ZGY**: file format for fast random access to multi-dimensional volumetric data as supported by **OSDU OpenZGY**

[Seismic Data]({{< relref "seismicdata" >}})

[Seismic Sections]({{< relref "seismicsections" >}})
 
## Summary Table

![]({{< relref "" >}}images/plot-window/Summary_Table_WOPR.png)

**Summary Tables** are a display of curve data based on [Eclipse Summary Data]({{< relref "eclipsesummarydata" >}}) as a color map in table format. It shows summary data of vectors for the selectable categories: *Well*, *Group* or *Region*.

Summary tables are displayed with the summary vectors on each row, and time step values according to selected *Date Resampling* in each column - as shown with resampling *Year* in the screenshot above.

[Summary Tables]({{< relref "summarytables" >}})

## Producer/Injector Connectivity Table
![]({{< relref "" >}}images/plot-window/Producer_Injector_Connectivity.png)

[Producer/Injector Connectivity Tables]({{< relref "producerinjectorconnectivitytable" >}}) is a display of [Flow Diagnostics Data]({{< relref "flow-diagnostics-plots" >}}) as a color map in table format. The table either shows flow rate data for a single time step, or accumulated flow volume data over a range of time steps.


## Cell Filters for Faults and Intersections
![]({{< relref "" >}}images/release-notes/CellFilteredIntersection.png)

Intersections and faults can now be visually filtered by using cell filters, and can be useful if faults and intersections obscure other interesting parts of the model. The filtering using cell filters is by default activated.

[Intersection Filters]({{< relref "intersections" >}}#depth-and-range-filter)

[Fault Filters]({{< relref "faults" >}}#faults-properties)


## Regression Analysis and Decline Curve Analysis
![]({{< relref "" >}}images/plot-window/DeclineCurves.png)

[Decline Curve Analysis]({{< relref "declinecurveanalysis" >}})

[Regression Analysis]({{< relref "regressionanalysis" >}})

## Integer Cell Results
![]({{< relref "" >}}images/3d-main-window/CustomCategoryLegend.png)

**Integer Cell Results** can now be visualized using [Integer Color Legends]({{< relref "colorlegends" >}}#integer-cell-results) and use custom color names that can be displayed in the 3D view.

## Improved Visualisation of Ensemble Curves

![]({{< relref "" >}}images/plot-window/Ensemble.png)

The visual appearance of ensemble curves has been improved. Ensemble curves are displayed using a brighter color than the statistics curves.

A color selection dialog can be opened by clicking on the color icon in the **Project Tree**. This feature is also supported for single summary curves.
![]({{< relref "" >}}images/plot-window/ColorSelectionDialog.png)

## Other improvements

- [Create a new well]({{< relref "createnewwellpaths" >}}) based on an existing well path
- Improve renaming of summary and ensemble models
- Show Python version in About Dialog
- Full screen mode to maximize screen space for 3D view
- [Fault distance]({{< relref "faultdistance" >}}) calculations performs faster 
- In some models, the size of well targets was to small to work with. A scaling factor for [Well Targets]({{< relref "createnewwellpaths" >}}) is now available.



See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.