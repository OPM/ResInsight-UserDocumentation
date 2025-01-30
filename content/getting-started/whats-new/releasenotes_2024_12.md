+++
title = "What's New in 2024.12"
weight = 10
hidden = true

[build]
  list = 'never'
+++

## Grid Import Performance

ResInsight now offers the option to import geometry exclusively for active cells. This feature is particularly beneficial for large grids where active cells constitute only a small fraction of the total, significantly reducing memory usage. This optimization ensures efficient handling of large models while maintaining full functionality for active cells.

[Preferences]({{% relref "preferences" %}}#grid)

[Performance Hints]({{% relref "performancehints" %}})

## Quick Access View

![](/images/3d-main-window/quick-access-main.png)

For large projects with numerous views and grid models, navigating to specific information can sometimes be time-consuming. To address this, we've introduced a dedicated dialog called **Quick Access**. This dialog displays selected information from a view, making it easier to find what you need efficiently.  

By default, the **Quick Access** dialog is located to the right of the 3D views.  

[Quick Access]({{% relref "quickaccess" %}})

## Cloud Services

![](/images/cloud-services/osdu-well-path-3dview.png)

When accessing cloud services, an authentication token is saved to a file in your home folder. Occasionally, this token may become invalid, leading to a failure in establishing a cloud connection. If this occurs, you can resolve the issue by using the **Delete Token** button in the **Preferences** menu. Once the token is deleted, the authentication dialog will appear the next time you attempt to access cloud services, and a new token will be generated automatically.

[Cloud Services]({{% relref "cloudservices" %}})

[Cloud Services Preferences]({{% relref "preferences" %}}#importexport)

## Framework Updates
Qt has been upgraded from version 5 to version 6, bringing significant changes that impact several aspects of ResInsight, particularly its application engine. This update affects certain visual features of the user interface:  

- The font system has been modernized, which may result in subtle differences in font appearance and size on some systems.  
- Default spacing between interface elements has been slightly increased to improve layout consistency.  

Additionally, the build instructions have been updated to align with Qt 6. Building with Qt 5 is no longer supported.

[Build Instructions Ubuntu]({{% relref "build-instructions-ubuntu" %}})

## Other improvements
- Summary Table: Add user option to set time range on x-axis [#11803](https://github.com/OPM/ResInsight/issues/11803)
- When highlighting a curve, also highlight other curves for the same realization [#11771](https://github.com/OPM/ResInsight/issues/11771)
- Add a vertical line indicating the selected time in Result Plot [#11768](https://github.com/OPM/ResInsight/issues/11768)
- Plot scaled and unscaled relperm curves in the same plot [#11684](https://github.com/OPM/ResInsight/issues/11684)
- Fix visibility control of curve legends [#11966](https://github.com/OPM/ResInsight/issues/11966)
- Fixed issues with P10 and P90 curves for some wells [#11941](https://github.com/OPM/ResInsight/issues/11941)
 
## Python API
- Make all features for **Completion Export Parameters** and **Multi Segment Well Options** available in Python.
- If a field is available in Python, the Python code to access this field can be copied using the right-click menu on the label in the **Property Editor** https://github.com/OPM/ResInsight/issues/11923

See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.
