+++
title = "Aggregation of Grid Cell Values"

weight = 30
+++

### Calculate statistics for sum of mobile oil for an ensemble

**Workflow description**

- Import an ensemble of grid models with identical IJK into a **Grid Case Group**.
- Create a view on one of the source grid models, and create a cell filter for the region of interest.
- Create an expression for mobile oil `MOBILE_OIL := if(((SOIL-SOWCR) < 0.00), 0.00, PORV*(SOIL-SOWCR))`
- Select a subset of time steps. This will significantly affect performance for for large grids with many time steps.
- Create an expression to aggregate values for all visible cells `SUM_MOBILE_OIL := sum(MOBILE_OIL)` Use the result from the previous calculation as input to the variable, use `MOBILE_OIL` from the **Generated** category.
- Make sure **Apply to All Cases** is checked.
- The individual values for each realization and time step is displayed as text in **Messages**. The statistics for each time step is displayed at the bottom.


![image](https://github.com/OPM/ResInsight/assets/1793152/bf53a448-94ce-4fbb-850e-b912c060a6d4)

See draft workflow with screenshots here:
https://github.com/OPM/ResInsight/discussions/10913