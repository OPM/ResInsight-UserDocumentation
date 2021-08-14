+++
title = "Create Multilaterals Well Paths"
published = true
weight = 32
+++

![]({{< relref "" >}}images/3d-main-window/MultiLateralWell_3d_view.png)

ResInsight lets the user create additional well path laterals by clicking in the 3D view. Completions can be added to laterals, and the complete specification of the well can 
be exported using the [Completion Export]({{< relref "completionexport" >}})

## Building a well path

1. Start from an existing well path, either imported or [create a new well path]({{< relref "createnewwellpaths" >}}) 
2. In the 3D view, right-click on the well path at the depth location for your lateral
![]({{< relref "" >}}images/3d-main-window/MultiLateralWell_create.png)
3. A new well path lateral is created, and click in the 3D scene to define targets for the lateral
4. Repeat from 2. for more laterals

## Tie In Control
The parent well and the measured depth of the tie in location can be adjusted from the property editor.

![]({{< relref "" >}}images/3d-main-window/MultiLateralWell_property_editor.png)

## Naming of laterals
When a lateral is created, the postfix **Y1** is added to the original well path. The first lateral is given the postfix **Y2**. See the image above for an example of naming.

## Well Target Interaction

![]({{< relref "" >}}images/well-modeling/well-targets-and-handles-2.png)

### Activate well targets
Activate the well target handles, either by clicking on the well target spheres or by selecting **Well Targets** in the **Project Tree**.

### Well Target Interaction Operations
When the well target handles are active in the 3D view, the following operations are possible when pressing left mouse button on well target handles:

|User Interaction           | Description |
|---------------------------|-------------|
|Mouse Move                 | Modification of a single target |
|Mouse Move + CTRL          | Modification of all well target on selected well (laterals excluded) |
|Mouse Move + CTRL + SHIFT  | Modification of all well targets (laterals included) |

Similar behaviour is available when modifying the well target for the tie-in well target.

## Link Reference Point
If you want to move multiple wells at the same time, you can activate Link Reference Point. If the reference point is updated in any of the linked wells, all wells will be updated accordingly.
![]({{< relref "" >}}images/well-modeling/well-modeling-link-reference-property-editor.png)

Selection of multiple well, and activation of **Link Reference Point**
![]({{< relref "" >}}images/well-modeling/well-modeling-link-reference.png)