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

See [Formations in Well Log Plots]({{% relref "WellLogFormations" %}}) for the formation settings. RFT, PLT and Well Allocation Plots use the same settings.

## Well Picks

Well Picks can be set for a single well path, defined on measured depths of the well path. Unlike formations for k-layers, formations for a well path can only be used to annotate plots. A well pick can be either a *fluid* or a *formation*.

### Import of Well Pick Files

Well Pick files are imported by using the command: **File->Import->Well Data->Import Well Picks**. Depth-based FMU well formation files (_`formations.csv`_) are imported from **Well Picks (Formations)** in the **Plot Project Tree**.

See [Formations and Well Picks]({{% relref "FormationImport" %}}#well-picks) for file formats.

### Viewing the Well Picks
See [Well Picks]({{% relref "WellLogFormations" %}}#well-picks) in Formations in Well Log Plots.
