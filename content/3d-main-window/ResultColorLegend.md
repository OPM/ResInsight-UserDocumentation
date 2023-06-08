+++
title = "Result Color Legend"
published = true
weight = 30
+++

![Legend Configuration]({{< relref "" >}}images/3d-main-window/legend_configuration.PNG)

The color mapping of the displayed cell result is controlled by the **Color Legend** item in **Project Tree**. 
The legend can be shown or hidden by checking or unchecking the box in front of the **Color Legend** item.

## Legend configuration
As shown above, the Legend configuration for cell results allows the following settings:

- **Number of levels** -- Defines the number of tick marks displayed next to the color legend
- **Significant digits** -- Defines the number of significant digits in the number formatting
- **Number format** -- Defines how the numbers are formatted
- **Colors** -- Defines the color palette for the legend by selecting from [Color Legends]({{< relref "colorlegends" >}})
- **Mapping** -- Defines the mapping of numerical values to legend colors:
  - **Discrete Linear** -- Legend divided into linear levels defined by **Number of levels**
  - **Continuous Linear** -- Continuous linear legend with tick mark count defined by **Number of levels**
  - **Continuous Logarithmic** -- Continuous logarithmic legend with tick mark count defined by **Number of levels**
  - **Discrete Logarithmic** -- Logarithmic legend divided into levels defined by **Number of levels**
  - **Category** -- Legend with one level per category for formation names and discrete data (e.g. result names ending with _`NUM`_)
- **Range type**:
  - **All Timesteps** -- use of values for all time steps to find numerical range of legend (unavailable for Flow Diagnostics results)
  - **Current Timestep** -- use of current (single) time step to find min and max values  
  - **User Defined Range** -- user specified range from minimum to maximum numerical value

Furthermore, the legend may display semi-transparent with a sorrounding box by selecting the **Show Box around Legends** option of the 
[Preferences dialog]({{< relref "preferences" >}}).

![Legend Background]({{< relref "" >}}images/3d-main-window/legend_background.png) ![Show Box around legends]({{< relref "" >}}images/3d-main-window/legend_with_background.png)


## Legend configuration for category results
The **Category** type of legend mapping concerns such as formation names and discrete numbered results (e.g. result names with trailing _`NUM`_). 

**Category** type of legends invoke the Property Editor shown below. 
Here the default **Category Mode** *Interpolate* is shown to color all formations.

![Legend Configuration]({{< relref "" >}}images/3d-main-window/LegendConfigCategoryInterpolate.png)

In the example below, the **Category Mode** *Exclusively Category Colors* has been selected to produce a 3D visualization of formations according to the category numbers of *Selected Formations Legend*. 
As seen, formations according to the category numbers are displayed in colors while the others are displayed in grey. 
Please see [Color Legends]({{< relref "colorlegends" >}}) for more information about legends and category numbers.

![Legend Configuration]({{< relref "" >}}images/3d-main-window/LegendConfigCategoryExclusive.png)


