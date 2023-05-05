+++
title = "Seismic Cases"
published = true
weight = 12
+++

![]({{< relref "" >}}images/import/SeismicHeaderImage.png)

## Importing a Seismic Case 
ResInsight supports the following seismic file formats:

- **SEGY**: file format developed by the Society of Exploration Geophysicists for storing geophysical data
- **VDS**: file format for fast random access to multi-dimensional volumetric data as supported by OSDU OpenVDS
- **ZGY**:  file format developed by Schlumberger for storing 3D data for seismic interpretation

A seismic file is imported by right-clicking the **Seismic** item in **Project Tree** or by using menu item **File->Import->Seismic Cases**. 

![]({{< relref "" >}}images/import/SeismicImport.png)

## Conversion of SEGY files for fast random access
ResInsight converts SEG-Y files to VDS to obtain fast random access.
Selecting a SEG-Y file (`*.sgy`, `*.segy`) thus triggers the **Convert SEG-Y to VDS file format** dialog shown below.

![]({{< relref "" >}}images/import/SeismicConvertSEGYtoVDS.png)

The options for conversion of SEG-Y files are:

- **Input/Output files**: specifying path and file name of input SEG-Y and output VDS file
- **Convert Options**: 
  - *Depth (Z) Unit*: specifying unit of depth
  - *Depth (Z) Offset Override*: correction of incorrect or missing depth offset on file 
  - *Header Definition File*: optional file specifying [OpenVDS SEG-Y Import Options](https://osdu.pages.opengroup.org/platform/domain-data-mgmt-services/seismic/open-vds/tools/SEGYImport/README.html).
