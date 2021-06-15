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

See [Eclipse Summary Data]({{< relref "eclipsesummarydata" >}}) for description on how to import data.

The input commands can also be accessed in the right-click menu for the **Summary Cases** entry in the **Plot Project Tree**.
Notably, the right-click menu also allows creating a [delta ensemble]({{< relref "ensembleplotting" >}}#delta-ensemble) 
and [delta summary case]({{< relref "summaryplots" >}}#delta-summary-case).

During summary file import, ResInsight checks whether the summary file is restarted, i.e. has an origin file. If an origin file is found, the [Origin Files]({{< relref "eclipsesummarydata" >}}#origin-files) dialog is displayed.


### Summary Case Groups
A selection of cases can be grouped by right-clicking  a selection of summary cases and selecting the command **Group Summary Cases**. Summary cases can also be drag-dropped between summary groups. The groups will be used when listing the cases in the [Summary Plot Editor]({{< relref "summaryploteditor" >}}).


### Delta Summary Case
A **Delta Summary Case** can be created as either the sum or difference between two existing summary cases. 
To create a delta summary case, select two existing summary cases in **Plot Project tree**, then right click and select **New Delta Summary Case**. 
A new delta ensemble is created with the two selected summary cases as input and a default arithmetic operator. 
An existing delta summary case may be input to a new delta summary case.

The Property Editor for the new delta summary case allows to modify display name, the two base summary cases, and the arithmetic operator.
In addition, it is possible to specify a specific time step to be used in delta computation.
As an example according to the settings in the figure below, the delta computation between two cases for a given parameter, e.g. *WBHP*, will be:
$$WBHP\_{delta}(t) = WBHP\_{case1}(@02.01.2000) - WBHP\_{case2}(t)$$

![]({{< relref "" >}}images/plot-window/DeltaSummaryCasePropertyEditor.png)


### Replace Summary Case
A summary case can be replaced by right-clicking on it and selecting the command **Replace**. This will redisplay all configured plots with data from the newly imported case.

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

- **Summary Vector** -- Options to select case, vector to plot, resampling, axis specification, and error bars.
- **Stacking** - Options to control stacking of curves optionally with phase colors.
- **Appearance** -- Options to control curve color, symbols, line style etc.
- **Curve Name** -- Controls how the curve is labeled in the legend.
- **Advanced** -- Specification of additional options.

### Summary Vector
This group of options is used to define summary vector data that the curve will display. 

- **Case** -- Selects the imported Summary or Observed Data case to use as source.
- **Vector** -- Displays the acronym of the selected vector.
- **Resampling** - Option to sample curve data per day, week, month, quarter, half year, year, or decade.
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

