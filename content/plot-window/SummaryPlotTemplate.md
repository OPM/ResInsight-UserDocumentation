+++
title = "Summary Plot Template"
published = true
weight = 45
+++

![]({{< relref "" >}}images/plot-window/SummaryPlotTemplate.png)


## Template creation
A summary plot template is defined by a number of subplots and curves with preset appearance and vector names. 
Having tailored a plot setup, the user can save the setup as a template for later reuse via the **Plots** window right-click command **Save As Plot Template** which pops the **Export Plot Template** dialog seen above.

![]({{< relref "" >}}images/plot-window/SummaryPlotTemplateSave.png)

A Summary Plot Template can subsequently be used for summary plotting of various data sources. The data sources that can be selected and varied by the user are:

- case(s), ensemble(s), and realization(s)
- well(s), group(s), and region(s)

When saving a Summary Plot Template, ResInsight by default incorporates placeholders for using the template in conjuction with various wells, groups, and regions. 
On the other hand, expand and check the appropriate boxes if you want to persist wells, groups, and/or regions.
To exemplify, checking *Wells* for persistence enables plotting of data for the exact wells of the template in conjuction with any ensemble realization.

![]({{< relref "" >}}images/plot-window/SummaryPlotTemplateSavePersistentObjectNames.png)

Each summary plot template is stored in a single file on disk. ResInsight searches a set of directories for template files which are listed and managed by [**Plotting Preferences**]({{< relref "preferences#plotting" >}}). 
Given a new path, ResInsight will ask the user to confirm whether the path of the stored template is to be included in subsequent searches for templates. 

![]({{< relref "" >}}images/plot-window/SummaryPlotTemplatePath.png)


## Template usage
Right-clicking in **Data Sources** and clicking **Create Summary Plot from Template** will list available summary plot templates for selection. To reapply the previously used template, invoke **Create Plot from Last Used Template** or simply press **Ctrl-T**. Both approaces create a summary plot according to template.

![]({{< relref "" >}}images/plot-window/SummaryPlotTemplateUsage.png)


{{% notice note %}}
Summary templates made with prior versions are incompatible with ResInsight 2022 due to significant extensions of functionality. Please load summary plots of prior versions via project files or re-establish plots prior to saving templates with ResInsight 2022.
{{% /notice %}}


## Template window
The template window enables overview of summary plot templates by directory and offers the following functionality:

- rename of template
- edit of template XML file in the text editor specified as *Script Editor* in 
[Preferences]({{< relref "preferences#scripting" >}}) 
- reload templates in ResInsight in case of directory or file changes on disk

![]({{< relref "" >}}images/plot-window/SummaryPlotTemplateWindow.png)
