+++
title = "Summary Plot Source Stepping"
published = true
weight = 20
+++

![]({{< relref "" >}}images/plot-window/SummarySourceSteppingBanner.png)

Summary Plot Source Stepping enables the user to efficiently step through multiple vectors, wells, summary cases, ensembles, groups, regions, blocks, and aquifers for plotting purposes.
Source stepping is available from both the **Source Stepping Toolbar** and the **Property editor** as described below.

## Source Stepping using the toolbar
The toolbar for source stepping is:

![]({{< relref "" >}}images/plot-window/SummarySourceSteppingToolbar.png)

Following this example, the available options are:

- Explicitly setting **Step By** to vector WBHP by 
{{< image-in-text src="images/plot-window/SummarySourceSteppingToolbarExplicit.png" >}}
- Change existing plot to display previous or next vector by pressing one of the buttons
{{< image-in-text src="images/plot-window/SummarySourceSteppingToolbarPrevNext.png" >}}
- Step previous or next vector and add a *plot* by the buttons
{{< image-in-text src="images/plot-window/SummarySourceSteppingToolbarAddPlotPrevNext.png" >}}
- Step previous or next vector and add a *curve* by the buttons
{{< image-in-text src="images/plot-window/SummarySourceSteppingToolbarAddCurvePrevNext.png" >}}

## Source Stepping using the Property Editor
Source Stepping is also available through the **Property Editor**.
By selecting a subplot in **Plots** as in the example below, the *Data Sources* section of the **Property editor** emerges.
As seen, ResInsight per default lists the most probable stepping dimensions by a consideration of the actual plot being a vector of a specific well. 

![]({{< relref "" >}}images/plot-window/SummarySourceSteppingPropertyEditor.png)

## Change Well Data Source from 3D View
If multiple plots are using well as data source, the plot content can be uptedate by clicking on well geometry in 3D. This can be efficient if there are many wells in a model.

- create plots based on well summary vectors
- make sure source stepping dimension is set to **Well**
- activate the update of plots by clicking on button with tool tip text *"Update wells used in plots from well selections in 3D view."*
- open a 3D view, click on wells and the well data source in plots will be updated accordingly


![]({{< relref "" >}}images/plot-window/SummarySourceStepping3dview.png)


## Source Stepping dimensions
ResInsight decides default step dimensions based on a consideration of visible curves in the current plot or subplot. For instance, well stepping is set as default if all curves display data from the same well, c.f. examples above.
However, the complete set of source stepping dimensions is always available in both the toolbar and Property Editor:

- Vector
- Well
- Summary Case
- Ensemble
- Group
- Region
- Block
- Aquifer

When clicking a *next* or *previous* button, all curves are changed to display data for the selected source stepping dimension. 
For instance, when clicking {{< image-in-text src="images/plot-window/SummarySourceSteppingToolbarPrevNext.png" >}}
with *Well* as source stepping dimension, all curves in the current plot are changed to display data for previous/next well.


