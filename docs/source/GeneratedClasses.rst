.. _AllClasses:

Project Tree Classes
====================
ResInsight provides access to a number of other objects in the Project Tree. These all inherit the
:ref:`PdmObjectBaseLabel` class.

You can look for objects of a specific type by using the **descendants** method of **rips.project** ::

   import rips
   # Connect to ResInsight instance
   resinsight = rips.Instance.find()
   # Example code
   print("ResInsight version: " + resinsight.version_string())
   # Get a list of all Eclipsev view in the project
   views = resinsight.project.descendants(rips.EclipseView)

.. automodapi:: rips


