+++
title = "Formations and Well Picks"

weight = 30
+++

ResInsight imports two kinds of formation data:

- **Formations for k-layers** -- formation names for ranges of grid k-layers. Used for cell results, property filters and plot annotations. See [Zonations/Formations]({{% relref "formations" %}}).
- **Well picks** -- formation tops and bases along a well, given as measured depth. Used to annotate well log, RFT and PLT plots, and to filter RFT correlation plots.

## Formations for K-layers

Formation files are imported by using the command: **File->Import->Import Formations**.

Supported formation files are:

- Formation Names description files (_`*.lyr`_)
- FMU Zone Ranges (_`zonation_ecl_map.yml`_ or _`zonation_ecl_map.yaml`_)
- FMU Layer Zone Table (_`layer_zone_table.txt`_)

To select the appropriate file type, use the button to the right of file name in the *Import Formations* dialog.
The imported files are listed in the **Project Tree** in a folder named **Formations**. See [Select the Formation File in a Case]({{% relref "formations" %}}#select-the-formation-file-in-a-case) for how to assign a formation file to a case.

### Formation Names Description Files (_`*.lyr`_)
Formation Names description files (_`*.lyr`_) consist of a list of entries containing formation name, k-range, and *optionally* a formation color.
Formation color can be given as a World Wide Web Consortium [SVG color keyword name](https://www.w3.org/TR/SVG11/types.html#ColorKeywords)
or a six-digit, three-byte hexadecimal number used in HTML, CSS, SVG, and other computing applications to represent the red, green and
blue components of the color, c.f. example below:

```txt
-- Any text as comment
'My First  Formation Name'                             4 - 12   red
'My Second Formation Name'                            15 - 17   green
'Formation spanning 3 k-layers, i.e. 18,19 and 20'       3      blue
'Last Formation Name'                                 21 - 21   #FFFF00
```

### FMU Zone Ranges (_`zonation_ecl_map.yml`_)
The FMU Zone Ranges file defines a one-based k-layer range for each zone in a `zranges` section. Both the _`.yml`_ and _`.yaml`_ file extensions are supported. Below is an example of a _`zonation_ecl_map.yml`_ file:

```yaml
zranges:
  - Valysar: [1, 20]
  - Therys: [21, 54]
  - Volon: [55, 69]
```

Only files named _`zonation_ecl_map`_ are read as zone ranges. Other yaml files are ignored.

### FMU Layer Zone Table (_`layer_zone_table.txt`_)
The FMU Layer Zone Table (_`layer_zone_table.txt`_) contains two columns to correlate each grid k-layer with a formation name.
Below is an example of a _`layer_zone_table.txt`_ file:

```txt
1   UpperReek
2   UpperReek
3   UpperReek
4   UpperReek
5   UpperReek
6   MidReek
7   MidReek
8   MidReek
9   MidReek
10  MidReek
11  LowerReek
12  LowerReek
13  LowerReek
14  LowerReek
```

### Zone Colors from _`stratigraphy.json`_
When an FMU Zone Ranges file or an FMU Layer Zone Table is imported, ResInsight looks for a _`stratigraphy.json`_ file in the same folder and uses it to color the zones. A zone name is matched against the subzone names first; the color of a parent zone is used only when no subzone has the same name. If the file is missing or invalid, the zones are imported with default colors and a warning is written to the log.

```json
[
    {
        "name": "TopVolantis_BaseVolantis",
        "color": "#6EA35A",
        "subzones": [
            { "name": "Valysar", "color": "#6EA35A" },
            { "name": "Therys",  "color": "#EDAF4C" },
            { "name": "Volon",   "color": "#CA413D" }
        ]
    }
]
```

In a typical FMU setup, these files are located in _`rms/output/zone/`_ of each realization.

### Automatic Import for Grid Case Ensembles
When a grid case ensemble is created, or a project containing one is opened, ResInsight automatically imports the formations for each realization. The search starts in the folder of the grid file and checks these folders in order:

1. _`../../rms/output/zone/`_
2. _`../../`_

The first folder that contains a supported formation file is used. If a folder contains several supported files, the file type with the highest priority is imported:

1. Formation Names description file (_`*.lyr`_) -- may also contain formation colors
2. FMU Zone Ranges (_`zonation_ecl_map.yml`_ or _`zonation_ecl_map.yaml`_) -- colors from _`stratigraphy.json`_
3. FMU Layer Zone Table (_`layer_zone_table.txt`_) -- colors from _`stratigraphy.json`_

If more than one file of the same type is found, the first one is used and a warning is written to the log.

The formations can be used in data filters for ensemble contour maps. See [Ensemble Contour Maps]({{% relref "EnsembleContourMap" %}}#data-filter).

### Reload of Formation Data
If a formation file is modified outside ResInsight, the formation data can be imported again by the right-click menu **Formations->Reload**. This command will import formations for the selected formation files.

## Well Picks

Two well pick formats are supported. Both give the top and base of each formation in a well as measured depth.

### Well Pick Files for Well Paths

Well Pick files are imported by using the command: **File->Import->Well Data->Import Well Picks**.
The user is asked to select _`*.csv`_ files for import.

The imported Well Pick files will be added to their associated well path, if a match on well name can be found. If not, new paths will be created, and they can all be found in **Wells** in the **Project Tree**. The file path of the formations can be found in a well path's **Property Editor**.

![](/images/3d-main-window/wellPathFormationsInPropertyEditor.PNG)

A Well Pick file is a csv-file, which uses semicolon to separate entries in a table. Below is an example of such a file:

```
Well name; Column name; Unit name; Top MD; Base MD
B-3H; FLUID; GAS;2203.2;2317.4
B-3H; FLUID; OIL;2317.4;2459
B-3H; STRAT; FANGST GP. ;2203.399902;2223.350098
B-3H; STRAT;   Ile Fm. ;2203.399902;2223.350098
B-3H; STRAT;     Ile Fm. 3 ;2203.401123;2219.26001
B-3H; STRAT;     Ile Fm. 2 ;2219.26001;2222.399902
B-3H; STRAT;       Ile Fm. 2.2 ;2219.26;2219.350098
B-3H; STRAT;       Ile Fm. 2.1 ;2219.350098;2222.399902
B-3H; STRAT;     Ile Fm. 1 ;2222.399902;2223.350098
B-3H; STRAT; BAAT GP. ;2223.350098;2979.28125
B-3H; STRAT;   Ror Fm. ;2223.350098;2285.199951
B-3H; STRAT;     Ror Fm. 2 ;2223.350098;2246
B-3H; STRAT;     Ror Fm. 1 ;2246;2285.199951
B-2H; FLUID; GAS;2144.4;2338.5
B-2H; FLUID; OIL;2338.5;2440
B-2H; STRAT; FANGST GP. ;2144.199951;2158.389893
B-2H; STRAT;   Ile Fm. ;2144.199951;2158.389893
B-2H; STRAT;     Ile Fm. 2 ;2144.201416;2156.197266
B-2H; STRAT;     Ile Fm. 1 ;2156.197266;2158.38501
```

The file must have the columns "Well name", "Unit name" (i.e. formation name), "Top MD" and "Base MD" (i.e. measured depth) to be regarded as a Well Pick file. They can be listed in any order, and all other columns will be ignored.

The three unit names *OIL*, *GAS* and *WATER* are interpreted as *fluids*. Other unit names with only capital letters are *groups*. A unit name without an index is simply a *formation*. Unit names with one number is a *formation 1*, unit names with *one* punctuation is a *formation 2*, two punctuations, *formation 3* and so on. Indentions in column name will be ignored.

See [Well Picks]({{% relref "formations" %}}#well-picks) for how to show the well picks in plots.

### FMU Well Formations (_`formations.csv`_)

FMU well formation files are not tied to a well path, and can be used for wells without a trajectory, for example in RFT plots. To import a file, right-click **Well Picks (Formations)** under **Data Sources** in the **Plot Project Tree** and select **Import Well Formations...**. Selecting an imported file shows its content as a table in the **Property Editor**.

The file is comma separated, with one row for each zone in a well:

```
X_UTME,Y_UTMN,TOP_TVD,TOP_MD,ZONE_CODE,WELL,BASE_TVD,BASE_MD,ZONE
460994.9,5933813.29,1644.0,1693.0,1,R_A2,1662.0,1711.0,Valysar
460994.9,5933813.29,1662.0,1711.0,2,R_A2,1678.0,1727.0,Therys
```

The columns **WELL**, **ZONE**, **TOP_MD**, **BASE_MD**, **TOP_TVD** and **BASE_TVD** are used. Other columns are ignored.

In well log tracks, select **Well Picks (no trajectory)** as **Zonation/Formation Names** source, then select the **Formations File** and the **Well**. The **Add Well Picks** button imports a file and selects it in one step. RFT plots select this source automatically when the well has no well path and a matching well formations file is found. See [RFT Correlation Plot]({{% relref "RftCorrelationPlot" %}}#well-formations).
