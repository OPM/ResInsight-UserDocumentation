+++
title = "What's New in 2026.06"
weight = 95
hidden = false
search_ignore = true
aliases = ["/releases/release-notes/latest/"]
+++

## RFT improvements
- Correlation plots can now be enabled for RFT data.
- Ensemble curve sets can be selected directly in the plot, and clicking a curve highlights it.
- Rft Segment Plots: Device-layer segment assignment is now driven by segment topology instead of measured depth, giving more reliable results for multi-branched wells.

![](/images/plot-window/RftCorrelationPlot.png)

[RFT Correlation Plot]({{% relref "RftCorrelationPlot" %}})

## Grid Ensemble
- Import of grid ensembles now uses the shared **file set** concept, and grid and summary ensembles can be imported together in a single unified import dialog.
- Several separate grid-import features have been merged into one, simplifying the import menus and user interface.
- A visual indicator is shown when a grid ensemble has a varying number of K layers.

## Import of VTK for Geomechanical Models
Geomechanical simulation results can now be imported from VTK files. The import handles tensor data such as stress and strain, and supports displacement visualization.

## Single Filter Folder
- Geometry and property filters are now available in a single combined folder.
- Case-level cell filters can be shared across views, with support for configuring them from Python.
- A cell filter can be attached to limit a perforation interval.

## Fault Distance
- Fault distance can now be calculated to a selected set of faults.
- The user interface has been reorganized and the calculation performance improved.

## Sector Model Export
Sector model export has been substantially improved, including support for a custom input DATA file, refinement of individual cells or groups of cells, and handling of aquifer, FIP, valve, **BCCON** and **BCPROP** keywords.

## Well Events and Schedule Export
- Generation of time-dependent well events and schedule data.
- Improved keyword grouping and ordering in exported schedule files, optional export of **WELSEGS** and **COMPSEGS**, and added time precision in exported timelines.

## Correlation and Tornado Plots
- Correlation report plots support click-to-select realization and improved control over subplot visibility.
- Correlation and tornado bar-chart behavior has been harmonized, and sorting of realizations in tornado plots improved.
- Ensemble correlation plots can be created using a delta ensemble.

## Python Improvements
- Access to the tie-in depth of a well path, control of well path and polygon colors, and the port number exposed on the **Instance** class.
- Create discrete grid properties, read well log information, get regular surface information, and organize **Polygon** objects in folders.
- Improved enum handling and documentation in the API, and a modernized Python project setup.

## Fixes and Improvements
- **ACTNUM** is now imported correctly when stored only in the **EGRID** file.
- Flip XY is now applied when loading a project file, and completion export no longer omits perforation intervals when a grid has been Y-flipped.
- Well completion now uses fracture properties and K-indexes for dual porosity models.
- Plot Well Allocation no longer omits the first well connection in the plot and plot data.
- Negative values are now included in DEPTH calculations for grid models.
- Improved near/far clipping-plane calculation so very small models are placed correctly in the view.
- Fixed summary curve appearance not responding for ensemble cross-plotting, and missing individual-realization curves in the Plot Editor.
- Fixed a crash when picking a cell with a combined **MULT** result displayed.
- Removed duplicate entries in the recently used files list.
- General robustness and crash-handling improvements driven by automated crash reports.
