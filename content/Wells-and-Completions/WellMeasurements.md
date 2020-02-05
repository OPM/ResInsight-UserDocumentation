+++
title = "Well Measurements"
published = true
weight = 70
+++

![]({{< relref "" >}}images/3d-main-window/ResInsight_WellMeasurements.png)

ResInsight can import well measurements from a comma-separated values file. 

## Importing Well Measurements

The command **File -> Import -> Well Data -> Import Measurements** will read well measurements from the selected files, and create one entry for each file under the {{< image-in-text src="images/3d-main-window/WellCollection.png" >}} **Wells -> Well Measurements** item in the **Project Tree**. 


## File Format

The format is comma-separated values with one measurement per line. The following requirements have to be met:

- Each data line must contain seven values: Well Name, MD, Date, Measurement Kind, Value, Quality, and Comment.
- The values must be separated by commas.
- Lines starting with `"#"` is considered to be comment lines, and will be ignored.
- Blank lines are also ignored.

#### Example 1:

    # Example well measurements csv file.
    # This is a comment
    #
    # Well Name, MD, Date, Kind, Value, Quality, Comment
    C-3 H, 1465.18, 2001-10-13, XLOT, 1.76, 3, Good test
    C-3 H, 1865.18, 2002-10-13, XLOT, 1.91, 1, Poor test
    C-3 H, 1995.18, 2002-10-13, XLOT, 2.45, 1, Poor test
    C-3 H, 2065.18, 2002-10-13, XLOT, 2.91, 1, Poor test
    E-3 H,  634.12, 2005-10-24, DP,    0.0, 0, Wash outs
    E-3 H, 1000.12, 2005-10-24, DP,    0.0, 0, Wash outs

    
### Measurement properties

- **Well Name** -- The name of the well. ResInsight will try to associate each measurement with a well path with a matching name. The well name should be the same as imported [here]({{< relref "wellpaths" >}}).
- **MD** -- Measured depth.
- **Date** -- The date of the measurement. Expects [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Calendar_dates) extended format: `yyyy-MM-dd`, e.g. `2019-12-24`.
- **Kind** -- The type of measurement.
- **Value** -- Floating point value.
- **Quality** -- Integer describing the quality of the measurement.
- **Comment** -- Short description of the measurement.


### Reloading Well Measurements
The well measurements are copied into the ResInsight project. Each measurement is linked to the file it was imported from. The contents of the file can be reloaded by right-clicking on one of the files under **Wells -> Well Measurements** and selecting **Reload**.

{{% notice info %}}
Reloading measurements from a file will delete all the previously imported measurements from this particular file, and then reimport the current contents of the file. 
{{% /notice %}}


## Well Measurements Visualization

All the imported well measurements are available **Project Tree** under the **Well Measurements** for each 3D view.

![]({{< relref "" >}}images/3d-main-window/WellMeasurementsInTree.png)

The measurements are shown in all the 3D Views in the project as cylinders on the well path at the specified MD. Double-clicking on measurement will show details in the **Result Info** panel.


### Well Measurement Property Editor

The well measurement property editor lets the user filter which measurement to show based on quality, value and measurement kind. The value of the measurement is used to determine the color, and this changed in the **Color Legend**.

![]({{< relref "" >}}images/3d-main-window/WellMeasurementsPropertyEditor.png)

- **Value Filter Settings** -- Filter measurements by value range.
- **Wells** -- Show this measurement kind for the selected wells.
- **Quality** -- Filter by measurement quality.
- **Radius Scale** -- Scale the radius of well measurement in the 3D view. Relative to the radius of the well path.

