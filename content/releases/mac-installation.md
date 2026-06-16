+++
title = "Mac Installation"

hidden = false
weight = 15
+++

## ResInsight Installation

1. Download the ZIP binary distribution from [https://github.com/OPM/ResInsight/releases](https://github.com/OPM/ResInsight/releases "release section on GitHub")
2. Unzip the file to extract the `ResInsight.app` application bundle
3. Remove the Gatekeeper quarantine attribute before the first launch:

       sudo xattr -r -d com.apple.quarantine ResInsight.app

4. Launch the application by double-clicking `ResInsight.app` in Finder, or from a terminal:

       open ResInsight.app

{{% notice info %}}
The application bundle is <b>not</b> code-signed and <b>not</b> notarized, so macOS Gatekeeper quarantines it on download. Removing the quarantine attribute as shown above is required before the first launch. The distribution requires macOS 15 (Sequoia) or newer and is built with Qt 6.7.0.
{{% /notice %}}
