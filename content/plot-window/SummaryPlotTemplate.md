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

Having tailored a plot setup, the user can save the setup as a template via the right-click command **Save As Plot Template**, c.f. figure above. It is also possible to select a summary plot in the **Plot Project Tree** and use the right-click menu to save a template. 
Both options save a template definition to file for later reuse.

{{% notice note %}}
Summary Plot Templates are created for all *Summary Plots* including ensemble plots by right-click menu option **Save As Plot Template** available in both the plot window and via their entries in the **Plot Project Tree**.
{{% /notice %}}

Given a new path, ResInsight will ask the user to confirm whether the path of the stored template is to be included in subsequent searches for templates. 

![]({{< relref "" >}}images/plot-window/SummaryPlotTemplatePath.png)


## Template usage

Having selected items of interest in the **Plot Project Tree** (i.e. cases, wells, groups, and regions) a template plot can be created.

Invoke the right-click menu shown below to select a specific summary plot template. 
Here two summary cases have been selected prior to invoking the right-click menu.
As seen, available options for select a specific template are:

- **Create Plot from Last Used Summary Template**  is a menu option to invoke the last used summary plot template.
- **Create Plot from Template** shows all available templates in a separate dialog for search and selection. 

![]({{< relref "" >}}images/plot-window/SummaryPlotTemplateUsage.png)

{{% notice note %}}
**Ctrl-T** is a shortcut to swiftly create a plot based on the last used summary template. 
{{% /notice %}}


## Template file search and organization
Each summary plot template is stored in a single file on disk. ResInsight searches a set of directories for template files
which can be managed by menu option **Edit->Preferences** and the [**Plotting tab**]({{< relref "preferences#plotting-tab" >}}).

