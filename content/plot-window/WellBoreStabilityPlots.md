+++
title = "Well Bore Stability Plots"
published = true
weight = 80
+++

![]({{< relref "" >}}images/plot-window/WellBoreStability.png)

ResInsight can create **Well Bore Stability** plots for Geomechanical cases. These plots are specialized [Well Log Plots]({{< relref "welllogsandplots" >}}) to visualize [Formations]({{< relref "formations" >}}), [Well Path Attributes]({{< relref "wellpaths" >}}#well-path-attributes) as well as a set of well path derived curves in different tracks. 

In the figure above, the first track contains [Formations]({{< relref "formations" >}}) and an indication of sea level.

| Sea Level | Formations |
|-----------|------------|
|![]({{< relref "" >}}images/plot-window/WaterLevel.png) | ![]({{< relref "" >}}images/plot-window/FormationLevels.png) |

The second track contains a visualisation of the well, with well attributes of [Casing Design]({{< relref "wellpaths" >}}#casing-design) as well [Completions]({{< relref "Completions" >}})

The third track, which is disabled by default, contains the input parameters of the plot as described in the [Input Requirements](#input-requirements) section.

The fourth track (third visible by default) shows the following stability gradients (all normalized by mud weight):

- **FG**: Fracture Gradient in sands based on Kirsch and in shale based on the K0_FG parameter or proportional to SHMIN. 
- **OBG**: Overburden stress gradient: Stress component S_33.
- **PP**: Pore pressure.
- **SFG**: Shear Failure Gradient for shale based on Stassi-d'Alia.
- **SHMIN**: Minimum horizontal stress from grid.
- **SH_MK**: Minimum horizontal stress from Matthews & Kelly.

The fifth track contains curves showing the angular orientation of the well path as azimuth (deviation from vertical) and inclination (deviation from x-axis) in degrees.

## Create Well Bore Stability plots

Well Bore Stability plots can be created from the right-click menu for a well path in **Project Tree** or from the the right-click menu of the Well Log Plots entry in **Plot Project Tree**. In the former case, the well bore stability plot will be created for the selected **Well Path**. In the latter case, it will be created for the first well path in the well path list and the well path for the entire plot can be changed with the [Change Data Source Feature]({{< relref "welllogsandplots" >}}#change-data-source-for-plots-and-curves).

![]({{< relref "" >}}images/plot-window/WellBoreStabilityCreation.png) 
![]({{< relref "" >}}images/plot-window/WellBoreStabilityCreation2.png)

## Input requirements

In order to calculate **PP**, **FG**, **SFG** and **SH_MK**, the following input parameters are required:

| Curve | Required Parameters            |
|-------|--------------------------------|
|  PP   | Pore Pressure in reservoir (PP Reservoir) and outside the reservoir (PP Non-Reservoir) |
|  FG   | Pore Pressure (PP Reservoir), Poissons' Ratio in Sand, FG Shale in shale |
|  SFG  | Uniaxial Compressive Strength (UCS) |
| SH_MK | K0_SH, Overburden Gradient at initial time (OBG0) and the Depletion Factor (DF) |

The numbering for import is order of preference if multiple sources are found.

| Parameter     | Default | Sources |
|---------------|---------|-------------------|
| Density of Sea Water | $1.03 g/cm^3$ | User setting in GUI|
| PP Reservoir | Grid Nodal Values (POR) | 1. Grid (Grid units), 2. LAS-file as equivalent mud-weight (Variable: "PP_INP", Units: SG_EMW), 3. Element Property Table (Variable: "POR", Units: Pascal)|
| PP Non-Reservoir | Hydrostatic PP (from TVDRKB, Density of Sea Water and gravity) | 1. LAS-file as equivalent mud-weight (Variable: "PP_INP", Units: SG_EMW), 3. Element Property Table (Variable: "POR", Units: Pascal), 4. Hydrostatic Pressure|
| Poissons' Ratio | 0.35 | 1. LAS-file (Variable: "POISSON_RATIO_INP"), 2. Element Property Table (Variable: "POISSON_RATIO")|
| UCS             | 100 bar | 1. LAS-file (Variable: "UCS_INP", Units: bar), 2. Element Property Table (Variable: "UCS", Units: MPa) |
| K0_FG | 0.75 x Hydrostatic PP | LAS-file (Variable: "K0_FG_INP", Units: SG_EMW) |
| K0_SH | 0.65 x Hydrostatic PP | LAS-file (Variable: "K0_SH_INP", Units: SG_EMW) | 
| Initial Overburden Gradient (OBG0) | OBG at initial time step | 1. Grid (Grid units), 2. LAS-file (Variable: "OBG0_INP", Units: Bar) | 
| FG Shale | Derived from K0_FG | 1. Derived from K0_FG and PP Non-Reservoir, 2. Proportional to SH, 3. LAS-file (Variable: "FG_SHALE_INP", Units: SG_EMW)|

In addition to the units above, it LAS-files it is possible to supply PP in Bar and UCS in Pascal or MPa. Conversion will be handled automatically.

![]({{< relref "" >}}images/plot-window/WellBoreStabilityParameters.png)

## Equations and calculations

### Stresses at the borehole wall - Kirsch equations

The basic input to wellbore stability models is the stresses at the borehole wall given by the Kirsch equations in cylindrical coordinates:

![]({{< relref "" >}}images/plot-window/WellBoreStabilityKirschEquations.png)

The transformation of stresses from cartesian coordinate system to x', y', z' is performed by pre- and transposed postmultiplication of the stress tensor with a 3x3 transformation matrix **M**, i.e. 
{{< image-in-text src="images/plot-window/WellBoreStabilityStressTransformation.png" >}}. 



### Fracture gradient calculations based on Kirsch in sand

To estimate the fracture gradient *FG*, first step is to find the principal effective stresses at the borehole wall:

$$\sigma'_1 = \sigma'_1 (\theta)= \sigma'_r = p_w - p_0$$

$$\sigma'_2 = \sigma'_2 (\theta) = \sigma\_{t \max} = \frac{1}{2} \left( (\sigma_z + \sigma\_\theta) + \sqrt{(\sigma_z + \sigma\_\theta)^2 + 4\tau\_{\theta z}^2} \right) - p_0$$

$$\sigma'_2 = \sigma'_3 (\theta) = \sigma\_{t \min} = \frac{1}{2} \left( (\sigma_z + \sigma\_\theta) - \sqrt{(\sigma_z + \sigma\_\theta)^2 + 4\tau\_{\theta z}^2} \right) - p_0$$

Next step is to solve for the value of $\theta \in [0 - 180]$ that yields $\sigma'_3 (\theta) = 0$ which in turn gives us $\sigma\_\theta$ which can be used to solve for $P_w$ in the Kirsch equations.

Then calculate *FG* in equivalent mud weight units as
$$ FG = \frac{P_w}{TVD\_{RKB} \\: g  \\: \rho}$$ where $TVD\_{RKB} = TVD\_{MSL} + AirGap$, the gravity acceleration $g = 9.81 m/s^2$ and  the density of sea water $\rho$ in $kg/m^3$ (thus 1000 x the UI input in $g/cm^3$).

### Stassi-d'Alia failure criterion in shale

Stassi-d'Alia failure criterion in shale is calculated by finding the well pressure $P_w$ that satisfies the following equation 
for  $\theta \in [0 - 180]$:

![]({{< relref "" >}}images/plot-window/WellBoreStabilityStassiEquations.png)

where {{< image-in-text src="images/plot-window/WellBoreStabilityPrincipalStresses.png" >}} are the effective principal stresses from the Fracture Gradient calculation.
and *UCS* is the *uniaxial compressive strength*.

The Shear Failure Gradient is then given as

$$SFG = \frac{P_w}{TVD\_{RKB} \\: g \\: \rho}$$

## Python Interface
The ResInsight Python Server has specific functionality for creating Well Bore Stability Plots in Python. In particular the Python ```Case``` class has a method ```create_well_bore_stability_plot``` method ([API doc]({{< relref "pythonrips" >}}#create_well_bore_stability_plotwell_path-time_step))

See the [Create WBS Plot example]({{< relref "pythonexamples" >}}#create-wbs-plot) for an example of use.