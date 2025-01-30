+++
title = "Grid Case Groups and Statistics"

weight = 120
aliases = [
    "/3d-main-window/casegroupsandstatistics/"
]
+++

![](/images/3d-main-window/GridCaseGroupTree.png)

**Grid Case Group**'s are designed to make it easy to calculate statistics per cell and per time step of a large number of Eclipse simulation Cases with identical Grids (often labeled *realizations*).
 
If you have several Eclipse simulations with different input parameters available, you can put all the realizations into a Grid Case Group and easily calculate each of the cells mean value, range and max/min values at each time step. Grid calculations can optionally be used as a data source for computations.

## Creating Grid Case Groups

### From Files
The easiest way to create a **Grid Case Group** is to use the Import command:
**File->Import->Eclipse Cases->Create Grid Case Group**

This command will display the recursive file import dialog described on the [Summary Plots page]({{% relref "eclipsesummarydata" %}}#ensemble-file-import).

ResInsight then creates a **Grid Case Group** for you, and populates its **Source Cases** with the Cases you selected. Then the first of those Cases are read completely, while the others are just scanned to verify that the Grids match and to detect changes in the Active Cells layout. This makes it quite fast to load even a quite large number of realizations.

### Manually
A Grid Case Group can be created from the right-click menu of a Result Case, Input Case or a different Grid Case Group. **Source Cases** can then be added by using the mouse to *drag and drop* cases with equal grids into the **Grid Case Group**'s **Source Case** folder.
This is useful if you want to create statistics based only on a subset of the source cases in an already created **Grid Case Group**.

**Drag and Drop** of cases will normally copy the cases to the new destination, but moving them is possible by pressing and holding the **Shift** key while dropping.

## Viewing Special Source Cases
To reduce the number of views, only a view for the first case is created automatically. If you want to inspect the results of a particular source case, select **New view** from the right-click menu. A new 3D View will the be created on that particular case.

{{% notice note %}}
<h5>How to limit system resource allocation</h5>
To reduce memory usage, project loading time etc. remember to delete the 3D Views you do not need. 3D Views uses a lot of system resources. 
{{% /notice %}}

## Statistics
After creating a grid case group, an empty **Statistics Case** is created for you in the **Derived Statistics** folder of the **Grid Case Group**. 

### Setting Up and Calculate

**Settings for grid case property statistics**

![](/images/calculated-data/StatisticsCaseProperties.png  )  

- **Compute** --  Starts to calculate requested statistical Properties.
- **Edit** -- Deletes the calculated results, and makes the controls to edit the setup available.
- **Summary of calculation setup** -- Summarizes what to calculate.
- **Properties to consider** -- These options makes it possible to select what Eclipse properties to include in the Statistical calculations. Adding variables increase the memory usage and the computational time.
- **Percentile Setup** -- Selects whether to calculate percentiles, what method and what percentile levels should be used. Turning this off speeds up the calculations.
- **Well Data Source Case** -- This option selects which set of **Simulation Wells** to be shown along with the statistical results. You can select one of the **Source Cases**.


**Settings for grid cell calculations**

![](/images/calculated-data/StatisticsCaseGridCalculation.png  )  

- **Data Source** --  Defines either a cell property or a grid calculation expression to be used as data source for the statistical calculations.
- **Grid Calculation** -- List of all defined calculations in the project.
- **Filter By View** -- Limit the calculation to visible cells in a selected view.

Cell values in a selection of cells can be aggregated as described in [Aggregation of Grid Cell Values]({{% relref "aggregationofgridcellvalues" %}})

**Settings for when statistics has been computed**

![](/images/calculated-data/StatisticsCaseGridAfterComputations.png )

 
#### Percentile Methods

Three Percentile methods are implemented:

- **Interpolated Observation** --
The values are sorted, and the two observations representing the probabilities closest to the percentile are interpolated to find the value for the percentile. This is the default method.
- **Nearest Observation** --
The values are sorted, and the first observation representing a probability higher or equal to the percentile probability is selected as the value for the percentile. This method is by some considered to be statistically more puristic.
- **Histogram based estimate** --
A histogram is created and the percentile is calculated based on the histogram. This method will be faster when having a large number of realizations, because no value sorting is involved. You would however need several hundred realizations before this method should be considered.


### Viewing the Results
When the computation is complete, you have to create a 3D View on the **Statistics Case** to view the results. Use the right-click menu of the **Statistics Case** to create it.

### Adding Statistics Cases
A new statistical calculation can be created by activating the right-click menu for **Derived Statistic->New Statistics Case**.
