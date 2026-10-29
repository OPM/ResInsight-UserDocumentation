+++
title = "Project File Revisions"

weight = 15
+++



### Revision History
A backup of a project file is added to a project file database when the project file is saved. The backup file is named with the extension _`*.rspdb`_ and is stored in the same directory as the project file. The backup file is created with the same content as the project file at the time of the save operation. 

### Restore Revision from Backup
All revisions in the project database can be restored by selecting **File > Restore Previous Project Versions...**.

![](/images/misc/ProjectFileRevisions.png)

In the dialog, specify:

- **Recent Project Files** -- Select a recently used project to fill in the fields below
- **Project File** -- The project file to restore revisions for. Defaults to the currently open project. The backup database _`*.rspdb`_ must be present next to the project file.
- **Export Folder** -- The folder where the revisions are written. Defaults to the folder of the project file.

A project file is written to the export folder for each revision, named by the time of the save operation, e.g. _`2026-10-22_13-12-10.rsp`_. The restored revisions are then listed with the newest first. Select a revision to open it in ResInsight and inspect the content of the project file at the time of the save operation.