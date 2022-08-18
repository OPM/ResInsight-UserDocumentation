+++
title = "RFT Segment Plot"
published = true
weight = 90
+++

![]({{< relref "" >}}images/plot-window/RFTSegmentPlot.png)

RFT Segment Data can be plotted as horizontal Well Log Plots. RFT data can be imported based on a summary case or a grid case.


## Create RFT Segment Plot

Open a summary case with RFT data

### Optional Step - Additional data from WSEGLINK
If **WSEGLINK** data is required, set the path to the file containing this data, or to the top level **.DATA** file.

![]({{< relref "" >}}images/plot-window/RFTSummaryDataSource.png)
![]({{< relref "" >}}images/plot-window/RftSegmentDataDeck.png)

From the right-click menu of the summary case, select **Reload** to make sure the data from **WSEGLINK** is imported.

### Create Default Plot
From the right-click menu of the summary case, select **Create RFT Segment Plot**

Select the **Well Log Plot**. Adjust the data source to desired well or branch. These settings are also available from the toolbar above the plot. Useful options to adjust for a curve is color, line style and area fill.

### Additional Features

If a grid and well path is present, a visualization of the well casing including completions can be created. The casing design can then be visualized in a well log track along with the curves to make it easy correlate the curves with installed equipment in the well.

[Create Casing Design]({{< relref "wellpaths.md" >}}#casing-design)

[Visualize Casing Design in a Well Log Plot]({{< relref "welllogsandplots.md" >}}#tracks)

## Create RFT Segment Plot - Step by Step

**From the Project Tree in the Plot Main Window**

- Select right-click command **New Well Log Plot** for _Well Log Plots_
- Select right-click command **New Well Log RFT Curve** for a Track

![]({{< relref "" >}}images/plot-window/RFTSegmentNewCurve.png)
 
- Change orientation of the **Well Log Plot** to _Horizontal_

![]({{< relref "" >}}images/plot-window/RFTSegmentPlotOrientation.png)


- If TVD depth is plotted, optionally invert the Y-axis when the track is selected

![]({{< relref "" >}}images/plot-window/RFTSegmentInvertAxis.png)

- Add more tracks with to the same plot, and use copy/paste of a track for fast duplication. Stacking can be used when plotting curves for multiple phases

![]({{< relref "" >}}images/plot-window/RFTSegmentStackCurves.png)

- Data Source for curves can be modified to quickly switch between wells, dates and branch numbers

![]({{< relref "" >}}images/plot-window/RFTSegmentDataSourceStepping.png)



## Related documents

[Well Log Plots]({{< relref "WellLogsAndPlots.md" >}})