+++
title = "Summary Data Import"
published = true
weight = 20
+++

## Summary Data
Summary data is usually available as **SMSPEC** and **UNSRMY** files. Data in **UNSMRY** files are store in a binary format, and all data for one time step is stored one section. When extracting data for all time steps for a single summary vector, data must be read from multiple sections. This can give bad performance for large datasets.

### ESMRY File Format

**\*.ESMRY** files contains the same data as **SMSPEC/UNSMRY**. The data in these files store all data for a summary vector in one section to give significantly better performance when accessing single summary vectors compared to **SMSPEC/UNSMRY**.

**ResInsight** will by default use this file format.

If no **ESMRY** files are available, **ResInsight** can produce these files. This can be configured in [Preferences]({{< relref "preferences" >}}#summary). Note that all summmary data is read and write into a new **ESMRY** file. This operation will take some time, and can take minutes for a large ensemble.
