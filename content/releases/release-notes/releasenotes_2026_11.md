+++
title = "What's New in 2026.11"
weight = 93
hidden = false
search_ignore = true
aliases = ["/releases/release-notes/latest/"]
+++

## Correlation Plots
- The correlation report shows the history curve in the summary plot, and the cross plot shows the history value at the selected time step.
- Clicking a bar in the tornado plot updates the other plots in the correlation report.
- The RFT correlation plot supports filtering by formations, and formations can be read from an ensemble `formations.csv` file.

![](/images/plot-window/CorrelationPlotsHistoryValues.png?width=500px)

[Correlation Plots]({{% relref "CorrelationPlots" %}})

[RFT Correlation Plot]({{% relref "RftCorrelationPlot" %}})

## Decline Curve Analysis
- New **Auto (Arps)** decline curve type, where the decline constant is fitted to the data.
- Decline parameters can be found by regression on the history values, in addition to matching the start and end point.
- The decline equations can be displayed in the plot, and the time range is selected by date.
- Decline curves are created with distinct colors.

![](/images/plot-window/DeclineCurveAnalysis.png?width=500px)

[Decline Curve Analysis]({{% relref "DeclineCurveAnalysis" %}})

## Contour Maps in 3D Views
Contour maps, including ensemble contour maps, can be shown inside a regular 3D view together with the grid, wells and surfaces. The map surface and contour lines can be drawn on a flat plane, or draped onto the top of the visible geometry.

![](/images/3d-main-window/ContourMapIn3dView.png?width=500px)

[Contour Maps in 3D Views]({{% relref "ContourMaps" %}}#contour-maps-in-3d-views)

## Summary Plots
- A common legend can be shown above the subplots of a summary plot. When the curve color and symbol are given by different summary dimensions, the legend is split into a color legend and a symbol legend.
- Ensemble history vectors are plotted from the first realization only, without statistics, and drawn on top of the realization curves.

![](/images/plot-window/SummaryPlotCommonLegend.png?width=500px)

[Common legend for subplots]({{% relref "SummaryPlots" %}}#common-legend-for-subplots)

[History curves]({{% relref "EnsemblePlotting" %}}#history-curves)

## Generic View
A generic view can display well paths, surfaces, polygons and annotations without a loaded grid model. A generic view is created automatically when well paths or surfaces are imported into a project without 3D views.

![](/images/3d-main-window/GenericView.png?width=500px)

[Generic View]({{% relref "GenericView" %}})

## Restore Previous Project Versions
Previous versions of a project file can be restored from the project backup database using **File > Restore Previous Project Versions...**. This replaces the standalone restore tool.

[Project File Revisions]({{% relref "ProjectFileRevisions" %}})

## Formations
- Formation zones can be imported from an FMU zone range file (`zonation_ecl_map.yml`), in addition to `.lyr` files and `layer_zone_table.txt`.
- Zone colors are read from an FMU `stratigraphy.json` file located next to the zone file.
- Formations are imported automatically for each realization in a grid case ensemble. When several formation files are present, `.lyr` files take priority over `zonation_ecl_map.yml`, followed by `layer_zone_table.txt`.

[Formations and Well Picks]({{% relref "FormationImport" %}})

## Additional Fixes and Improvements
- Flow diagnostics is supported for grids imported with the opm-common reader.
- Polygon intersections can be created from a polygon digitized in the 3D view.
- Ensemble contour maps can be filtered by an ensemble data filter, for example on formations or a property value range. See [Ensemble Contour Maps]({{% relref "EnsembleContourMap" %}}#data-filter).
- Ensemble well logs can be created directly from a well path, with default import of EGRID files and improved handling of file names that do not match the ensemble pattern. See [Ensemble Well Log]({{% relref "EnsembleWellLog" %}}).
- **Compute Contour Map Peaks** detects the locations of local maxima in a contour map. See [Contour Map Peaks]({{% relref "ContourMaps" %}}#contour-map-peaks).
- MSW export supports optional minimum and maximum segment length per segment interval.
- Relative permeability plots can show 1-SGAS on the x-axis.
- Grid models can be reordered in the project tree.
- Recently used folders are shown when selecting a folder.
- Ensemble parameters can be exported to file.
- User-defined plot axis ranges are kept when summary cases and ensembles are added, reloaded or replaced.
- PLT and RFT plots are supported for wells in radial grids.
- Improved performance of geometry computations when opening a grid.
- Python: Added support for ensemble summary data and multiple ensembles in plots, and updated the summary multi plot interface.
- Fixed wrong units for field unit models in RFT plots, LAS export, observed FMU data and fracture D-factor.
- Fixed several crashes, including crashes when reading malformed input files.
