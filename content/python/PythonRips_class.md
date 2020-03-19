+++ 
title =  "Python Classes (BETA)" 
published = true 
weight = 95 
+++ 
# Introduction

As the Python interface is growing release by release, we are investigating how to automate the building of documentation. This document shows the inheritance relationship between objects derived from **PdmObject**. The **PdmObject** is the base object for all objects automatically created based on the data model in ResInsight.## PdmObject

## Case
**Inherits PdmObject**

The ResInsight base class for Cases

Attribute | Type | Description
--------- | ---- | -----------
file_path | str | Case File Name
id | int | Case ID
name | str | Case Name

### GeoMechCase
**Inherits Case**

The Abaqus Based GeoMech Case


### Reservoir
**Inherits Case**

Abtract base class for Eclipse Cases


#### EclipseCase
**Inherits Reservoir**

The Regular Eclipse Results Case


## Project
**Inherits PdmObject**

The ResInsight Project


## EclipseResult
**Inherits PdmObject**

An eclipse result definition

Attribute | Type | Description
--------- | ---- | -----------
flow_tracer_selection_mode | str | Tracers
phase_selection | str | Phases
porosity_model_type | str | Porosity
result_type | str | Type
result_variable | str | Variable
selected_injector_tracers | str | Injector Tracers
selected_producer_tracers | str | Producer Tracers
selected_souring_tracers | str | Tracers

### CellColors
**Inherits EclipseResult**

Eclipse Cell Colors class


## GridCaseGroup
**Inherits PdmObject**

A statistics case group

Attribute | Type | Description
--------- | ---- | -----------
group_id | int | Case Group ID
user_description | str | Name

## SummaryCase
**Inherits PdmObject**

The Base Class for all Summary Cases

Attribute | Type | Description
--------- | ---- | -----------
auto_shorty_name | str | Use Auto Display Name
short_name | str | Display Name
summary_header_filename | str | Summary Header File

### FileSummaryCase
**Inherits SummaryCase**

A Summary Case based on SMSPEC files

Attribute | Type | Description
--------- | ---- | -----------
include_restart_files | str | Include Restart Files

### GridSummaryCase
**Inherits SummaryCase**

A Summary Case based on extracting grid data.


## SummaryPlotCollection
**Inherits PdmObject**


## ViewWindow
**Inherits PdmObject**

The Base Class for all Views and Plots in ResInsight


### PlotWindow
**Inherits ViewWindow**

The Abstract base class for all MDI Windows in the Plot Window

Attribute | Type | Description
--------- | ---- | -----------
id | int | View ID

#### Plot
**Inherits PlotWindow**

The Abstract Base Class for all Plot Objects


#### SummaryPlot
**Inherits Plot**

A Summary Plot

Attribute | Type | Description
--------- | ---- | -----------
is_using_auto_name | str | Auto Title
normalize_curve_y_values | str | Normalize all curves
plot_description | str | Name
show_plot_title | str | Plot Title

#### WellLogPlot
**Inherits PlotWindow**

A Well Log Plot With a shared Depth Axis and Multiple Tracks

Attribute | Type | Description
--------- | ---- | -----------
auto_scale_depth_enabled | str | Auto Scale
depth_type | str | Type
depth_unit | str | Unit
maximum_depth | float | Max
minimum_depth | float | Min
show_depth_grid_lines | str | Show Grid Lines
show_title_in_plot | str | Show Title

#### WellBoreStabilityPlot
**Inherits WellLogPlot**

A GeoMechanical Well Bore Stabilit Plot


### View
**Inherits ViewWindow**

Attribute | Type | Description
--------- | ---- | -----------
background_color | str | Background
current_time_step | int | Current Time Step
disable_lighting | str | Disable Results Lighting
grid_z_scale | float | Z Scale
id | int | View ID
perspective_projection | str | Perspective Projection
show_grid_box | str | Show Grid Box
show_z_scale | str | Show Z Scale Label

#### GeoMechView
**Inherits View**

The Geomechanical 3d View


#### GeoMechContourMap
**Inherits GeoMechView**

A contour map for GeoMech cases


#### EclipseView
**Inherits View**

The Eclipse 3d Reservoir View


#### EclipseContourMap
**Inherits EclipseView**

A contour map for Eclipse cases


## WbsParameters
**Inherits PdmObject**

Attribute | Type | Description
--------- | ---- | -----------
df_source | str | Depletion Factor (DF)
fg_multiplier | float | SH Multiplier for FG in Shale
fg_shale_source | str | FG in Shale Calculation
k0_fg_source | str | K0_FG
k0_sh_source | str | K0_SH
obg0_source | str | Initial Overburden Gradient
poission_ratio_source | str | Poisson Ratio
pore_pressure_non_reservoir_source | str | Non-Reservoir Pore Pressure
pore_pressure_reservoir_source | str | Reservoir Pore Pressure
ucs_source | str | Uniaxial Compressive Strength
user_df | float | User Defined DF
user_k0_fg | float | User Defined K0_FG
user_k0_sh | float | User Defined K0_SH
user_poisson_ratio | float | User Defined Poisson Ratio
user_pp_non_reservoir | float |   Multiplier of hydrostatic PP
user_ucs | float | User Defined UCS [bar]
water_density | float | Density of Sea Water [g/cm^3]

## SimulationWell
**Inherits PdmObject**

An Eclipse Simulation Well

Attribute | Type | Description
--------- | ---- | -----------
name | str | Name

## WellPath
**Inherits PdmObject**

The Base class for Well Paths

Attribute | Type | Description
--------- | ---- | -----------
name | str | Name

### ModeledWellPath
**Inherits WellPath**

A Well Path created interactively in ResInsight


### FileWellPath
**Inherits WellPath**

Well Paths Loaded From File


