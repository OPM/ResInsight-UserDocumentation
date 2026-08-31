+++
title = "What's New in 2026.09"
weight = 94
hidden = false
search_ignore = true
aliases = ["/releases/release-notes/latest/"]
+++

## Window Management
- 3D and plot windows now use a modern docking framework, making it easier to organize multiple views and combine 3D and 2D plot views on the same screen.
- Tiling operations are now updated and a tiling button is available from the toolbar

[Window Tiling]({{% relref "windowmanagement" %}})

## Grid Ensemble
- Ensemble contour maps are now supported, with improved performance for large data sets. Contour maps are cached locally to improve project import performance.

![](/images/import/ImportGridAndSummaryEnsemble.png?width=500px)

[Grid and Summary Ensemble]({{% relref "ImportGridAndSummaryEnsemble" %}})

[Grid Ensemble]({{% relref "GridEnsemble" %}})

[Ensemble Contour Map]({{% relref "ensemblecontourmap" %}})


## Histogram Logarithmic Scale
![](/images/plot-window/histogram-plot.png)

Histograms can now display logarithmic values, allowing properties such as PERM to be plotted on a logarithmic axis.

[Histogram Plots]({{% relref "histogram" %}})


## MSW Data Model and Export
The MSW data model and its corresponding text export have been updated to support future enhancements.

## Additional Fixes and Improvements
- Added **Import Summary Case** to the **File** menu.
- Added the SGAS result for two-phase gas-water models when it is missing from the simulation results.
- Fixed calculated-vector plots for delta ensembles to show all realizations.
- Statistical grid cases can now be used as sources in grid-calculator expressions.
- Fixed refresh of 3D filters after creation.
- Added RMS seed values from RMS_SEED_USED files as realization attributes.
- Fixed handling of invalid PORO_DEV values.