+++
title = "Project Tree"
published = true
weight = 7
+++

![]({{< relref "" >}}images/getting-started/ResInsightPlotProjectTreeAndWindow.png)

As described in [Overview]({{< relref "Overview.md" >}}), ResInsight has two main windows, one for 3D related visualizations and one for 2D graphs and plots. The content and appearance of displayed information is managed and controlled by the **Project Tree** and the **Plot Project Tree**, respectively. This page describes some of their general functionality illustrated by examples using **Plot Project Tree**.


## Multiple selection and collective actions
Multiple selection of items in ResInsight offers an entrance to powerful combinations and collective actions. 
To exemplify, consider the plot of *Bottom Hole Pressure* for a number of wells atop this page. By multi-selection of wells in **Plot Project Tree**, you may for instance change the color to yellow for all wells with prefix *B* as shown below.

![]({{< relref "" >}}images/getting-started/ResInsightPlotProjectTreeMultiSelectAction.png)

Several options are available for multi selection of items which can be used in combination for efficiency and convenience:

- **Ctrl + left mouse button** for selecting individual items

- **Shift + left mouse button** for selecting a range of consecutive items

- **Item right-click menu**:

  -- **Sub Items On**: select all sub-items of an item in project tree

  -- **Sub Items Off**: deselect all sub-items of an item in project tree

  -- **Toggle Sub Items**: deselect previously selected sub-items and select previously not selected sub-items

![]({{< relref "" >}}images/getting-started/ResInsightPlotProjectTreeItemMenu.png)

  
## Undo and Redo
ResInsight offers powerful **Undo** and **Redo** functionality. If the user regrets an action, for instance the color setting for multiple wells as exemplified above, the collective action can be undone by pressing **Undo**.

**Undo** and **Redo** is available by: 

- Toolbar icons {{< image-in-text src="images/getting-started//ResInsightPlotProjectTreeToolbarUndoRedo.png" >}}
- **Edit menu** items **Undo** and **Redo**
- Shortcuts **Ctrl+Z** and **Ctrl+Y**



## Context sensitive help
ResInsight offers context sensitive for any item in project tree. Most convenient is just to press the **F1** help key for any selected item. Alternatively, you may right-click an item (e.g. *Summary Curves*) and the help system will identify the item as subject and perform the actual search for information by menu item **Search Help For**.

![]({{< relref "" >}}images/getting-started/ContextSensitiveHelp.png)

