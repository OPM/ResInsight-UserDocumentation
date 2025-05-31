+++
title = "GOCAD Surface"

weight = 10
+++

## GOCAD Surface format

GOCAD is a computer application that allows you to import, create, modify, integrate, view, and export geological objects in 3D.
The GOCAD export file format supported by ResInsight is **TSURF** (*.ts). 
A TSURF data file is a triangle based surface format containing vertex coordinates and triangle to vertex connectivities as exemplified below. 
ResInsight import vertex and triangle identifiers from the first TFACE section in such a file.

```txt
GOCAD TSurf 1 
HEADER { 
name:MF_027_SU 
} 
GOCAD_ORIGINAL_COORDINATE_SYSTEM 
NAME Default 
AXIS_NAME "X" "Y" "Z" 
AXIS_UNIT "m" "m" "m" 
ZPOSITIVE Depth 
END_ORIGINAL_COORDINATE_SYSTEM 
TFACE 
VRTX 1 458177.767090 7322538.712891 1643.655884 CNXYZ 
VRTX 2 458260.834961 7322392.890625 1596.685303 CNXYZ 
VRTX 3 457985.662109 7322783.783203 1542.060059 CNXYZ 
VRTX 4 459601.453125 7322511.427734 3639.000000 CNXYZ 
VRTX 5 459422.015625 7322689.230469 3639.000000 CNXYZ 
VRTX 6 459793.410156 7322338.230469 3639.000000 CNXYZ 
...
TRGL 2 61 98  
TRGL 20 153 66  
TRGL 152 19 65  
END 
```
