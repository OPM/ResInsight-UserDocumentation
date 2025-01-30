+++
title = "Filters"

weight = 70
+++

![]({{< relref "" >}}images/3d-main-window/FiltersOverview.png)

Filters are used to control the visibility of cells in the 3D view. Two types of filters exist:

- **Cell Filter** -- Extracts subset(s) of grid cells
- **Property Filter** -- Extracts cells with a property value matching a value range

{{% notice note %}}
The visibility of cells connected to wells, and fences can be controlled from <b> <a href="{{< relref "simulationwells" >}}">Simulation Wells</a></b>.<br> 
<small><i>(Not applicable for Geomechanical cases)</i></small>
{{% /notice %}}

## Filters Settings

Filters can be turned on and off using their check-boxes in **Project Tree** and controlled by their corresponding **Property Editor**. The sequence of the filters can be rearranged by clicking the arrow icons of selected filter.

![]({{< relref "" >}}images/3d-main-window/FiltersInTreeView.png)

Cell Filters and Property filters can either be set to **Include** or **Exclude** the matching cells. 
The *Include* setting marks the cells as visible while the *Exclude* setting is used to remove cells from visualization regardless of other filters. 
The icon in front of each filter show a + or - sign to indicate *Include* or *Exclude* {{< image-in-text src="images/3d-main-window/FilterIncEx.png" >}}.

## Cell Filters
**Cell Filters** enables the user to define a set of visible regions in the 3D view.
Each *Include* cell filter will add cells to the visualization and the resulting 3D view will show the union of all the *Include* cell filters.

The logical operation combining multiple **Cell Filters** is defined by *"Combine Polygon and Range Filters Using Operation"*

![]({{< relref "" >}}images/3d-main-window/cellfilters_combine.png)

A new cell filter can be added by invoking the right-click menu for the **Cell Filters** collection in **Project Tree**. 

![]({{< relref "" >}}images/3d-main-window/CellFilterTypes.png)

The available cell filters are:

- **Polygon Filter**: Defining a filter by marking target points of a polygon in 3D view to include or exclude matching cells. The polygon can be defined as part of the filter or referencing a polygon defined in the [Polygons]({{< relref "polygons" >}}) collection.

- **User Defined Filter**: Defining a filter by specifying explicit cells to include or exclude by their IJK-index.

- **Range Filter**: Defining a filter to include or exclude cells by specifying IJK-ranges. For radial models, IJ represents angle and radius.

- **Slice Filter**: Defining a filter to include or exclude a slice of cells in either I-, J-, or K-direction.

The following exemplifies the use of a **Polygon Filter** and target points. Target points are defined and manipulated in 3D view as decribed in [Polygons]({{< relref "polygons" >}}). Vertically, the filter can be set to use the XY target positions or IJK-index of targeted cells. The actual filtering can be specified to whole cells inside polygon, cell center inside polygon, or any cell corner inside polygon.

![]({{< relref "" >}}images/3d-main-window/CellFilter_Polygon.png)

{{% notice note %}}
A filter can be added directly from <b>3D View</b> by right-clicking a cell using the displayed menu. 
{{% /notice %}}

Below is a snapshot of the **Property Editor** for the **Range Filter** type of Cell Filter:

![]({{< relref "" >}}images/3d-main-window/RangeFilterProperties.png)

 - **Filter Type** -- The filter can either make the specified range visible ( *Include* ), or remove the range from the View ( *Exclude* ).
 - **Grid** --  This option selects which of the grids the range is addressing.
 - **Apply to Subgrids** -- This option tells ResInsight to use the visibility of the cells in the current grid to control the visibility of the cells in sub-LGR's. If this option is turned off, Sub LGR-cells is not included in this particular Range Filter.  
 
The **Start** and **Width** labels in front of the sliders features a number in parenthesis denoting maximum available value.
The **Start** labels show the index of the start of the active cells.
The **Width** labels show the number of active cells from the start of the active cells.

## Property Filters

**Property Filters** applies to the results of the **Cell Filters** and limits the visible cells to the ones approved by the filter. For a cell to be visible it must be accepted by all property filters. 

A new property filter is created by activating the right-click menu on **Property Filters** or by right-clicking inside a 3D view. The new property filter is based on the currently viewed cell result by default. 

The name of the property filter is automatically set to *"propertyname (min .. max)"* as you edit the property filter.

{{% notice note %}}
The right-click command <b>Apply As Cell Result</b> on a property filter, sets the Cell Color Result to the same values as the selected property filter.
{{% /notice %}}

Below is a snapshot of the **Property Editor** of the **Property Filter**.
  
![]({{< relref "" >}}images/3d-main-window/PropertyFilterProperties.png)

### Property Value Range
The filter is based on a property value range (Min - Max). Cells in the range are either shown or hidden depending on the **Filter Type** (*Include*/*Exclude*). Exclude-filters removes the selected cells from the **View** even if some other filter includes them.

#### Range Behavior for Flow Diagnostic Results
Normally the available range in the sliders is the max and min of all the values in all the time steps. For Flow Diagnostics results, however, the available range is based on the current time step. 

We still need to keep the range somewhat fixed while moving from time step to time step, so in order to do so ResInsight tries to keep the intentions of your range settings, as the available range changes. If either the max or min value is set to the limit, ResInsight will keep that setting at the limit even when the limit changes. If you set a specific value for the max or the min, that setting will keep its value, even if it happens to end up outside the available range at a time step.   

### Category Selection
If the property is representing integer values, well tracer names or [ formation names ]({{< relref "" >}}3d-main-window/formations), the property filter displays a list of available categories used to filter cells. The separate values can then be toggled on or off using the list in the Property Editor.

![]({{< relref "" >}}images/3d-main-window/PropertyFilterWithCategories.png)

If it is more convenient to filter the values using a value range, toggle the **Category Selection** option off.

