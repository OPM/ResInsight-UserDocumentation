+++
title = "PTL Surface"

weight = 10
+++

### Petrel Surface PTL files

ResInsight is capable of importing a surface defined by a **PTL** (*.ptl) file format.
A PTL data file specifies the quads of a surface by *x*, *y*, *z* nodal coordinates and the *i* and *j* indices as exemplified below. 
As seen, *#* denotes comment lines.

```txt
#Type: scattered data
#Version: 6
#Description: No description
#Format: free
#Field: 1 x
#Field: 2 y
#Field: 3 z meters
#Field: 4 column
#Field: 5 row
#Projection: Local Rectangular
#Units: meters
#End: 
#Information from grid
#Grid_size: Not_avaiable
#Grid_space: Not_available
#Z_field: z
#Vertical_faults: Not_available
#History: No history
#Z_units: meters
443479.500000 7305390.500000 -1000.000000 1 1
443479.500000 7305488.500000 -1000.000000 1 2
443479.500000 7305586.500000 -1000.000000 1 3
443479.500000 7305684.500000 -1000.000000 1 4
443479.500000 7305782.500000 -1000.000000 1 5
443479.500000 7305880.500000 -1000.000000 1 6
...
```
