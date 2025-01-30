+++
title = "What's New in 2020.10.1"

weight = 10
hidden = true
+++

ResInsight 2020.10.1 is the latest version of ResInsight, the professional quality, open source 3D visualization, curve plotting and post-processing tool for reservoir models and simulations. Version 2020.04.1 is a patch update with several critical fixes.


**Most important fixes**
- Using text filter to select summary curves for ensembles now works
- Summary address selection for analysis and tornado plots can now select single address instead of always all wells
- Fixed several visualization issues related to contour plots
- Make sure the color legend is drawn as discrete instead of continuous
- Recalculate required curves when summary case is replaced
- Fixed crash when closing combined view
- Fixed crash for color legends with less than two colors
- 2D plots : Allow inverted y-axis when user defined min/max is active
- Well Targets : Fixed crash when toggling target at sea level

**Python API fixes**
- case.replace() created wrong model name
- project.open() caused currently running Python script to be disconnected
- set_grid_property() caused crash for ASCXII cases
- Avoid crash when UNSMRY file is missing

**Improvements**
- Data source stepping supports aquifers
- Import dialog : Add recently use folders
- Import dialog : Support replace of 'realization-n' to 'realization-*'
- Import dialog : Sort file names based on numbers instead of text
- Color Legend : Improved default settings for logarithmic variables

[Release notes for 2020.10.1](https://resinsight.org/getting-started/whats-new/releasenotes_2020_10_1)

### Fixes since ResInsight 2020.10.1
https://github.com/OPM/ResInsight/milestone/310?closed=1


**Release Notes on GitHub**

[Release info on GitHub](https://github.com/OPM/ResInsight/releases/)
