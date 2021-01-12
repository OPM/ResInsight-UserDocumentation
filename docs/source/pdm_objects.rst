Automatically Generated Classes
==========================================

ResInsight provides access to a number of other objects in the Project Tree. These client code for these is automatically generated with the ResInsight build.

While the documentation refers to for example **rips.generated.resinsight_classes.EclipseView** the **generated.resinsight_classes** part is not necessary and the class
can simply be referred to as rips.EclipseView.

You can look for objects of a specific type by using the **descendants** method of **rips.project** ::

   import rips
   # Connect to ResInsight instance
   resinsight = rips.Instance.find()
   # Example code
   print("ResInsight version: " + resinsight.version_string())
   # Get a list of all Eclipsev view in the project
   views = resinsight.project.descendants(rips.EclipseView)

.. automodule:: rips.generated.resinsight_classes
   :members:
   :show-inheritance:

.. autoattribute:: rips.generated.resinsight_classes