+++
title = "Surfaces"
published = true
weight = 85
+++

![]({{< relref "" >}}images/3d-main-window/SurfacesOverview.png)

ResInsight is capable of mapping properties and simulation results onto 3D surfaces imported from GOCAD and Petrel as specified below. 


## Import and appearance of surfaces

3D surfaces from GOCAD and Petrel are imported into ResInsight by the menu option **File**->**Import**->**Import Surfaces** 
in the **3D Main Window**.

![]({{< relref "" >}}images/3d-main-window/SurfacesImport.png)

Imported surfaces are listed under the {{< image-in-text src="images/3d-main-window/SurfacesProjectTreeNode.png" >}} entry 
in the **Project Tree**. You can click on a surface to change i.e. the name or color of the surface, or change the file to read the surface data from. 

![]({{< relref "" >}}images/3d-main-window/SurfacesPropertyEditor.png)

You can also change the depth of the surface by adding a depth offset (positive or negative). This could be used i.e. to import the same surface file multiple times and assign each instance of the surface a separate depth offset. When a depth offset is set, the offset value will be shown as part of the surface name in the project tree.

![]({{< relref "" >}}images/3d-main-window/surface_multiple.png)

{{% notice note %}}
Multiple surfaces can be imported at the same time by choosing more than one input file in the file selection window that shows up when you start an import.
{{% /notice %}}


## Using folders

To make it easier to organize the surfaces you import into your project, ResInsight supports creating surface folders in the project tree. To create a new folder, right-click on the top level **Surfaces** folder in the project tree and choose **Add Folder**.

![]({{< relref "" >}}images/3d-main-window/surface_addfolder.png)


## Surface Results

Per default, ResInsight maps current **Cell Result** on a given surface. 
If another result is to be displayed, specify the result under **Separate Surface Results** as shown below.

![]({{< relref "" >}}images/3d-main-window/SurfacesSeparateSurfaceResults.png)

Clicking a surface of a **View** in the **Project Tree** activates the Property Editor for allowing view settings as shown below. 

To change result displayed on the surface, please specify the desired result in the **Separate Result Reference**
section of the Property Editor.

![]({{< relref "" >}}images/3d-main-window/SurfacesViewPropertyEditor.png)


## Reloading Surfaces

If you have modified a surface file using an external program, you can easily load the changes into ResInsight by using the reload surface feature. Bring up the right-click menu for the surface you want to reload and choose  **Reload**. The views will automatically update with the new data (could take a few seconds).

![]({{< relref "" >}}images/3d-main-window/surface_reload.png)

## Create a copy

You can easily create a copy of an existing surface by choosing  **Create Copy** in the surface right-click menu. A new, identical surface will show up at the same level in the project tree. You can now give it a new name, change depth offset etc.

![]({{< relref "" >}}images/3d-main-window/surface_copy.png)

## Grid Case Surfaces

In addition to importing surfaces from file, ResInsight can also generate grid case surfaces. You do that by bringing up the right-click menu for the {{< image-in-text src="images/3d-main-window/SurfacesProjectTreeNode.png" >}} project tree entry and choose **Create Grid Case Surfaces**.

![]({{< relref "" >}}images/3d-main-window/surface_gridcase.png)

A grid case surface has the same properties as a surface imported from file, but instead of choosing which file the data should come from, you choose a source case, a slice direction and a slice index. The slice direction and index will be added to the surface name shown in the project tree.

![]({{< relref "" >}}images/3d-main-window/surfaces_gridcaseproperties.png)


## Exporting Surfaces

ResInsight can export surfaces to the GOCAD TSurf file format. Grid case surfaces can additionally be exported to Petrel Surface PTL format. Use the right-click menu for the surface you want to export and choose the export format you want to use. A file selection window will show up allowing you to choose where you want to save the exported data.

![]({{< relref "" >}}images/3d-main-window/surface_export.png)

## Supported Surface Formats

### GOCAD Surface format

GOCAD is a computer application that allows you to import, create, modify, integrate, view, and export geological objects in 3D.
The GOCAD export file format supported by ResInsight is **TSURF** (*.ts). 
A TSURF data file is a triangle based surface format containing vertex coordinates and triangle to vertex connectivities as exemplified below. 
ResInsight import vertex and triangle identifiers from the first TFACE section in such a file.

```
GOCAD TSurf 1 
HEADER { 
name:MF_027_SU 
} 
GOCAD_ORIGINAL_COORDINATE_SYSTEM 
NAME Default 
AXIS_NAME "X" "Y" "Z" 
AXIS_UNIT "m" "m" "m" 
ZPOSITIVE Depth 
END_ORIGINAL_COORDINATE_SYSTEM 
TFACE 
VRTX 1 458177.767090 7322538.712891 1643.655884 CNXYZ 
VRTX 2 458260.834961 7322392.890625 1596.685303 CNXYZ 
VRTX 3 457985.662109 7322783.783203 1542.060059 CNXYZ 
VRTX 4 459601.453125 7322511.427734 3639.000000 CNXYZ 
VRTX 5 459422.015625 7322689.230469 3639.000000 CNXYZ 
VRTX 6 459793.410156 7322338.230469 3639.000000 CNXYZ 
...
TRGL 2 61 98  
TRGL 20 153 66  
TRGL 152 19 65  
END 
```


### Petrel Surface PTL files

ResInsight is capable of importing a surface defined by a **PTL** (*.ptl) file from Schlumberger Petrel.
A PTL data file specifies the quads of a surface by *x*, *y*, *z* nodal coordinates and the *i* and *j* indices as exemplified below. 
As seen, *#* denotes comment lines.

```
#Type: scattered data
#Version: 6
#Description: No description
#Format: free
#Field: 1 x
#Field: 2 y
#Field: 3 z meters
#Field: 4 column
#Field: 5 row
#Projection: Local Rectangular
#Units: meters
#End: 
#Information from grid
#Grid_size: Not_avaiable
#Grid_space: Not_available
#Z_field: z
#Vertical_faults: Not_available
#History: No history
#Z_units: meters
443479.500000 7305390.500000 -1000.000000 1 1
443479.500000 7305488.500000 -1000.000000 1 2
443479.500000 7305586.500000 -1000.000000 1 3
443479.500000 7305684.500000 -1000.000000 1 4
443479.500000 7305782.500000 -1000.000000 1 5
443479.500000 7305880.500000 -1000.000000 1 6
...
```




### OpenWorks XYZ Surface files

ResInsight is capable of importing a surface defined by a **XYZ** (*.dat) file from OpenWorks.
A XYZ data file specifies the quads of a surface by *x*, *y*, *z* nodal coordinates organized in a regular grid. 
As seen, *#* and *@* denotes comment lines.
```
@File_Version: 4
@Coordinate_Type_is: 1
@Export_Type_is: 1
@Number_of_Projects 1
@Project_Type_Name: , 3,xxx,
@Project_Unit_is: meters , xxx
#File_Version____________-> 4
#Project_Name____________-> xxx
#Project_Type____________-> 3
#Export_XY_Unit__________-> meters
#OpenWorks_Project_______-> 'xxx'
#Master_Project_______->
#Coordinate_type_________-> 1
#Number_of_points_in_hzd_-> 1
#Horizon_internal_id_____-> xxx
#Horizon_extremes_are____-> xxx,xxx
#Horizon_onset_is_Minimum_____-> 1
#Horizon_type_is_DEPTH_STRUCTURE______-> 2
#Horizon_color_is________-> 255 0 0
#Horizon_name____________-> xxx
#Horizon_attribute_______-> DEPTH_STRUCTURE
#Horizon_version_________-> UNKNOWN
#Horizon_interp_status___-> defaultStat
#Horizon_class___________-> defaultClass
#Export_Z_Unit___________-> meters
#Horizon_onset_type______-> Minimum
#Horizon_data_domain_____-> DEPTH
#Horizon_remark_size_____-> 50
Horizon from Grid on Fri Aug 14 13:42:10 CEST 2020
#End_of_Horizon_ASCII_Header_
   4.5423435e+05   7.3239079e+06   1.5970070e+03
   4.5424414e+05   7.3239157e+06   1.5970485e+03
   4.5425392e+05   7.3239234e+06   1.5970899e+03
   4.5426371e+05   7.3239312e+06   1.5971314e+03 
```
