+++
title = "Performance Hints"
published = true
weight = 15
+++

## Performance Hints

As the simulation models grow in size, the requirements on processing resources and memory are increasing. ResInsight have some options that can improve performance by transformation of data or reduction of data input.

## Summary Data
Summary data is usually available as **SMSPEC** and **UNSRMY** files. **UNSMRY** files are stored in a binary format, and all data for one time step is stored one section. When extracting data for all time steps for a single summary vector, data must be read from multiple sections. This can give bad performance for large datasets.

For best performance, transform these data files to **ESMRY File Format**

[Summary Data Import]({{< relref "summarydata" >}})

## Grid Data
ResInsight has two grid import readers, **ResData** and **opm-common**. For best performance, use **opm-common**. 

Active cells is often a small subset of total number of cells in a grid model. When this mode is activated, all inactive cells are skipped. Only geometry for active cells is imported, and all operations related to grid computations will perform better. 

[Preferences]({{< relref "preferences" >}})