+++
title = "Ensemble Well Log"

weight = 90
+++

![]({{< relref "" >}}images/workflows/well_log_ensemble_plot_depth_eq.png)

## Introduction

To study the uncertainty for well log extraction curves, ResInsight enables the user to import an ensemble of well logs and compute the statistical distribution in this ensemble. 

## Workflow

- From the right-click menu of Wells, select **Create Ensemble Well Log**
![]({{< relref "" >}}images/workflows/create_ensemble_well_log_menu.png)

- In the ensemble import dialog, select the files for import into ensembles
![]({{< relref "" >}}images/workflows/well_log_ensemble_file_dialog.png)

- Select well path and properties for export, select time step for dynamic properties, and use the checkbox to control if you want to create a well log ensemble based on the exported well log files
![]({{< relref "" >}}images/workflows/well_log_ensemble_well_path.png)

Click **OK** when you are ready

- A **Well Log Plot** is created in the **Plot Window** 
![]({{< relref "" >}}images/workflows/well_log_ensemble_plot.png)


- If the geometry is different in the ensembles (structural uncertainty), a depth equalization method is implemented. If the well is crossing layers in the same order across the different ensembles, it is possible to apply a depth equalization from the **Property Editor**

![]({{< relref "" >}}images/workflows/property_editor_depth_eq.png)
![]({{< relref "" >}}images/workflows/well_log_ensemble_plot_depth_eq.png)

In the plot above, the part where the crossing of K-layers is consistent, we get an easy to read plot. When the K-layer crossings do not match anymore, it is clearly visible that the plot is not able to display the information correctly. 


## Related documentation

[Well Log Extraction]({{< relref "welllogsandplots" >}})
[Ensemble File Dialog]({{< relref "ensemblefiledialog" >}})
