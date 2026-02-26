+++
title = "Sector Model Export [BETA]"

weight = 65
+++

The **Sector Model Export [BETA]** feature exports a subset of a simulation model to a standalone DATA file that can be used as input for a new simulation. It supports boundary conditions, grid refinement, model padding, and optional direct integration with an OPM Flow simulation job.

To launch the wizard, right-click on a **3D View** and select **Export Sector Model [BETA]**.

The export is configured through a step-by-step wizard with the following pages.

---

## General Settings

Specify the name and output folder for the new sector model.

- **Sector Model Name** -- The base name (without extension) for the exported DATA file.
- **Export Folder** -- The folder where the exported files will be written. Must differ from the source case folder.
- **Source Information** -- Read-only display of the source case name and location on disk.

---

## Sector Model Definition

Select which cells to include in the export.

- **Cells to Export** -- Choose one of the following options:
  - **Visible Cells Box** -- IJK bounding box around currently visible cells (controlled by range and property filters in the view).
  - **Active Cells Box** -- IJK bounding box around all active cells in the grid.
  - **Visible Wells Box** -- IJK bounding box surrounding visible wells, extended by a configurable number of cells.
    - **Well Padding** -- Number of extra cells to add around visible wells (default: 2).
  - **Full Grid Box** -- The complete grid including inactive cells.
  - **Manual Selection** -- Enter the IJK min/max coordinates directly.

The dialog shows the **Total cells to export** to help assess the size of the sector model.

---

## Refinement

Optionally refine the exported grid by subdividing cells in each direction.

- **Enable Grid Refinement** -- Check to activate refinement.
- **Cell Count I, J, K** -- Number of sub-cells per original cell in each direction (range 1–10). Grid result values are not interpolated; all new sub-cells inherit the value of their parent cell.

---

## Boundary Conditions

Configure how boundary conditions are defined for the sector model faces.

- **Boundary Condition Type** -- Select one of:
  - **OPERNUM/OPERATER** -- Uses OPERNUM and OPERATER keywords to define boundary conditions. A **PORV Multiplier** can be set to scale the pore volume at the sector model boundary (default: 1.0e6).
  - **BCCON/BCPROP** -- Uses BCCON and BCPROP keywords. A table of BCPROP keywords is shown, with one row per BCCON region. The number of rows is determined automatically from the maximum BCCON value found in the grid (defaulting to 6 for the six faces).

---

## Keyword Adjustments

Control which keywords from the source DATA file are excluded from the exported sector model.

- **Keywords to Remove from Output** -- A list of keywords that will be stripped from the export. The default list contains: `ACTION`, `ACTIONX`, `ACTIONW`, `BOX`, `UDQ`. Use the **Reset to Default** button to restore this list.

---

## Model Padding

Optionally extend the sector model grid in the Z direction by adding inactive padding layers above and/or below the exported cells. This can be useful to ensure that the sector model has a complete pressure column.

- **Enable Model Padding** -- Check to activate padding.

**Upper Padding**

- **Number of Z Layers** -- Number of padding layers to add above the model.
- **Top Depth** -- Depth of the top of the uppermost padding layer.
- **Porosity** -- Porosity value assigned to the upper padding layers (range 0–1).
- **EQUILNUM** -- EQUILNUM region number for the upper padding layers.

**Lower Padding**

- **Number of Z Layers** -- Number of padding layers to add below the model.
- **Bottom Depth** -- Depth of the bottom of the lowermost padding layer.

**Grid Options**

- **Minimum Layer Thickness** -- Minimum thickness of each padding layer (default: 0.1).
- **Fill Gaps in Z Direction** -- Fill any gaps between the model and the padding layers.
- **Enforce Monotonic Z-Corners** -- Ensures that Z-corner values are monotonically increasing.
- **Make Pillars Vertical** -- Forces the pillars of padding cells to be vertical.

---

## Simulation Job Settings

Optionally create an OPM Flow simulation job from the exported sector model, and/or immediately run it.

- **Create New Simulation Job** -- Check to add a new OPM Flow job using the exported sector model DATA file as input.
  - **Job Name** -- Name of the new simulation job (defaults to the sector model name).
  - **Working Folder** -- Folder where the simulation job will store input and output files. Must differ from the export folder and the source case folder.
- **Start Simulation Job After Export** -- When checked, all existing OPM Flow jobs that use the exported sector model file as input will be started automatically after the export completes.

See [OPM Flow Integration]({{% relref "opm-flow-integration" %}}) for more details on working with simulation jobs.
