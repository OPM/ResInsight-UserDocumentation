+++
title = "Flow Vector Result"
published = true
weight = 50
+++

![]({{< relref "" >}}images/3d-main-window/FlowVectorResult.PNG)

The Flow Vector Result View lets the user investigate fluxes by visualizing flow vectors in the reservoir. It allows for selecting and combining different fluids and directions. Selected vectors can be combined and scaled.

The flow vectors are based on the Eclipse properties **FLRGASI/J/K FLRWATI/J/K FLROILI/J/K**

### Open the Flow Vector Result View

In order to show Flow Vector Results, select and check the checkbox next to **Flow Vector Result** in the **Project Tree**.

![]({{< relref "" >}}images/3d-main-window/FlowVectorResultMenu.PNG)

The 3D View gets updated with arrows visualizing the fluxes. The directions, data source fluids, color, scale and threshold can be adjusted in the Property Editor.

### Legend

![]({{< relref "" >}}images/3d-main-window/FlowVectorResultLegend.PNG)

The legend maps the Flow Vector colors to their respective result values. By default it shows the max values for all time steps. The legend settings can be changed in the **Color Legend** sub item of the **Flow Vector Result** item in the **Project Tree**.

**Note:**\
When combining several fluids, the max value shown in the legend is an aggregation of the single max values of each selected fluid. This means that this number might be higher than the result of any flow vector.


### Adjust the View

In the *Property Editor*, there are four different settings groups.

![]({{< relref "" >}}images/3d-main-window/FlowVectorResultProperties.PNG)

#### Fluids
The fluxes of the fluids selected here are shown as aggregated vectors in the 3D view.

#### Visibility

**View Vectors**
- **Per Face:** Show one flow vector per cell face. Each direction has its own vector.
- **Cell Center Total:** Show only one vector per cell, located at the cell's center position. This vector is an aggregation of all single direction vectors.

**Vectors Touching Surface** (only enabled when **View vectors** is set to **Per Face**)
- **At vector anchor:** The vectors are starting at the cells' faces.
- **At vector center:** The vectors' centers are located at the cell's faces.

**I/J/K**
- Use flows in **I/J/K** direction for computing vectors.

**Show NNC data**
- Visualize flows between non-neighbouring cells.

**Threshold**
- All vectors with flow result values below this number are hidden.

#### Vector Colors
- **Result Colors:** Color vectors in the flow result color according to the *Element Vector Result* legend shown in the 3D View.
- **Uniform:** Color vectors in a uniform color.

#### Vector Size

**Size Scale**
- Scales the length of the vectors by this value.

**Scale Method**
- **Result:** Scale the vectors according to their flow result value.
- **Result (logarithmically):** Scale the vectors according to their flow result value but in a logarithmic scale. **Note:** all values are increased by 1 in order to be able to properly show flow result values smaller than 1.*
- **Constant:** All vectors have the same constant length.