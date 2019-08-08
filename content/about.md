+++
title = "About"
published = true
hidden = true
+++

ResInsight is an open source, cross-platform 3D visualization, curve plotting and post processing tool for Eclipse reservoir models and simulations. 
It can also be configured to visualize geomechanical simulations from ABAQUS.

The system also constitutes a framework for further development and can be extended to support new data sources and visualization methods, e.g. additional solvers, seismic data, CSEM, and more.

### Efficient User Interface
The user interface is tailored for efficient interpretation of reservoir simulation data with specialized visualizations of properties, faults and wells. It enables easy handling of a large number of realizations and calculation of statistics. To be highly responsive, ResInsight exploits multi-core CPUs and GPUs. Efficient plotting of well log plots and summary vectors is available through selected plotting features.

### Data Support
The main input data is
_`*.GRID`_ and _`*.EGRID`_ files along with their _`*.INIT`_ and restart files _`*.XNNN`_ and _`*.UNRST`_. 
Summary vectors can be imported from _`*.SMSPEC`_ files.
ResInsight also supports selected parts of Eclipse input files and can read grid 
information and corresponding cell property data sets from _`*.GRDECL`_ files. 
Well log data can be imported from _`*.LAS`_ files.

ResInsight can also be built with support for Geomechanical models from ABAQUS in the _`*.odb`_ file format.

### Updating and Refining Eclipse simulation models
ResInsight contains several pre-processing tools for updating and improving Eclipse reservoir models, including but not limited to:

- Adding **Well Path Completions** such as fractures, fishbones and perforations to well paths, including transmissibility calculations to allow for simulation in Eclipse.
- Easily and visually generate setup files for **Local Grid Refinement** (LGR)
- The generation of Eclipse **Multi Segment Well**-models for well path completions.

### Flow Diagnostics
Flow diagnostics calculations are embedded in the user interface and allows instant visualization of several well-based flow diagnostics properties, such as : Time of flight, flooding and drainage regions, well pair communication, well tracer fractions, well allocation plots and well communication lines. The calculations are performed by a library called [opm-flowdiagnostics](https://github.com/OPM/opm-flowdiagnostics) developed by [SINTEF Digital](http://www.sintef.no/digital). [More...]({{< ref "/3d-main-window/cellresults.md#flow-diagnostic-results" >}})

### Octave Integration
Integration with GNU Octave enables powerful and flexible result manipulation and computations. Derived results can be returned to ResInsight for further handling and visualization. Eventually, derived and computed properties can be directly exported to Eclipse input formats for further simulation cycles and parameter studies.

### Project organization
ResInsight is developed by [Ceetron Solutions](https://www.ceetronsolutions.com/) in collaboration with with [Equinor] (https://www.equinor.com/).

ResInsight is a part of the [Open Porous Media Initiative](http://opm-project.org/).
The software is hosted at [GitHub](https://github.com/OPM/ResInsight), and the development progress can be monitored there. The GitHub issue tracker is heavily used to organize the development process.

The software is licensed under GPL 3+, see [Licensing details](https://github.com/OPM/ResInsight/blob/master/COPYING).

### Web site programming and design
Web site is built with [Grav](https://getgrav.org) and [Hugo](https://gohugo.io)
