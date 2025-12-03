+++
title = "Initial Configuration"

weight = 10
+++


## Install OPM Flow

You need at least version 2025.04 of OPM Flow installed to use it with ResInsight.

Follow the **flow** installation instructions: https://opm-project.org/?page_id=245

## Windows support

To be able to run OPM Flow on your Windows computer, you need to first install **WSL**.

A guide for installing WSL and OPM Flow can be found [here](https://github.com/CeetronSolutions/OPM-flow-WSL-guide).

## ResInsight setup

ResInsight needs to know where to find the OPM Flow executable. To do this, open the ResInsight preferences:

![ResInsight Preferences - OPM Flow](/images/opm-flow-integration/preferences.png)

**Path to OPM Flow Executable:**
Enter the full path of the **flow** executable. Do not add any extra parameters here.

**Use WSL to run OPM Flow:** (Windows only)
Turn this option on if you want to run OPM Flow using WSL on Windows. In case you have multiple WSL distributions installed, select the one you have flow installed in. 

**Enable MPI:**
Turn this option on if you want to run OPM Flow in parallel using MPI. You need to enter the full path to the mpirun executable you want to use. Do not add any extra parameters here.

**Default command line settings:**
This is where you define the command line parameters you want ResInsight to pass on to OPM Flow. The settings in this section will be the default settings for any new OPM Flow job you create in ResInsight. The settings can be overridden in a particular job, if needed. 

NOTE: If you change anything in this section, existing jobs will not be updated. The new settings will only be used by any new jobs you create.

**Process Control:**
Here you can specify the number of MPI processes to run in parallel if MPI has been enabled. You can also adjust the number of threads each process is allowed to use. Using more processes and threads could increase the performance of OPM Flow, but only to certain extent.

Refer to the [OPM Flow manual](https://opm-project.org/?page_id=955) for a description of the remaining parameters.




