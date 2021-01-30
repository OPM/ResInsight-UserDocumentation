Main Classes
============

Case class
----------
Access to case information.
Inherits :ref:`PdmObjectBase<PdmObjectBaseLabel>` and all its members.

Can be accessed with the case() and cases() methods on rips.Project ::

   # Import module
   import rips
   # Connect to running instance
   resinsight = rips.Instance.find()
   # Get a list of cases
   cases = resinsight.project.cases()

In practise each object is of the sub-classes rips.EclipseCase and rips.GeoMechCase.
See :ref:`AllClasses` for a description of them.

.. _result-definition-label:

Result Definition
^^^^^^^^^^^^^^^^^
When working with grid case results, the following two arguments are used in many functions to identify a
result

**Result Definition enums**::
    
    property_type           |       | porosity_model
    (str enum)              |       | (str enum)
    ----------------------- | ----- | --------------
    DYNAMIC_NATIVE          |       | MATRIX_MODEL
    STATIC_NATIVE           |       | FRACTURE_MODEL
    SOURSIMRL               |       |
    GENERATED               |       |
    INPUT_PROPERTY          |       |
    FORMATION_NAMES         |       |
    FLOW_DIAGNOSTICS        |       |
    INJECTION_FLOODING      |       |

Detailed documentation :class:`rips.Case`

Examples
^^^^^^^^
See :ref:`all_cases`, :ref:`load_case` and :ref:`selected_cases`.

Grid class
----------
Access to grid information

Detailed documentation :class:`rips.Grid`

Examples
^^^^^^^^
See :ref:`grid_information`.

Instance - the main starting point
----------------------------------
The basic access class to ResInsight. Use to find or launch a running instance of ResInsight ::

   import rips
   # Connect to ResInsight instance
   resinsight = rips.Instance.find()
   # Get the ResInsight project
   project = resinsight.project

Detailed documentation :class:`rips.Instance`

Examples
^^^^^^^^
See :ref:`instance_example` and :ref:`launch_with_commandline_options`.

.. _PdmObjectBaseLabel:

PdmObjectBase class
-------------------
The base class of all data classes in ResInsight. Not used directly but all attributes
and methods are available in the other ResInsight data classes.

For any object based on PdmObjectBase you can access ancestors and descendants using the methods
ancestors(), children() and descendants() using a class name as the argument ::

   import rips
   # Connect to ResInsight instance
   resinsight = rips.Instance.find()
   # Get a list of all plot windows
   plot_windows = resinsight.project.descendants(rips.PlotWindow)

See :ref:`AllClasses` for all classes based on PdmObjectBase.

Detailed documentation :class:`rips.PdmObjectBase`

Project class
-------------
The ResInsight project. Inherits :ref:`PdmObjectBase<PdmObjectBaseLabel>` and all its members.
Always available as an object member "project" on the rips.Instance ::

   # Import the module
   import rips
   # Connect to a ResInsight instance
   resinsight = rips.Instance.find()
   # Get the project
   project = resinsight.project

Detailed documentation :class:`rips.Project`

Examples
^^^^^^^^
See :ref:`open_project`

View class
----------
The base class of all views in ResInsight.
Inherits :ref:`PdmObjectBase<PdmObjectBaseLabel>` and all its members

Detailed documentation :class:`rips.View`

Examples
^^^^^^^^
See :ref:`view_example` and :ref:`set_cell_result`.
