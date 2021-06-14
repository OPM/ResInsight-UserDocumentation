+++
title = "What's New in 2021.06"
published = true
weight = 10
hidden = true
+++

Version 2021.06 is a major update bringing a range of significant new and enhanced features as described below.

## Multilateral Wells
![]({{< relref "" >}}images/3d-main-window/MultiLateralWell_3d_view.png)
ResInsight lets the user create [Multilateral Well Paths]({{< relref "wells-and-completions/createmultilateralwellpaths" >}}) by clicking in the 3D view. Completions can be added to laterals, and the complete specification of the well can 
be exported using the [Completion Export]({{< relref "completionexport" >}})


## Streamlines
![]({{< relref "" >}}images/3d-main-window/Streamlines.png)

[Streamlines]({{< relref "3d-main-window/Streamlines" >}}) lets the user investigate the flow of different phases through a reservoar. It allows for selecting both an individual phase or a combination of phases colored by the dominant phase or velocity. The visualization and animation of streamlines requires the Eclipse properties **FLRGASI/J/K FLRWATI/J/K FLROILI/J/K**.


## Objective Functions
![]({{< relref "" >}}images/plot-window/ObjectiveFunctionsPlotColoring.png)

[Objective Functions]({{< relref "plot-window/ObjectiveFunctions" >}}) are used to color the curves of an ensemble plot in ResInsight to highlight characteristics by a function definition based on individual summary vectors. As shown in the example above, the legend relates colours to values as calculated by a particular objective function and shows the use and formula of the objective function in the plot.


## Vertical Flow Performance Plots
![]({{< relref "" >}}images/plot-window/VFP_Plot.png)

A [Vertical Flow Performance Plot (VFP Plot)]({{< relref "plot-window/VfpPlot" >}}) shows the relationship between bottom hole well conditions and wellhead pressure describing a well's ability to lift fluids to the surface. ResInsight can display both production and injection VFP plots.

## Integrated ResInsight Help
If you need the [User Manual]({{< relref "helpmenuanddocumentation" >}}) for an object, you can use the right-click menu of the object and select **Search Help for:**. This will open up the user manual for the selected object from **resinsight.org**.

![]({{< relref "" >}}images/getting-started/help_on_context_menu.png)

## ResInsight Online Tutorials
![]({{< relref "" >}}images/getting-started/tutorials-you-tube.png)

- [ResInsight Tutorial Videos (YouTube)](https://www.youtube.com/channel/UCEJoH_ti1YZXz4hPMeAKMgw)
- [ResInsight Tutorials](https://github.com/CeetronSolutions/resinsight-tutorials)

## Polygon Cell Filter
![]({{< relref "" >}}images/3d-main-window/CellFilter_Polygon.png)

[Polygon Cell Filter]({{< relref "3d-main-window/Filters" >}}#cell-filters) allows the user to define a filter by marking target points of a polygon in 3D view to include or exclude matching cells. Target points are defined and manipulated in 3D view as decribed in [User Defined Polyline Annotations]({{< relref "Annotations.md" >}}). Vertically, the filter can be set to use the XY target positions or IJK-index of targeted cells. The actual filtering can be specified to whole cells inside polygon, cell center inside polygon, or any cell corner inside polygon.


## Multiselect including Undo/Redo of Operations
![]({{< relref "" >}}images/getting-started/ResInsightPlotProjectTreeMultiSelectAction.png)

[Multiple selection]({{< relref "getting-started/projecttree" >}}) of items in ResInsight offers an entrance to powerful combinations and collective actions including [Undo and Redo]({{< relref "getting-started/projecttree" >}}) functionality {{< image-in-text src="images/getting-started//ResInsightPlotProjectTreeToolbarUndoRedo.png" >}}. If the user regrets an action, for instance the color setting for multiple wells as exemplified above, the collective action can be undone by pressing *Undo*.

## Ensemble RFT Plot - Color by Ensemble Parameter
![]({{< relref "" >}}images/plot-window/EnsembleRftPlotColors.png)

[Ensemble RFT Plot]({{< relref "plot-window/ensemblerftplot" >}}#color-by-ensemble-parameter) can be colored by Ensemble Parameter. One ensemble parameter is selected to control coloring. The ensemble parameter value for each case is used to pick a color in a color range. In this case a color legend appears.


## Additional New Features and Enhancements

- Support for relperm and PVT plots for dual porosity models
- Fixed issue related to negative values in delta case contour maps
- Color legend for water saturations (SWAT) will now have blue on top
- Execute last script from context menu of script folder

See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.
