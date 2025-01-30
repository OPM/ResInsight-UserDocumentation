+++
title = "Seismic Data"

weight = 12
+++

![](/images/import/SeismicHeaderImage.png)

## Importing Seismic Data 
ResInsight supports the following seismic file formats:

- **SEGY**: file format developed by the **Society of Exploration Geophysicists** for storing geophysical data
- **VDS**: file format for fast random access to multi-dimensional volumetric data as supported by **OSDU OpenVDS**
- **ZGY**: file format for fast random access to multi-dimensional volumetric data as supported by **OSDU OpenZGY**

A seismic file is imported by right-clicking the **Seismic** item in **Project Tree** or by using menu item **File->Import->Import Seismic**. 

![](/images/import/SeismicImport.png)

To look at seismic data, create a [Seismic View]({{% relref "seismicview" %}}). Combined display of both grid model geometry and seismid data is  described in [Seismic Sections]({{% relref "seismicsections" %}}).

## Difference Cube
The difference between two seismic cubes can be created using the following workflow:
- Select two seismic cubes with identical geometry (same count of **XLines** and **Inlines** located at identical geometrical locations)
- From the right-click menu select "Create Seismic Difference"
- A new seismic data source is created, and data can be mapped onto seismic intersections

![](/images/import/SeismicCreateDifference.png)


## Property Editor
The Property Editor for seismic data lists the available properties:
- **General**: Name and file for fast random access
- **Color Mapping**: 
  - **Colors**: [Color Legend]({{% relref "colorlegends" %}}) applicable to all [Seismic Sections]({{% relref "seismicsections" %}}) using this data set 
  - **Override Data Range**: option to override data range by specifying clip value, c.f. below
- **File Information**: key information such as ranges and data channels 

![](/images/import/SeismicPropertyEditor.png)

To improve visualization of seismic data, the data range can be overridden by checking **Override Data Range** and specify **Clip Value**.

![](/images/import/SeismicOverrideDataRange.png)

The **Seismic Histogram** may provide valuable information for deciding how to map the data values to colors.
- **Clip Value**: Defines the maximum and minimum value for color legend
- **Mute Value**: All values below the specified threshold is set to zero

![](/images/import/SeismicHistogram.png)


## Conversion of SEGY files for fast random access
ResInsight converts SEG-Y files to VDS to obtain fast random access.
Selecting a SEG-Y file (`*.sgy`, `*.segy`) thus triggers the **Convert SEG-Y to VDS file format** dialog shown below.

![](/images/import/SeismicConvertSEGYtoVDS.png)

The options for conversion of SEG-Y files are:

- **Input/Output files**: specifying path and file name of input SEG-Y and output VDS file
- **Convert Options**: 
  - *Depth (Z) Unit*: specifying unit of depth for display purposes (no conversion performed)
  - *Depth (Z) Offset Override*: correction of incorrect or missing depth offset on file 
  - *Header Definition File*: optional file specifying [OpenVDS SEG-Y Import Options](https://osdu.pages.opengroup.org/platform/domain-data-mgmt-services/seismic/open-vds/tools/SEGYImport/README.html).
  
Subsequent to SEG-Y conversion, please check resulting key information for correctness by inspecting **File Information** of the [**Property Editor**]({{% relref "seismicdata" %}}#property-editor), notably *Inline*, *Xline*, and *Z* ranges.
In case of discrepancy, the conversion of SEG-Y file has to be performed anew by specifying **Depth (Z) Offset Override** or specifying a JSON file as described in the documentation of the [OpenVDS SEG-Y Import Tool](https://osdu.pages.opengroup.org/platform/domain-data-mgmt-services/seismic/open-vds/tools/SEGYImport/README.html).

![](/images/import/SeismicOpenVDSdoc_snip.png)

A further option is to run the [OpenVDS SEG-Y Import Tool](https://osdu.pages.opengroup.org/platform/domain-data-mgmt-services/seismic/open-vds/tools/SEGYImport/README.html) from command line as the OpenVDS *SEGYImport* tool is part of your ResInsight intallation.






