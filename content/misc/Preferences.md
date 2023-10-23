+++
title = "Preferences"
published = true
weight = 10
+++

In this section the different settings that controls the default behavior of ResInsight is described. These settings can be controlled using the **Preferences** dialog available from the **Edit -> Preferences** menu.
Preferences are not stored in project files, but in a platform specific way for each user.
Essential preferences are listed below.

## General

![]({{< relref "" >}}images/misc/PreferencesGeneral.png)

When changing the preferences, any default color, font or Z-scale Factor that has not been changed by the user in the various views, will be applied immediately. If the user has changed font sizes in specific plots or annotations from the default value, ResInsight will ask if the user wants the new defaults applied to all existing views and plots even where custom settings have been set.

- **Default Colors**: This group contains the colors that will be applied to the 3D views:
	- **Viewer Background** 
	- **Mesh Color** 
	- **Mesh Color Along Faults**
	- **Well Label Color**

- **Default Font Sizes**: This group contains fonts preferences when using ResInsight:
	- **Viewer Font Size** -- The fonts used for axes labels, legends and info boxes in the 3d View.
	- **Annotation Font Size** -- The font used as default for Text Annotations.
	- **Well Label Font Size** -- The font used for all Well Path labels.
	- **Plot Font Size** - The font used for plot legends, axes, and labels.

- **3D Views**: This group of options controls visual settings to be used when creating new views:
	- **Show Grid Lines** -- Controls whether to show the grid lines by default for all cells or just along faults.
	- **Navigation mode** -- Defines the use of mouse for interaction with 3D model, c.f.  [Model Navigation]({{< relref "modelnavigation" >}}).
	- **Default Z Scale Factor** -- Default depth scale for grid models.
	- **Show Box around Legends** -- Create a semi-transparent box containing each legend in the 3D Views.
	- **Enable Faults by Default** -- Controls default visibility of faults in views
	- **Show Info Box in New Projects** -- Controls default visibility Info Box in upper right corner
	- **Show Grid Box in New Projects** -- Controls default visibility of grid box

- **Other**: 
	- **SSIHUB Address** -- Optional URL to Equinor internal web service used to import well paths
	- **Enable Undo/Redo for Property Editor Changes** -- enable undo/redo functionality

## Grid

![]({{< relref "" >}}images/misc/PreferencesEclipseGrid.png)

- **Compute DEPTH Related Properties** -- If not present, compute DEPTH, DX, DY, DZ, TOP, BOTTOM when loading new cases.
- **Load and Show SOIL** -- Control if SOIL is loaded and applied to grid per default.
- **Import Faults/NNCs/Advanced MSW Data** -- Disable options to reduce case import time.
- **Include File Absolute Path Prefix** -- Prefix used on Windows if include files use absolute UNIX paths.
- **Use Result Index File** -- If enabled ResInsight will try to save a result index file when opening a new case (stored in the same directory as the _`*.EGRID`_ file with filename _`<casename>.RESINSIGHT_IDX`_) If existing, ResInsight will use the index file when loading the case resulting in a significant speedup.
- **Skip Import of Simulation Well Data** -- Disable import of simulation well data for reducing case import time.

## Summary

![]({{< relref "" >}}images/misc/PreferencesEclipseSummary.png)

- **Origin Files**: c.f. [Origin Files]({{< relref "eclipsesummarydata#origin-files" >}}) for details.
- **Summary Data Import** including file format for summary data import, c.f. [Ensemble Summary]({{< relref "eclipsesummarydata#summary-data-file-formats" >}}):
  - **h5 (HDF5)** Import data from h5 files
  - **UNSMRY (libecl)** Import data from native UNSMRY files
  - **ESMRY (opm-common)** Import data from ESMRY files


## Plotting

![]({{< relref "" >}}images/misc/PreferencesPlotting.png)

- **Summary Plots**: 
  - **Create Plot On Summary Data Import**: governs automatic creation of summary plots when importing a summary case
     - *No Plots*: do not automatically create summary plots
     - *Use Data Vector Names*: Create summary plots automatically based on given vector names, e.g. `FOPT WOPT*`
     - *Use Plot Templates*: Create summary plots automatically based on default templates. 
  - **Cross Plot Addresses**: List of vector pairs defining cross plot curves separated by semicolon. If a well or group is selected, the corresponding well or group address is displayed and used.
  - **Default Curve Style for History Vectors**: allows specifying *symbols* and/or *lines* as preference.
  - **Append History Vectors**: automatically include the corresponding history vector when appending a simulated summary vector.
  - **Curve Color By Phase**: distinguish each phase by separate color.
  
- **Multi Plot Defaults**: specification of number of rows and columns for each page containing multiple summary plots.
- **Plot Templates**: specification of folders and folder search depth for templates.
  - Press **Append** to browse for folder to append. 
  - Specify **Maximum Plot Template Folder Search Depth** to restrict the depth of subdirectories to be searched for templates.
- **General**
  - **Date** and **Time** format preferences.
  - **Page Setup**: Physical page size, orientation, and margins. 

 {{% notice note %}}
Please consider the location and folders of your templates with care to cater for structured usage but also to limit the folder search depth for performance reasons.
{{% /notice %}}

  
  

## Scripting

![]({{< relref "" >}}images/misc/PreferencesScripting.png)

- **Octave** c.f. [Octave Interface]({{< relref "octaveinterface.md" >}}) for details:
  - **Octave Executable Location** -- Define binary file location for Octave, usually without path on Linux and including path on Windows.
  - **Show text header when executing scripts** -- Enables the default output from octave when started.

- **Python** c.f.  [ResInsight Python API](https://api.resinsight.org) for details:
  - **Enable Python Script Server**
  - **Show Python Debug Info**
  - **Default Python Script Server Port**
  - **Python Executable Location** 

- **Script Files**:
  - **Shared Script Folder(s)** -- Defines the search paths for octave scripts
  - **Script Editor** -- The text editor to invoke when editing scripts

