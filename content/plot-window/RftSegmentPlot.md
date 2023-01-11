+++
title = "RFT Segment Plot"
published = true
weight = 90
+++

![]({{< relref "" >}}images/plot-window/RFTSegmentPlot.png)

RFT Segment Data can be plotted as horizontal Well Log Plots. RFT data can be imported based on a summary case or a grid case.


## Create RFT Segment Plot

Open a summary case with RFT data

### Additional data from WSEGLINK
Some cases require data from **WSEGLINK** keyword. When importing summary data, ResInsight will automatically search for the related ***.DATA**  file. The identified file can be seen or changed from the **Property Editor.**

![]({{< relref "" >}}images/plot-window/RFTSummaryDataSource.png)
![]({{< relref "" >}}images/plot-window/RftSegmentDataDeck.png)


### Create Default Plot
From the right-click menu of the **RFT Case** object , select **Create RFT Segment Plot** or **Create RFT Multi Phase Segment Plot**

Select the generated **Well Log Plot**. Adjust the data source to desired well or branch. These settings are also available from the toolbar above the plot. Useful options to adjust for a curve is color, line style and area fill.

## Additional settings and adjustments

### General
- Select the plot, and use **Data Source** to change wells, dates and branch numbers

![]({{< relref "" >}}images/plot-window/RFTSegmentDataSourceStepping.png)

- If TVD depth is plotted, optionally invert the Y-axis when the track is selected

![]({{< relref "" >}}images/plot-window/RFTSegmentInvertAxis.png)

- Add more tracks with to the same plot, and use copy/paste of a track for fast duplication. Stacking can be used when plotting curves for multiple phases.

![]({{< relref "" >}}images/plot-window/RFTSegmentStackCurves.png)


### Axis and legend settings
![]({{< relref "" >}}images/plot-window/RFTSegmentPlotPropertyEditor.png)

- Control if the depth axis should be visible for a single or all track from **Axis Visibility.**
- Use the **Plot Title** group to adjust the text of the title. Define a Template Text for full flexibility. Available variable names can be seen when hoovering over the Template Text label.
- Define where the location of curve legend using the **Legend Position** control.


## Related documents

[Well Log Plots]({{< relref "WellLogsAndPlots.md" >}})