+++
title = "What's New in 2023.03"
published = true
weight = 10
hidden = true
+++

## MSW Well Improvements
![]({{< relref "" >}}images/getting-started/msw_with_valves.png)

[Multi Segmented Wells - MSW]({{< relref "simulationwells" >}}) is updated with new features and improved visualization
- Fixes wrong well geometry for some cases
- Added optional visualization of valves


## Calculator Improvements
![]({{< relref "" >}}images/calculated-data/calculated-well-curve.png)

A calculated summary vector for a well will now by default be available for all wells.

[[Summary Calculator]]({{< relref "CurveCalculator" >}})  [[Calculator Expressions]]({{< relref "CalculatorExpressions" >}}) [[Grid Calculator]]({{< relref "GridPropertyCalculator" >}}) 

## Radial Grids

![]({{< relref "" >}}images/3d-main-window/radial-grid.png)

Import of radial grids are now supported. Using I and J range filters will filter the model based on angle and radius (Theta and R).


## Well Allocation over Time
![]({{< relref "" >}}images/plot-window/WellAllocationOverTime.png)

Use the Well Allocation over time to see how the allocation changes between time steps.


## Summary Plot Improvements

- Make sure on/off state for ensemble statistics is stable during source stepping
- Custom time axis tick marks [[Custom Time Axis Properties]]({{< relref "summaryplots" >}}#custom-time-axis-properties)
- Show correct group name for group vectors
- Blank space around legend items has been reduced, makes it possible to show legends on less screen space
- Fixed issue for import of simulations for large time span into future (after year 2262)
- Default name for summary vector is now a descriptive text (Oil Production instead of FOPT) The settings for curve names can be controlled from [[Curve Properties]]({{< relref "summaryplots" >}}#editing-a-summary-curve)

## Import of Pressure Data
Pressure data in a custom file format can be imported.

[[Pressure Depth Data]]({{< relref "pressuredata" >}})







## Other improvements






See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.