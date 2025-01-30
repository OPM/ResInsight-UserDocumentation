+++
title = "What's New in 2019.08"

weight = 10
hidden = true
+++

ResInsight 2019.08 is the latest version of ResInsight, the professional quality, open source 3D visualization, curve plotting and post-processing tool for Eclipse reservoir models. Version 2019.08 opens up a range of new and efficient workflows by adding Python script support in ResInsight.

## Python scripting

Basic example on how to update views from Python

```python
import rips
# Connect to ResInsight instance
resInsight = rips.Instance.find()

# Check if connection worked
if resInsight is not None:
    # Get a list of all cases
    cases = resInsight.project.cases()
    for case in cases:
        # Get a list of all views
        views = case.views()
        for view in views:
            # Set some parameters for the view
            view.setShowGridBox(not view.showGridBox())
            view.setBackgroundColor("#3388AA")            
            # Update the view in ResInsight
            view.update()
```

For more information and examples, please see the [ResInsight Python API](https://api.resinsight.org).


## Launch ResInsight without user interface

It is now possible to launch ResInsight as a console application with no user interface. Some workflows might include servers with no graphics card, and the console mode enables use of ResInsight in this context.

See [Command Line Interface]({{% relref "CommandLineInterface.md" %}})

## Plotting improvements

![](/images/plot-window/SummaryCurveHighlight.png)

- Date and time can now be customized to exactly the format you prefer
- To easily see the difference between history vectors and other vectors, the default style for history vector is symbols without lines
- Curves in a plot will be hightlighted when left-clicking the curve

See [Summary Plotting]({{% relref "summaryplots.md#curve-hightlight" %}})

