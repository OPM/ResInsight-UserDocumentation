+++
title = "What's New in 2020.10"

weight = 10
hidden = true
+++

ResInsight 2020.10 is the latest version of ResInsight, the professional quality, open source 3D visualization, curve plotting and post-processing tool for reservoir models and simulations. Version 2020.10 is a major update bringing a range of significant new and enhanced features.

## Surfaces
![]({{< relref "" >}}images/3d-main-window/SurfacesOverview.png)

ResInsight supports import of [ 3D Surfaces ]({{< relref "3d-main-window/surfaces" >}}), and allows mapping properties and simulation results onto these surfaces. In addition, it is now possible to create a surface from the top of a K-layer in a grid model.

OpenWorks XYZ file format is now supported. 

## Color Management

[ Color Legends ]({{< relref "3d-main-window/colorlegends" >}}) can be customized and managed by the user. User defined color legends can be used for any result mapping.

## Analysis Plots
![]({{< relref "" >}}images/plot-window/AnalysisPlotsEnsemble.png )

[ Analysis Plots ]({{< relref "plot-window/analysisplots" >}}) are bar charts used to compare summary data at specific timesteps across *Ensembles* and *Summary Cases*.

## Correlation Plots
![]({{< relref "" >}}images/plot-window/CorrelationPlotsPearsonCoefficient.png )

[ Correlation Plots ]({{< relref "plot-window/correlationplots" >}}) are plots used to visualize correlations between ensemble parameters and summary result vectors.
Several visualizations can be created, including tornado plots, correlation matrices, and cross plots.

## Derived Geomechanical Results

More derived geomechanical results are now available. These includes Mud Weight Window, Stress Anisotropy timelapse, Shear Slip Indicator and Pore Compressibility.

For more details on these parameters see [Geomechanical Derived Results]({{< ref "derivedresultsgeomech.md" >}})

## Flow Vectors

![]({{< relref "" >}}images/3d-main-window/FlowVectorResult.PNG)

The Flow Vector Result View lets the user investigate fluxes by visualizing flow vectors in the reservoir. It allows for selecting and combining different fluids and directions.

[Flow Vector Result]({{< ref "flowvectorresult.md" >}})

## Application Themes

![]({{< relref "" >}}images/3d-main-window/ApplicationTheme.png )

An increasing number of engineers are now used to working with customized visual themes on their desktops. In order to allow the users to work with ResInsight in this settings, we have established support for application themes. Many icons are also updated to improve communication with the user.

The active application theme can be modified from **Preferences->GUI Theme**

## Python Documentation
The Python documentation is updated with new features

![]({{< relref "" >}}images/scripting/apiResInsightOrg.png)

Here are the highlights of new features for Python

- Surface management


[ Python Documentation ](https://api.resinsight.org)


**Release Notes on GitHub**

[Release info on GitHub](https://github.com/OPM/ResInsight/releases/)
