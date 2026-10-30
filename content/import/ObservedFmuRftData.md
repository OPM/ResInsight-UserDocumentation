+++
title = "Observed FMU RFT Data"

weight = 30
+++

Observed RFT data from an FMU run can be imported and displayed in an [Ensemble RFT Plot]({{% relref "EnsembleRftPlot" %}}).

## Import

Right-click **Observed Data** in the **Plot Project Tree** and select **Import Observed FMU Data**. Then select a folder. Observed FMU data is imported from the folder and its subfolders.

![](/images/plot-window/EnsembleRftImportObservedData.png)

The folder is expected to contain the following files:

- _`well_date_rft.txt`_ -- well measurement dates
- _`<well_name>.obs`_ -- observed pressure and error
- _`<well_name>.txt`_ -- position and reservoir zone of each observation
- _`layer_zone_table.txt`_ -- correlation of grid k-layers and formations

{{% notice note %}}
  The data file _`well_date_rft.txt`_ is required. If missing, no Observed FMU data will be imported.
{{% /notice %}}

## File Formats

### Correlation of Grid and Formations

The file _`layer_zone_table.txt`_ can be used to correlate each grid k-layer with a formation name.
This file is identical for all cases in the same ensemble. See [FMU Layer Zone Table]({{% relref "FormationImport" %}}#fmu-layer-zone-table-layer_zone_tabletxt) for the file format.

### Observed Pressure and Error
For a given well name, the file _`<well_name>.obs`_ is a data file containing two columns to specify observed pressure and error.
Column one contains observed pressure and column two contains error. The observation data is valid for one and only one layer/formation.

Example file for well *OP_1*, i.e. _`OP_1.obs`_:
```txt
303.000   3.000
304.000   3.000
305.000   3.000
```

### Multiple Observations for a Well
If there are multiple observations for a well at different dates, the naming of the files include a measurement ID.

Example file _`well_date_rft.txt`_:
```txt
R_A2 2018-03-01 1
R_A2 2019-03-01 2
```

Measurement ID is the last column. The corresponding observations files are named as follows, the measurement ID is appended to the well name.
```txt
R_A2_1.obs
R_A2_1.txt
R_A2_2.obs
R_A2_2.txt
```

### Reservoir Zone Name
For a given well name, the file _`<well_name>.txt`_ is a data file containing five columns that specify its correlation with reservoir zones.
Each line of data must contain:

- Utmx: x-coordinate in UTM
- Utmy: y-coordinate in UTM
- Measured Depth relative to the Kelly Bushing (MDRKB)
- True Vertical Depth referenced to Mean Sea Level (TVDMSL)
- Reservoir zone name

Example file for well *OP_1*, i.e. _`OP_1.txt`_:
```txt
461288.719   5933415.000   1816.200   1611.692   UpperReek
461288.685   5933415.027   1824.560   1620.052   MidReek
461288.683   5933415.029   1840.000   1635.492   LowerReek
```

### Well Measurements - Date Format 1
The data file _`well_date_rft.txt`_ contains well measurements. The file contains five columns for each well measurement:

- Well Name
- Date in two digit form \<DD>
- Month in two digit form \<MM>
- Year in four digit form \<YYYY>
- Measurement index

There can be multiple measurement for each well.

Example file _`well_date_rft.txt`_:
```txt
OP_1   01 02 2000   1
OP_2   01 02 2000   1
OP_4   01 01 2001   1
WI_1   01 02 2000   1
WI_3   01 03 2001   1
```

### Well Measurements - Date Format 2
The data file _`well_date_rft.txt`_ contains well measurements. The file contains three columns for each well measurement:

- Well Name
- Date on the format \<YYYY-MM-DD>
- Measurement index

There can be multiple measurement for each well.

Example file _`well_date_rft.txt`_:
```txt
R_A2 2018-03-01 1
R_A2 2019-03-01 2
R_A6 2018-11-07 1
R_A6 2018-11-07 2
R_A6 2018-11-07 3
```
