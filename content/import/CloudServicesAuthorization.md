+++
title = "Cloud Services - Authorization"
published = true
weight = 10
+++
 

## Authorization

Currently supported cloud services use **OAuth 2.0**, the industry-standerd protocol for authentication. The first time a user initiates data from a cloud service, a browser window will appear for the user to enter username/password followed by additional two-factor authentication. A text string usually called a token is created, containing the access and authorization information required to access the cloud data source. This token is cached by ResInsight in the `.resinsight` folder in your home folder. A token is by default valid for several days.

If you experience issues with connection to cloud data, the local cached tokens can be deleted. The next time you access to cloud services, a brower window for authentication is displayed.

Use of cloud services is supported on both Windows and Linux.

https://auth0.com/intro-to-iam/what-is-oauth-2


![]({{< relref "" >}}images/cloud-services/web-authentication.png)

## Configuration
The configuration settings for cloud services can be seen in **Preferences->Import/Export**. The settings can be loaded from a **JSON** file in your home folder or on a shared folder on the file system.

    home_folder/.resinsight/osdu_config.json
    home_folder/.resinsight/sumo_config.json

    location_of_executable/../share/cloud_services/osdu_config.json
    location_of_executable/../share/cloud_services/osdu_config.json
