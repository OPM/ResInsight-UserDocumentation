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
in **Project Tree** allowing for change of name, file, and color.

![]({{< relref "" >}}images/3d-main-window/SurfacesPropertyEditor.png)

## Surface Results

Per default, ResInsight maps current **Cell Result** on a given surface. 
If another result is to be displayed, specify the result under **Separate Surface Results** as shown below.

![]({{< relref "" >}}images/3d-main-window/SurfacesSeparateSurfaceResults.png)

Clicking a surface of a **View** in **Project Tree** activates the Property Editor for allowing view settings as shown below. 
Please note the **Depth Offset** capability to offset a surface in z-direction and initiate result mapping to the surface 
at that particular depth.
To change result displayed on the surface, please specify the desired result in the **Separate Result Reference**
section of the Property Editor.

![]({{< relref "" >}}images/3d-main-window/SurfacesViewPropertyEditor.png)


## Supported Surface Import Formats

### GOCAD Surface Import

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


### Petrel Surface Import from PTL files

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




