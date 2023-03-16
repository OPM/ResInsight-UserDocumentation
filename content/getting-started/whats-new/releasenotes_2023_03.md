+++
title = "What's New in 2023.03"
published = true
weight = 10
hidden = true
+++



## Calculator Improvements
![]({{< relref "" >}}images/calculated-data/calculated-well-curve-ensemble.png)

A calculated summary vector is now by default available for all wells, all cases and all ensembles.

[[Summary Calculator]]({{< relref "CurveCalculator" >}})  [[Calculator Expressions]]({{< relref "CalculatorExpressions" >}}) [[Grid Calculator]]({{< relref "GridPropertyCalculator" >}}) 

## Radial Grids
![]({{< relref "" >}}images/3d-main-window/radial-grid.png)

Import of radial grids including local grid refinement(LGR) are now supported. Using I and J range filters will filter the grid case based on angle and radius (Theta and R).

## Multi Segment Well Improvements
![]({{< relref "" >}}images/getting-started/msw_with_valves.png)

[Multi Segmented Wells - MSW]({{< relref "simulationwells" >}}) is updated with new features and improved visualization
- Fixes wrong well geometry for some cases
- Added optional visualization of valves

## Well Allocation Over Time
![]({{< relref "" >}}images/plot-window/WellAllocationOverTime.png)

Use [Well Allocation Over Time]({{< relref "flowdiagnosticsplots" >}}#well-allocation-over-time) to see the allocation over multiple restart time steps.

## Depth Plot

![]({{< relref "" >}}images/3d-main-window/DepthPlotIn3D.png)

The [[Depth Plot]]({{< relref "depthplot" >}}) can be used to display values for all K-cells for one or multiple selected IJ cells.

## Summary Plot Improvements

- Make sure on/off state for ensemble statistics is stable during source stepping
- Custom time axis tick marks [[Custom Time Axis Properties]]({{< relref "summaryplots" >}}#custom-time-axis-properties)
- Show correct group name for group vectors
- Blank space around legend items has been reduced, makes it possible to show legends on less screen space
- Fixed issue for import of simulations for large time span into future (after year 2262)
- Default name for summary vector is now a descriptive text (Oil Production instead of FOPT) The settings for curve names can be controlled from [[Curve Properties]]({{< relref "summaryplots" >}}#editing-a-summary-curve)

## Improved RFT Plotting

- [[Pressure Depth Data]]({{< relref "pressuredata" >}}) can be imported from a custom file format.
- More flexible RFT plotting; it is now possible to combine ensemble RFT data sith single RFT curves and other observed curves.


## Other improvements

- Fixed parsing of GRDECL files if a comment is added on the same line after a keyword end character ‘/’
- Fixed freeze during import of grid model (Progress bar freezes at 28%)
- New button next to file path to quickly copy text to clipboard
- Added more scaling factors to 3D view, and support for custom scale value in **Preferences**
- GRDECL export: Added option to export NOECHO and ECHO to generated text file
- `CTRL-E` as shortcut to open [[Summary Plot Editor]]({{< relref "summaryploteditor" >}}) 
- Added slider to quickly switch between time step
- Improved user interface for range filters
- When clicking on a cell: Show center coordinates and corner coordinates [[Result Info]]({{< relref "resultinfo" >}}) 



See [**Release Notes on GitHub**](https://github.com/OPM/ResInsight/releases/) for further details and information.