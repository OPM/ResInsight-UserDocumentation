+++
title = "Pressure/Depth Data"

weight = 30
+++

## Import Pressure/Depth Data
Importing pressure data to ResInsight may be performed in two different ways:

- By selecting the main menu item **File -> Import -> Import Pressure Depth Data**
- By using the right-click command **Import Pressure Data** on the **Observed Data** item in the **Plot Main Window Project Tree** 


The imported pressure data can visualized in [[RFT Plots]]({{% relref "rftplot" %}})



#### Pressure/Depth File Format


```txt
--TVDMSL 
RFT  
--
WELLNAME 'OP_1'
DATE 28-FEB-2000
PRESSURE DEPTH
BARSA METRES
302.88 1605.91
303.88 1615.91
304.88 1625.91
304.38 1635.91
--
WELLNAME 'OP_2'
DATE 28-FEB-2000
PRESSURE DEPTH
BARSA METRES
302.88 1600.91
303.68 1610.91
303.88 1612.91
303.99 1620.91

```
