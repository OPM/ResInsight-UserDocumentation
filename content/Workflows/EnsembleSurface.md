+++
title = "Ensemble Surface"

weight = 90
+++

![](/images/surface/surface-in-3d.png)

## Introduction

To study the structural uncertainty, ResInsight enables the user to create and import an ensemble of surfaces and compute the statistical surfaces based on this ensemble. This page describes the interactive workflow, but in many cases it can be useful to create scripts related to mangement of **Ensemble Surfaces**. See  [Python Examples](https://api.resinsight.org/en/stable/PythonExamples.html) for more details.

## Create Ensemble Surface

- From the right-click menu of surfaces, select **Import Ensemble Surface**
![](/images/workflows/create_ensemble_surface_menu.png)

- Select the ensemble grid models to create surfaces for, either **"*.EGRID"** or **"*.GRDECL"**

- In the following dialog, select the K layers. Control if the generated surfaces should be imported into an ensemble surface immediately.
![](/images/workflows/ensemble_surface_select_k_layers.png)

## Import Ensemble Surface

An **Ensemble Surface** can be imported for one or multiple K-layers.

- From the right-click menu of surfaces, select **Import Ensemble Surface**
![](/images/surface/import-ensemble-surface.png)

- In the ensemble import dialog, select the surface files for import into ensembles
![](/images/surface/ensemble-surface-file-selection.png)

- One or multiple ensemble surface objects will be created
![](/images/surface/surface-project-tree.png)

- Import one source grid model and create a 3D view
- Control the visibility of the statistics surfaces in the **Surfaces** section in the **Property Editor** for the 3D view
![](/images/surface/surface-in-view-project-tree.png)

## Show uncertainty on intersections

- Create a well path
- Create an intersection along the well path
- Select the intersection in the **Property Editor**
- From the right-click menu, select **Create Intersection Band**
![](/images/surface/create-surface-intersection-band.png)

- Optionally add an Intersection Curve
- Adjust options for the intersection bands and curves
![](/images/surface/intersection-band-in-3d-view.png)


## Related documentation

[Create a Well Path]({{< relref "CreateNewWellPaths.md" >}})

[Intersections]({{< relref "Intersections.md" >}})