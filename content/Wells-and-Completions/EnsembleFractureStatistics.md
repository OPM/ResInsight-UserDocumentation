+++
title = "Ensemble Fracture Statistics"
published = true
weight = 50
+++


## Importing Ensemble Fracture Statistics

Right-click on **Completion Templates > Ensemble Fracture Statistics** in the **Project Tree** and select the **Import StimPlan Fracture Recursively** option. Then select the StimPlan fracture Xml files to be part of the ensemble.

After importing the **Property Panel** of the **Ensemble Fracture Statistics** item has these options:

- **Name** -- Name of the ensemble fracture statistics.
- **Exclude Zero Width Fractures** -- Toggle to remove zero width fractures from the statistics.
- **Mesh Alignment** -- Specifies how to align the mesh.
  - **Mesh Depth** -- Use the raw mesh depths from file without adjustment.
  - **Perforation Depth** -- Adjusts the mesh location to have the perforation at the same location when computing the statistics.
- **Mesh Type** -- Specifies the meshing strategy. See details below.
- **Statistics Type** -- The statistics to compute.


## Mesh Types

The imported StimPlan fractures are stacked on top of each, and a statistics mesh is created. The statistics mesh covers the extents of
all the individual meshes in the ensemble.


### Adaptive Mesh

The adaptive mesh tries to optimize the horizontal depth spacing to have coarse sampling where the
source meshes are coarse, and fine sampling where necessary. This is achieved by grouping the layer thicknesses of 
the individual meshes into fixed bins, and then scaling the vertical size of each layer according to their mean size.

- **Mean Type** -- The mean calculation used to scale the layer thickness.
  - **Harmonic** -- See [Harmonic mean](https://en.wikipedia.org/wiki/Harmonic_mean) for details.
  - **Arithmetic** -- Average. See [Arithmetic Mean](https://en.wikipedia.org/wiki/Arithmetic_mean) for details.
  - **Geometric** -- See [Geometric Mean](https://en.wikipedia.org/wiki/Geometric_mean) for details.
  - **Minimum** -- Use the minimum thickness. 
- **Number of Layers** -- Specifies the number of layers to create.
  - **Average** -- Use the average number of layers of the individual fractures of the ensemble.
  - **Minimum** -- Use the minimum number of layers of the individual fractures of the ensemble.
  - **Maximum** -- Use the maximum number of layers of the individual fractures of the ensemble.
  - **User-Defined** -- The user specifies the number of layers.

The mesh is evenly spaced in the lateral direction using the maximum number of cells in the individual fractures of the ensemble.


### Uniform Mesh

The uniform mesh has cells of a equal size. The minimum and maximum extents of all the meshes in both directions is found, and the interval is divided into equal cells.

- **X** -- The number of cells in lateral direction.
- **Y** -- The number of cells in depth direction.


### Naive Mesh

The naive method produces a mesh where every depth in all the individual fractures of the ensemble is present. 

The mesh is evenly spaced in the lateral direction using the maximum number of cells in the individual fractures of the ensemble.



## Statistics Mesh Computation

The statistics mesh samples each individual fracture of the ensemble in each cell center. The value of the cell containing the
statistics mesh cell center is used. Invalid values or empty cells are ignored. The values at each cell center are gathered, and
the chosen statistics (e.g. P10 and Mean) is computed per cell.

The statistics meshes are written to file in a StimPlan compatible XML file, and is imported into **Fracture Templates** in the 
**Project Tree**.



## Statistics Table

The statistics table contains overall statistics on key properties of the fractures.

- **Height** -- Longest aggregate height of conductive cells.
- **Area** -- Area of the conductive cells of the fracture.
- **Width** -- Width of conductive cells weighted by their area.
- **Halflength (Xf)** -- Length of the fracture is area divided by height. Xf is half of the length.
- **Conductivity (KfWf)** -- Conductivity weighted by area.
- **Permeability** -- Permeability (i.e. conductivity divided by width) weighted by area.
- **Formation Dip** -- Formation dip as reported in the Xml file.
