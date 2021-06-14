Installation and Configuration
==============================

.. image:: images/python-logo-master-v3-TM.png

The ResInsight Python API is compatible with `Python 3 <https://www.python.org/download/releases/3.0/>`_. 


Use rips as bundled with ResInsight executable
----------------------------------------------
If you download the ResInsight binaries, the rips package is bundeled with ResInsight and can be used directly from the user interface of ResInsight.

1. Download ResInsight
2. Make sure that Python 3 is installed
3. Make sure the dependencies of rips are installed
   python -m pip install grpcio protobuf
4. Make sure python executable is available from the ResInsight session
   - python executable is added to environment variables
   - full path to python executable is defined in Preferences->Scripting->Python Executable Location
  
Install rips using package system
---------------------------------
As admin user, the necessary Python client package is available for install via the Python PIP package system:

.. code-block:: console

   python -m pip install rips

or as a regular user:
   
.. code-block:: console

   python -m pip install --user rips
   
On some systems the `python -m pip` command can be simplified to `pip`.

Usage from within ResInsight
----------------------------
Add your script folder to Scripts
From the context menu of a Python script, select Execute
Text output is reported in Process Monitor

Troubleshooting
---------------
"ModuleNotFoundError: No module named 'grpc' 
Make sure grpc is installed using 

.. code-block:: console

   python -m pip install grpcio


"ModuleNotFoundError: No module named 'google.protobuf' 
Make sure protobuf is installed using 
   
   .. code-block:: console
   
      python -m pip install protobuf
   



To configure the **ResInsight Python Script Server**, check *Enable Python Script Server* and verify Python settings in the *Scripting* tab of the ResInsight *Preference* dialog.

.. image:: images/PrefGrpc.png

The availability of the ResInsight Python Script Server can be confirmed by ResInsight *About* dialog.
If unavailable, please consult ResInsight Build Instructions on `resinsight.org <https://resinsight.org/>`_.








