+++
title = "Eclipse Summary Data"
published = true
weight = 10
+++
 
Summary data can be imported as a single summary file or an ensemble of summary files.

## Basic Summary Import
Summary data is located in two files, summary vector names in **\*.SMSPEC** and curve data in **\*.UNSMRY**.  

For import of ensemble datasets, see [Ensemble File Dialog]({{< relref "ensemblefiledialog" >}}).

## Origin Files
![]({{< relref "" >}}images/plot-window/OriginFileDialog.png)

During summary file import, ResInsight checks whether the summary file is restarted, i.e. has an origin file. If an origin file is found, the Origin Files dialog is displayed.

Depending on what triggered the summary file import, the dialog shows slightly different information. If the summary file import was triggered by a grid file import, the dialog displays information about grid files in addition to the summary origin file(s). If the summary file was imported directly, information about grid files are not relevant and thus not displayed.

The dialog contents are organized in groups:

- **Current Grid and Summary Files** or **Current Summary Files**: This group displays the name of the main summary file to import. If the import is triggered by a grid file import, the name of the grid file is also displayed.
- **Origin Summary Files**: This group displays the names of the origin summary file(s) found. If there are more than one file listed, it means that the found origin file also has an origin file. ResInsight will search the "chain" of summary origin files until it reaches the end.
  - **Import Options** There are three options to control how origin summary file are imported
    - **Unified**: The main summary files and all origin files are imported into one single summary case
    - **Separate Cases**: The main files and all origin files are imported into separate summary cases
    - **Skip**: Only the main summary file is imported. The origin summary files are skipped.
- **Origin Grid Files**: If the summary file import was triggered by a grid file import, this group is visible. It contains a list of the grid files associated to the origin summary files
  - **Import Options** There are two options to control how the grid files are imported
    - **Separate Cases**: All "origin" grid files are imported into separate grid cases
    - **Skip**: Only the main grid file is imported. The "origin" grid files are skipped.

By default the file names are displayed using relative path based on the common root folder for all files. In order to display the full path, check the **Show full paths** checkbox. Regardless of the checkbox state, there is always a tooltip showing the full path for every file. It is also possible to copy a full path file name to the clipboard. Right click on the file name and select **Copy file name**.

If the user selected multiple summary files or grid files, this dialog will be displayed for every file that has an origin summary file. In this case the button **OK to All** appears. When this button is clicked, the rest of the files will be imported silently using the same options.

## Summary Data File Formats

**ResInsight** is able to import summary data in three file formats. Default exported by *Eclipse* is **\*.SMSPEC/.UNSMRY**. In addition, *Eclipse* can export into **\*.h5** for improved performance.

For best performance, **ResInsight** has support for **\*.ESMRY** file format. **ResInsight** is able to produce this file format based on **\*.SMSPEC/UNSMRY** files.

See configuration in [Eclipse Summary Preferences]({{< relref "preferences#eclipse-summary" >}}).

### SMSPEC/UNSMRY File Format

*Eclipse* will by default export summary data to **\*.SMSPEC** and **\*.UNSMRY**. Data is organized by simulation time step and extraction of data for one summary vector can be time consuming for large data sets.

### ESMRY File Format

**\*.ESMRY** files contains the same data as **SMSPEC/UNSMRY**. The data in these files are organized in a different way that will give significantly better performance when accessing single summary vectors compared to **SMSPEC/UNSMRY**.

**ResInsight** will by default use this file format.

### h5 File Format

*Eclipse* is able to produce summary data in a file format with the extension **\*.H5** with the same content as **\*.UNSMRY**.
