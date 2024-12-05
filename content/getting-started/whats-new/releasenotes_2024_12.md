+++
title = "What's New in 2024.12"
published = true
weight = 10
hidden = true
+++

## Grid Import Performance

ResInsight now offers the option to import geometry exclusively for active cells. This feature is particularly beneficial for large grids where active cells constitute only a small fraction of the total, significantly reducing memory usage. This optimization ensures efficient handling of large models while maintaining full functionality for active cells.


 TODO: link to opm-common active cells

[Performance Hints]({{< relref "performancehints" >}})

## Cloud Services

![]({{< relref "" >}}images/cloud-services/osdu-well-path-3dview.png)

When we access cloud services, an authentication token is stored to a file in your home folder. In some situations this token can become invalid causing the cloud connection to fail. If this happens, a button in Preferences can be used to delete this token. The next time you try to access cloud services, the normal authentication dialog will be displayed and a fresh token is created.

TODO: Add description in preferences

[Cloud Services]({{< relref "cloudservices" >}})


## Quick Access View

![]({{< relref "" >}}images/3d-main-window/quick-access-main.png)

For large projects with many views and many grid models, it can take some time to navigate to the information you are looking for. We have now added a special dialog named **Quick Access**, where selected information from a view is displayed. The default location for the dialog is at to the right of the 3D views.

[Quick Access]({{< relref "quickaccess" >}})

## Framework Updates
Qt has been updated from version 5 to version 6. This is a quite large change that affects several parts, especially the application engine of ResInsight. Some visual user interface features will be affected. The font system is updated, and the appearance and size of fonts will on some systems be slightly different. The default spacing between elements in the user interface is increased slightly.

The build instructions is now updated for Qt 6
[Build Instructions Ubuntu]({{< relref "build-instructions-ubuntu" >}})



## Other improvements
- Summary Table: Add user option to set time range on x-axis [#11803](https://github.com/OPM/ResInsight/issues/11803)
- When highlighting a curve, also highlight other curves for the same realization [#11771](https://github.com/OPM/ResInsight/issues/11771)
- Add a vertical line indicating the selected time in Result Plot [#11768](https://github.com/OPM/ResInsight/issues/11768)
- Plot scaled and unscaled relperm curves in the same plot [#11684](https://github.com/OPM/ResInsight/issues/11684)
- Fix visibility control of curve legends [#11966](https://github.com/OPM/ResInsight/issues/11966)
- Fixed issues with P10 and P90 curves for some wells [#11941](https://github.com/OPM/ResInsight/issues/11941)
- 






## Python API
- Make all features for **Completion Export Parameters** and **Multi Segment Well Options** available in Python.
- If a field is available in Python, the Python code to access this field can be copied using the right-click menu on the label in the **Property Editor** https://github.com/OPM/ResInsight/issues/11923



See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.





## Eksempel
![]({{< relref "" >}}images/plot-window/VFP_Plot.png)

The import of VFP data is changed, and the management of VFP Plots is now improved.

[VFP Plots]({{< relref "vfpplot" >}})
