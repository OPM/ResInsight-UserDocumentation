+++
title = "Derived Results - Eclipse"

weight = 100
hidden = false
aliases = [
    "/3d-main-window/derivedresults/"
]
+++

ResInsight computes several derived results. In this section we will explain what they are, and briefly how they are calculated.

## Derived Results for Eclipse Cases

ResInsight calculates several derived cell properties that is made available as **Static** or **Dynamic** cell properties.
The derived results listed at the bottom of the **Static** result properties, are shown below.

![](/images/appendix/DerivedStaticResults.png)

### Transmissibility Normalized by Area
The transmissibility for cells and Non-Neighbor Connections (NNCs) are dependent on both cell properties and geometry. ResInsight normalizes TRANX, TRANY and TRANZ with the overlapping flow area for both neighbor cells and NNC-cells. The results are named **riTRANXbyArea**, **riTRANYbyArea** and **riTRANZbyArea** respectively.

The normalized transmissibilities make it easier to compare and check the flow capacity visually. This can be useful when history matching pressure differences across a fault. 

### Overall Transmissibility Multiplier
Transmissibility can be set or adjusted with multiple keywords in an Eclipse data deck. To visualize the adjustments made, ResInsight calculates a multiplicator for the overall change. First unadjusted transmissibilities for all neighbor cells and NNCs are evaluated based on geometry and permeabilities, similar to the NEWTRAN algorithm in Eclipse. For x- and y-directions, the NTG parameter is also included. The results are named **riTRANX**, **riTRANY** and **riTRANZ** respectively.

The TRANX, TRANY and TRANZ used in the simulation are divided by the ResInsight calculated transmissibilities and the resulting multiplicators are named **riMULTX**, **riMULTY** and **riMULTZ** respectively. The derived properties are listed under **Static** properties. The riMULT-properties are useful for quality checking consistence in user input for fault seal along a fault plane. 

### Classification of Cells having NNCs

The static result **riNncCells** use 1 to represent cells having a NNC and 0 for other cells.

### Directional Combined Results

Cell properties with names ending in I, J, K, X, Y, or Z, and an optional "+" or "-" are combined into derived results post-fixed with IJK, or XYZ depending on their origin. (Eg. the static cell properties MULTX, MULTY, MULTZ, and their negatives are combined into the result MULTXYZ, while the dynamic cell properties FLRGASI, FLRGASJ, FLRGASK are combined to FLRGASIJK). 

These combined cell properties visualize the property as a color in all directions combined when selected in 
as a **Cell Result** and **Separate Fault Result**. 

The face of a cell is then colored based on the value associated with that particular face. The Positive I-face of the cell gets the cell X/I-value, while the J-face gets the Y/J-value etc. The negative faces, however, get the value from the neighbor cell on that side. The negative I-face gets the X-value of the IJK-neighbor in negative I direction, and so on for the J- and K-faces.

The directional combined parameters available are:

- Static Properties
  - **TRANXYZ** (inluding NNCs)
  - **MULTXYZ**
  - **riTRANXYZ** (inluding NNCs)
  - **riMULTXYZ** (inluding NNCs)
  - **riTRANXYZbyArea** (inluding NNCs)
- Dynamic Properties
  - **FLRWATIJK** (inluding NNCs)
  - **FLROILIJK** (inluding NNCs)
  - **FLRGASIJK** (inluding NNCs)
- Generated
  - Octave generated results with same name but ending with I,J and K will also be combined into a _`<name>IJK`_ cell property.

### Completion Type

![](/images/appendix/CompletionTypes.png)

The dynamic cell property named **Completion Type** is calculated from the intersections between [Completions]({{< relref "completions" >}}) and the grid cells. All grid cells intersected by a completion will be assigned a color based on the type of completion that intersects the cell.

If a cell is completed with multiple completions, the following priority is used : **Fracture**, **Fishbones**, and **Perforation Interval**.

### Identification of Questionable NNCs
In the process of normalizing transmissibility by the overlapping flow area, the NNCs in the model without any shared surface between two cells are identified. These NNCs are listed in the **Faults/NNCs With No Common Area** folder. These NNCs are questionable since flow normally is associated with a flow area.

![](/images/appendix/ResInsight_NNCsWithNoCommonArea.png)
 
### Water Flooded PV

Water Flooded PV, also called _Number of flooded porevolumes_ shows the amount of flow from a selected set of simulation tracers into a particular cell, compared to the cells mobile pore volume. A value of 1.0 will tell that the tracers accumulated flow into the cell has reached a volume equal to the mobile pore volume in the cell.   

### Mobile Pore Volume

Mobile Pore Volume **MOBPORV** is computed based on the grid cell properties **PORV**, **SWCR** and **MULTPV**.

If **MULTPV** is missing, **MULTPV** is set to 1.0.
If **SWCR** is missing, **SWCR** is et to 0.0.

$ MOBPORV = MULTPV * PORV * (1.0 - SWCR) $

### Cell Volume

The static property **riCellVolume** contains the geometrical volume of a cell.
