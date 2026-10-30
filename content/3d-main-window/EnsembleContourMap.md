+++
title = "Ensemble Contour Maps"
weight = 40
+++

![](/images/3d-main-window/ensemble-grid-contour-map.png)

ResInsight can create contour maps from an ensemble of grid models based on different forms of aggregation of 3D reservoir simulation data onto a 2D plane.

[Video Tutorial: Ensemble Contour Map](https://youtu.be/qE_PeNx3xP0?si=tSmzJhmmAtENsiYN)

## Creating Contour Maps

Use **Import Grid and Summary Ensemble** to import the grid ensemble. Select **Create Grid Ensemble**, choose the realizations to import, and click **OK**. See [Grid and Summary Ensemble]({{% relref "ImportGridAndSummaryEnsemble" %}}) for details.

Right-click the imported grid ensemble in the **Project Tree** and select **New Ensemble Contour Map**.

## Creating Contour Maps (obsolete from version 2026.09)

Import grid models using the **File->Import->More->Create Grid Case Ensemble**. The grid models can have individually specified geometry. For grids with equal geometry, consider using [Grid Case Group]({{% relref "casegroupsandstatistics" %}}). The formation information is imported for each grid.

![](/images/3d-main-window/import-grid-case-ensemble.png)

Select **"New Ensemble Contour Map"** from the right-click menu on the grid ensemble.

## Properties of the Contour Maps

![](/images/3d-main-window/statistics-contour-map-properties.png)

The **General** group is used to define how to compute the contour map. See [Contour Map]({{% relref "contourmaps" %}}) for details.

The grid case model defined by *"Primary Case"* is used for fault and simulation well visualization. The 2D area used to evaluate the contour map values is based on the bounding box of the **Primary Case**. Use **Bounding Box Expansion** to ensure that the area covers the geometry variation within the ensemble.

### Time Step Selection

Select the time steps to compute the contour map for.

### Data Filter

Select a **Data Filter** to compute the contour map from a subset of the grid cells, for example a set of formations or a property value range. Only cells accepted by the filter are used. The **Data Filter** group is shown when the grid ensemble has at least one data filter.

The filter is evaluated for each realization, so a property filter or a formation filter can select different cells in each realization. If the filter is based on a dynamic property, the cells are selected per time step, also when the contour map shows a static property.

Click **Compute** to apply a changed filter selection. The name of the active filter is shown as overlay text in the contour map view.

#### Create Data Filters

Data filters are defined on the grid ensemble and can be shared by several ensemble contour maps. Right-click the grid ensemble in the **Project Tree** and select a filter from the **Data Filters** sub menu:

- **New Property Filter** -- select cells by property value or category. Use the **Formation Names** result type to filter on formations. See [Property Filters]({{% relref "filters" %}}#property-filters).
- **Polygon Filter** -- select cells inside a polygon.
- **Range Filter** -- select cells in an I, J or K range.

The filters are listed in a **Data Filters** folder under the grid ensemble. The formations for each realization are imported automatically, see [Automatic Import for Grid Case Ensembles]({{% relref "FormationImport" %}}#automatic-import-for-grid-case-ensembles).

{{% notice note %}}
The **Formation Selection** group used in earlier versions has been replaced by data filters. A formation selection stored in a project from version 2026.09 or older is no longer applied, and a warning is shown in the log when the project is opened. Create a property filter on formation names to get the same result.
{{% /notice %}}

### Result Definition

Select the property to compute the contour map for.

## Performance Considerations

When working with multiple grid models, importing and processing data will take time. Understand how to limit the data involved in calculations, and consider a test run with a small number of realizations before using the full ensemble.

Consider setting the **Sampling Resolution** to coarse to improve performance. Note that this option will introduce some interpolation effects.

Click the **Compute** button in the **Property Editor** to start the computation.

## Display of Contour Map Data

A view is automatically created and displayed when the computation is completed. Select the **Map Projection** object to control the display. Create additional views from the right-click menu of the **Ensemble Contour Map** object.

![](/images/3d-main-window/ensemble-grid-map-projection.png)

Select the current statistical property from **Statistics Type**. A value filter can be used to filter the display of the contour map.

## Create Polygon

Select "*Create Polygon from Contour Map*" from the right-click menu. This will create a polygon of the outline of the contour map. The shape of the polygon can be simplified using the right-click menu of the generated polygon.

### References

[Contour Map]({{% relref "contourmaps" %}})

[Grid Case Group]({{% relref "casegroupsandstatistics" %}})

[Ensemble File Dialog]({{% relref "ensemblefiledialog" %}})
