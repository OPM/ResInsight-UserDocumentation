+++
title = "Summary Plot Template"

weight = 45
+++

![](/images/plot-window/SummaryPlotTemplate.png)


## Template creation
A summary plot template is defined by a number of subplots and curves with preset appearance and vector names. 
Having tailored a plot setup, the user can save the setup as a template for later reuse via the **Plots** window right-click command **Save As Plot Template** which pops the **Export Plot Template** dialog seen above.

![](/images/plot-window/SummaryPlotTemplateSave.png)

A Summary Plot Template can subsequently be used for summary plotting of various data sources. The data sources that can be selected and varied by the user are:

- case(s), ensemble(s), and realization(s)
- well(s), group(s), and region(s)

When saving a Summary Plot Template, ResInsight incorporates by default placeholders for using the template in conjunction with various wells, groups, and regions. 
On the other hand, expand and check the appropriate boxes if you want to **persist** the specific wells, groups, and/or regions as part of the plot template definition.
To exemplify, checking *Wells* for persistence enables plotting of data for the exact wells of the template in conjunction with any ensemble realization.

![](/images/plot-window/SummaryPlotTemplateSavePersistentObjectNames.png)

Upon export, ResInsight automatically categorizes the template as an **Ensemble Template** if the template involves plotting of data for an ensemble. 
Otherwise the template is categorized as a **Summary Case** template.
Ensemble Templates are listed with the icon 
{{< image-in-text src="images/plot-window/IconEnsembleTemplate.png" >}} 
while Summary Case templates are listed with the icon
{{< image-in-text src="images/plot-window/IconSummaryCaseTemplate.png" >}}
in the [Templates Window]({{< relref "summaryplottemplate#templates-window" >}}), c.f. below.

Each summary plot template is stored in a single file on disk. ResInsight searches a set of directories for template files which are listed and managed by [**Plotting Preferences**]({{< relref "preferences#plotting" >}}). 
Given a new path, ResInsight will ask the user to confirm whether the path of the stored template is to be included in subsequent searches for templates. 

![](/images/plot-window/SummaryPlotTemplatePath.png)


## Template usage
Right-clicking in **Data Sources** and clicking **Create Summary Plot from Template** will list available summary plot templates for selection. To reapply the previously used template, invoke **Create Plot from Last Used Template** or simply press **Ctrl-T**. Both approaces create a summary plot according to template.

![](/images/plot-window/SummaryPlotTemplateUsage.png)


{{% notice note %}}
Summary templates made with prior versions are incompatible with ResInsight 2022 due to significant extensions of functionality. Please load summary plots of prior versions via project files or re-establish plots prior to saving templates with ResInsight 2022.
{{% /notice %}}


## Default templates
Default templates is a powerful feature to automate the generation of summary plots when importing a summary case or ensemble. The basis for automation is the selection of one or more default templates.

Specify each default template by right-clicking in the **Templates** window.
Then activate the use of default templates by specifying **Use Plot Templates** in the **Plotting tab** of Preferences, c.f. menu option [**Edit&rarr;Preferences**]({{< relref "preferences#plotting" >}}).

![](/images/plot-window/SummaryPlotTemplateWindow.png)

As shown, default templates are listed with a green color in their icon.
Both {{< image-in-text src="images/plot-window/IconSummaryCaseTemplate.png" >}}**Summary Case templates** and {{< image-in-text src="images/plot-window/IconEnsembleTemplate.png" >}}**Ensemble templates** may constitute default templates. 
When loading a summary case, the default Summary Case templates will be applied automatically, while default Ensemble templates will be applied automatically when loading an ensemble.


## Templates window
As seen above, the **Templates** window enables management and overview of summary plot templates by directory and offers the following functionality:

- create new plot based on selected template
- rename template
- delete template
- edit template XML file in the *Script Editor* specified in 
[Preferences]({{< relref "preferences#scripting" >}}) 
- specifying default template as described above
- reload templates in ResInsight in case of directory or file changes on disk

See also menu option [**Edit&rarr;Preferences**]({{< relref "preferences#plotting" >}}) for managing template folders and template searches.
