+++
title = "Surfaces"

weight = 85
+++

![](/images/3d-main-window/SurfacesOverview.png)

ResInsight is capable of mapping properties and simulation results onto 3D surfaces imported from GOCAD and Petrel as specified below. 


## Import and appearance of surfaces

3D surfaces from GOCAD and Petrel are imported into ResInsight by the menu option **File**->**Import**->**Import Surfaces** 
in the **3D Main Window**.

Surface file formats are described in [Surface Data]({{% relref "reference-manual/surfaces" %}})

![](/images/3d-main-window/SurfacesImport.png)

Imported surfaces are listed under the {{< image-in-text src="images/3d-main-window/SurfacesProjectTreeNode.png" >}} entry 
in the **Project Tree**. You can click on a surface to change i.e. the name or color of the surface, or change the file to read the surface data from. 

![](/images/3d-main-window/SurfacesPropertyEditor.png)

You can also change the depth of the surface by adding a depth offset (positive or negative). This could be used i.e. to import the same surface file multiple times and assign each instance of the surface a separate depth offset. When a depth offset is set, the offset value will be shown as part of the surface name in the project tree.

![](/images/3d-main-window/surface_multiple.png)

{{% notice note %}}
Multiple surfaces can be imported at the same time by choosing more than one input file in the file selection window that shows up when you start an import.
{{% /notice %}}


## Using folders

To make it easier to organize the surfaces you import into your project, ResInsight supports creating surface folders in the project tree. To create a new folder, right-click on the top level **Surfaces** folder in the project tree and choose **Add Folder**.

![](/images/3d-main-window/surface_addfolder.png)


## Surface Results

Per default, ResInsight maps current **Cell Result** on a given surface. 
If another result is to be displayed, specify the result under **Surface Results** as shown below.

![](/images/3d-main-window/SurfacesSeparateSurfaceResults.png)

Clicking a surface of a **View** in the **Project Tree** activates the Property Editor for allowing view settings as shown below. 

To change result displayed on the surface, please specify the desired result in the **Result Reference**
section of the **Property Editor**.

![](/images/3d-main-window/SurfacesViewPropertyEditor.png)


## Reloading Surfaces

If you have modified a surface file using an external program, you can easily load the changes into ResInsight by using the reload surface feature. Bring up the right-click menu for the surface you want to reload and choose  **Reload**. The views will automatically update with the new data (could take a few seconds).

![](/images/3d-main-window/surface_reload.png)

## Create a copy

You can easily create a copy of an existing surface by choosing  **Create Copy** in the surface right-click menu. A new, identical surface will show up at the same level in the project tree. You can now give it a new name, change depth offset etc.

![](/images/3d-main-window/surface_copy.png)

## Grid Case Surfaces

In addition to importing surfaces from file, ResInsight can also generate grid case surfaces. You do that by bringing up the right-click menu for the {{< image-in-text src="images/3d-main-window/SurfacesProjectTreeNode.png" >}} project tree entry and choose **Create Grid Case Surfaces**.

![](/images/3d-main-window/surface_gridcase.png)

A grid case surface has the same properties as a surface imported from file, but instead of choosing which file the data should come from, you choose a source case, a slice direction and a slice index. The slice direction and index will be added to the surface name shown in the project tree.

![](/images/3d-main-window/surfaces_gridcaseproperties.png)

## Depth Surfaces

A flat surface at a specified depth can be created from the right-click menu and select **Create Depth Surface**. A transparent surface is created, and color and transparency can be adjusted.


## Exporting Surfaces

ResInsight can export surfaces to the GOCAD TSurf file format. Grid case surfaces can additionally be exported to Petrel Surface PTL format. Use the right-click menu for the surface you want to export and choose the export format you want to use. A file selection window will show up allowing you to choose where you want to save the exported data.

![](/images/3d-main-window/surface_export.png)

