+++
title = "Log ASCII Standard File"

weight = 15
+++

![]({{< relref "" >}}images/3d-main-window/3dWellLogCurves.png)

Log ASCII Standard (LAS) is a standard file format common in the oil-and-gas industry to store well log information. 

## Importing a LAS file

Log ASCII Standard (LAS) files can be imported using the command: **File->Import-> Well Data->Import Well Logs from File**.

ResInsight will look for the the well name in the imported LAS-files among the existing **Well Paths**.
If a match is found, the LAS-file is placed as a child of that well path. If not, a new empty well path entry is created with the imported LAS-file under it. A well path may have more than one LAS-files as children.

![]({{< relref "" >}}images/3d-main-window/LasFilesInTree.png)

If the LAS-file does not contain a well name, the file name is used instead. 

### Moving a LAS file
If ResInsight's automatic well matching fails and a LAS-file is matched with the wrong well path, it is possible to move the LAS-file to the correct well path. Select the LAS-file right-click menu click **Move LAS File to Well Path** and select destination well path.

![]({{< relref "" >}}images/3d-main-window/MoveLasFileMenu.png)


### Look for an Existing Well Path
Well names may vary slightly among different files from the same well. When importing a well log file, ResInsight have to look for an existing well path item to ensure that the well log data and well path are imported to the correct well path item. The lookup is based on name comparison this way:

- First remove any prefix (like `xxxxx1111/1111-` or `xxxxx1111/1111_`)
- Then try an exact name match
- If not found, try to match the names ignoring all spaces, dashes and underscores
- If still no match, no existing well was found and a new one is created


## Supported Date Formats

During LAS import, ResInsight parses a date on file according to the following expressions. Supported separators between day, month, and year are **space**, **underscore**, **hyphen**, and **dot**.

| Expression | Description |
|--------------|-------------|
| d    | day as number without a leading zero (1 to 31), e.g. *7*  |
| dd   | day as a two digit number (01 to 31), e.g. *07*   |
| M    | month as number without a leading zero (1-12), e.g. *8*  |
| MM   | month as a two digit number (01-12), e.g. *08*    |
| MMM  | short month name in uppercase or lowercase ('Jan' to 'Dec'), e.g. *AUG* |
| yy   | year as a two digit number (00-99), e.g. *19*     |
| yyyy | year as a four digit number, e.g. *2019*          |

Examples of supported date expressions are listed in the following table.

| Expression  | Example |
|-------------|-------------|
| yyyy MM dd  | 2019 08 16  |
| yyyy-MM-dd  | 2019-08-16  |
| yyyy MMM dd | 2019 Aug 16 |
| MMM dd yyyy | Aug 16 2019 |
| d.M.yy      | 1.8.89      |
| dd_MM_yyyy  | 16_08_2019  |
| dd.MMM.yyyy | 16.Aug.2019 |   



