+++
title = "Well Paths"

weight = 20
+++

![](/images/3d-main-window/ResInsight_WellPathWithSimulationWell.png)

ResInsight can import well paths from simple Ascii files. 
In addition, ResInsight is able to retrieve well paths from an Equinor internal web service.

ResInsight also supports creation of your own user-defined well paths. See [Create Well Paths]({{< relref "createnewwellpaths" >}})

## Ascii Well Paths

The command **File -> Import -> Well Data -> Import Well Paths From File** will read the well paths in the selected file, and create one entry for each well path under the {{< image-in-text src="images/3d-main-window/WellCollection.png" >}} **Wells** item in the **Project Tree**. 
    
## Importing well paths from OSDU

Well path trajectories can be downloaded from an OSDU cloud service. When storing the project file, the reference to the OSDU trajectory is stored. This will ensure that authentication and access is checked before the trajectory is downloaded.

Download of OSDU trajectories will not work if the project is used on a server, as the user is required to authenticate before download of data.

The command **File -> Import -> Well Data -> Import Well Paths From OSDU** launches a wizard to guide you through the process of selecting the well paths you need.
Having completed the wizard, the imported wells are accessible as Items under the {{< image-in-text src="images/3d-main-window/WellCollection.png" >}} **Wells** item in the **Project Tree**.

[OSDU Cloud Service]({{< relref "cloudservices" >}})

{{% notice info %}}
<strong>Access to Cloud Data </strong>
Make sure you have access to "OSDU - Base acces" and "Linux Exclusion Conditional Access".
{{% /notice %}}

## Well Path Visualization

All the imported well paths are available below the {{< image-in-text src="images/3d-main-window/WellCollection.png" >}} **Wells** item in the **Project Tree**. 

![](/images/3d-main-window/WellsInTree.png)

The visible wells are always shown in all the 3D Views in the complete project, so the toggles and settings control the overall project visibility of the Well Paths. The **Property Editor** of the **Wells** item is shown below 

![](/images/3d-main-window/WellPathCollectionProperties.png)

- **Global well path visibility** -- This option forces the well paths on or off, ignoring the individual settings unless it is set to Individual.
- **Clip Well Paths** -- This option hides the top of the Well Paths to avoid displaying the very long lines from the reservoir to the sea surface.
- **Well Path clipping depth distance** -- This number is the distance from the top of the reservoir to the clipping depth.

## Individual Well Path
A well path will hold well log data and well path data imported from files. A well path file is placed inside the well path item, while one or more well log files are placed as child items under the well path in the project tree.

### Importing Well Log Files
Well log data is [imported from LAS-files]({{< relref "lasfile" >}}#importing-a-las-file).

### Well Path Property Editor
The well path property editor lets the user control the appearance of the well path and associate the well path to a simulation well. It also gives some information about the well path metadata.

![](/images/3d-main-window/WellPathPropertyEditor.png)

- **Appearance group** -- Settings in this group affect the well path appearance in the 3D view
- **File group** -- Information about the well path file
- **Simulation Well group** -- Associated simulation well. ResInsight will try to associate each well path with a simulation well. This is done in the exact same way as looking up an existing well path. If the auto-association fails, the user can set the correct simulation well here.
- **Well Info group** -- Metadata for the well path
- **Well Picks group** -- Information about imported [well picks]({{< relref "formations" >}}#well-picks) file containing data for the current well path

### Casing Design
Some Casing Design elements can be assigned to the well path by selecting **Create Casign Design** from the right-click menu of the well path.

This will create a new child object for the Well Path, named **Casing Design**. In the **Casign Design** Property editor 
well path containment properties such as Casing (with Casing Shoe) and Liner can be added to the well path along with a start and end depth and a diameter. 

![](/images/3d-main-window/CasignDesign.png)

These can be visualised in the 3D View and Well Log Plots on a [Well Log Track]({{< relref "welllogsandplots" >}}#tracks).

![](/images/3d-main-window/CasignDesign3D.png) 

![](/images/3d-main-window/CasignDesignPlot.png)


## Ascii Well Paths File Format
The supported ASCII format is quite flexible but the main requirements are: 

- Each data line must contain four numbers: X Y TVD(MSL) MD(RKB) separated with white-space.
- Lines starting with `"--" or "#"` is considered to be comment lines
- A line starting with none-number-characters are used as a well name after the following rules:
  - If the line contains a pair of : ```  "'", "`", "´", "’" or "‘" ``` the text between the quotation marks is used as a well name.
  - If the line contains the case insensitive string "name" with an optional ":" after then the rest of the line is used as a well name. 
  - If there are no quotes or "name"'s, the complete line is used as a well name.
  - If there are several consecutive name-like lines, only the last one will be used 
- If a well name is found, a new well is created and the following data points are added to it.

#### Example 1:
```txt
WELLNAME: WELL1
6507.1	725	2542	2590
6523.5	757	2549	2626.6
6523.5	760	2559	2637.1
-999
WELLNAME: WELL2
550.7 1020.2  2410   2410
551   1004.1  2422.2 2430.2
555.2  993.9  2425   2441.6
-999
```

#### Example 2:
```txt
X Y TVD(MSL) MD(RKB)
Name Well_1
6507.1	725	2542	2542
6523.5	757	2549	2578.6
6523.5	760	2559	2589.1

-- A Comment new well
This is not its name
Name Well_2
550.7	1020.2	2410	2520
551	1004.1	2422.2	2540.2
# a comment inside the data 
555.2	993.9	2425	2551.6

3Q AHB-J
5507.0	4638.5	0.0	0.0
5507	4638.5	1628.6	1628.6
```
