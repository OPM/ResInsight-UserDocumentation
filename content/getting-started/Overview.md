+++
title = "Overview"

weight = 5
+++

### User Interface 

ResInsight has two main windows, one for 3D related visualizations and one for 2D graphs and plots. 

#### 3D Main Window
![ResInsight User Interface]({{< relref "" >}}images/getting-started/ResInsightUIMediumSize.png)

#### Plot Main Window
![ResInsight User Interface]({{< relref "" >}}images/getting-started/ResInsightMainPlotMediumSize.png)

#### Switching Between the Two Main Windows

The two main windows has a toolbar button each, that directly opens and raises the other window. {{< image-in-text src="images/getting-started/3DWindow24x24.png" >}}{{< image-in-text src="images/getting-started/PlotWindow24x24.png" >}}

Each of the windows can also be closed freely, but if both are closed, ResInsight exits.

#### Docking Windows

Each of the main windows has a central area and several docking windows surrounding it. The different docking 
windows can be managed from the **Windows** menu or directly using the local menu bar of the docking window.

- **Project Tree** -- contains all application objects in a tree structure.
- **Property Editor** -- displays all properties for the selected object in the **Project Tree**
- **Process Monitor** -- displays output from Octave when executing Octave scripts
- **Result Info** -- displays info for the selected object in the 3D scene
- **Result Plot** -- displays curves based on result values for the selected cells in the 3D scene
- **Messages** -- displays occasional info and warnings related to operations executed.

Result Info and Result Plot is described in detail in [ Result Inspection ]({{< relref "resultinspection" >}})

{{% notice note %}}
<b>Use several Project Trees and Property Editors: </b>
If you want to pin the property editor for a certain object, you can add 
a new Project Tree and Property Editor by using the command <b>Windows->New Project and Property View</b>.
{{% /notice %}}

### Toolbars 

A selected subset of actions are presented as controls in the toolbar. The different sections in the toolbar can be dragged and positioned anywhere as small floating toolbars. Management of the toolbar is done by right-clicking on the toolbar and then manipulating the displayed menu.

#### Managing 3D Views and Plot Windows 

In the main area of the application, several 3D views or plot windows can be open at the same time. One of them will be active and the active view can be either maximized to use the whole main area, or restored so that you can see the open windows.

Standard window management for applying minimized, normal and maximized state is available in the upper right corner.

![Restore Down]({{< relref "" >}}images/getting-started/RestoreDown.PNG)

Commands to arrange the windows in the standard ways are available from the **Windows** menu

- **Tile Windows** -- distribute all open view windows to fill available view widget space
  - The order of the tiled windows are determined by the window positions and the type of view at the time of running the tile command. The leftmost window are tiled first, then the next leftmost and so on. Master views are tiled before slave views.
- **Cascade Windows** -- organize all open view windows slightly offset on top of each other
- **Close All Windows** -- close all open view windows

#### Editing 3D Views and Plot Windows Content

Most of the settings and features of ResInsight is accessible through the **Project Tree** and the **Property Editor**. Selecting an item in the **Project Tree** activates the corresponding Window, and shows the item properties in the **Property Editor** available for editing. 

Toggling a checkbox next to an item in the **Project Tree** will toggle visibility in the window. Toggling a checkbox for a collection of items will affect the visibility for all items in the collection {{< image-in-text src="images/getting-started/TreeViewToggle.png" >}}.
Right-click menu commands are also available to do special operations on a selected set of items.

ResInsight stores all views and settings in a [Project File]({{< relref "projectfile" >}}) to easily continue the work in a subsequent session. 

[Model Navigation]({{< relref "modelnavigation" >}}) describes how to interact and manipulate the 3D model. 


### Cases and Their Types

A *Case* in ResInsight means a Grid model with a particular set of results or property data. There are three different types of Eclipse cases and one type of Geomechanical cases.

#### Eclipse Cases
The following Eclipse cases can be imported into ResInsight via the **File->Import->Eclipse Cases** menu, 
see [Import Eclipse Cases]({{< ref "eclipsecases.md" >}}): 

**Result Case {{< image-in-text src="images/getting-started/Case24x24.png" >}}**

This is a Case based on the results of an Eclipse simulation, read from a grid file together with static and restart data. Multiple Cases can be selected and read from a folder.

**Input Case {{< image-in-text src="images/getting-started/EclipseInput24x24.png" >}}**

This Case type is based on a _`*.GRDECL`_ file, or a part of an Eclipse *Input* file. This Case type supports loading single ASCII files defining Eclipse Cell Properties, and also to export modified property sets to ASCII files.
Each of the Eclipse properties are listed as separate entities in the **Project Tree**, and can be renamed and exported.
See [ Grid Import and Property Export ]({{< relref "eclipsecases" >}})

**Statistics Case {{< image-in-text src="images/getting-started/Histogram24x24.png" >}}**

This is a Case type that belongs to a *Grid Case Group* and makes statistical calculations based on the source cases in the Grid Case Group. See [ Grid Case Groups and Statistics ]({{< relref "casegroupsandstatistics" >}}).

**Summary Case {{< image-in-text src="images/getting-started/SummaryCase24x24.png" >}}**

This is the case type listed in the Plot Main Window, and represents an _`*.SMSPEC`_ file. These Cases are available for Summary Plotting. See [ Summary Plots ]({{< relref "summaryplots" >}}).
 
#### Geomechanical cases

There are only one type of geomechanical {{< image-in-text src="images/getting-started/GeoMechCase24x24.png" >}}
 cases, namely the ABAQUS-odb case type. 
When ResInsight is compiled with ABAQUS-odb support, _`*.odb`_ files can be imported by selecting the menu item:
**File->Import->Geo Mechanical Cases-> {{< image-in-text src="images/getting-started/GeoMechCase24x24.png" >}} Import Geo Mechanical Model**.

The geomechanical cases are sorted into its own folder in the project tree named **Geomechanical Models** {{< image-in-text src="images/getting-started/GeoMechCases24x24.png" >}} as opposed to the **Grid Models** folder where the Eclipse cases and **Grid Case Groups** resides.

See [Build Instructions]({{< ref "cmake-configuration.md" >}}) on how to compile ResInsight with odb-support.

#### Grid Case Groups

A **Grid Case Group**  {{< image-in-text src="images/getting-started/GridCaseGroup24x24.png" >}} is a group of Eclipse **Result Cases** with identical grids, but generally different active cells, initial values and results. These cases are called *Source Cases*. The purpose of a Grid Case group is to make it easy to calculate statistics across the source cases both for static and dynamic Eclipse Properties. See [ Grid Case Groups and Statistics ]({{< relref "casegroupsandstatistics" >}}).
