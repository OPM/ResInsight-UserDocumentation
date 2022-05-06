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

- Explicitly setting stepping dimension and vector, e.g. WBHPH by 
{{< image-in-text src="images/plot-window/SummarySourceSteppingToolbarExplicit.png" >}}
- Change existing plot to display previous or next quantity by pressing one of the buttons
{{< image-in-text src="images/plot-window/SummarySourceSteppingToolbarPrevNext.png" >}}
- Step to previous or next quantity and add a *plot* of that quantity by the buttons
{{< image-in-text src="images/plot-window/SummarySourceSteppingToolbarAddPlotPrevNext.png" >}}
- Step to previous or next quantity and add a *curve* for that quantity by the buttons
{{< image-in-text src="images/plot-window/SummarySourceSteppingToolbarAddCurvePrevNext.png" >}}

## Source Stepping using the Property Editor
Source Stepping is also available through the **Property Editor**.
By selecting a subplot in **Plots** as in the example below, the *Data Sources* section of the **Property editor** emerges.
As seen, ResInsight per default lists the most probable stepping dimensions by a consideration of the actual plot being a vector of a specific well. 

![]({{< relref "" >}}images/plot-window/SummarySourceSteppingPropertyEditor.png)

## Source Stepping dimensions
ResInsight decides default step dimensions based on a consideration of visible curves in the current plot or subplot. For instance, well stepping is set as default if all curves display data from the same well, c.f. examples above.
However, the complete set of source stepping dimensions is always available in both the toolbar and Property Editor:

- Quantity
- Wells
- Summary Cases
- Ensembles
- Groups
- Regions
- Blocks
- Aquifers

When clicking a *next* or *previous* button, all curves are changed to display data for that item of selected source stepping dimension. 
For instance, when clicking {{< image-in-text src="images/plot-window/SummarySourceSteppingToolbarPrevNext.png" >}}
with *Well* as source stepping dimension, all curves in the current plot are changed to display data for previous/next well.


