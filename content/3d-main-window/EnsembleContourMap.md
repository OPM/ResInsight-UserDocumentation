+++
title = "Ensemble Contour Maps"
weight = 40
+++

![](/images/3d-main-window/ensemble-grid-contour-map.png)

ResInsight can create contour maps from an ensemble of grid models based on different forms of aggregation of 3D Eclipse data onto a 2D plane.

## Creating Contour Maps

Import grid models using the **Create Grid Case Ensemble**. The grid models can have individually specified geometry. For grids with equal geometry, consider using [Grid Case Group]({{% relref "casegroupsandstatistics" %}}). The formation information is imported for each grid.

![](/images/3d-main-window/import-grid-case-ensemble.png)

Select "New Statistics Contour Map" from the right-click menu on the grid ensemble.

## Properties of the Contour Maps

![](/images/3d-main-window/statistics-contour-map-properties.png)

The **General** group is used to define how to compute the contour map. See [Contour Map]({{% relref "contourmaps" %}}) for details.

The grid case model defined by *"Primary Case"* is used for fault and simulation well visualization. The 2D area used to evaluate the contour map values is based on the bounding box of the **Primary Case**. Use **Bounding Box Expansion** to ensure that the area covers the geometry variation within the ensemble.

### Time Step Selection

Select the time steps to compute the contour map for.

### Formation Selection

Select the formations to compute the contour map for.

### Result Definition

Select the property to compute the contour map for.

## Performance Considerations

When working with multiple grid models, importing and processing data will take time. Understand how to limit the data involved in calculations, and consider a test run with a small number of realizations before using the full ensemble.

As the grid geometry can be defined individually, grid cell geometry needs to be imported for each case. To ensure the import of only required geometry, use the **opm-common (beta)** grid reader and make sure to import only active cell geometry, as configured in [Preferences]({{% relref "performancehints" %}}).

Consider setting the **Sampling Resolution** to coarse to improve performance. Note that this option will introduce interpolation effects.

Click the **Compute** button in the **Property Editor** to start the computation.

## Display of Contour Map Data

A view is automatically created and displayed when the computation is completed. Select the **Map Projection** object to control the display. Create additional views from the right-click menu of the **Statistics Contour Map** object.

![](/images/3d-main-window/ensemble-grid-map-projection.png)

Select the current statistical property from **Statistics Type**. A value filter can be used to filter the display of the contour map.

## Create Polygon

Select "*Create Polygon from Contour Map*" from the right-click menu. This will create a polygon of the outline of the contour map. The shape of the polygon can be simplified using the right-click menu of the generated polygon.

### References

[Contour Map]({{% relref "contourmaps" %}})

[Grid Case Group]({{% relref "casegroupsandstatistics" %}})