+++
title = "What's New in 2021.10"

weight = 10
hidden = true
+++


## Ensemble Surface
![](/images/surface/surface-in-3d.png)

 To study the structural uncertainty for an ensemble of cases, ResInsight enables the user to import an [Ensemble Surface]({{< relref "ensemblesurface" >}}) and compute the statistical surfaces based on this ensemble.

## Ensemble Well Log
![](/images/workflows/well_log_ensemble_plot_depth_eq.png)

To study the uncertainty for well log extraction curves, ResInsight enables the user to import an [Ensemble Well Log]({{< relref "ensemblewelllog" >}}) and compute the statistical distribution in this ensemble. 

## Performance
Improved performance for grid model import from **GRDECL**. Improved performace for surface geometry import.

## Multiselect including Undo/Redo of Operations
![](/images/getting-started/ResInsightPlotProjectTreeMultiSelectAction.png)

[Multiple selection]({{< relref "getting-started/projecttree" >}}) of items in ResInsight offers an entrance to powerful combinations and collective actions including [Undo and Redo]({{< relref "getting-started/projecttree" >}}) functionality {{< image-in-text src="images/getting-started//ResInsightPlotProjectTreeToolbarUndoRedo.png" >}}. If the user regrets an action, for instance the color setting for multiple wells as exemplified above, the collective action can be undone by pressing *Undo*.

## Python API
Several improvements and more examples

- well path completion export
- generate ensemble of well logs
- generate ensemble of surfaces
- modeled well path with laterals
- create well path from well targets

https://api.resinsight.org/en/stable/PythonExamples.html



## Additional New Features and Enhancements

- Support for relperm and PVT plots for dual porosity models
- Fixed issue related to negative values in delta case contour maps
- Color legend for water saturations (SWAT) will now have blue on top
- Execute last script from context menu of script folder

See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.
