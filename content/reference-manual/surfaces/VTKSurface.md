+++
title = "VTK Surface"

weight = 10
+++

# VTK Unstructured Grid

Individual surfaces can be imported from the VTK file format with the extension **VTU**. If the data in a surface is changing between time steps, a dictionary **PVD** file can be used. The **PVD** file contains time stamps and references to **VTU** files.

A VTK UnstructuredGrid file stores 3D mesh data with properties attached to cells or points. It's an XML file that describes the shape of your mesh and the data values on it.

Example files are located at [GitHub](https://github.com/OPM/ResInsight/tree/dev/ApplicationLibCode/UnitTests/TestData/RifVtkSurfaceImporter)

## Basic Structure

```xml
<VTKFile type="UnstructuredGrid" version="0.1" byte_order="LittleEndian">
  <UnstructuredGrid>
    <Piece NumberOfCells="24" NumberOfPoints="19">
      <!-- Data goes here -->
    </Piece>
  </UnstructuredGrid>
</VTKFile>
```

The file has one main piece with:
- **NumberOfCells**: How many cells (triangles, quads, etc.) you have
- **NumberOfPoints**: How many corner points your mesh has

## Main Sections

### 1. CellData - Properties on cells
```xml
<CellData>
  <DataArray type="Float32" Name="ReservoirCell" format="ascii">
    83769 83769 83769 ...
  </DataArray>
</CellData>
```
This stores values that belong to each cell, like:
- Cell IDs
- Permeability values  
- Temperature, pressure, etc.

### 2. Points - Where your mesh corners are
```xml
<Points>
  <DataArray type="Float32" Name="Coordinates" NumberOfComponents="3" format="ascii">
    1095 1095 2604.45 1095 1095 2603.84 ...
  </DataArray>
</Points>
```
Lists x, y, z coordinates for every point in your mesh.

### 3. Cells - How points connect together
This has three parts:

**Connectivity** - Which points make each cell:
```xml
<DataArray type="Int32" Name="connectivity" format="ascii">
  0 1 2 0 2 3 0 3 4 ...
</DataArray>
```

**Offsets** - Where each cell ends:
```xml
<DataArray type="Int32" Name="offsets" format="ascii">
  3 6 9 12 15 18 ...
</DataArray>
```

**Types** - What kind of cell each one is:
```xml
<DataArray type="UInt8" Name="types" format="ascii">
  5 5 5 5 5 5 ...
</DataArray>
```

## Cell Types
- **5** = Triangle
- **8** = Quad  
- **10** = Tetrahedron
- **12** = Hexahedron (cube)

## Data Types
- **Float32** - Regular numbers (coordinates, properties)
- **Int32** - Whole numbers (point indices)
- **UInt8** - Small positive numbers (cell types)

## VTU File Format

```xml
<?xml version="1.0"?>
<VTKFile type="UnstructuredGrid" version="0.1" byte_order="LittleEndian">
  <UnstructuredGrid>
    <Piece NumberOfCells="24" NumberOfPoints="19">
      <CellData Scalars="ReservoirCell">
        <DataArray type="Float32" Name="ReservoirCell" NumberOfComponents="1" format="ascii">
          83769 83769 83769 83769 83769 83769 70169 83769 83769 83769 83769 83769
          83769 83769 77369 77369 83769 83769 83769 83769 83769 83769 83769 70169
        </DataArray>
        <DataArray type="Float32" Name="ReservoirPerm" NumberOfComponents="1" format="ascii">
          1.2e-13 1.2e-13 1.2e-13 1.2e-13 1.2e-13 1.2e-2 1.2e-13 1.2e-13 nan nan 1.2e-13 1.2e-13
          1.2e-13 1.2e-13 1.2e-13 1.2e-13 1.2e-13 1.2e-13 1.2e-13 1.2e-13 1.2e-13 1.2e-13 1.2e-13 1.2e-13
        </DataArray>
        <DataArray type="Float32" Name="ReservoirDist" NumberOfComponents="1" format="ascii">
          10 11 12 13 14 15 16 17 17 19 20 21
          22 23 24 25 26 27 28 29 30 31 32 33
        </DataArray>
      </CellData>
      <Points>
        <DataArray type="Float32" Name="Coordinates" NumberOfComponents="3" format="ascii">
          1095 1095 2604.45 1095 1095 2603.84 1094.47 1095 2604.15 1094.47 1095 2604.76
          1095 1095 2605.06 1095.53 1095 2604.76 1095.53 1095 2604.15 1095 1095 2603.23
          1094.39 1095 2603.39 1093.94 1095 2603.84 1093.78 1095 2604.45 1093.94 1095 2605.06
          1094.39 1095 2605.51 1095 1095 2605.67 1095.61 1095 2605.51 1096.06 1095 2605.06
          1096.22 1095 2604.45 1096.06 1095 2603.84 1095.61 1095 2603.39
        </DataArray>
      </Points>
      <Cells>
        <DataArray type="Int32" Name="connectivity" NumberOfComponents="1" format="ascii">
          0 1 2 0 2 3 0 3 4 0 4 5
          0 5 6 0 6 1 1 7 8 1 8 2
          2 8 9 2 9 10 2 10 3 3 10 11
          3 11 12 3 12 4 4 12 13 4 13 14
          4 14 5 5 14 15 5 15 16 5 16 6
          6 16 17 6 17 18 6 18 1 1 18 7
        </DataArray>
        <DataArray type="Int32" Name="offsets" NumberOfComponents="1" format="ascii">
          3 6 9 12 15 18 21 24 27 30 33 36
          39 42 45 48 51 54 57 60 63 66 69 72
        </DataArray>
        <DataArray type="UInt8" Name="types" NumberOfComponents="1" format="ascii">
          5 5 5 5 5 5 5 5 5 5 5 5
          5 5 5 5 5 5 5 5 5 5 5 5
        </DataArray>
      </Cells>
    </Piece>
  </UnstructuredGrid>
</VTKFile>
```

## PVD File Format

```xml
<?xml version="1.0"?>
<VTKFile type="Collection"
         version="0.1"
         byte_order="LittleEndian"
         compressor="vtkZLibDataCompressor">
 <Collection>
   <DataSet timestep="1234567.123" file="fracture-00000.vtu"/>
   <DataSet timestep="7654321.765" file="fracture-00001.vtu"/>
 </Collection>
</VTKFile>
```
