+++
title = "Allan Diagram"

weight = 91
+++

![]({{< relref "" >}}images/3d-main-window/AllanDiagram.png)

**Allan Diagrams** displays the overlap of formations and layers across fault faces.

## Separate Fault Result

The **Allan Diagram** is dispayed by selecting the **Separate Fault Result** in the project tree. 
![]({{< relref "" >}}images/3d-main-window/AllanDiagramPropertyEditor.png)

See [Faults ]({{< relref "faults/#separate-fault-result" >}}) for more details.

## Property Editor Settings

- **Binary Formation Allan** One color for all NNC areas with same formation on across fault, and one color for NNC with different formations across fault
- **Formation Allan** Formation colors are used, and a mix of the two formation colors are displayed if we have different formations across fault

## Mouse interaction
When clicking on an NNC area multiple times, the highlighted cell switched from the cell in front of the formation and behind the fault. The Result Info text is updated when the selected cell is changed.

![]({{< relref "" >}}images/3d-main-window/AllanDiagramCellHighlight.png)

## Other related results

Other useful NNC results are descrived in [Derived Results]({{< relref "derivedresults" >}}) 