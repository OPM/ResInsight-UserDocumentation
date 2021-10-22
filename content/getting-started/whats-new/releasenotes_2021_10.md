+++
title = "What's New in 2021.10"
published = true
weight = 10
hidden = true
+++


## Performance
Improved performance related to several text import features. Input of a grid model from **GRDECL** has improved significantly. Also surface geometry import has improved.

![]({{< relref "" >}}images/3d-main-window/MultiLateralWell_3d_view.png)
ResInsight lets the user create [Multilateral Well Paths]({{< relref "wells-and-completions/createmultilateralwellpaths" >}}) by clicking in the 3D view. Completions can be added to laterals, and the complete specification of the well can 
be exported using the [Completion Export]({{< relref "completionexport" >}})

## Ensemble Surface
![]({{< relref "" >}}images/surface/surface-in-3d.png)

 To study the structural uncertainty for an ensemble of cases, ResInsight enables the user to import an [Ensemble Surface]({{< relref "ensemblesurface" >}}) and compute the statistical surfaces based on this ensemble.

## Ensemble Well Log
![]({{< relref "" >}}images/workflows/well_log_ensemble_plot_depth_eq.png)

To study the uncertainty for well log extraction curves, ResInsight enables the user to import an [Ensemble Well Log]({{< relref "ensemblewelllog" >}}) and compute the statistical distribution in this ensemble. 


## Ensemble Fractures
![]({{< relref "" >}}images/plot-window/VFP_Plot.png)

**TODO**


## Multiselect including Undo/Redo of Operations
![]({{< relref "" >}}images/getting-started/ResInsightPlotProjectTreeMultiSelectAction.png)

[Multiple selection]({{< relref "getting-started/projecttree" >}}) of items in ResInsight offers an entrance to powerful combinations and collective actions including [Undo and Redo]({{< relref "getting-started/projecttree" >}}) functionality {{< image-in-text src="images/getting-started//ResInsightPlotProjectTreeToolbarUndoRedo.png" >}}. If the user regrets an action, for instance the color setting for multiple wells as exemplified above, the collective action can be undone by pressing *Undo*.


## Additional New Features and Enhancements

- Support for relperm and PVT plots for dual porosity models
- Fixed issue related to negative values in delta case contour maps
- Color legend for water saturations (SWAT) will now have blue on top
- Execute last script from context menu of script folder

See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.
