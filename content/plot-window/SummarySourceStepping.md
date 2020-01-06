+++
title = "Summary Plot Source Stepping"
published = true
weight = 20
+++

![]({{< relref "" >}}images/plot-window/SummarySourceSteppingBanner.png)

## Summary Plot Source Stepping
Summary Source Stepping is a function which enables the user to swiftly step through multiple vectors. 
The functionality applies both to single summary curves and ensemble curve sets.

The functionality is available from both the toolbar and the **Summary Curves** property editor under a **Summary Plot** item in the **Main Plot Window Project Tree**.

The toolbar allows use of [vector filters]({{< relref "summaryplots#property-editor" >}}) in addition to source stepping:

![]({{< relref "" >}}images/plot-window/SummarySourceSteppingToolbar.png)

The corresponding property editor is:

![]({{< relref "" >}}images/plot-window/SummarySourceSteppingPropertyEditor.png)

When ResInsight decides stepping dimensions to display, all visible curves in the current plot are taken into account. For instance, well stepping is enabled if all curves display data from the same well, c.f. figure above. This policy applies to the following source stepping dimensions:

- Cases
- Wells
- Well groups
- Regions
- Completions
- Segments
- Block
- Summary Vectors

## Assign source stepping curve
If the plot contains a mix of different curves, ResInsight might end up with no common stepping dimensions available. 
By right-clicking a summary curve or ensemble curve set, the menu item **Set as Source Stepping Curve** will use the selected curve as basis for source stepping. All source stepping dimensions for the selected curve will be displayed. When a curve or ensemble is marked for source stepping, a source stepping icon is displayed.

![]({{< relref "" >}}images/plot-window/SummaryCurveSetSourceStepping.png)

Right-clicking the summary curve or ensemble curve set, and select **Clear Source Stepping Curve** to leave this mode.


## Handling of summary curves and history summary curves
If a plot displays both a summary curve and the corresponding history summary curve, the source stepping can be applied to both curves at the same time. If you have a mix of several curves, it might be required to mark one of the curves using **Set as Source Stepping Curve**.

## Applying data source change
When one of the **next buttons** are clicked, all curves are changed to display data for the next item for the clicked source dimension. Example: The user clicks the **next well button**. Then the well source for all curves in the current plot are changed to display data for the next well.
