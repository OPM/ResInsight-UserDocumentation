+++
title = "Linux Installation"

hidden = false
weight = 10
+++




## Install From Binary Packages on Linux 

{{% notice info %}}
Please not that the distribution by the OPM Project will be updated some time after the release of a new version on GitHub.
{{% /notice %}}

### Ubuntu 
On the command line do: 

    sudo apt-get update
    sudo apt-get install software-properties-common
    sudo apt-add-repository ppa:opm/ppa
    sudo apt-get update
    sudo apt-get install resinsight
    sudo apt-get install octave-resinsight

Launch the application using the command `ResInsight`

{{% notice info %}}
For further installation details, see the ResInsight distribution on [Opm Project Downloading and Installing](http://opm-project.org/?page_id=36).
{{% /notice %}}
 
{{% notice info %}}
The binary distributions does not support ABAQUS odb files. For building ResInsight with ABAQUS support, see 
[Build Instructions]({{% ref "cmake-configuration.md" %}}).
{{% /notice %}}

## Custom Qt configuration
If you are using a version of Qt that is not available in system path, you need to do the following to make runtime Qt paths available to ResInsight

    export LD_LIBRARY_PATH=/path_to_qt
    export QT_PLUGIN_PATH=/path_to_qt/plugins:$QT_PLUGIN_PATH


### Display Menu Icons in GNOME (Optional)
By default, icons are not visible in menus in the GNOME desktop environment. ResInsight has icons for many menu items, and icons can be set visible by issuing the following commands (Tested on RHEL6) :

```txt
gconftool-2 --type boolean --set /desktop/gnome/interface/buttons_have_icons true
gconftool-2 --type boolean --set /desktop/gnome/interface/menus_have_icons true
```

This fix was taken from reply number 11 in this [thread](https://bbs.archlinux.org/viewtopic.php?id=117414)

## Setup Octave Interface (optional)

1. Install Octave directly from the package manager in Linux. See the documentation for your particular distribution. 
2. Launch ResInsight, open **Edit->Preferences** 
3. Enter the path to the Octave command line interpreter executable `octave-cli`

## Workaround for crash using Virtual Box
Uncheck **Settings->Display->Enable 3D Acceleration**. Disabling this option will cause OpenGL operations to be executed in software, so the the performance of graphics operations in ResInsight will be slower, but will not crash.

Here is a pointer addressing the issue with Virtual Box, this is not testes by us:

[https://superuser.com/questions/541537/how-to-solve-issues-with-shader-model-in-virtualbox](https://superuser.com/questions/541537/how-to-solve-issues-with-shader-model-in-virtualbox)
