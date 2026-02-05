+++
title = "What's New in 2025.12"
weight = 97
hidden = false
search_ignore = true
aliases = ["/releases/release-notes/latest/"]
+++

## Radial Grid
![](/images/import/radial-grid-overview.png)

ResInsight now supports radial grids, enabling visualization and analysis of reservoir models that use radial coordinate systems. This feature is particularly useful for well-centric models and near-wellbore analysis.

[Radial Grids]({{% relref "radialgrid" %}})

## Relative Permeability and PVT Plots
![](/images/3d-main-window/RelativePermeability.png)

**New Features**

- Imbibition Curve Support: Added display and styling for imbibition relative permeability curves, with visual differentiation from drainage curves
- Interactive Curve Tracking: Introduced cursor-based tracker that displays curve values near the mouse position for enhanced data analysis
- Dual Curve Display: Support for simultaneously showing both scaled and unscaled relative permeability curves in the same plot
- Dynamic UI Controls: Added checkboxes to independently control visibility of drainage and imbibition curve sets

**Improvements**

- Enhanced Cell Information: Added SATNUM and IMBNUM result display in the cell reference information panel
- RelPerm/PVT Display Support: Added support for displaying RelPerm/PVT data using the opm-common grid reader
- Smart Imbibition Detection: Imbibition curve selection is automatically enabled/disabled based on IMBNUM values in the data
- Performance: Access time to retrieve curve data is significantly reduced

[Relative Permeability Plots]({{% relref "resultinspection" %}}#relative-permeability-plot)

## Integration of Reservoir Simulators 

ResInsight is now able to prepare simulation files and then run a reservoir simulator. Most testing has been done using opm-flow, but other compatible simulators are expected to work. In this initial integration, it is possible to add a new well, run the simulation, and open the results from the simulator in ResInsight.

An improved sector model export is now available, including the following features:
- Export of a subset of cells
- Definition of boundary conditions for the sector model
- Conversion of IJK indices for relevant data in the model, including simulation well cells, NNCs and fault definitions
- Refinement of the sector model

[Integration of opm-flow]({{% relref "opm-flow-integration" %}})


## Improvements to Export Completions

The export dialog is now simplified slightly, and there are now two options for file splitting, either a single unified file or one file for each well. The deprecated features are marked with ~~[Deprecated] and strikethrough.~~

[Completion Export Dialog]({{% relref "completionexport" %}})

The naming of the generated files will now add "MSW" and "LGR" as postfix to make sure that the start of the filename is identical for all generated files for a simulation model.

https://github.com/OPM/ResInsight/issues/13264

## Python API

Several improvements have been made to the Python API:
- Support for completion and MSW data as Python data structures. This provides a direct way to get completion data in addition to the existing export to text files. The most important keywords for table data are WELSEGS, COMPSEGS, WSEGVALV, and WSEGAICD. LGR variants are also supported.
- Readout of ZCORN, COORD and ACTNUM from any type of grid
- Creation of grids based on ZCORN, COORD and ACTNUM

[Python Examples](https://api.resinsight.org/en/main/PythonExamples.html)

## Stability Improvements

ResInsight writes log information to text files on the local file system. This includes log messages, warnings, errors, and crash reports. These files are important for developers to track down and fix crash situations. Based on analysis of these files, performance and stability issues have been identified and fixed.

[Application Logging]({{% relref "applicationlogging" %}})

## Other

- Import of OSDU data was not working due to data center move. Import of OSDU well paths is now working as expected. https://github.com/OPM/ResInsight/issues/13026

See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.
