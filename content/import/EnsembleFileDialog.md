+++
title = "Ensemble File Dialog"

weight = 10
+++
 
## Ensemble File Import
When using the standard file selection dialog, the user is limited to select files in one directory only. If the interesting files are distributed over multiple directories, the dialog has to be opened once for each directory. The recursive file selection dialog is created to circumvent this limitation. This dialog is able to search a directory tree for files matching a specified pattern.


{{% notice note %}}
This dialog is used for import of different file types like *.EGRID, *.SMSPEC, *.TS, *.GRDECL, ...
{{% /notice %}}

![](/images/plot-window/RecursiveImportDialog2.png)

The dialog consists of the following fields:

- **Path Pattern**: The path filter uses normal wildcard file globbing, like in any unix shell. When the filter ends with a single "**" (eg. "/home/*"), however, ResInsight will search recursively in all subdirectories from that point. This is indicated by "..." in the **Effective Filter** label below.
- **File Pattern**: The search pattern that applies to the file name.
  - **\*** Matches any number of any characters except the path separator
  - **?** Matches one character exception the directory separator
  - **[abc]** Matches one of the specified characters. Ex. a, b or c
  - **\*[!D]** Exclude files ending with the character 'D' (file extension is not considered)
- **File Type**: The available file types will depend on the type of data to import. When importing summary data, there will be several items, and one with **SMSPEC**. 
- **File Extensions**: List of file extensions, ie ".EGRID .GRID". The extension text is independent to the file type defined above, e.g. _CSV_ data can be imported from a file with extension "TXT"
- Use 'realization-*' in filter : Replace the text "realization-12" with "realization-\*"
- Ensemble grouping : Group ensemble by Main folder or Sub Folder (Used by FMU workflow)
- **Effective Filter**: The effective filter displays the resulting full path search pattern. It is updated on the fly as the user edits the pattern fields. A text string of "..." indicates a complete recursive directory search.

## Ensemble File Structure
Multiple summary files defining an ensemble can be organized differently in folders. ResInsight support two different modes, Sub Folder and Main Folder.

### Sub Folder

Example folder structure 

    real-1/case-1
          /case-2
    real-2/case-1
          /case-2
    real-3/case-1
          /case-2

Using the option **Group By Sub Folder** will identify **case-1** and **case-2** as the ensemble names. This folder structure is used by the **FMU workflow**.

### Main Folder

Example folder structure

    case-1/real-1
    case-1/real-2
    case-1/real-3

    case-2/real-1
    case-2/real-2
    case-2/real-3

Using the option **Group By Main Folder** will identify **case-1** and **case-2** as the ensemble names. This folder structure is used by the **Everest workflow**.

After pressing the **Find** button, a file search is performed in the root directory and the directories below matching the path pattern. The files found are presented in a list, where the user can check/uncheck each file individually.

When the **OK** button is pressed, all checked files are imported.


## Examples of Use of Ensemble Import Dialog

[Ensemble Surface]({{< relref "ensemblesurface" >}})

[Ensemble Summary]({{< relref "ensembleplotting" >}})
