+++
title = "What's New in 2026.02"
weight = 96
hidden = false
search_ignore = true
aliases = ["/releases/release-notes/latest/"]
+++

## Ensemble Import

Realizations can now be excluded when importing ensembles using `!`. For example, the expression `1-7, !4-5` produces the list `[1, 2, 3, 6, 7]`.

See [Ensemble File Dialog]({{% relref "ensemblefiledialog" %}}) for details.

## Validation and Consistency
A valid range can now be defined for variables in the project file. During import, values outside the specified range will be clamped to the valid range.

## Telemetry and Log Reporting
**ResInsight** produces log messages, warnings, errors, and crash reports. These have previously been stored on the local file system. They can now optionally be sent to a cloud logging service, improving visibility into error situations and enabling an overview of selected application usage metrics.

## Visualization of Well Segments
**WELSEGS** can be exported from ResInsight. It is now possible to visualize the segments along the well path for QC purposes. Clicking a segment displays segment data as text. Segment boundaries can also be shown as annotations in well log plots. See [Visualization of Well Segments]({{% relref "wellpaths" %}}#visualization-of-well-segments-welsegs) for details.

## Calculator Expressions
- Improved handling of mixed upper and lower case
- Fixed issue with nested aggregation functions. The following expression now works correctly: `a := min(if(b>3, 5), 50)`

## Simulation Modeling Improvements
- Added support for **WSEGSICD**
- Added support for **COMPLUMP** https://github.com/OPM/ResInsight/issues/13254

## Summary Plotting
- Added support for calculation of block vectors in the form **BPR:15,28,1**
- Fixed issue for **_DIFF** vectors when only the Mean statistics curve was visible
- Improved interpretation and display of network summary vectors
- Fixed issue when switching to "Time From Simulation Start" for ensemble realizations
- Custom ensemble percentiles are now supported. See [User-Defined Percentiles]({{% relref "ensembleplotting" %}}#statistics-curves) for details.
- Avoid time axis zoom when stepping vectors for ensemble curves

## Surface Display Mode

When a surface cuts through a grid model, z-fighting and visual noise can occur where the surface and result geometry overlap. A new **Surface Display Mode** setting has been added at both the surface collection level and per individual surface, allowing control over whether to show the surface color, result colors, or both. See [Surface Display Mode]({{% relref "3d-main-window/surfaces" %}}#surface-display-mode) for details.

## Fixes and Improvements
- Dual Porosity: When computing COMPDAT for dual porosity models, ResInsight now reads all input values from the **Fracture** result section. When exporting COMPDAT and similar data to file, the K index for fracture results is used.
- Fixed issues with field units in VFP plots
- Fixed issue for RMS well paths with spaces in the name
- Fixed issue with the user interface for statistical ensemble surfaces
- Fixed issue with formation dip for fractures
- Improved display of formation colors in 2D plots (well log plots and RFT plots)
