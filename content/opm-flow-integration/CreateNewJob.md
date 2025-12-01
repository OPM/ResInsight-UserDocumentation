+++
title = "Create an OPM Flow Job"

weight = 20
+++

### Overview

ResInsight refers to OPM Flow Simulations as OPM Flow Jobs. They are located in the Scripts/Jobs tree, shown in both the 3D Main Window and the Plot Main Window.

You can create a new job in two ways: From an already loaded grid case or from a .DATA file located on a local or network disk drive. In both cases, ResInsight creates a copy of the provided input in the selected working folder, keeping the original files unmodified.

### Create job from grid case

Right-click on an already loaded grid case in the 3D Main Window project tree. Select "New OPM Flow Simulation Job...".
You will be asked to select a working folder, where the job will store all input to and all output from the OPM Flow simulation.
It is recommended to use an empty folder.

NOTE: The grid case selected needs to have the related .DATA file located in the same folder as the grid file.

### Create job from .DATA file

Go to the Scripts/Jobs tree, right-click on the Jobs folder, and select "New OPM Flow Simulation Job...". You will be asked to provide the input .DATA file to use.

You will then be asked to select a working folder, where the job will store all input to and all output from the OPM Flow simulation.
It is recommended to use an empty folder.

