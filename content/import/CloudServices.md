+++
title = "Cloud Services"

weight = 10
+++
 
![](/images/cloud-services/sumo-summary-plot.png)

Configuration of cloud services is described in [Cloud Services - Authorization]({{< relref "cloudservicesauthorization" >}}).


## Summary Ensembles from SUMO

![](/images/cloud-services/sumo-data-sources.png)

Summary ensemble data can be accessed from SUMO. ResInsight will store the required information to the data source, and fetch data from the cloud during project import.

- Select **Cloud Data**, this will show available fields with cases in the **Data Source Property Editor**
- Select **Field** and **Case**, and a list of available ensembles are displayed
- Select **Ensembles** and push **Add Ensembles**. This operation creates a cloud ensemble data source and a summary plot connected to this data source.
- Use the button **Add Data Sources** if you want to avoid creation of summary plots

### Example of summary ensembles
![](/images/cloud-services/sumo-ensembles.png)

### Example of summary plot with SUMO data
![](/images/cloud-services/sumo-summary-plot.png)

## Well Paths from OSDU
![](/images/cloud-services/osdu-well-path-import.png)

From the right-click menu of **Wells**, select **Import Well Paths from OSDU**. A wizard will be displayed where field and well can be selected for import.

The imported well path will store required information to the location in OSDU, and the well path trajectory will be fethed during project import.

### Example of well paths from OSDU
![](/images/cloud-services/osdu-well-path-3dview.png)
