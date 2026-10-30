+++
title = "Ensemble RFT Plot"

weight = 95
+++

![](/images/plot-window/EnsembleRftPlot.png)

ResInsight allows the user to create a ensemble RFT plot similar to summary ensemble plots. 
The functionality also computes statistics, e.g. P10, P90, and mean.
When possible, ResInsight avoids loading the grid when reading ensemble RFT data.

An ensemble RFT plot can also be used as the basis for an [RFT Correlation Plot]({{% relref "RftCorrelationPlot" %}}), which relates the RFT pressure response to the ensemble parameters.

## Create New Ensemble RFT Plot

When a [summary ensemble has been imported]({{% relref "ensembleplotting" %}}#import),
observed FMU data can be imported. See [Observed FMU RFT Data]({{% relref "ObservedFmuRftData" %}}).

To create ensemble RFT plot, right-click **RFT Plots** and select **New RFT Plot**.

![](/images/plot-window/EnsembleRftNewRftPlot.png)




## Property Editor
The property editor lets the user select which curves to display in the RFT plot.

![](/images/plot-window/EnsembleRftPlotPropertyEditor.png)

### Well Name
Select the well to display in the plot. Wells postfixed by _'(Well Path)'_ have an associated well trajectory loaded.

### Sources
Subsequent to selecting a well in the Well Name field, the relevant sources for that well will appear in the **Sources** field. The sources for this particular case are: 

- **Ensembles with RFT Data** -- List of ensembles which contain RFT data with check-boxes to activate display.
- **Observed FMU data** -- Observed data imported from a FMU run, see [Observed FMU RFT Data]({{% relref "ObservedFmuRftData" %}}).

When the user selects one or more sources, a selection of their time steps appears in the **Time Steps** field.

### Time Steps
The **Time Steps** field contains the relevant time steps according to the source selection. Time steps are deemed to be relevant by the following rules:

1. If a single source or sources of the same type are selected, all available time steps in those sources are shown.
2. If sources from two or tree types are selected, the time steps are filtered: 
  - The time steps matching the observed case(s) time steps.
  - If no time steps from a case match the observed time step, the two adjacent ones are shown.
  - The first time step from any grid case(s) (as initial pressure reference).
If the Observed data isn't selected, the RFT data serves as filter reference. 

Each time step is postfixed by letter(s) to indicate source type(s) of each time step. The source types are indicated in square brackets:

- **O** -- Time step has Observed data
- **E** -- Time step has Ensemble data
- **R** -- Time step has RFT data
- **G** -- Time step has Grid data

More than one letter for one single time step, means that the time step comes from multiple case types.

### Zonation/Formation Names
The display of formations lines is controlled in the same manner as for [RFT plots]({{% relref "RftPlot" %}}#zonationformation-names).
Please see the [full documentation]({{% relref "WellLogFormations" %}}) of the formations property editor for details about formations.

### Legend and Axis
Visual properties of legend and axes is controlled in the same manner as for [RFT plots]({{% relref "RftPlot" %}}#legend-and-axis).

### Color by Ensemble Parameter
One ensemble parameter is selected to control coloring. The ensemble parameter value for each case is used to pick a color in a color range. In this case a color legend appears.


![](/images/plot-window/EnsembleRftPlotColors.png)
