+++
title = "What's New in 2025.09"
weight = 98
hidden = false
search_ignore = true
+++

## Ensemble Import and Management

The import dialog when searching the file system for ensemble data is improved, allowing for easy selection of multiple ensembles. When an ensemble is imported, the realization numbers in the form of a text string (1-21,30-35, 40-60) can be edited for import of a subset of realizations.

![](/images/plot-window/summary-file-set.png)
![](/images/plot-window/Ensemble.png)


[Ensemble Import Dialog]({{% relref "ensemblefiledialog" %}})

[Ensemble Summary Plotting]({{% relref "ensembleplotting" %}})

## Performance
There has been several improvements related to summary performance in this release. These improvements are related to file operations and plot updates. The overall improved performace is significant for large cases with many summary ensembles and many plots.

## Other improvements
- Logging of application operations and crash report to log file by default stored in `home_folder/.resinsight/logs`
- Improved color control of RFT ensemble curves
- Length and area of a [Polygon]({{% relref "polygons" %}}) can be displayed as a label
- Geomechanical data import has been expanded beyond the existing ABAQUS file format support. VTK grid files can now be imported as an additional source for geomechanical data, providing users with more flexibility in data ingestion. Most existing geomechanical analysis features are available for data imported from VTK.
- Import of surface in IRAP and GRI
- Import of [RMS Well Path]({{% relref "wellpaths" %}}) and RMS Well Logs

## Python API
Several improvements have been made to the Python API. 
- Improved error management and error reporting
- Create grid from COORD, ZCORN and ACTNUM
- Create regular surface 
- Added support for Non-Darcy parameters for perforation intervals
- Create polygon from list of point
- Create perforation interval

[Python Examples](https://api.resinsight.org/en/main/PythonExamples.html)



## Command Line
- New option to define the maximum number of threads to be used by ResInsight `--threadcount` This command line option can also be specified when [launching a ResInsight process from Python](
https://api.resinsight.org/en/main/api/rips.Instance.html#rips.Instance.launch)



See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.
