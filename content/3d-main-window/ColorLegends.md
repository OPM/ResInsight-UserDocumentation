+++
title = "Color Legends"

weight = 32
+++

![](/images/3d-main-window/ColorLegendCollections.png)
![](/images/3d-main-window/ContourMaps.png)

ResInsight offers both a rich set of built-in color legends and functionality for import and customizing color legends. 
All color legends are available from the **Color Legends** item in **Project Tree**.

## Standard Color Legends
ResInsight offers an extensive set of built-in color legends as listed by *Standard Color Legends*.
As *Standard Color Legends* cannot be modified, you must create a *Custom Color Legend* when needing a legend that is not covered by *Standard Color Legends*.

![](/images/3d-main-window/ColorLegendStandardCollection.png)

## Create a Custom Color Legend
Custom Color Legends are created by right-clicking the **Color Legends** item in **Project Tree** to either import a 
[Formation file]({{% relref "formations" %}}) with color settings or create a new *Custom Color Legend*. 

![](/images/3d-main-window/ColorLegendCreateCustomColorLegend.png)

It is also possible to copy a standard legend to create a *Custom Color Legend* as basis for customization.

![](/images/3d-main-window/ColorLegendCollectionCopyStandardLegend.png)

When importing a [Formation Names]({{% relref "formations" %}}) description files (_`*.lyr`_) with colors, ResInsight automatically creates a color legend and use this as default color legend when visualizing formations in the 3D view.

## Customizing a Color Legend

A newly created *Custom Color Legend* is initially empty as basis for inclusion of *Color Legend Items* by right-clicking its entry.  
As seen below, the right-click menu also allows for deletion of a *Color Legend Item*.
The property editor is used to define each *Color Legend Item*.
 
![](/images/3d-main-window/ColorLegendCollectionColorLegendItem.png)

The sequence of *Color Legend Items* can be modified by clicking the arrow symbols seen below.

![](/images/3d-main-window/ColorLegendCollectionSequenceColorLegendItem.png)

The listed *Custom Color Legend* is used to form the 3D visualization of formations seen by the top figure of this page.
Activating this particular *Custom Color Legend* is performed by specifying it as 
[Result Color Legend]({{% relref "ResultColorLegend" %}}).


## Integer Cell Results

When displaying interger cell results, the default color mapping will be set to a category color mapping. This color legend is used when displaying **Formation Names**. If an integer result is loaded, a custom color legend with names can be used.

Example workflow
- Select an integer cell result, i.e. FIPNUM
- Create a custom color legend or create a copy of an existing color legend, name it **"MyColorLegend"**
- Define colors and assign names to colors
- Use the custom color legend. Note that the color item names are visible in the color legend in the view.


![](/images/3d-main-window/CustomCategoryLegend.png)
