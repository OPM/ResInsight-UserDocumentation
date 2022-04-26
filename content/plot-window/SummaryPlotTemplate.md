+++
title = "Summary Plot Template"
published = true
weight = 45
+++

![]({{< relref "" >}}images/plot-window/SummaryPlotTemplate.png)


## Template creation
A summary plot template is defined by a number of curves with preset appearance and vector names. 
The parameters that are selected or varied by the user are:

- case(s)
- item(s), i.e. well(s), group(s), region(s)

Having tailored a plot setup, the user can save the setup as a template for later reuse via the **Plots** window right-click command **Save As Plot Template**.  

![]({{< relref "" >}}images/plot-window/SummaryPlotTemplateSave.png)

Given a new path, ResInsight will ask the user to confirm whether the path of the stored template is to be included in subsequent searches for templates. 

![]({{< relref "" >}}images/plot-window/SummaryPlotTemplatePath.png)

Each summary plot template is stored in a single file on disk. ResInsight searches a set of directories for template files which can be managed by [**Plotting Preferences**]({{< relref "preferences#plotting" >}}).

## Template usage
Right-clicking in **Data Sources** and clicking **Create Summary Plot from Template** will list available summary plot templates for selection. This will create a summary plot according to the selected template.

![]({{< relref "" >}}images/plot-window/SummaryPlotTemplateUsage.png)


{{% notice note %}}
Previously made summary templates are incompatible with ResInsight 2022 due to extended functionality. Please load summary plots of previous versions via project files or re-establish the plots prior to saving templates with ResInsight 2022.
{{% /notice %}}
