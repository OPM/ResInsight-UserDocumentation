+++
title = "Advanced Text Input"

weight = 30
+++

When the user is requested to specify a list of integer values, it can be useful to input the list using a text string. This can be a selection of K slices, a selection of realisations or a selection of integer values in a integer cell result.

## Supported text format
```txt
5,10-13,20-26:2
```

This text will produce an integer array with values
```txt
[5, 10, 11, 12, 13, 20, 22, 24, 26]
```

Using the syntax **"20-26:2"** will produce integer values in the range at a step of 2, resulting in **[20, 22, 24, 26]**
