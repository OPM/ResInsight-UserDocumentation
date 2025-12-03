+++
title = "What's New in 2025.12"
weight = 97
hidden = false
search_ignore = true
+++

## Radial Grid
![](/images/import/radial-grid-overview.png)

ResInsight supports radial grids, enabling visualization and analysis of reservoir models that use radial coordinate systems. This is particularly useful for well-centric models and near-wellbore analysis.

[Radial Grids]({{% relref "radialgrid" %}})

## Relative Permeability and PVT plots

**New Features**

- Imbibition Curves Support: Added display and styling for imbibition relative permeability curves, with visual differentiation from drainage curves
- Interactive Curve Tracking: Introduced cursor-based tracker that displays curve values near the mouse position for enhanced data analysis
- Dual Curve Display: Support for simultaneously showing both scaled and unscaled relative permeability curves in the same plot
- Dynamic UI Controls: Added checkboxes to independently control visibility of drainage and imbibition curve sets

**Improvements**

- Enhanced Cell Information: Added SATNUM and IMBNUM result display in cell reference information panel
- Support for display of RelPerm/PVT is now supported using the opm-common grid reader
- Smart Imbibition Detection: Imbibition curve selection is automatically enabled/disabled based on IMBNUM values in the data
- Performance: The access time to retrieve curve data is significantly reduced

[Relative Permeability Plots]({{% relref "resultinspection" %}}#relative-permeability-plot)

## Integration of Reservoir Simulators 

ResInsight has now able to prepare simulation files and then run a reservoir simulator. Most of the testing is done using opm-flow, but other compatible simulators is expected to work. In this first integration, it is possible to add a new well, run the simulation, and open the result from the simulator in ResInsight.

An improved export of sector model is now available, including the following features:
- export of a subset of cells
- definition of boundary conditions for the sector model
- conversion of IJK indices for relevant data in model, including simulation well cells, NNCs and fault definitions
- refinement of sector model

[Integration of opm-flow]({{% relref "opm-flow-integration" %}})


## Improvements to Export Completions

The export dialog is now simplified slightly, and there are now two options for file splitting, either a single unified file or one file for each well. The deprecated features are marked with ~~[Deprecated] and strikethrough.~~

[Completion Export]({{% relref "completionexport" %}})

The naming of the generated files will now add "MSW" and "LGR" as postfix to make sure that the start of the filename is identical for all generated files for a simulation model.

https://github.com/OPM/ResInsight/issues/13264

## Python API

Several improvements have been made to the Python API. 
- Suppport for completion and MSW data as Python data structures. This is added as a direct way to get completion data in addition to the existing export to text files. Most important keywords for tables data is WELSEGS, COMPSEGS, WSEGVALV, WSEGAICD. In addition, LGR variants are also supported.
- Readout of ZCORN, COORD and ACTNUM from any type of grid
- Creation of grid based on ZCORN, COORD and ACTNUM

[Python Examples](https://api.resinsight.org/en/main/PythonExamples.html)

## Stability Improvements

ResInsight writes log information to a text file on the local file system. This includes log messages, warnings, errors and crash reports. These files are important for developers to track down and fix crash situations. Based on some of these files, performance and stability issues has been identified and fixed.


See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.
