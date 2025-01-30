+++
title = "Comparison View"

weight = 135
+++

![]({{< relref "" >}}images/3d-main-window/3DComparisonView.png)

ResInsight offers a **Comparison View** to compare two existing views in terms of grid geometry, results, intersections and more. 
The Comparison View allows comparison of information of different grids and different solutions on the same grid in a single view.
This improves efficiency and simplifies the workflow when working with related but different models.

The figure above exemplifies a Comparison View for comparison of two different simulations models and results. 
The left hand side is used to display grid and results of an [Eclipse simulation]({{< relref "eclipsecases" >}})
while the right hand side displays an ABAQUS grid and simulation results from [geomechanical analysis]({{< relref "geomechanicaldata" >}}). 

A different way to use the Comparison View is to compare the same geometrical grid with different [Cell Results]({{< relref "cellresults" >}}). 
Thus two cell results can easily be seen together in the same view.

## Creating a Comparison View

A Comparison View can be created as follows:

- In **Project Tree**, select a view and specify **Comparison View** in the **Viewer** section of **Property Editor**
- Right-click a 3D View, and select **Compare To...**


![]({{< relref "" >}}images/3d-main-window/3DComparisonViewCreate.png)

## Comparison View Divider

In the figure below, the Comparison View is used to compare two different grids in the same view, one to the left and the other to the right of the  divider between them.  The screen aligned divider is  possible to drag right and left by clicking the handle marked by a green circle.

![]({{< relref "" >}}images/3d-main-window/3DComparisonViewDividerHandle.png)

## View Properties and Settings

Properties of an individual view included in a Comparison View are controlled by their respective settings, notably 
[3D Views]({{< relref "3dviews" >}}), 
[Cell Results]({{< relref "cellresults" >}}), 
[Result Color Legend]({{< relref "resultcolorlegend" >}}), 
[Cell Filters]({{< relref "filters" >}}),
and [Intersections]({{< relref "intersections" >}}).

Setting up [Linked Views]({{< relref "linkedviews" >}}) may also be relevant, e.g. to syncronize [cell results]({{< relref "cellresults" >}})
and [cell filters]({{< relref "filters" >}}).

{{% notice note %}}
[Polyline Intersections]({{< relref "intersections" >}}#polyline-intersection) does not facilitate picking points across the Comparison View divider. However, an intersection can be copied betweens views, see [Intersections]({{< relref "intersections" >}}) for details.
{{% /notice %}}
