+++
title = "Well Bore Stability Plots"
published = true
weight = 80
+++

![]({{< relref "" >}}images/plot-window/WellBoreStability.png)

ResInsight can create **Well Bore Stability** plots for Geomechanical cases. These plots are specialized [Well Log Plots]({{< relref "welllogsandplots" >}}) to visualize [Formations]({{< relref "formations" >}}), [Well Path Attributes]({{< relref "wellpaths" >}}#well-path-attributes) as well as a set of well path derived curves in different tracks. 

In the figure above, the first track contains [Formations]({{< relref "formations" >}}) while the second track contains well attributes of 
[Casing Design]({{< relref "wellpaths" >}}#casing-design).
The third track shows the following stability gradients (all normalized by mud weight):

- **FG**: Fracture Gradient for sands based on Kirsch.
- **OBG**: Overburden stress gradient: Stress component S_33.
- **PP**: Pore pressure.
- **SFG**: Shear Failure Gradient for shale based on Stassi-d'Alia.
- **SH**: Minimum horizontal stress.

The fourth track contains curves showing the angular orientation of the well path as azimuth (deviation from vertical) and inclination (deviation from x-axis) in degrees.

## Create Well Bore Stability plots

Well Bore Stability plots can be created from the right-click menu for a well path in **Project Tree** or from the the right-click menu of the Well Log Plots entry in **Plot Project Tree**. In the former case, the well bore stability plot will be created for the selected **Well Path**. In the latter case, it will be created for the first well path in the well path list and the well path for the entire plot can be changed with the [Change Data Source Feature]({{< relref "welllogsandplots" >}}#change-data-source-for-plots-and-curves).

![]({{< relref "" >}}images/plot-window/WellBoreStabilityCreation.png) 
![]({{< relref "" >}}images/plot-window/WellBoreStabilityCreation2.png)


## Input requirements

In order to calculate **FG**  and **SFG**, the following input parameters are required:

| Curve | Required Parameters            |
|-------|--------------------------------|
|  FG   | Pore Pressure (PP), Poissons' Ratio |
|  SFG  | Uniaxial Compressive Strength (UCS) |

These parameters may be read in in the following ways. 

[Change Data Source Feature]({{< relref "welllogsandplots" >}}#change-data-source-for-plots-and-curves)


The numbering for import is order of preference if multiple sources are found.

| Parameter     | Default | Import mechanisms |
|---------------|---------|-------------------|
| PP | Hydrostatic PP (TVD x 9.81 / 100 bar) | 1. Grid (Grid units), 2. LAS-file as mud-weight (Variable: "PP", Units: kg / m^3), 3. Element Property Table (Variable: "POR", Units: Pascal)|
| Poissons' Ratio | 0.25 | 1. LAS-file (Variable: "POISSON_RATIO"), 2. Element Property Table (Variable: "POISSON_RATIO")|
| UCS             | 100 bar | 1. Las-file (Variable: "UCS", Units: bar), 2. Element Property Table (Variable: "UCS", Units: MPa) |



## Equations and calculations

### Stresses at the borehole wall - Kirsch equations

The basic input to wellbore stability models is the stresses at the borehole wall given by the Kirsch equations in cylindrical coordinates:

![]({{< relref "" >}}images/plot-window/WellBoreStabilityKirschEquations.png)

The transformation of stresses from cartesian coordinate system to x', y', z' is performed by pre- and transposed postmultiplication of the stress tensor with a 3x3 transformation matrix **M**, i.e. 
{{< image-in-text src="images/plot-window/WellBoreStabilityStressTransformation.png" >}}. 



### Fracture gradient calculations based on Kirsch in sand

To estimate the fracture gradient *FG*, first step is to find the principle effective stresses at the borehole wall:

![]({{< relref "" >}}images/plot-window/WellBoreStabilityKirschSandEquations.png)

Next step is to find the well pressure *Pw* that gives 
{{< image-in-text src="images/plot-window/WellBoreStabilitySigmaTminZero.png" >}} for 
{{< image-in-text src="images/plot-window/WellBoreStabilitySigmaTmin.png" >}}.
Then calculate *FG* in equivalent mud weight units as *FG* = *Pw* / (*TVDRKB* * *g* * 1000) where *TVDRKB = TVDMSL + RKB* and 
*g = 9.81*.


### Stassi-d'Alia failure criterion in shale

Stassi-d'Alia failure criterion in shale is calculated by finding the well pressure *Pw* that satisfies the following equation 
for {{< image-in-text src="images/plot-window/WellBoreStabilitySigmaTmin.png" >}}.

![]({{< relref "" >}}images/plot-window/WellBoreStabilityStassiEquations.png)

where {{< image-in-text src="images/plot-window/WellBoreStabilityPrincipalStresses.png" >}} are the effective principal stresses 
and *UCS* is the *uniaxial compressive strength*.

Shear Failure Gradient is then given as *SFG* = *Pw* / (*TVDRKB* * *g* * 1000) where *TVDRKB = TVDMSL + RKB* and *g = 9.81*.



