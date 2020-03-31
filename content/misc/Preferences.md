+++
title = "Preferences"
published = true
weight = 10
+++

In this section the different settings that controls the default behavior of ResInsight is described. These settings can be controlled using the **Preference** dialog available from the **Edit -> Preferences** menu.

![]({{< relref "" >}}images/3d-main-window/Preferences.png)

When changing the preferences, any default color, font or Z-scale Factor that has not been changed by the user in the various views, will be applied immediately. If the user has changed font sizes in specific plots or annotations from the default value, ResInsight will ask if the user wants the new defaults applied to all existing views and plots even where custom settings have been set.

![]({{< relref "" >}}images/3d-main-window/Preferences_ApplyToAll.png)

The preferences are not stored in the project files, but rather in a platform specific way for each user.

## General - tab

### Default Colors

This group contains the colors that will be applied to the 3D views.

- **Viewer Background** 
- **Mesh Color** 
- **Mesh Color Along Faults**
- **Well Label Color**

### Default Font Sizes

This group contains the different fonts which are used through ResInsight.

- **Viewer Font Size** -- The fonts used for axes labels, legends and info boxes in the 3d View.
- **Annotation Font Size** -- The font used as default for Text Annotations.
- **Well Label Font Size** -- The font used for all Well Path labels.
- **Plot Font Size** - The font used for legends, axes labels, values in Plots. This affects the docked plots in the main 3D window as well (Result Plot, Relative Permeability etc), although because of the reduces space available in these plots, the font size applied will be one less than the **Plot Font Size**.

### 3D Views

This group of options controls visual settings that will be used when creating new views.

- **Show Grid Lines** -- Controls whether to show the grid lines by default for all cells or just along faults.
- **Navigation mode** -- Defines how to use the mouse to interact with with the 3D model. Please refer to [Model Navigation]({{< relref "modelnavigation" >}}) for details.
- **Default Z Scale Factor** -- Default depth scale for grid models.
- **Show Box around Legends** -- Create a semi-transparent box containing each legend in the 3D Views.
- **Use shaders** -- This option controls the use of OpenGL shaders. Should be left **On**. Available only for testing purposes.
- **Show 3D Information** -- Displays graphical resource usage as text in the 3D view.

### Other
- **Date Format** -- Defines the date format to be used in time legend plotting
- **Time Format** -- Defines the time format to be used in time legend plotting
- **SSIHUB Address** -- Optional URL to Equinor internal web service used to import well paths
- **Show LAS Curve Without TVD Warning** - Turn off the warning displayed when showing LAS curves in TVD mode

## Eclipse - tab

![]({{< relref "" >}}images/3d-main-window/EclipsePreferences.png)

### Behavior When Loading Data

- **Compute DEPTH Related Properties** -- If not present, compute DEPTH, DX, DY, DZ, TOP, BOTTOM when loading new cases.
- **Load and Show SOIL** -- Control if SOIL is loaded and applied to grid.
- **Import Faults/NNCs/Advanced MSW Data** -- Disable import of data for a case to reduce case import time.
- **Include File Absolute Path Prefix** -- Prefix used on Windows if include files use absolute UNIX paths.
- **Use Result Index File** -- If enabled ResInsight will try to save a result index file when opening a new case. The file is stored in the same directory as the _`*.EGRID`_ file with filename _`<casename>.RESINSIGHT_IDX`_ If it exists, ResInsight will use this when loading the case, resulting in a significant speedup.
- **Skip Import of Simulation Well Data** -- Disable import of simulation well data for a case to reduce case import time (opposite toggling than the other import commands).

### Origin Files
Please refer to [Summary Origin]({{< relref "summaryplots.md#origin-files" >}}) for details related to handling of **Origin Files**.


## Plotting - tab

![]({{< relref "" >}}images/misc/PreferencesPlotting.png)

- **Default Summary Curves**: Defines default curves for import when creating a new summary plot, e.g. `FOPT WOPT*`
- **Default Curve Style for History Vectors**: allows specifying *symbols* and/or *lines* as preference.
- **Date** and **Time** format preferences.
- **Show resample time text** preference
- **Use multiple threads** preference which may improve performance when loading summary data
- **Plot Templates** allows setting preferences for:
  - *Plot Template Folder(s)*: Allows to enter and delete folder(s) that are searched for plot templates. Press *Append* to browse for folder to append. 
  - Checking *Search Plot Templates Recursively* instructs ResInsight to search subdirectories of specified folder(s) for templates.


## Scripting - tab

![]({{< relref "" >}}images/3d-main-window/Preferences_Scripting.png)

### Octave

- **Octave Executable Location** -- Defines the binary file location for Octave. Usually without path on Linux, and including path on Windows.
- **Show text header when executing scripts** -- Enables the default output that octave outputs when started.

Please refer to [Octave Interface]({{< relref "octaveinterface.md" >}}) for more details.

### Python

- **Enable Python Script Server**
- **Default Python Script Server Port**
- **Python Executable Location** 

Please refer to the [ResInsight Python API](https://api.resinsight.org) for more details.

### Script Files

- **Shared Script Folder(s)** -- Defines the search paths for octave scripts
- **Script Editor** -- The text editor to invoke when editing scripts


## Export - tab

![]({{< relref "" >}}images/3d-main-window/Preferences_Export.png)

- **CSV Text Export Field Separator**
