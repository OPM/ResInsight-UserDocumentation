+++
title = "Measurement"

weight = 152

+++

![](/images/3d-main-window/Measurement.png)

ResInsight supports measurements in the 3D views. To enter measurement mode, press the ruler toolbar button {{< image-in-text src="images/3d-main-window/MeasurementButton.png" >}} or the keyboard shortcut **Ctrl-M**. This mode can also be activated from the right-click menu in a 3D view.


![](/images/3d-main-window/MeasurementToolbar.png)

When ResInsight is in measurement mode, clicking on an surface in the 3D view will set the first measurement point. Clicking on a different surface will set the second measurement point, and display a label with measurements. Additional clicking will start a new measurement between two points.

The measurement label contains the following:

- **Length** - The length of the measurement segment
- **Horizontal Length** - The length of the measurement segment projected onto the XY plane

ResInsight also supports measuring a polyline (a set of line segments), which can be activated with the polyline ruler toolbar button {{< image-in-text src="images/3d-main-window/PolylineMeasurementButton.png" >}} or **Ctrl-Shift-M**. The measurement label will now contain additional measurements.

![](/images/3d-main-window/PolylineMeasurement.png)

The measurement label contains several lengths.

- **Segment Length** - The length of the last segment
- **Segment Horizontal Length** - The length of the last segment projected onto the XY plane
- **Total Length** - The total length of the measurement polyline
- **Total Horizontal Length** - The total length of the measurement polyline projected onto the XY plane
- **Horizontal area** - The area of the polyline projected onto the XY plane

To leave measurement modes, press the toolbar button, press the **Esc** button  or press the keyboard shortcut used to activate the mode again.
