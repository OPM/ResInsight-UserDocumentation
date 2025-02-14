+++
title = "Project File Revisions"

weight = 15
+++



### Revision History
A backup of a project file is added to a project file database when the project file is saved. The backup file is named with the extension _`*.rspdb`_ and is stored in the same directory as the project file. The backup file is created with the same content as the project file at the time of the save operation. 

### Restore Revision from Backup
All revisions in the project database can be restored using the tool **restore-projectfile-versions**. Specify the project file database and the output directory where the revisions should be restored. The tool will create a copy of the project file for each revision in the output directory.

     extract-projectfile-versions <projectfiledatabase.rspdb> <output-directory>

Open the restored project files in ResInsight to inspect the content of the project file at the time of the save operation.