+++
title = "Eclipse Summary Data"
published = true
weight = 10
+++
 
Summary data can be imported as a single summary file or an ensemble of summary files.

### Basic Summary Import
Summary data is located in two files, summary vector names in **\*.SMSPEC** and curve data in **\*.UNSMRY**.  



## Ensemble File Import
When using the standard file selection dialog, the user is limited to select files in one directory only. If the interesting files are distributed over multiple directories, the dialog has to be opened once for each directory. The recursive file selection dialog is created to circumvent this limitation. This dialog is able to search a directory tree for files matching a specified pattern.

{{% notice note %}}
This dialog is used for import of different file types like *.EGRID and *.SMSPEC.
{{% /notice %}}

![]({{< relref "" >}}images/plot-window/RecursiveImportDialog2.png)

The dialog consists of the following fields:

- **Path Pattern**: The path filter uses normal wildcard file globbing, like in any unix shell. When the filter ends with a single "**" (eg. "/home/*"), however, ResInsight will search recursively in all subdirectories from that point. This is indicated by "..." in the **Effective Filter** label below.
  - **\*** Matches any number of any characters except the path separator
  - **?** Matches one character exception the directory separator
  - **[abc]** Matches one of the specified characters. Ex. a, b or c
- **File Pattern**: The search pattern that applies to the file name.
- **Effective Filter**: The effective filter displays the resulting full path search pattern. It is updated on the fly as the user edits the pattern fields. A text string of "..." indicates a complete recursive directory search.

After pressing the **Find** button, a file search is performed in the root directory and the directories below matching the path pattern. The files found are presented in a list, where the user can check/uncheck each file individually.

When the **OK** button is pressed, all checked files are imported.

### Origin Files
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

### Summary Data File Formats

**h5 File Format**

*Eclipse* is able to reorganize the summary data after a simulations has completed. This will produce an additional curve data file with the extension **h5**. The curve data in this file is identical to curve data in **UNSMRY**.

ResInsight will now by default use **H5** files to import summary data, as this format has good performance for large datasets. The native *Eclipse* **UNSMRY** reader can be used when configured in [Eclipse Summary Preferences]({{< relref "preferences#eclipse-summary" >}}).


