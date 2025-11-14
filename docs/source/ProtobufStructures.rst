Protocol Buffer Data Structures
=================================

This page documents the Protocol Buffer message structures used in the ResInsight Python API.

Overview
--------

ResInsight uses Protocol Buffers (protobuf) for efficient data serialization and communication between Python and the ResInsight application via gRPC. The protobuf definitions define the structure of data that can be exchanged with ResInsight.

The generated Python classes from these protobuf files are used as return types and parameters in many rips API methods.

Source Files
~~~~~~~~~~~~

The Protocol Buffer definition files (.proto) are automatically downloaded from the `ResInsight repository <https://github.com/OPM/ResInsight/tree/dev/GrpcInterface/GrpcProtos>`_ and stored in the ``docs/proto`` directory.

The generated Python files are located in ``docs/rips/generated/`` and include:

* ``Definitions_pb2.py`` - Basic data types (Vec3d, Vec3i, CellCenters, etc.)
* ``SimulatorTables_pb2.py`` - Well completion data structures
* ``Case_pb2.py`` - Case-related structures
* ``Grid_pb2.py`` - Grid-related structures
* ``Properties_pb2.py`` - Property data structures
* ``SimulationWell_pb2.py`` - Simulation well structures
* And more...

Common Data Structures
----------------------

Basic Vector Types
~~~~~~~~~~~~~~~~~~

Vec3d
^^^^^

A 3D vector with double-precision floating-point coordinates.

**Attributes:**

* ``x`` (float): X-coordinate
* ``y`` (float): Y-coordinate
* ``z`` (float): Z-coordinate

**Used in:** Cell centers, coordinates, spatial positions

Vec3i
^^^^^

A 3D vector with integer coordinates.

**Attributes:**

* ``i`` (int): I-index
* ``j`` (int): J-index
* ``k`` (int): K-index

**Used in:** Grid dimensions, cell indices

Well Completion Data
--------------------

SimulatorTableData
~~~~~~~~~~~~~~~~~~

Container for well completion data returned by :meth:`rips.WellPath.completion_data`.

**Attributes:**

* ``compdat`` (list[SimulatorCompdatEntry]): List of completion data entries (COMPDAT format)
* ``welspecs`` (list[SimulatorWelspecsEntry]): List of well specification entries (WELSPECS format)

SimulatorCompdatEntry
~~~~~~~~~~~~~~~~~~~~~

Represents a single COMPDAT (completion data) entry for Eclipse simulator format.

**Required Attributes:**

* ``well_name`` (str): Well name
* ``grid_i`` (int): Grid I-index (1-based)
* ``grid_j`` (int): Grid J-index (1-based)
* ``upper_k`` (int): Upper K-layer index (1-based)
* ``lower_k`` (int): Lower K-layer index (1-based)
* ``open_shut_flag`` (str): Open/shut status ("OPEN", "SHUT", "AUTO")

**Optional Attributes:**

* ``saturation`` (float): Saturation value
* ``transmissibility`` (float): Connection transmissibility factor
* ``diameter`` (float): Wellbore diameter
* ``kh`` (float): Permeability-thickness product
* ``skin_factor`` (float): Skin factor for pressure drop
* ``d_factor`` (float): D-factor for non-Darcy flow
* ``direction`` (str): Well direction ('X', 'Y', 'Z', or angle)
* ``start_md`` (float): Start measured depth along wellbore
* ``end_md`` (float): End measured depth along wellbore
* ``comment`` (str): Comment text

SimulatorWelspecsEntry
~~~~~~~~~~~~~~~~~~~~~~

Represents a single WELSPECS (well specification) entry for Eclipse simulator format.

**Required Attributes:**

* ``well_name`` (str): Well name
* ``group_name`` (str): Well group name
* ``grid_i`` (int): Grid I-index for well head location (1-based)
* ``grid_j`` (int): Grid J-index for well head location (1-based)
* ``phase`` (str): Primary phase ('OIL', 'WATER', 'GAS', 'LIQ')

**Optional Attributes:**

* ``bhp_depth`` (float): Reference depth for bottom hole pressure
* ``drainage_radius`` (float): Drainage radius
* ``inflow_equation`` (str): Inflow equation type
* ``auto_shut_in`` (str): Automatic shut-in flag
* ``cross_flow`` (str): Cross-flow capability flag
* ``pvt_num`` (int): PVT region number
* ``hydrostatic_density_calc`` (str): Hydrostatic density calculation method
* ``fip_region`` (int): Fluid-in-place region number

SimulatorTableRequest
~~~~~~~~~~~~~~~~~~~~~

Request message for retrieving well completion data.

**Attributes:**

* ``wellpath_name`` (str): Name of the well path
* ``case_id`` (int): ID of the case to extract data from

Usage Examples
--------------

Working with SimulatorTableData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :meth:`rips.WellPath.completion_data` method returns a ``SimulatorTableData`` object containing well completion information:

.. code-block:: python

    import rips

    # Connect to ResInsight
    resinsight = rips.Instance.find()
    project = resinsight.project

    # Get a case
    case = project.cases()[0]

    # Get well path
    well_path = project.well_paths()[0]

    # Get completion data
    completion_data = well_path.completion_data(case.id)

    # Access COMPDAT entries
    for compdat_entry in completion_data.compdat:
        print(f"Well: {compdat_entry.well_name}")
        print(f"  Grid location: i={compdat_entry.grid_i}, j={compdat_entry.grid_j}")
        print(f"  K layers: {compdat_entry.upper_k} to {compdat_entry.lower_k}")
        print(f"  Status: {compdat_entry.open_shut_flag}")
        if compdat_entry.HasField('transmissibility'):
            print(f"  Transmissibility: {compdat_entry.transmissibility}")
        if compdat_entry.HasField('diameter'):
            print(f"  Diameter: {compdat_entry.diameter}")

    # Access WELSPECS entries
    for welspecs_entry in completion_data.welspecs:
        print(f"Well: {welspecs_entry.well_name}")
        print(f"  Group: {welspecs_entry.group_name}")
        print(f"  Phase: {welspecs_entry.phase}")
        print(f"  Grid location: i={welspecs_entry.grid_i}, j={welspecs_entry.grid_j}")
        if welspecs_entry.HasField('bhp_depth'):
            print(f"  BHP Depth: {welspecs_entry.bhp_depth}")

Working with Optional Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many protobuf messages contain optional fields. Use the ``HasField()`` method to check if an optional field is set:

.. code-block:: python

    # Check if optional field is set before accessing
    if entry.HasField('saturation'):
        saturation_value = entry.saturation
    else:
        saturation_value = None

    # Or use getattr with a default value
    saturation = getattr(entry, 'saturation', None)

Working with Vec3d and Vec3i
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many protobuf messages use ``Vec3d`` (3D double vector) or ``Vec3i`` (3D integer vector) for coordinates:

.. code-block:: python

    # Vec3d example (cell centers, coordinates)
    cell_centers = grid.cell_centers()
    for center in cell_centers.centers:
        print(f"Center: x={center.x}, y={center.y}, z={center.z}")

    # Vec3i example (grid indices)
    grid_dims = grid.dimensions()
    print(f"Grid dimensions: i={grid_dims.i}, j={grid_dims.j}, k={grid_dims.k}")

See Also
--------

* :doc:`rips` - Main API documentation
* :doc:`GeneratedClasses` - Auto-generated class documentation
* :doc:`PythonExamples` - Python code examples

External Resources
~~~~~~~~~~~~~~~~~~

* `Protocol Buffers Documentation <https://protobuf.dev/>`_
* `gRPC Python Documentation <https://grpc.io/docs/languages/python/>`_
* `ResInsight Source Repository <https://github.com/OPM/ResInsight>`_
