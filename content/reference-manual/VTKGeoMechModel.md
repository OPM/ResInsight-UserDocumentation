+++
title = "VTK Geomechanical Model"

weight = 20
+++

# VTK Unstructured Grid

A geomechanical simulation model can be imported from the VTK file format, see [Geomechanical Data]({{% relref "GeomechanicalData" %}}#import-from-vtk-files) for the import procedure. The model geometry and results are stored in **VTU** unstructured-grid files. When the model has more than one time step, a **PVD** collection file references one **VTU** file per time step.

A VTK UnstructuredGrid file is an XML file that stores the 3D mesh and the result values attached to its points and cells. For a geomechanical model the cells are hexahedral (HEX8) elements.

Example files are located at [GitHub](https://github.com/OPM/ResInsight/tree/dev/ApplicationLibCode/UnitTests/TestData/RifVtkReader).

## Basic Structure

```xml
<VTKFile type="UnstructuredGrid" version="0.1" byte_order="LittleEndian">
  <UnstructuredGrid>
    <Piece NumberOfCells="2" NumberOfPoints="12">
      <!-- Data goes here -->
    </Piece>
  </UnstructuredGrid>
</VTKFile>
```

The file has one main piece with:
- **NumberOfCells**: the number of elements in the model
- **NumberOfPoints**: the number of nodes (corner points)

## Main Sections

### 1. PointData - Results on nodes
```xml
<PointData>
  <DataArray type="Float32" Name="disp" NumberOfComponents="3" format="ascii">
    0 0 0  0 0 0  0 0 0
    ...
  </DataArray>
</PointData>
```
Stores result values that belong to each node. The **disp** array holds the nodal displacement vector (three components per node) used for deformation visualization.

### 2. CellData - Results on cells
```xml
<CellData>
  <DataArray type="Float32" Name="Stress" NumberOfComponents="1" format="ascii">
    100.0 200.0
  </DataArray>
</CellData>
```
Stores result values that belong to each element, such as stress and strain.

### 3. Points - Where the nodes are
```xml
<Points>
  <DataArray type="Float32" Name="Coordinates" NumberOfComponents="3" format="ascii">
    0 0 0  1 0 0  2 0 0
    ...
  </DataArray>
</Points>
```
Lists the x, y, z coordinates for every node in the mesh.

### 4. Cells - How nodes connect together
This has three parts.

**Connectivity** - the nodes that make up each element (eight per hexahedron):
```xml
<DataArray type="Int32" Name="connectivity" format="ascii">
  0 1 4 3 6 7 10 9
  1 2 5 4 7 8 11 10
</DataArray>
```

**Offsets** - where each element ends in the connectivity list:
```xml
<DataArray type="Int32" Name="offsets" format="ascii">
  8 16
</DataArray>
```

**Types** - the cell type of each element:
```xml
<DataArray type="UInt8" Name="types" format="ascii">
  12 12
</DataArray>
```

## Cell Types
Geomechanical models use cell type **12** - the hexahedron (HEX8).

## Data Types
- **Float32** - Regular numbers (coordinates, results)
- **Int32** - Whole numbers (node indices)
- **UInt8** - Small positive numbers (cell types)

## VTU File Format

```xml
<?xml version="1.0"?>
<VTKFile type="UnstructuredGrid" version="0.1" byte_order="LittleEndian">
  <UnstructuredGrid>
    <Piece NumberOfCells="2" NumberOfPoints="12">
      <PointData>
        <DataArray type="Float32" Name="disp" NumberOfComponents="3" format="ascii">
          0 0 0  0 0 0  0 0 0
          0 0 0  0 0 0  0 0 0
          0 0 0  0 0 0  0 0 0
          0 0 0  0 0 0  0 0 0
        </DataArray>
      </PointData>
      <CellData>
        <DataArray type="Float32" Name="Stress" NumberOfComponents="1" format="ascii">
          100.0 200.0
        </DataArray>
      </CellData>
      <Points>
        <DataArray type="Float32" Name="Coordinates" NumberOfComponents="3" format="ascii">
          0 0 0  1 0 0  2 0 0
          0 1 0  1 1 0  2 1 0
          0 0 1  1 0 1  2 0 1
          0 1 1  1 1 1  2 1 1
        </DataArray>
      </Points>
      <Cells>
        <DataArray type="Int32" Name="connectivity" NumberOfComponents="1" format="ascii">
          0 1 4 3 6 7 10 9
          1 2 5 4 7 8 11 10
        </DataArray>
        <DataArray type="Int32" Name="offsets" NumberOfComponents="1" format="ascii">
          8 16
        </DataArray>
        <DataArray type="UInt8" Name="types" NumberOfComponents="1" format="ascii">
          12 12
        </DataArray>
      </Cells>
    </Piece>
  </UnstructuredGrid>
</VTKFile>
```

## PVD File Format

```xml
<?xml version="1.0"?>
<VTKFile type="Collection" version="0.1" byte_order="LittleEndian">
  <Collection>
    <DataSet timestep="1.0" file="model-00000.vtu"/>
    <DataSet timestep="2.0" file="model-00001.vtu"/>
  </Collection>
</VTKFile>
```
