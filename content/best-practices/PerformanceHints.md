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
ResInsight has two grid import readers, **ResData** and **opm-common**. 

#### opm-common
ResInsight now offers the option to import geometry exclusively for active cells. This feature is particularly beneficial for large grids where active cells constitute only a small fraction of the total, significantly reducing memory usage. This optimization ensures efficient handling of large models while maintaining full functionality for active cells. Enable this option using the checkbox **Only Load Active Cell Geometry**

Features currently not supported when using **opm-common**
- Relative Permeability plots
- PVT plots
- Flow Diagnostics

[Preferences]({{< relref "preferences" >}})