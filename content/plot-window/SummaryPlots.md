+++
title = "Summary Plots"
published = true
weight = 10
+++

![]({{< relref "" >}}images/plot-window/ResInsightMainPlotMediumSize.png)

A Summary Plot is a window displaying a graph in the main area of the **Plot Main Window**. As described below, a Summary Plot can contain Summary Curves, Grid time history curves, and pasted ascii curves.

A new Summary Plot can be created by using the right-click menu of **Summary Plots** in the **Plot Project Tree** and activate 
{{< image-in-text src="images/plot-window/SummaryPlot16x16.png" >}} **Open Summary Plot Editor** or 
{{< image-in-text src="images/plot-window/SummaryPlot16x16.png" >}} **New Summary Plot**. 

{{% notice info %}}
If you have many open plots, it can be useful to collapse all other plots by activating **Collapse Other Plots** from right-click menu of a plot in the <b>Plot Project Tree</b>.
{{% /notice %}}

## Plot Data

ResInsight can create summary plots based on vectors from SUMMARY files ( _`*.SMSPEC`_ ), imported Observed Time History Data, Grid Cell Time history Curve, and pasted ascii curves. 

### SUMMARY Files

When opening an Eclipse case in the 3D view, the associated summary file is opened automatically by default, and made available as a **Summary Case**.
Summary files can also be imported directly using one of the following commands in the **File->Import->Summary Cases** menu:

- **Import Summary Case**: Brings up the standard file selection dialog. Multiple selections are allowed.
- **Import Summary Cases Recursively**: Brings up the recursive file selection dialog. This dialog is described in details [below](#recursive-summary-file-import)
- **Import Summary Case Group**: Brings up the recursive file selection dialog. All files selected are automatically grouped in ResInsight.
- **Import Ensemble**: Similar to the above, but in addition to just create a group, ResInsight performs some extra checking related to ensembles and converts the group to an ensemble. See [ensemble support description]({{< relref "ensembleplotting" >}}).

These commands can also be accessed in the right-click menu for the **Summary Cases** entry in the **Plot Main Window Project Tree** under which the imported cases will also be listed.

During summary file import, ResInsight checks whether the summary file is restarted, i.e. has an origin file. If an origin file is found, the Origin Files dialog is displayed. Origin file support is described [below](#origin-files).

### Summary Case Groups
A selection of cases can be grouped by right-clicking  a selection of summary cases and selecting the command **Group Summary Cases**. Summary cases can also be drag-dropped between summary groups. The groups will be used when listing the cases in the [Summary Plot Editor]({{< relref "summaryploteditor" >}}).

### Observed Data

See [Observed Time History Data]({{< relref "observeddata" >}})

### Grid Cell Time History Curve

Time history curves from a grid cell property can also be added to a Summary Plot. 
See [Result Inspection]({{< relref "resultinspection" >}}#result-plot).

### Pasted Ascii Curves

You can copy an ascii table directly from Excel or any text source and paste it directly into a Summary Plot using the command **Paste Excel Data to Summary Plot**. See [Paste Excel Time History Data]({{< relref "pasteexceltimedata" >}}).

## Summary Plots

Summary plots are created in the **Plot Project Tree** by right-clicking **Summary Plots** and selecting 
{{< image-in-text src="images/plot-window/SummaryPlot16x16.png" >}} **Open Summary Plot Editor** or 
{{< image-in-text src="images/plot-window/SummaryPlot16x16.png" >}} **New Summary Plot**. 
Having created a Summary Plot, its entry is listed in the Plot Project Tree. 
The settings of the Plot are controlled by its sub items in the **Plot Project Tree** and the **Property Editor** as described below.

![]({{< relref "" >}}images/plot-window/SummaryPlotTree.png)


### Property Editor

The Property Editor allows **Text-Based Curve Creation** based on selected sources and setting **General Plot Options**.

![]({{< relref "" >}}images/plot-window/SummaryPlotPropertyEditor.png)

**Text-Based Curve Creation** allows specification of a list of vectors for plotting based on selected sources.
The vectors to plot are specified by the following syntax:
`<vectorshortname>[:<item>[:<subitem>[:i,j,k]]]`.
The specification of vectors allows use of wildcards and multiple entries separated by space: 

- `WOPT:*`: One total oil production curve for each well.
- `FOPT FWPT`: Two curves with oil and water total production.
- `BPR:15,28,*`: Oil phase pressure for all blocks along k as separate curves.

**General Plot Options** allows the following settings:

- **Show Title** -- Toggles whether to show the axis title 
- **Auto Title** -- If enabled, the Plot title is derived automatically
- **Name** -- Allows manual setting of plot title if **Auto Title** is disabled
- **Show Legends** -- Toggles whether to legends
- **Legend Font Size** -- Font size to be used in plot
- **Normalize all curves** -- Scales all curves into the range 0.0-1.0

### Time Axis Properties

![]({{< relref "" >}}images/plot-window/SummaryTimeAxisProperties.png)

- **Axis Title**
  - **Show Title** -- Toggles whether to show the axis title
  - **Title** -- A user defined name for the axis 
  - **Title Position** --  Either *Center* or *At End* 
  - **Font Size** -- The font size used for the axis title
- **Time Values**
  - **Time Mode** -- Option to show the time from *Simulation Start*, or as real date-times. 
  - **Max**/**Min** -- The range of visible date/time in the Plot.
  - **Automatic Date/Time labels** -- Option to invoke automatic date/time labels.
  - **Font Size** -- The font size used for the date/time axis ticks, c.f. [Preferences]({{< relref "preferences.md" >}}) for default.
- **Date/Time Label Format**
  - **Date Label Format** -- Date format for the time axis, c.f. [Preferences]({{< relref "preferences.md" >}}) for default.
  - **Time Label Format** -- Time format for the time axis, c.f. [Preferences]({{< relref "preferences.md" >}}) for default.

### Y-axis Properties

![]({{< relref "" >}}images/plot-window/summary_plot_yaxis_properties.png)

- **Title Text**
  - **Auto Title** -- If enabled, the y-axis title is derived automatically with the following options:
     - **Names** -- Add quantity long name to y-axis title.
     - **Acronyms** -- Add quantity acronym to y-axis title.
	 - **Units** - Add unit of quantity to y-axis title.
  - **Title** -- If **Auto Title** is disabled, the **Title** field emerges to facilitate manual setting of plot title.
- **Title Layout**
  - **Title Position** -- Controls the position of the title; *Center* or *At End*.
  - **Font Size** --  Defines the font size used for the axis title. 
- **Axis Values**
  - **Logarithmic Scale**  - Draw plot curves using a logarithmic scale. 
  - **Invert Axis**  - Invert the axis, e.g. when depth is represented by the Y-axis.
  - **Number Format** -- Defines how the legend numbers are formatted.
     - **Auto** -- Legend numbers are displayed by either scientific or decimal notation depending on actual value.
     - **Decimal** -- Legend numbers are displayed using decimal notation.
     - **Scientific** -- Legend numbers are displayed using scientific notation (e.g. 1.2e+6).
  - **Number of Decimals** -- Controls the number of digits after "." for  **Decimal** and **Scientific**.
  - **Scale Factor** -- Displays the y-axis values by multiplying with a specific scale factor for **Decimal** and **Scientific**.
  - **Max and Min** -- Defines the visible y-range.
  - **Font Size** -- The font size for showing values at the axis ticks.   

### Plot Mouse Interaction

- **Value Tracking** -- When the mouse cursor is close to a curve, the closest curve sample is highlighted and the curve sample value at this location is displayed in a tooltip. 
- **Selection** -- Left mouse button click can be used to select several of the parts in the plot, and display them in the Property Editor:
  - The closest curve.
  - Each of the Plot Axes.
  - The Plot itself if none of the above is hit and the Plot window is activated by the mouse click.
- **Window Zoom** -- Window zoom is available by dragging the mouse when the left mouse button is pressed. Use {{< image-in-text src="images/plot-window/ZoomAll16x16.png" >}} **Zoom All** to restore default zoom level.
- **Wheel Zoom** -- The mouse wheel will zoom the plot in and out towards the current mouse cursor position.

### Curve Highlight

![]({{< relref "" >}}images/plot-window/SummaryCurveHighlight.png)

Summary curves will be highlighted when left-clicked in a plot. This allows for detailed investigation on curve values when many curves are plotted. All other curves can be hidden by activating the right-click menu of a plot, and select **On - Others Off**

### Accessing the Plot Data

Right-clicking a plot and selecting **Show Plot Data** will open a window containing the plot data as text columns. 
This dialog supports plot data displayed by day, week, month, quarter, half year and year.

The text content of this window is easy to copy and paste into Excel or other tools for further processing.
It is also possible to save the text data to a file directly by using the right-click command **Export Plot Data to Text File**. 

## Editing properties of single Summary Curve

Selecting a specific Summary Curve is possible via the **Plot Project Tree**.

![]({{< relref "" >}}images/plot-window/SummaryCurveSelection.png)

Having selected a Summary Curve, its properties are shown by the **Property Editor**.

![]({{< relref "" >}}images/plot-window/summary_curve_properties.png)

As seen, the Property Editor organizes the available options into the following groups:

- **Summary Vector** -- Options to select case, vector to plot, axis specification, and error bars.
- **Appearance** -- Options to control curve color, symbols, line style etc.
- **Curve Name** -- Controls how the curve is labeled in the legend.
- **Advanced** -- Specification of additional options.

### Summary Vector

This group of options is used to define summary vector data that the curve will display. 

- **Case** -- Selects the imported Summary or Observed Data case to use as source.
- **Vector** -- Displays the acronym of the selected vector.
- **Axis** -- Controls whether the curve is to be associated with the left or right Y-Axis. 

Selection of vector is performed using a vector acronym or pressing the button to the right. 
Pressing the button opens a dialog similar to the [Summary Plot Editor]({{< relref "summaryploteditor" >}}).

{{% notice note %}}
Switching the Y-Axis for several curves in one go can be done using the right-click command <b>Switch Plot Axis</b>.  
{{% /notice %}}



### Curve Name 

The user can control the curve name used in the plot legend by the following options:

- **Contribute To Legend** -- This option controls whether the curve will be visible in the plot legend. A curve with an empty name will be removed from legend. 
- **Auto Name** -- If enabled, ResInsight will create a name for the curve automatically based on the settings in this option group.
- **Curve Name** -- If **Auto Name** is off, you can enter a curve name here. If empty, the curve will be removed from the legend, but still visible in the plot.
- **Case Name, Vector name ...** etc. -- These options controls what part of the summary vector information to use in the curve auto-name.

## Copy and Paste 

Copy and Paste of selections of Summary Plots and Curves, is possible using the Project Tree right-click menu and standard keyboard shortcuts (CTRL-C/CTRL-V).

## Recursive summary file import
When using the standard file selection dialog, the user is limited to select files in one directory only. If the interesting files are distributed over multiple directories, the dialog has to be opened once for each directory. The recursive file selection dialog is created to circumvent this limitation. This dialog is able to search a directory tree for files matching a specified pattern.

![]({{< relref "" >}}images/plot-window/RecursiveImportDialog2.png)

The dialog consists of the following fields:

- **Path Pattern**: The path filter uses normal wildcard file globbing, like in any unix shell. When the filter ends with a single "**" (eg. "/home/*"), however, ResInsight will search recursively in all subdirectories from that point. This is indicated by "..." in the **Effective Filter** label below.
  - **\*** Matches any number of any characters except the path separator
  - **?** Matches one character exception the directory separator
  - **[abc]** Matches one of the specified characters. Ex. a, b or c
- **File Pattern**: The search pattern that applies to the file name.
- **Effective Filter**: The effective filter displays the resulting full path search pattern. It is updated on the fly as the user edits the pattern fields. A text string of "..." indicates a complete recursive directory search.

After pressing the **Find** button, a file search is performed in the root directory and the directories below matching the path pattern. The files found are presented in a list, where the user can check/uncheck each file individually.

When the **OK** button is pressed, all checked files are imported.

### Origin Files
![]({{< relref "" >}}images/plot-window/OriginFileDialog.png)

During summary file import, ResInsight checks whether the summary file is restarted, i.e. has an origin file. If an origin file is found, the Origin Files dialog is displayed.

Depending on what triggered the summary file import, the dialog shows slightly different information. If the summary file import was triggered by a grid file import, the dialog displays information about grid files in addition to the summary origin file(s). If the summary file was imported directly, information about grid files are not relevant and thus not displayed.

The dialog contents are organized in groups:

- **Current Grid and Summary Files** or **Current Summary Files**: This group displays the name of the main summary file to import. If the import is triggered by a grid file import, the name of the grid file is also displayed.
- **Origin Summary Files**: This group displays the names of the origin summary file(s) found. If there are more than one file listed, it means that the found origin file also has an origin file. ResInsight will search the "chain" of summary origin files until it reaches the end.
  - **Import Options** There are three options to control how origin summary file are imported
    - **Unified**: The main summary files and all origin files are imported into one single summary case
    - **Separate Cases**: The main files and all origin files are imported into separate summary cases
    - **Skip**: Only the main summary file is imported. The origin summary files are skipped.
- **Origin Grid Files**: If the summary file import was triggered by a grid file import, this group is visible. It contains a list of the grid files associated to the origin summary files
  - **Import Options** There are two options to control how the grid files are imported
    - **Separate Cases**: All "origin" grid files are imported into separate grid cases
    - **Skip**: Only the main grid file is imported. The "origin" grid files are skipped.

By default the file names are displayed using relative path based on the common root folder for all files. In order to display the full path, check the **Show full paths** checkbox. Regardless of the checkbox state, there is always a tooltip showing the full path for every file. It is also possible to copy a full path file name to the clipboard. Right click on the file name and select **Copy file name**.

If the user selected multiple summary files or grid files, this dialog will be displayed for every file that has an origin summary file. In this case the button **OK to All** appears. When this button is clicked, the rest of the files will be imported silently using the same options.
