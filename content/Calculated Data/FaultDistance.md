+++
title = "Fault Distance"
published = true
weight = 100
hidden = false
+++

## Fault Distance

When planning new well paths, it can be usedful to see the distance from the current cell to the closest fault. This result is available in **Static->FAULTDIST**


![]({{< relref "" >}}images/calculated-data/FaultDistance.png)

## Calculation
The distance is calculated based on the distance from each cell face center to the closest fault face center. One value is calculated per each cell. The calculation is started when the **FAULTDIST** result is selected.
