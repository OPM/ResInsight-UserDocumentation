+++
title = "Create Multilaterals Well Paths"
published = true
weight = 32
+++

![]({{< relref "" >}}images/3d-main-window/MultiLateralWell_3d_view.png)

ResInsight lets the user create additional well path laterals by clicking in the 3D view. Completions can be added to laterals, and the complete specification of the well can 
be exported using the [Completion Export]({{< relref "completionexport" >}})

### Building a well path

1. Start from an existing well path, either imported or [create a new well path]({{< relref "createnewwellpaths" >}}) 
2. In the 3D view, right-click on the well path at the depth location for your lateral
![]({{< relref "" >}}images/3d-main-window/MultiLateralWell_create.png)
3. A new well path lateral is created, and click in the 3D scene to define targets for the lateral
4. Repeat from 2. for more laterals

### Settings
The visual appearance of well targets can be controlled from the property editor.

![]({{< relref "" >}}images/3d-main-window/MultiLateralWell_property_editor.png)

### Naming of laterals
When a lateral is created, the postfix **Y1** is added to the original well path. The first lateral is given the postfix **Y2**. See the image above for an example of naming.