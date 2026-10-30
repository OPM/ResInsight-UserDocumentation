+++
title = " Zonations/Formations"

weight = 95
+++

![](/images/3d-main-window/formations_legend.PNG)

This section will describe how to use formations for different k-layers of a case, and how to use well picks/zonations for ranges of measured depths of a well path.

## Formations for k-layers

Formation information can be utilized in ResInsight as cell colors, used in property filters and are displayed in the **Result info** panel when selecting single cells.

To use this functionality you will need to :

1. Import one or more Formation Names file(s)
2. Select the correct Formation Names file in the Case of interest

### Import of Formation Files

Formation files are imported by using the command: **File->Import->Import Formations**. Supported files are _`*.lyr`_, FMU zone ranges (_`zonation_ecl_map.yml`_) and FMU layer zone tables (_`layer_zone_table.txt`_). For grid case ensembles, the formations are imported automatically for each realization.

See [Formations and Well Picks]({{% relref "FormationImport" %}}) for file formats, zone colors and the priority used when several formation files are present.

### Select the Formation File in a Case

If only one formation file is imported, the formation will automatically be set in the active view's case. If more than one formation file is imported at once, or if a case must change formation file, the formation file for a case can be set later on. This option is available in the **Property Editor** for a case. The formation is selected in the combo box for property **Formation Names File**.

![](/images/3d-main-window/formations_property_editor.PNG)

### Viewing the Formation Information

#### Formations in 3D View
The formations can be visualized as a result property in **Cell Results**, **Cell Edge Result**, and **Separate Fault Result**. When selected, a special legend displaying formation names is activated.

#### Property Filter Based on Formations
Formation names are available in Property Filters as Result Type **Formation Names**. This makes it easy to filter geometry based on formation specifications.

See [ Cell Filters ]({{% relref "filters" %}}) for details.

#### Picking in 3D View
Picking on a cell being part of a formation will display the formation name in the **Result Info** windows, in addition to other pick info for the cell.

#### Annotations on Plots
Formation can be used to annotate the following plot types:

- [Well Log Plots]({{% relref "welllogsandplots" %}})
- [RFT Plots]({{% relref "rftplot" %}})
- [PLT Plots]({{% relref "pltplot" %}})

For RFT and PLT Plots, **Zonation/Formation Names** can be found in the plot's **Property Editor**. Tick "Show Formations" and choose the case with the desired formations. 

In Well Log Plots and Well Allocation Plots, **Zonation/Formation Names** can be found in the **Property Editor** for a **Track** or **Branch**. In addition to choosing case, the path to show formations for must also be selected, as each track can have curves with data from more than one path.

![](/images/3d-main-window/caseFormationsPropEditor.PNG)

## Well Picks

Well Picks can be set for a single well path, defined on measured depths of the well path. Unlike formations for k-layers, formations for a well path can only be used to annotate plots. A well pick can be either a *fluid* or a *formation*.

### Import of Well Pick Files

Well Pick files are imported by using the command: **File->Import->Well Data->Import Well Picks**. Depth-based FMU well formation files (_`formations.csv`_) are imported from **Well Picks (Formations)** in the **Plot Project Tree**.

See [Formations and Well Picks]({{% relref "FormationImport" %}}#well-picks) for file formats.

### Viewing the Well Picks
See [Annotations on plots](#annotations-on-plots). Annotations are added to plots in the same way as for k-layered formations, but the source is different.

![](/images/3d-main-window/wellFormationsPropEditor.PNG)

In the **Property Editor**, choose **Well Path** as **Source**, and all well paths with formations will be shown in the drop-down list below. All disjoint well picks for the chosen well path is shown on default. To reduce the number of annotations, the **Well Pick Filter** can be used.

![](/images/3d-main-window/wellPickFilter.png)

The **Well Pick Filter** will show formations down to the specified level. If more there are more than one formation within 0.1m of an MD, only the lowermost formation is shown. Well picks interpreted as *Fluids* are only shown by ticking the **Show Fluids** mark.
