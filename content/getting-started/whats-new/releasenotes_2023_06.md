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

## Injector/Producer Communication Table


## Cell Filters for Faults and Intersections
![]({{< relref "" >}}images/release-notes/CellFilteredIntersection.png)

Intersections and faults can now be visually filtered by using cell filters, and can be useful if faults and intersections obscure other interesting parts of the model. The filtering using cell filters is by default activated.

[Intersection Filters]({{< relref "intersections" >}}#depth-and-range-filter)

[Fault Filters]({{< relref "faults" >}}#faults-properties)


## Regression and Decline curves

## Integer Cell Results
Improved support for import and tagging of integer cell results. Improved legend for integer results.
Improved support for named categories in color legend. Supported for both ROFF and Eclipse data.


## Improved visual ensemble curves
use bright transparent curves
allow direct access to curve colors in tree
https://github.com/OPM/ResInsight/issues/10214







## Other improvements

- Create a new well with targets based on an existing static well path ##add doc##
- Improve renaming of summary and ensemble models
- Show Python version in About Dialog
- Full screen mode to maximize screen space for 3D view
- Fault distance calculations performs faster (add doc) https://github.com/OPM/ResInsight/issues/10141
- In some models, the size of well targets was to small to work with. A scaling factor well targets is added.



See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.