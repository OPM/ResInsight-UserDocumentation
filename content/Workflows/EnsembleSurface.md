+++
title = "Ensemble Surface"
published = true
weight = 90
+++

![]({{< relref "" >}}images/surface/surface-in-3d.png)

## Introduction


To study the structural uncertainty, ResInsight enables the user to import an ensemble of surfaces and compute the statistical surfaces based on this ensemble. 

How to create ensemble surfaces

## Workflow

- From the right-click menu of surfaces, select **Import Ensemble Surface**
![]({{< relref "" >}}images/surface/import-ensemble-surface.png)

- In the ensemble import dialog, select the surface files for import into ensembles
![]({{< relref "" >}}images/surface/ensemble-surface-file-selection.png)

- One or multiple ensemble surface objects will be created
![]({{< relref "" >}}images/surface/surface-project-tree.png)

- Import one source grid model and create a 3D view
- Control the visibility of the statistics surfaces in the **Surfaces** section in the **Property Editor** for the 3D view
![]({{< relref "" >}}images/surface/surface-in-view-project-tree.png)

## Show uncertainty on intersections

- Create a well path
- Create an intersection along the well path
- Select the intersection in the Property Editor
- From the right-click menu, select **Create Intersection Band**
![]({{< relref "" >}}images/surface/create-surface-intersection-band.png)

- Optionally add an Intersection Curve
- Adjust options for the intersection bands and curves
![]({{< relref "" >}}images/surface/intersection-band-in-3d-view.png)


## Related documentation

[Create a Well Path]({{< relref "CreateNewWellPaths.md" >}})

[Intersections]({{< relref "Intersections.md" >}})