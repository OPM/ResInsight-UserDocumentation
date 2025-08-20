+++
title = "What's New in 2025.09"
weight = 98
hidden = false
search_ignore = true
+++

## Ensemble Import and Management

The import dialog when searching the file system for ensemble data is improved, allowing for easy selection of multiple ensembles. When an ensemble is imported, the realization numbers in the form of a text string (1-21,30-35, 40-60) can be edited for import of a subset of realizations.

![](/images/plot-window/Ensemble.png)

[Ensemble Import Dialog]({{% relref "ensemblefiledialog" %}})

[Ensemble Summary Plotting]({{% relref "ensembleplotting" %}})


## Other improvements
- Logging of application operations and crash report to log file by default stored in `home_folder/.resinsight/logs`


## Python API
- Added support for fishbones completions

## Command Line
- New option to define the maximum number of threads to be used by ResInsight `--threadcount` This command line option can also be specified when [launching a ResInsight process from Python](
https://api.resinsight.org/en/main/api/rips.Instance.html#rips.Instance.launch)



See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.
