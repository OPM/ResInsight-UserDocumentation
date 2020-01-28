+++
title = "What's New in 2019.12.1"
published = true
weight = 10
hidden = true
+++

ResInsight 2019.12.1 is the latest version of ResInsight, the professional quality, open source 3D visualization, curve plotting and post-processing tool for reservoir models and simulations.
Version 2019.12.1 consists of a few critical issues and minor functionality changes.


## Bugfixes

[Release info on GitHub](https://github.com/OPM/ResInsight/releases/tag/v2019.12.1)


## Changes in behavior

### WELSEGS 
Output of segment depth is based on center of segment. Previously the segment end was reported.

[ Export of Completions and MSW ]({{< ref "completionexport.md#exported-msw-data" >}})

### Multiple completions in same cell
In previous releases, no connection factor has been reported if multiple fracture completions has been detected in the same cell. Now, when multiple fracture are detected, they are combined and reported similar to other completion types.

[ Export of Completions ]({{< ref "completionexport.md" >}})
