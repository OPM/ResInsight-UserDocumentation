+++
title = "OpenWorks Surface"

weight = 10
+++

### OpenWorks XYZ Surface files

ResInsight is capable of importing a surface defined by a **XYZ** (*.dat) file from OpenWorks.
A XYZ data file specifies the quads of a surface by *x*, *y*, *z* nodal coordinates organized in a regular grid. 
As seen, *#* and *@* denotes comment lines.

```txt
@File_Version: 4
@Coordinate_Type_is: 1
@Export_Type_is: 1
@Number_of_Projects 1
@Project_Type_Name: , 3,xxx,
@Project_Unit_is: meters , xxx
#File_Version____________-> 4
#Project_Name____________-> xxx
#Project_Type____________-> 3
#Export_XY_Unit__________-> meters
#OpenWorks_Project_______-> 'xxx'
#Master_Project_______->
#Coordinate_type_________-> 1
#Number_of_points_in_hzd_-> 1
#Horizon_internal_id_____-> xxx
#Horizon_extremes_are____-> xxx,xxx
#Horizon_onset_is_Minimum_____-> 1
#Horizon_type_is_DEPTH_STRUCTURE______-> 2
#Horizon_color_is________-> 255 0 0
#Horizon_name____________-> xxx
#Horizon_attribute_______-> DEPTH_STRUCTURE
#Horizon_version_________-> UNKNOWN
#Horizon_interp_status___-> defaultStat
#Horizon_class___________-> defaultClass
#Export_Z_Unit___________-> meters
#Horizon_onset_type______-> Minimum
#Horizon_data_domain_____-> DEPTH
#Horizon_remark_size_____-> 50
Horizon from Grid on Fri Aug 14 13:42:10 CEST 2020
#End_of_Horizon_ASCII_Header_
   4.5423435e+05   7.3239079e+06   1.5970070e+03
   4.5424414e+05   7.3239157e+06   1.5970485e+03
   4.5425392e+05   7.3239234e+06   1.5970899e+03
   4.5426371e+05   7.3239312e+06   1.5971314e+03 
```
