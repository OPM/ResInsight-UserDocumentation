+++
title = " Radial Grid"

weight = 30
+++

ResInsight now supports radial grids, enabling visualization and analysis of reservoir models that use radial coordinate systems. This is particularly useful for well-centric models and near-wellbore analysis.

![](/images/import/radial-grid-overview.png)
*Example of a radial grid model displayed in ResInsight showing pressure distribution around a well*

## Overview

Radial grids use a cylindrical coordinate system (r, θ, z) instead of the traditional Cartesian (x, y, z) system. This allows for more accurate representation of phenomena around wells and other cylindrical geometries.

## Importing Radial Grid Models

Radial grid models can be imported into ResInsight through the standard import workflow:

1. **File → Import → Eclipse Files**
2. Select your radial grid files (.EGRID, .INIT, .UNRST, etc.)
3. ResInsight will automatically detect if the grid uses radial coordinates
4. The model will be loaded and converted for visualization. Choose file reader and how to handle radial grids from **Preferences**.
5. If the radial grid has a low number of angular cells, ResInsight will automatically create a temporary Local Grid Refinement (LGR) with higher angular refinement for improved visualization. This LGR can be seen in the project tree as "Radial LGR".

## Visualization Features

When working with radial grids, ResInsight provides:

- **3D Visualization**: Automatic conversion from radial to Cartesian coordinates for display
- **Property Mapping**: All standard property visualization features work with radial grids
- **Well Trajectories**: Enhanced visualization of wells in radial coordinate systems
- **Cross Sections**: Support for radial and angular cross-sections
- **Hex Element Approximation**: Radial grid cells can be approximated using hexahedral elements for improved visualization. This setting can be controlled from **Preferences**

## Preferences Settings

Radial grid behavior can be controlled through **Edit → Preferences → EGRID Settings**:

- **Radial Grid Display Mode**: Choose between:
  - **Cylindrical**: Uses cylindrical coordinates for radial grids (default behavior). No support for local grid refinement (LGR)
  - **Cartesian**: Forces Cartesian coordinate interpretation. This mode enstimates the cylindrical cells by hex element, and supports visualization of radial LGR.

## Key Considerations

- **Coordinate Conversion**: ResInsight handles the conversion between radial and Cartesian coordinates internally
- **Property Interpolation**: Properties are correctly interpolated considering the radial grid geometry
- **Export Functions**: Exported data maintains the original radial grid structure when appropriate

## Troubleshooting

If you encounter issues with radial grid imports:

- Verify that your grid files contain proper radial coordinate definitions
- Consider using a different reader for EGRID files
- Ensure all required grid files (.EGRID, .INIT) are present
- Review the ResInsight log for any import warnings or errors