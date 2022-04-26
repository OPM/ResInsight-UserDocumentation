+++
title = "Summary Plots"
published = true
weight = 10
+++

![]({{< relref "" >}}images/plot-window/SummaryPlotsMain.png)

Summary Plots are a display of curves based on 
[Eclipse Summary Data]({{< relref "eclipsesummarydata" >}})
which can be combined with 
[imported observed time history data]({{< relref "observeddata" >}}), 
[grid cell time history curve]({{< relref "resultinspection" >}}#result-plot), and 
[pasted ascii curves]({{< relref "pasteexceltimedata" >}}). 


Summary plots are displayed on screen by maximum four rows by four columns of plots. 
In the example above, ResInsight displays two columns and two rows of plots, each plot comprising a single curve. However, a plot may contain an arbitrary number of curves.
Essential helpers for setup of Summary Plots are:

- *Plots*: overview of established plots and their components
- [*Data Sources*]({{< relref "summaryplotdatasources" >}}):
searching and sourcing data from case, field, regions, wells, groups, or ensemble
- [*Plot Manager*]({{< relref "summaryplotmanager" >}}):
powerful text-based selection of vectors for summary plotting 
- *Property Editor*: settings for titles, legends, layout, axes etc


## Creating Summary Plots

### Using Data Sources to create Summary Plots

Having imported [Eclipse Summary Data]({{< relref "eclipsesummarydata" >}}), the **Data Sources** window provides an easy approach to create Summary Plots:

- Search or navigate **Data Sources** to find the desired source(s) and vector(s)
- *Right-click* selected vector(s) and select **New Summary Plot** 
- *Drag & Drop* additional vector(s) to append curves into an existing plot or vacant plot area

Please note the functionality of **Data Sources** to search for data sources and vectors across all available data.

Creating a new summary plot of *WBHP* of *Well B-1H* and subsequent *Drag & Drop* of WGOR produces the following. 

![]({{< relref "" >}}images/plot-window/SummaryPlots_WBHP_WGOR.png)

When applicable, the data source of displayed curves is rapidly changed by using:
- Toolbar buttons
- Keyboard shortcuts, i.e. *CTRL &larr;/&rarr;* for well and *CTRL &uarr;/&darr;* for vector

If a set of curves are pertinent to a single data source, you may easily append corresponding plots for other entries of the type. For instance, the above screenshot comprises plots for a single well so you may easily append corresponding plots for other wells by:

- Right-clicking a set of wells, and select *Append Plots for Wells*
  - Adjust the number of columns and rows for each page as desired
  - Use PgUp/PgDown or scroll wheel to validate the plots
- Ease visual comparison of individual curves by clicking the toolbar button *Sync axis Ranges in All Plots* to obtain plots with identical axes
- Snapshot the curves or export to PDF-file via the toolbar-buttons and Edit-menu

![]({{< relref "" >}}images/plot-window/SummaryPlotsAppendPlotsForWells.png)


### Using Plot Manager to create Summary Plots

Having imported [Eclipse Summary Data]({{< relref "eclipsesummarydata" >}}), the 
[**Plot Manager**]({{< relref "summaryplotmanager" >}}) 
provides an alternative and powerful approach to create Summary Plots by text-based selection of data sources and vectors to plot.


## Overview and Editing Summary Plots
The settings of each plot are listed in the **Plots** window for overview and are controlled by its sub-items and the **Property Editor**.

![]({{< relref "" >}}images/plot-window/SummaryCurveSelection.png)


### Editing a Summary Curve

By selecting a specific summary curve in the **Plots** window, its properties are displayed by the **Property Editor**.

![]({{< relref "" >}}images/plot-window/summary_curve_properties.png)

The Property Editor organizes the available options into the following groups:

- **Summary Vector** -- Options to select case, vector to plot, resampling, axis specification, and error bars.
- **Stacking** - Options to control stacking of curves optionally with phase colors.
- **Appearance** -- Options to control curve color, symbols, line style etc.
- **Curve Name** -- Controls how the curve is labeled in the legend.
- **Advanced** -- Specification of additional options.

Other actions are available via right-click menu for selected curve. For instance, the Y-Axis for one or more curves can be switched for using the right-click command <b>Switch Plot Axis</b>.  


### Time Axis Properties
Time axis properties are displayed by clicking the **Time Axis** subitem of a summary plot in **Plots** window. 

![]({{< relref "" >}}images/plot-window/SummaryTimeAxisProperties.png)

The property groups are:

- **Axis Title**: Toggle display of axis title, setting user defined name, position, and font. 
- **Time Values**: Show time from *Simulation Start*, or real date-times, specific or automatic date/time range, and font.
- **Date/Time Label Format**: Date and time format for the time axis, c.f. [Preferences]({{< relref "preferences.md" >}}) for default.


### Y-axis Properties
Y-axis properties are displayed by clicking one of the left/right axis subitems of a summary plot in **Plots** window.

![]({{< relref "" >}}images/plot-window/summary_plot_yaxis_properties.png)

The property groups are:

- **Title Text**: Caters for automatic or user specification of title and inclusion of vector name, acronym, and units in plot.
- **Title Layout**: Positioning of title (*Center* or *At End*) and font size. 
- **Axis Values**: Logarithmic scale, inversion of axis, legend number formatting, scale factor, 
max/max range, and font size.   


### Changing content of a Summary Plot
Right-clicking an existing summary plot in **Plots** and selecting *Edit Summary Plot* initiates the 
[*Summary Plot Editor*]({{< relref "summaryploteditor" >}}) which offers complete functionality to navigate and select vectors from all summary types.


## Summary Plot Functionality 

### Plot Mouse Interaction

- **Value Tracking**: When the mouse cursor is close to a curve, the closest curve sample is highlighted and the curve sample value at this location is displayed in a tooltip. 
- **Selection**: Left mouse button click can be used to select several of the parts in the plot, and display them in the Property Editor:
  - The closest curve.
  - Each of the Plot Axes.
  - The summary plot itself if none of the above is hit and the **Plots** window is activated by the mouse click.
- **Window Zoom**: Available by dragging the mouse with left mouse button pressed. 
Use toolbar button or *View* menu option 
{{< image-in-text src="images/plot-window/ZoomAll16x16.png" >}} *Zoom All* to zoom all summary curves and restore default zoom level.
- **Wheel Zoom**: The mouse wheel will zoom the plot in and out towards the current mouse cursor position presupposing use of mouse wheel is not disabled by toolbar button {{< image-in-text src="images/plot-window/ZoomDisableMouseWheelCapture.png" >}}.


### Highlighting a curve or axis
A summary curve is highlighted when left-clicked in a plot. This allows for detailed investigation of a specific curve among many others. Summary curves can also be activated and deactivated by clicking in **Plots** window. See also **Plots** right-click menu items, e.g. *On - Others Off* which is an effective way to deactivate all curves not selected.

Another essential feature is to left-click an axis in a summary plot which will highlight the curves corresponding to the particular axis.

![]({{< relref "" >}}images/plot-window/SummaryCurveHighlight.png)


### Accessing Plot Data
Right-clicking a plot in **Plots** window and selecting **Show Plot Data** will open a window containing the plot data as text columns. 
The window displays plot data by day, week, month, quarter, half year and year.

The text content of this window is easy to copy and paste into Excel or other tools for further processing.
It is also possible to save the text data to a file by the right-click command **Export to File**. 

### Copy and Paste 
Copy and Paste of summary plots and curves is possible using the **Plots** right-click menu and standard keyboard shortcuts (CTRL-C/CTRL-V).

