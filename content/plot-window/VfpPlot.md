+++
title = "VFP Plot"

weight = 105
+++

![](/images/plot-window/VFP_Plot.png)

A Vertical Flow Performance Plot (VFP Plot) shows the relationship between bottom hole well conditions and wellhead pressure describing a well's ability to lift fluids to the surface. ResInsight can display both production and injection VFP plots:

- **Production VFP Plots** show the outflow or downstream pressure based on the inlet or upstream pressure and the phases flowing. For a well, this means the table relates the flowing bottom-hole pressure
(*BHP*) to the well's tubing head pressure (*THP*) based on the oil, gas and water rates (and any artificial
lift quantities like gas lift gas), or phases ratios, flowing up the wellbore. The data is read from files containing the *VFPPROD* Eclipse keyword.

- **Injection VFP Plots** show the outflow or downstream pressure based on the inlet or upstream pressure and the phases being injected into the system. For a well, this means the table relates the flowing bottom-hole pressure (*BHP*) to the well's tubing head pressure (*THP*) based on the oil, gas or water injection rates. The data can be read from files containing the *VFPINJ* Eclipse keyword.


## Importing VFP data

VFP Plot data can be imported by right-clicking the **VFP Data** item in **Data Sources** to select VFP data from either text files (.ecl or .vfp) or from simulator files (.data). Multi-selection of files is possible.

![](/images/plot-window/VFP_DataSource_Import.png)

Alternatively, VFP Plot data can be imported by right-clicking the **VFP Plots** item in **Plot Project Tree**.

![](/images/plot-window/VFP_PlotTree_Import.png)

## Creating VFP Plots

Having imported VFP data, **Data Sources** lists all available VFP table numbers (c.f. VFPTAB keyword in Eclipse). A VFP plot can be created by right-clicking select VFP table entries.

![](/images/plot-window/VFP_DataSource_Create.png)

Plot data can be exported by right-clicking a VFP plot and selecting *Show Plot Data*.


## List of VFP Plots and settings
The **VFP Plots** item in **Plot Project Tree** lists existing VFP plots. 

![](/images/plot-window/VFP_PlotTree_Listing.png)

Available controls for each VFP plot are:

- **X-Axis** and **Y-Axis**: controls title, layout, fonts, and values of X- and Y-axes, respectively. 

- **Curve Colors**: When curves are plotted, the curve color is taken from the depicted list of colors. The curve colors can be changed by the user.

Most plot mouse interactions are available to VFP plots, c.f. [*Summary Plots*]({{< relref "summaryplots" >}}#plot-mouse-interaction).
Notably, interactive value tracking and zoom is available and double-clicking a VFP plot resets zoom.

## Property Editor

#### Production VFP Plot Property Editor

The Production VFP Plot Property Editor allows the following essential settings:

- **Configuration**

  -- *Curve Matching Type*: Defines curve matching, e.g. in case *Table A*: THP 200, 250, 300, 400 and *Table B*: THP 210, 300, 450.

  -- *Curve Value Options*: Defines if the options in the currently selected *Family variable* is defined by the Main VFP table, or a union of family values from all selected tables.

  -- *Interpolated Variable*: Y-axis variable. 
  
  -- *Primary Variable*: X-axis variable.
  
  -- *Family Variable*: Variable for grouping of properties. Available values for *Family Variable* may differ if multiple tables are selected.

- **Table Details**

  -- *Table Number*: The table number, c.f. VFPTAB keyword of Eclipse.

  -- *Reference Depth*: The reference depth used to generate the table, i.e. VFPREF keyword of Eclipse.

  -- *Flowing Phase*: The flowing phase in the system, i.e. FLO keyword of Eclipse.

  -- *Flowing Water Fraction*: Corresponds to the WFR keyword of Eclipse.

  -- *Flowing Gas Fraction*: Corresponds to the GFR keyword of Eclipse.

- **Comparison Tables**: Enables plots for comparison with other VFP production table numbers.

- **Selection Details**: Check-boxes for selection of numeric values per variable.

![](/images/plot-window/VFP_PROD_PropEd.png)

## Injection VFP Plot Property Editor

Referring to the detailing above, the injection VFP Plot Property Editor allows the following groups of settings: 

- **Configuration**

- **Table Details**

- **Comparison Tables**
