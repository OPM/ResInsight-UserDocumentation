from rips.pdmobject import PdmObjectBase
class CellFilterCollection(PdmObjectBase):
    """
    Attributes:
        active (str): Active
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.active = True
        PdmObjectBase.__init__(self, pb2_object, channel)
        if CellFilterCollection.__custom_init__ is not None:
            CellFilterCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class DataContainerFloat(PdmObjectBase):
    """
    Attributes:
        values (List of float): Float Values
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.values = []
        PdmObjectBase.__init__(self, pb2_object, channel)
        if DataContainerFloat.__custom_init__ is not None:
            DataContainerFloat.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class DataContainerString(PdmObjectBase):
    """
    Attributes:
        values (List of str): String Values
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.values = []
        PdmObjectBase.__init__(self, pb2_object, channel)
        if DataContainerString.__custom_init__ is not None:
            DataContainerString.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class DataContainerTime(PdmObjectBase):
    """
    Attributes:
        values (List of time): Time Values
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.values = []
        PdmObjectBase.__init__(self, pb2_object, channel)
        if DataContainerTime.__custom_init__ is not None:
            DataContainerTime.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class Case(PdmObjectBase):
    """
    The ResInsight base class for Cases

    Attributes:
        file_path (str): Case File Name
        id (int): Case ID
        name (str): Case Name
        name_setting (str): One of [FULL_CASE_NAME, SHORT_CASE_NAME, CUSTOM_NAME]
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.file_path = ""
        self.id = -1
        self.name = ""
        self.name_setting = "FULL_CASE_NAME"
        PdmObjectBase.__init__(self, pb2_object, channel)
        if Case.__custom_init__ is not None:
            Case.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class Reservoir(Case):
    """
    Abtract base class for Eclipse Cases

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        Case.__init__(self, pb2_object, channel)
        if Reservoir.__custom_init__ is not None:
            Reservoir.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def views(self):
        """All Eclipse Views in the case

        Returns:
             List of EclipseView
        """
        return self.children("Views", EclipseView)


class EclipseCase(Reservoir):
    """
    The Regular Eclipse Results Case

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        Reservoir.__init__(self, pb2_object, channel)
        if EclipseCase.__custom_init__ is not None:
            EclipseCase.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class ElasticProperties(PdmObjectBase):
    """
    Attributes:
        file_path (str): File Path
        properties_table (str): Properties Table
        show_scaled_properties (str): Show Scaled Properties
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.file_path = ""
        self.properties_table = ""
        self.show_scaled_properties = True
        PdmObjectBase.__init__(self, pb2_object, channel)
        if ElasticProperties.__custom_init__ is not None:
            ElasticProperties.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def add_property_scaling(self, formation="", facies="", property="", scale=0):
        """
        Add Elastic Property Scaling

        Arguments:
            formation (str): Formation
            facies (str): Facies
            property (str): Property
            scale (float): Scale
        Returns:
            ElasticPropertyScaling
        """
        return self._call_pdm_method("AddPropertyScaling", formation=formation, facies=facies, property=property, scale=scale)


    def property_scaling_collection(self):
        """PropertyScalingCollection

        Returns:
             ElasticPropertyScalingCollection
        """
        children = self.children("PropertyScalingCollection", ElasticPropertyScalingCollection)
        return children[0] if len(children) > 0 else None


class NamedObject(PdmObjectBase):
    """
    Attributes:
        name (str): Name
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.name = ""
        PdmObjectBase.__init__(self, pb2_object, channel)
        if NamedObject.__custom_init__ is not None:
            NamedObject.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class CheckableNamedObject(NamedObject):
    """
    Attributes:
        is_checked (str): Active
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.is_checked = True
        NamedObject.__init__(self, pb2_object, channel)
        if CheckableNamedObject.__custom_init__ is not None:
            CheckableNamedObject.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class ElasticPropertyScaling(CheckableNamedObject):
    """
    Attributes:
        facies (str): Facies
        formation (str): Formation
        property (str): One of [UNDEFINED, FACIES, LAYERS, POROSITY, PERMEABILITY_X, PERMEABILITY_Z, INITIAL_PRESSURE, PRESSURE, STRESS, INITIAL_STRESS, STRESS_GRADIENT, YOUNGS_MODULUS, POISSONS_RATIO, K_IC, PROPPANT_EMBEDMENT, BIOT_COEFFICIENT, K0, FLUID_LOSS_COEFFICIENT, SPURT_LOSS, TEMPERATURE, RELATIVE_PERMEABILITY_FACTOR, PORO_ELASTIC_CONSTANT, THERMAL_EXPANSION_COEFFICIENT, IMMOBILE_FLUID_SATURATION, NET_TO_GROSS, POROSITY_UNSCALED, EQLNUM, PRESSURE_GRADIENT, FORMATIONS]
        scale (float): Scale
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.facies = ""
        self.formation = ""
        self.property = "YOUNGS_MODULUS"
        self.scale = 1
        CheckableNamedObject.__init__(self, pb2_object, channel)
        if ElasticPropertyScaling.__custom_init__ is not None:
            ElasticPropertyScaling.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class ElasticPropertyScalingCollection(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        PdmObjectBase.__init__(self, pb2_object, channel)
        if ElasticPropertyScalingCollection.__custom_init__ is not None:
            ElasticPropertyScalingCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def elastic_property_scalings(self):
        """Elastic Property Scalings

        Returns:
             List of ElasticPropertyScaling
        """
        return self.children("ElasticPropertyScalings", ElasticPropertyScaling)


class SurfaceInterface(PdmObjectBase):
    """
    Attributes:
        depth_offset (float): Depth Offset
        surface_user_decription (str): Name
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.depth_offset = 0
        self.surface_user_decription = ""
        PdmObjectBase.__init__(self, pb2_object, channel)
        if SurfaceInterface.__custom_init__ is not None:
            SurfaceInterface.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def export_to_file(self, file_name=""):
        """
        Export a surface to file

        Arguments:
            file_name (str): Filename to export surface to
        Returns:
            DataContainerString
        """
        return self._call_pdm_method("ExportToFile", file_name=file_name)


class EnsembleStatisticsSurface(SurfaceInterface):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        SurfaceInterface.__init__(self, pb2_object, channel)
        if EnsembleStatisticsSurface.__custom_init__ is not None:
            EnsembleStatisticsSurface.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class SurfaceCollection(PdmObjectBase):
    """
    Attributes:
        surface_user_decription (str): Name
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.surface_user_decription = "Surfaces"
        PdmObjectBase.__init__(self, pb2_object, channel)
        if SurfaceCollection.__custom_init__ is not None:
            SurfaceCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def add_folder(self, folder_name="Surfaces"):
        """
        Add a new surface folder

        Arguments:
            folder_name (str): New surface folder name
        Returns:
            SurfaceCollection
        """
        return self._call_pdm_method("AddFolder", folder_name=folder_name)


    def import_surface(self, file_name=""):
        """
        Import a new surface from file

        Arguments:
            file_name (str): Filename to import surface from
        Returns:
            Surface
        """
        return self._call_pdm_method("ImportSurface", file_name=file_name)


    def new_surface(self, case="", k_index=0):
        """
        Create a new surface

        Arguments:
            case (Case): 
            k_index (int): 
        Returns:
            GridCaseSurface
        """
        return self._call_pdm_method("NewSurface", case=case, k_index=k_index)


    def sub_collections(self):
        """Surfaces

        Returns:
             List of SurfaceCollection
        """
        return self.children("SubCollections", SurfaceCollection)


    def surfaces_field(self):
        """Surfaces

        Returns:
             List of SurfaceInterface
        """
        return self.children("SurfacesField", SurfaceInterface)


class EnsembleSurface(SurfaceCollection):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        SurfaceCollection.__init__(self, pb2_object, channel)
        if EnsembleSurface.__custom_init__ is not None:
            EnsembleSurface.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class EnsembleWellLogs(NamedObject):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        NamedObject.__init__(self, pb2_object, channel)
        if EnsembleWellLogs.__custom_init__ is not None:
            EnsembleWellLogs.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class FaciesInitialPressureConfig(PdmObjectBase):
    """
    Attributes:
        facies_name (str): Facies
        facies_value (int): Value
        fraction (float): ? Pressure Fraction
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.facies_name = ""
        self.facies_value = 0
        self.fraction = 0
        PdmObjectBase.__init__(self, pb2_object, channel)
        if FaciesInitialPressureConfig.__custom_init__ is not None:
            FaciesInitialPressureConfig.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class FaciesProperties(PdmObjectBase):
    """
    Attributes:
        color_legend (str): Colors
        file_path (str): File Path
        properties_table (str): Properties Table
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.color_legend = ""
        self.file_path = ""
        self.properties_table = ""
        PdmObjectBase.__init__(self, pb2_object, channel)
        if FaciesProperties.__custom_init__ is not None:
            FaciesProperties.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def facies_definition(self):
        """

        Returns:
             EclipseResult
        """
        children = self.children("FaciesDefinition", EclipseResult)
        return children[0] if len(children) > 0 else None


class SummaryCase(PdmObjectBase):
    """
    The Base Class for all Summary Cases

    Attributes:
        auto_shorty_name (str): Use Auto Display Name
        id (int): Case ID
        name_setting (str): One of [FULL_CASE_NAME, SHORT_CASE_NAME, CUSTOM_NAME]
        short_name (str): Display Name
        summary_header_filename (str): Summary Header File
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.auto_shorty_name = False
        self.id = -1
        self.name_setting = "FULL_CASE_NAME"
        self.short_name = ""
        self.summary_header_filename = ""
        PdmObjectBase.__init__(self, pb2_object, channel)
        if SummaryCase.__custom_init__ is not None:
            SummaryCase.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def available_addresses(self, ):
        """
        

        Arguments:
            
        Returns:
            DataContainerString
        """
        return self._call_pdm_method("availableAddresses")


    def available_time_steps(self, ):
        """
        

        Arguments:
            
        Returns:
            DataContainerTime
        """
        return self._call_pdm_method("availableTimeSteps")


    def resample_values(self, address="", resampling_period=""):
        """
        

        Arguments:
            address (str): Formatted address specifying the summary vector
            resampling_period (str): Resampling Period
        Returns:
            ResampleData
        """
        return self._call_pdm_method("resampleValues", address=address, resampling_period=resampling_period)


    def summary_vector_values(self, address=""):
        """
        Get all values for a summary vector

        Arguments:
            address (str): Formatted address specifying the summary vector
        Returns:
            DataContainerFloat
        """
        return self._call_pdm_method("summaryVectorValues", address=address)


class FileSummaryCase(SummaryCase):
    """
    A Summary Case based on SMSPEC files

    Attributes:
        include_restart_files (str): Include Restart Files
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.include_restart_files = False
        SummaryCase.__init__(self, pb2_object, channel)
        if FileSummaryCase.__custom_init__ is not None:
            FileSummaryCase.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class FractureTemplateCollection(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        PdmObjectBase.__init__(self, pb2_object, channel)
        if FractureTemplateCollection.__custom_init__ is not None:
            FractureTemplateCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def append_fracture_template(self, file_path=""):
        """
        Create a new StimPlan Fracture Template

        Arguments:
            file_path (str): File Path to StimPlan Countour File
        Returns:
            StimPlanFractureTemplate
        """
        return self._call_pdm_method("AppendFractureTemplate", file_path=file_path)


class GeoMechPart(CheckableNamedObject):
    """
    Attributes:
        part_id (int): Part Id
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.part_id = 0
        CheckableNamedObject.__init__(self, pb2_object, channel)
        if GeoMechPart.__custom_init__ is not None:
            GeoMechPart.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class GeoMechPartCollection(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        PdmObjectBase.__init__(self, pb2_object, channel)
        if GeoMechPartCollection.__custom_init__ is not None:
            GeoMechPartCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def parts(self):
        """Parts

        Returns:
             List of GeoMechPart
        """
        return self.children("Parts", GeoMechPart)


class ViewWindow(PdmObjectBase):
    """
    The Base Class for all Views and Plots in ResInsight

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        PdmObjectBase.__init__(self, pb2_object, channel)
        if ViewWindow.__custom_init__ is not None:
            ViewWindow.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class View(ViewWindow):
    """
    Attributes:
        background_color (str): Background
        current_time_step (int): Current Time Step
        disable_lighting (str): Disable Results Lighting
        grid_z_scale (float): Z Scale
        id (int): View ID
        perspective_projection (str): Perspective Projection
        show_grid_box (str): Show Grid Box
        show_z_scale (str): Show Z Scale Label
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.background_color = "#3b3b3b"
        self.current_time_step = 0
        self.disable_lighting = False
        self.grid_z_scale = 5
        self.id = -1
        self.perspective_projection = True
        self.show_grid_box = True
        self.show_z_scale = True
        ViewWindow.__init__(self, pb2_object, channel)
        if View.__custom_init__ is not None:
            View.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class GeoMechView(View):
    """
    The Geomechanical 3d View

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        View.__init__(self, pb2_object, channel)
        if GeoMechView.__custom_init__ is not None:
            GeoMechView.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class GridCaseSurface(SurfaceInterface):
    """
    Attributes:
        slice_index (int): Slice Index (K)
        source_case (str): Source Case
        watertight (str): Watertight Surface (fill gaps)
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.slice_index = 1
        self.source_case = ""
        self.watertight = False
        SurfaceInterface.__init__(self, pb2_object, channel)
        if GridCaseSurface.__custom_init__ is not None:
            GridCaseSurface.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class GridSummaryCase(SummaryCase):
    """
    A Summary Case based on extracting grid data.

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        SummaryCase.__init__(self, pb2_object, channel)
        if GridSummaryCase.__custom_init__ is not None:
            GridSummaryCase.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class WellPath(PdmObjectBase):
    """
    A ResInsight Well Path

    Attributes:
        name (str): Name
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.name = ""
        PdmObjectBase.__init__(self, pb2_object, channel)
        if WellPath.__custom_init__ is not None:
            WellPath.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def add_fracture(self, measured_depth=0, stim_plan_fracture_template=""):
        """
        Add StimPlan Fracture

        Arguments:
            measured_depth (float): 
            stim_plan_fracture_template (StimPlanFractureTemplate): StimPlan Fracture Template
        Returns:
            WellPathFracture
        """
        return self._call_pdm_method("AddFracture", measured_depth=measured_depth, stim_plan_fracture_template=stim_plan_fracture_template)


class ModeledWellPath(WellPath):
    """
    A Well Path created interactively in ResInsight

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        WellPath.__init__(self, pb2_object, channel)
        if ModeledWellPath.__custom_init__ is not None:
            ModeledWellPath.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def append_lateral(self, tie_in_depth=0, lateral_name=""):
        """
        Append Well Path Lateral

        Arguments:
            tie_in_depth (float): Measured Depth on the Parent Well Path
            lateral_name (str): Lateral Name
        Returns:
            ModeledWellPath
        """
        return self._call_pdm_method("AppendLateral", tie_in_depth=tie_in_depth, lateral_name=lateral_name)


    def append_perforation_interval(self, start_md=0, end_md=0, diameter=0, skin_factor=0):
        """
        Append Perforation Interval

        Arguments:
            start_md (float): Start Measured Depth
            end_md (float): End Measured Depth
            diameter (float): Diameter
            skin_factor (float): Skin Factor
        Returns:
            Perforation
        """
        return self._call_pdm_method("AppendPerforationInterval", start_md=start_md, end_md=end_md, diameter=diameter, skin_factor=skin_factor)


    def well_path_geometry(self):
        """Trajectory

        Returns:
             WellPathGeometry
        """
        children = self.children("WellPathGeometry", WellPathGeometry)
        return children[0] if len(children) > 0 else None


class NonNetLayers(PdmObjectBase):
    """
    Attributes:
        cutoff (float): Cutoff
        facies (str): Facies
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.cutoff = 0
        self.facies = ""
        PdmObjectBase.__init__(self, pb2_object, channel)
        if NonNetLayers.__custom_init__ is not None:
            NonNetLayers.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def facies_definition(self):
        """

        Returns:
             EclipseResult
        """
        children = self.children("FaciesDefinition", EclipseResult)
        return children[0] if len(children) > 0 else None


class PressureTable(PdmObjectBase):
    """
    Attributes:
        pressure_date (str): Pressure Date
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.pressure_date = ""
        PdmObjectBase.__init__(self, pb2_object, channel)
        if PressureTable.__custom_init__ is not None:
            PressureTable.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def items(self):
        """Pressure Table Items

        Returns:
             List of PressureTableItem
        """
        return self.children("Items", PressureTableItem)


class PressureTableItem(PdmObjectBase):
    """
    Attributes:
        depth (float): Depth TVDMSL [m]
        initial_pressure (float): Initial Pressure [Bar]
        pressure (float): Pressure [Bar]
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.depth = 0
        self.initial_pressure = 0
        self.pressure = 0
        PdmObjectBase.__init__(self, pb2_object, channel)
        if PressureTableItem.__custom_init__ is not None:
            PressureTableItem.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class GeoMechCase(Case):
    """
    The Abaqus Based GeoMech Case

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        Case.__init__(self, pb2_object, channel)
        if GeoMechCase.__custom_init__ is not None:
            GeoMechCase.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def views(self):
        """All GeoMech Views in the Case

        Returns:
             List of GeoMechView
        """
        return self.children("Views", GeoMechView)


class Project(PdmObjectBase):
    """
    The ResInsight Project

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        PdmObjectBase.__init__(self, pb2_object, channel)
        if Project.__custom_init__ is not None:
            Project.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def import_summary_case(self, file_name=""):
        """
        Import Summary Case

        Arguments:
            file_name (str): 
        Returns:
            FileSummaryCase
        """
        return self._call_pdm_method("importSummaryCase", file_name=file_name)


    def summary_case(self, case_id=2092987072):
        """
        Find Summary Case

        Arguments:
            case_id (int): 
        Returns:
            FileSummaryCase
        """
        return self._call_pdm_method("summaryCase", case_id=case_id)


    def surface_folder(self, folder_name=""):
        """
        Get Surface Folder

        Arguments:
            folder_name (str): 
        Returns:
            SurfaceCollection
        """
        return self._call_pdm_method("surfaceFolder", folder_name=folder_name)


class ResampleData(PdmObjectBase):
    """
    Attributes:
        time_steps (List of time): Time Steps
        values (List of float): Values
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.time_steps = []
        self.values = []
        PdmObjectBase.__init__(self, pb2_object, channel)
        if ResampleData.__custom_init__ is not None:
            ResampleData.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class EclipseView(View):
    """
    The Eclipse 3d Reservoir View

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        View.__init__(self, pb2_object, channel)
        if EclipseView.__custom_init__ is not None:
            EclipseView.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def cell_result(self):
        """Cell Result

        Returns:
             CellColors
        """
        children = self.children("CellResult", CellColors)
        return children[0] if len(children) > 0 else None


    def cell_result_data(self):
        """Current Eclipse Cell Result

        Returns:
             str
        """
        return self._call_get_method("CellResultData")


    def set_cell_result_data(self, values):
        """Set Current Eclipse Cell Result

        Arguments:
            values (str): data
        """
        self._call_set_method("CellResultData", values)


class EclipseResult(PdmObjectBase):
    """
    An eclipse result definition

    Attributes:
        flow_tracer_selection_mode (str): One of [FLOW_TR_INJ_AND_PROD, FLOW_TR_PRODUCERS, FLOW_TR_INJECTORS, FLOW_TR_BY_SELECTION]
        phase_selection (str): One of [PHASE_ALL, PHASE_OIL, PHASE_GAS, PHASE_WAT]
        porosity_model_type (str): One of [MATRIX_MODEL, FRACTURE_MODEL]
        result_type (str): One of [DYNAMIC_NATIVE, STATIC_NATIVE, SOURSIMRL, GENERATED, INPUT_PROPERTY, FORMATION_NAMES, ALLAN_DIAGRAMS, FLOW_DIAGNOSTICS, INJECTION_FLOODING]
        result_variable (str): Variable
        selected_injector_tracers (List of str): Injector Tracers
        selected_producer_tracers (List of str): Producer Tracers
        selected_souring_tracers (List of str): Tracers
        show_only_visible_categories_in_legend (str): Show Only Visible Categories In Legend
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.flow_tracer_selection_mode = "FLOW_TR_INJ_AND_PROD"
        self.phase_selection = "PHASE_ALL"
        self.porosity_model_type = "MATRIX_MODEL"
        self.result_type = "DYNAMIC_NATIVE"
        self.result_variable = "None"
        self.selected_injector_tracers = []
        self.selected_producer_tracers = []
        self.selected_souring_tracers = []
        self.show_only_visible_categories_in_legend = True
        PdmObjectBase.__init__(self, pb2_object, channel)
        if EclipseResult.__custom_init__ is not None:
            EclipseResult.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class CellColors(EclipseResult):
    """
    Eclipse Cell Colors class

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        EclipseResult.__init__(self, pb2_object, channel)
        if CellColors.__custom_init__ is not None:
            CellColors.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class CommandRouter(PdmObjectBase):
    """
    The CommandRouter is used to call code independent to the project

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        PdmObjectBase.__init__(self, pb2_object, channel)
        if CommandRouter.__custom_init__ is not None:
            CommandRouter.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def extract_surfaces(self, grid_model_filename="", layers=[], minimum_i=-1, maximum_i=-1, minimum_j=-1, maximum_j=-1):
        """
        Extract Layer Surface

        Arguments:
            grid_model_filename (str): 
            layers (List of int): 
            minimum_i (int): 
            maximum_i (int): 
            minimum_j (int): 
            maximum_j (int): 
        Returns:
            
        """
        return self._call_pdm_method("ExtractSurfaces", grid_model_filename=grid_model_filename, layers=layers, minimum_i=minimum_i, maximum_i=maximum_i, minimum_j=minimum_j, maximum_j=maximum_j)


class EclipseContourMap(EclipseView):
    """
    A contour map for Eclipse cases

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        EclipseView.__init__(self, pb2_object, channel)
        if EclipseContourMap.__custom_init__ is not None:
            EclipseContourMap.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class GeoMechContourMap(GeoMechView):
    """
    A contour map for GeoMech cases

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        GeoMechView.__init__(self, pb2_object, channel)
        if GeoMechContourMap.__custom_init__ is not None:
            GeoMechContourMap.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class GridCaseGroup(PdmObjectBase):
    """
    A statistics case group

    Attributes:
        group_id (int): Case Group ID
        user_description (str): Name
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.group_id = -1
        self.user_description = "Grid Case Group"
        PdmObjectBase.__init__(self, pb2_object, channel)
        if GridCaseGroup.__custom_init__ is not None:
            GridCaseGroup.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class MudWeightWindowParameters(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        PdmObjectBase.__init__(self, pb2_object, channel)
        if MudWeightWindowParameters.__custom_init__ is not None:
            MudWeightWindowParameters.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class FractureTemplate(PdmObjectBase):
    """
    Attributes:
        orientation (str): One of [Azimuth, Longitudinal, Transverse]
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.orientation = "Transverse"
        PdmObjectBase.__init__(self, pb2_object, channel)
        if FractureTemplate.__custom_init__ is not None:
            FractureTemplate.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class StimPlanFractureTemplate(FractureTemplate):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        FractureTemplate.__init__(self, pb2_object, channel)
        if StimPlanFractureTemplate.__custom_init__ is not None:
            StimPlanFractureTemplate.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class StimPlanModel(CheckableNamedObject):
    """
    Attributes:
        anchor_position (str): Anchor Position
        auto_compute_barrier (str): Auto Compute Barrier
        azimuth_angle (float): Azimuth Angle
        barrier (str): Barrier
        barrier_dip (float): Barrier Dip
        barrier_fault_name (str): Barrier Fault
        barrier_text_annotation (str): Barrier Text Annotation
        bounding_box_horizontal (float): Bounding Box Horizontal
        bounding_box_vertical (float): Bounding Box Vertical
        distance_to_barrier (float): Distance To Barrier [m]
        eclipse_case (str): Dynamic Case
        extraction_depth_bottom (float): Depth
        extraction_depth_top (float): Depth
        extraction_offset_bottom (float): Bottom Offset
        extraction_offset_top (float): Top Offset
        extraction_type (str): One of [TVT, TST]
        formation_dip (float): Formation Dip
        fracture_orientation (str): One of [Longitudinal, Transverse, Azimuth]
        initial_pressure_eclipse_case (str): Initial Pressure Case
        measured_depth (float): Measured Depth
        perforation_interval (str): Perforation Interval
        perforation_length (float): Perforation Length [m]
        poro_elastic_constant (float): Poro-Elastic Constant
        relative_permeability_factor (float): Relative Permeability Factor
        show_all_faults (str): Show All Faults
        show_only_barrier_fault (str): Show Only Barrier Fault
        static_eclipse_case (str): Static Case
        thermal_expansion_coefficient (float): Thermal Expansion Coefficient [1/C]
        thickness_direction (str): Thickness Direction
        thickness_direction_well_path (str): Thickness Direction Well Path
        time_step (int): Time Step
        use_detailed_fluid_loss (str): Use Detailed Fluid Loss
        well_penetration_layer (int): Well Penetration Layer
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.anchor_position = [0, 0, 0]
        self.auto_compute_barrier = True
        self.azimuth_angle = 0
        self.barrier = True
        self.barrier_dip = 0
        self.barrier_fault_name = ""
        self.barrier_text_annotation = ""
        self.bounding_box_horizontal = 50
        self.bounding_box_vertical = 100
        self.distance_to_barrier = 0
        self.eclipse_case = ""
        self.extraction_depth_bottom = -1
        self.extraction_depth_top = -1
        self.extraction_offset_bottom = -1
        self.extraction_offset_top = -1
        self.extraction_type = "TST"
        self.formation_dip = 0
        self.fracture_orientation = "Longitudinal"
        self.initial_pressure_eclipse_case = ""
        self.measured_depth = 0
        self.perforation_interval = ""
        self.perforation_length = 10
        self.poro_elastic_constant = 0
        self.relative_permeability_factor = 0.5
        self.show_all_faults = False
        self.show_only_barrier_fault = False
        self.static_eclipse_case = ""
        self.thermal_expansion_coefficient = 0
        self.thickness_direction = [0, 0, 0]
        self.thickness_direction_well_path = ""
        self.time_step = 0
        self.use_detailed_fluid_loss = True
        self.well_penetration_layer = 2
        CheckableNamedObject.__init__(self, pb2_object, channel)
        if StimPlanModel.__custom_init__ is not None:
            StimPlanModel.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def export_to_file(self, directory_path=""):
        """
        Export StimPlan Model Plot to File

        Arguments:
            directory_path (str): Directory Path
        Returns:
            StimPlanModel
        """
        return self._call_pdm_method("ExportToFile", directory_path=directory_path)


class StimPlanModelCollection(CheckableNamedObject):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        CheckableNamedObject.__init__(self, pb2_object, channel)
        if StimPlanModelCollection.__custom_init__ is not None:
            StimPlanModelCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def append_stim_plan_model(self, well_path="", measured_depth=0, stim_plan_model_template=""):
        """
        Create a new StimPlan Model

        Arguments:
            well_path (WellPathBase): Well Path
            measured_depth (float): 
            stim_plan_model_template (StimPlanModelTemplate): StimPlan Model Template
        Returns:
            StimPlanModel
        """
        return self._call_pdm_method("AppendStimPlanModel", well_path=well_path, measured_depth=measured_depth, stim_plan_model_template=stim_plan_model_template)


    def stim_plan_models(self):
        """

        Returns:
             List of StimPlanModel
        """
        return self.children("StimPlanModels", StimPlanModel)


class PlotWindow(ViewWindow):
    """
    The Abstract base class for all MDI Windows in the Plot Window

    Attributes:
        id (int): View ID
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.id = -1
        ViewWindow.__init__(self, pb2_object, channel)
        if PlotWindow.__custom_init__ is not None:
            PlotWindow.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class DepthTrackPlot(PlotWindow):
    """
    Attributes:
        auto_scale_depth_enabled (str): Auto Scale
        axis_title_font_size (str): One of [XX_Small, X_Small, Small, Medium, Large, X_Large, XX_Large]
        axis_value_font_size (str): One of [XX_Small, X_Small, Small, Medium, Large, X_Large, XX_Large]
        depth_type (str): One of [MEASURED_DEPTH, TRUE_VERTICAL_DEPTH, PSEUDO_LENGTH, CONNECTION_NUMBER, TRUE_VERTICAL_DEPTH_RKB]
        depth_unit (str): One of [UNIT_METER, UNIT_FEET, UNIT_NONE]
        maximum_depth (float): Max
        minimum_depth (float): Min
        show_depth_grid_lines (str): One of [GRID_X_NONE, GRID_X_MAJOR, GRID_X_MAJOR_AND_MINOR]
        sub_title_font_size (str): One of [XX_Small, X_Small, Small, Medium, Large, X_Large, XX_Large]
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.auto_scale_depth_enabled = True
        self.axis_title_font_size = "Medium"
        self.axis_value_font_size = "Medium"
        self.depth_type = "MEASURED_DEPTH"
        self.depth_unit = "UNIT_METER"
        self.maximum_depth = 1000
        self.minimum_depth = 0
        self.show_depth_grid_lines = "GRID_X_MAJOR"
        self.sub_title_font_size = "Medium"
        PlotWindow.__init__(self, pb2_object, channel)
        if DepthTrackPlot.__custom_init__ is not None:
            DepthTrackPlot.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class StimPlanModelPlot(DepthTrackPlot):
    """
    A fracture model plot

    Attributes:
        eclipse_case (str): Case
        stim_plan_model (str): StimPlan Model
        time_step (int): Time Step
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.eclipse_case = ""
        self.stim_plan_model = ""
        self.time_step = 0
        DepthTrackPlot.__init__(self, pb2_object, channel)
        if StimPlanModelPlot.__custom_init__ is not None:
            StimPlanModelPlot.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class StimPlanModelPlotCollection(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        PdmObjectBase.__init__(self, pb2_object, channel)
        if StimPlanModelPlotCollection.__custom_init__ is not None:
            StimPlanModelPlotCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def append_stim_plan_model_plot(self, stim_plan_model=""):
        """
        Create a new StimPlan Model

        Arguments:
            stim_plan_model (StimPlanModel): StimPlan Model
        Returns:
            StimPlanModelPlot
        """
        return self._call_pdm_method("AppendStimPlanModelPlot", stim_plan_model=stim_plan_model)


    def stim_plan_model_plots(self):
        """

        Returns:
             List of StimPlanModelPlot
        """
        return self.children("StimPlanModelPlots", StimPlanModelPlot)


class StimPlanModelTemplate(NamedObject):
    """
    Attributes:
        default_permeability (float): Default Permeability
        default_porosity (float): Default Porosity
        dynamic_eclipse_case (str): Dynamic Case
        id (int): ID
        initial_pressure_eclipse_case (str): Initial Pressure Case
        overburden_facies (str): Overburden Facies
        overburden_fluid_density (float): Overburden Fluid Density [g/cm^3]
        overburden_formation (str): Overburden Formation
        overburden_height (float): Overburden Height
        overburden_permeability (float): Overburden Permeability
        overburden_porosity (float): Overburden Porosity
        reference_temperature (float): Temperature [C]
        reference_temperature_depth (float): Temperature Depth [m]
        reference_temperature_gradient (float): Temperature Gradient [C/m]
        static_eclipse_case (str): Static Case
        stress_depth (float): Stress Depth
        time_step (int): Time Step
        underburden_facies (str): Underburden Facies
        underburden_fluid_density (float): Underburden Fluid Density [g/cm^3]
        underburden_formation (str): Underburden Formation
        underburden_height (float): Underburden Height
        underburden_permeability (float): Underburden Permeability
        underburden_porosity (float): Underburden Porosity
        vertical_stress (float): Vertical Stress
        vertical_stress_gradient (float): Vertical Stress Gradient
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.default_permeability = 0.0001
        self.default_porosity = 0.01
        self.dynamic_eclipse_case = ""
        self.id = -1
        self.initial_pressure_eclipse_case = ""
        self.overburden_facies = ""
        self.overburden_fluid_density = 1.03
        self.overburden_formation = ""
        self.overburden_height = 50
        self.overburden_permeability = 1e-05
        self.overburden_porosity = 0
        self.reference_temperature = 70
        self.reference_temperature_depth = 2500
        self.reference_temperature_gradient = 0.025
        self.static_eclipse_case = ""
        self.stress_depth = 1000
        self.time_step = 0
        self.underburden_facies = ""
        self.underburden_fluid_density = 1.03
        self.underburden_formation = ""
        self.underburden_height = 50
        self.underburden_permeability = 1e-05
        self.underburden_porosity = 0
        self.vertical_stress = 238
        self.vertical_stress_gradient = 0.238
        NamedObject.__init__(self, pb2_object, channel)
        if StimPlanModelTemplate.__custom_init__ is not None:
            StimPlanModelTemplate.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def elastic_properties(self):
        """Elastic Properties

        Returns:
             ElasticProperties
        """
        children = self.children("ElasticProperties", ElasticProperties)
        return children[0] if len(children) > 0 else None


    def facies_initial_pressure_configs(self):
        """Facies Initial Pressure Configs

        Returns:
             List of FaciesInitialPressureConfig
        """
        return self.children("FaciesInitialPressureConfigs", FaciesInitialPressureConfig)


    def facies_properties(self):
        """Facies Properties

        Returns:
             FaciesProperties
        """
        children = self.children("FaciesProperties", FaciesProperties)
        return children[0] if len(children) > 0 else None


    def non_net_layers(self):
        """Non-Net Layers

        Returns:
             NonNetLayers
        """
        children = self.children("NonNetLayers", NonNetLayers)
        return children[0] if len(children) > 0 else None


    def pressure_table(self):
        """Pressure Table

        Returns:
             PressureTable
        """
        children = self.children("PressureTable", PressureTable)
        return children[0] if len(children) > 0 else None


class StimPlanModelTemplateCollection(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        PdmObjectBase.__init__(self, pb2_object, channel)
        if StimPlanModelTemplateCollection.__custom_init__ is not None:
            StimPlanModelTemplateCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def append_stim_plan_model_template(self, eclipse_case="", time_step=2097184, facies_properties_file_path="", elastic_properties_file_path=""):
        """
        Create a new StimPlan Model Template

        Arguments:
            eclipse_case (RimReservoir): Eclipse Case
            time_step (int): Time Step
            facies_properties_file_path (str): Facies Properties File Path
            elastic_properties_file_path (str): Elastic Properties File Path
        Returns:
            StimPlanModelTemplate
        """
        return self._call_pdm_method("AppendStimPlanModelTemplate", eclipse_case=eclipse_case, time_step=time_step, facies_properties_file_path=facies_properties_file_path, elastic_properties_file_path=elastic_properties_file_path)


    def stim_plan_model_templates(self):
        """StimPlan Model Templates

        Returns:
             List of StimPlanModelTemplate
        """
        return self.children("StimPlanModelTemplates", StimPlanModelTemplate)


class SummaryCaseSubCollection(PdmObjectBase):
    """
    Attributes:
        id (int): Ensemble ID
        is_ensemble (str): Is Ensemble
        name_count (str): Name
        summary_collection_name (str): Name
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.id = -1
        self.is_ensemble = False
        self.name_count = "Group"
        self.summary_collection_name = "Group"
        PdmObjectBase.__init__(self, pb2_object, channel)
        if SummaryCaseSubCollection.__custom_init__ is not None:
            SummaryCaseSubCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class Plot(PlotWindow):
    """
    The Abstract Base Class for all Plot Objects

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        PlotWindow.__init__(self, pb2_object, channel)
        if Plot.__custom_init__ is not None:
            Plot.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class SummaryPlot(Plot):
    """
    A Summary Plot

    Attributes:
        is_using_auto_name (str): Auto Title
        normalize_curve_y_values (str): Normalize all curves
        plot_description (str): Name
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.is_using_auto_name = True
        self.normalize_curve_y_values = False
        self.plot_description = "Summary Plot"
        Plot.__init__(self, pb2_object, channel)
        if SummaryPlot.__custom_init__ is not None:
            SummaryPlot.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class SummaryPlotCollection(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        PdmObjectBase.__init__(self, pb2_object, channel)
        if SummaryPlotCollection.__custom_init__ is not None:
            SummaryPlotCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def new_summary_plot(self, summary_cases=[], ensemble="", address=""):
        """
        Create a new Summary Plot

        Arguments:
            summary_cases (List of SummaryCase): Summary Cases
            ensemble (SummaryCaseSubCollection): Ensemble
            address (str): Formatted address string specifying the plot options
        Returns:
            SummaryPlot
        """
        return self._call_pdm_method("NewSummaryPlot", summary_cases=summary_cases, ensemble=ensemble, address=address)


class Surface(SurfaceInterface):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        SurfaceInterface.__init__(self, pb2_object, channel)
        if Surface.__custom_init__ is not None:
            Surface.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class WbsParameters(PdmObjectBase):
    """
    Attributes:
        df_source (str): One of [GRID, LAS_FILE, ELEMENT_PROPERTY_TABLE, USER_DEFINED, HYDROSTATIC, DERIVED_FROM_K0FG, PROPORTIONAL_TO_SH, UNDEFINED]
        fg_multiplier (float): SH Multiplier for FG in Shale
        fg_shale_source (str): One of [GRID, LAS_FILE, ELEMENT_PROPERTY_TABLE, USER_DEFINED, HYDROSTATIC, DERIVED_FROM_K0FG, PROPORTIONAL_TO_SH, UNDEFINED]
        k0_fg_source (str): One of [GRID, LAS_FILE, ELEMENT_PROPERTY_TABLE, USER_DEFINED, HYDROSTATIC, DERIVED_FROM_K0FG, PROPORTIONAL_TO_SH, UNDEFINED]
        k0_sh_source (str): One of [GRID, LAS_FILE, ELEMENT_PROPERTY_TABLE, USER_DEFINED, HYDROSTATIC, DERIVED_FROM_K0FG, PROPORTIONAL_TO_SH, UNDEFINED]
        obg0_source (str): One of [GRID, LAS_FILE, ELEMENT_PROPERTY_TABLE, USER_DEFINED, HYDROSTATIC, DERIVED_FROM_K0FG, PROPORTIONAL_TO_SH, UNDEFINED]
        poission_ratio_source (str): One of [GRID, LAS_FILE, ELEMENT_PROPERTY_TABLE, USER_DEFINED, HYDROSTATIC, DERIVED_FROM_K0FG, PROPORTIONAL_TO_SH, UNDEFINED]
        pore_pressure_non_reservoir_source (str): One of [GRID, LAS_FILE, ELEMENT_PROPERTY_TABLE, USER_DEFINED, HYDROSTATIC, DERIVED_FROM_K0FG, PROPORTIONAL_TO_SH, UNDEFINED]
        pore_pressure_reservoir_source (str): One of [GRID, LAS_FILE, ELEMENT_PROPERTY_TABLE, USER_DEFINED, HYDROSTATIC, DERIVED_FROM_K0FG, PROPORTIONAL_TO_SH, UNDEFINED]
        ucs_source (str): One of [GRID, LAS_FILE, ELEMENT_PROPERTY_TABLE, USER_DEFINED, HYDROSTATIC, DERIVED_FROM_K0FG, PROPORTIONAL_TO_SH, UNDEFINED]
        user_df (float): User Defined DF
        user_k0_fg (float): User Defined K0_FG
        user_k0_sh (float): User Defined K0_SH
        user_poisson_ratio (float): User Defined Poisson Ratio
        user_pp_non_reservoir (float):   Multiplier of hydrostatic PP
        user_ucs (float): User Defined UCS [bar]
        water_density (float): Density of Sea Water [g/cm^3]
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.df_source = "LAS_FILE"
        self.fg_multiplier = 1.05
        self.fg_shale_source = "DERIVED_FROM_K0FG"
        self.k0_fg_source = "LAS_FILE"
        self.k0_sh_source = "LAS_FILE"
        self.obg0_source = "GRID"
        self.poission_ratio_source = "LAS_FILE"
        self.pore_pressure_non_reservoir_source = "LAS_FILE"
        self.pore_pressure_reservoir_source = "GRID"
        self.ucs_source = "LAS_FILE"
        self.user_df = 0.7
        self.user_k0_fg = 0.75
        self.user_k0_sh = 0.65
        self.user_poisson_ratio = 0.35
        self.user_pp_non_reservoir = 1
        self.user_ucs = 100
        self.water_density = 1.03
        PdmObjectBase.__init__(self, pb2_object, channel)
        if WbsParameters.__custom_init__ is not None:
            WbsParameters.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class SimulationWell(PdmObjectBase):
    """
    An Eclipse Simulation Well

    Attributes:
        name (str): Name
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.name = ""
        PdmObjectBase.__init__(self, pb2_object, channel)
        if SimulationWell.__custom_init__ is not None:
            SimulationWell.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class WellLogPlot(DepthTrackPlot):
    """
    A Well Log Plot With a shared Depth Axis and Multiple Tracks

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        DepthTrackPlot.__init__(self, pb2_object, channel)
        if WellLogPlot.__custom_init__ is not None:
            WellLogPlot.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def new_well_log_track(self, title="", case="", well_path=""):
        """
        Create a new well log track

        Arguments:
            title (str): Title
            case (RimReservoir): Case
            well_path (WellPathBase): Well Path
        Returns:
            WellLogPlotTrack
        """
        return self._call_pdm_method("NewWellLogTrack", title=title, case=case, well_path=well_path)


class WellBoreStabilityPlot(WellLogPlot):
    """
    A GeoMechanical Well Bore Stabilit Plot

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        WellLogPlot.__init__(self, pb2_object, channel)
        if WellBoreStabilityPlot.__custom_init__ is not None:
            WellBoreStabilityPlot.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def parameters(self):
        """Well Bore Stability Parameters

        Returns:
             WbsParameters
        """
        children = self.children("Parameters", WbsParameters)
        return children[0] if len(children) > 0 else None


class PlotCurve(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        PdmObjectBase.__init__(self, pb2_object, channel)
        if PlotCurve.__custom_init__ is not None:
            PlotCurve.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class WellLogPlotCurve(PlotCurve):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        PlotCurve.__init__(self, pb2_object, channel)
        if WellLogPlotCurve.__custom_init__ is not None:
            WellLogPlotCurve.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class WellLogExtractionCurve(WellLogPlotCurve):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        WellLogPlotCurve.__init__(self, pb2_object, channel)
        if WellLogExtractionCurve.__custom_init__ is not None:
            WellLogExtractionCurve.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class WellLogPlotCollection(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        PdmObjectBase.__init__(self, pb2_object, channel)
        if WellLogPlotCollection.__custom_init__ is not None:
            WellLogPlotCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def new_well_log_plot(self, case="", well_path="", property_type="", property_name="", time_step=-1506042864):
        """
        Create a new well log plot

        Arguments:
            case (RimReservoir): Case
            well_path (WellPathBase): Well Path
            property_type (str): Property Type
            property_name (str): Property Name
            time_step (int): Time Step
        Returns:
            WellLogPlot
        """
        return self._call_pdm_method("NewWellLogPlot", case=case, well_path=well_path, property_type=property_type, property_name=property_name, time_step=time_step)


    def well_log_plots(self):
        """

        Returns:
             List of WellLogPlot
        """
        return self.children("WellLogPlots", WellLogPlot)


class WellLogPlotTrack(Plot):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        Plot.__init__(self, pb2_object, channel)
        if WellLogPlotTrack.__custom_init__ is not None:
            WellLogPlotTrack.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def add_extraction_curve(self, case="", well_path="", property_type="", property_name="", time_step=-1506042864):
        """
        Create a well log extraction curve

        Arguments:
            case (RimReservoir): Case
            well_path (WellPathBase): Well Path
            property_type (str): Property Type
            property_name (str): Property Name
            time_step (int): Time Step
        Returns:
            WellLogExtractionCurve
        """
        return self._call_pdm_method("AddExtractionCurve", case=case, well_path=well_path, property_type=property_type, property_name=property_name, time_step=time_step)


class FileWellPath(WellPath):
    """
    Well Paths Loaded From File

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        WellPath.__init__(self, pb2_object, channel)
        if FileWellPath.__custom_init__ is not None:
            FileWellPath.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class WellPathGeometry(PdmObjectBase):
    """
    Class containing the geometry of a modeled Well Path

    Attributes:
        air_gap (float): Air Gap
        attached_to_parent_well (str): Attached to Parent Well
        link_reference_point_updates (str): Link Reference Point
        md_at_first_target (float): MD at First Target
        reference_point (str): UTM Reference Point
        show_spheres (str): Spheres
        use_auto_generated_target_at_sea_level (str): Generate Target at Sea Level
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.air_gap = 0
        self.attached_to_parent_well = False
        self.link_reference_point_updates = False
        self.md_at_first_target = 0
        self.reference_point = [0, 0, 0]
        self.show_spheres = True
        self.use_auto_generated_target_at_sea_level = True
        PdmObjectBase.__init__(self, pb2_object, channel)
        if WellPathGeometry.__custom_init__ is not None:
            WellPathGeometry.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def append_well_target(self, coordinate=[0, 0, 0], absolute=False):
        """
        Create and Add New Well Target

        Arguments:
            coordinate (class cvf::Vector3<double>): Coordinate
            absolute (bool): Relative or Absolute Coordinate
        Returns:
            WellPathTarget
        """
        return self._call_pdm_method("AppendWellTarget", coordinate=coordinate, absolute=absolute)


    def auto_generated_target(self):
        """Auto Generated Target

        Returns:
             WellPathTarget
        """
        children = self.children("AutoGeneratedTarget", WellPathTarget)
        return children[0] if len(children) > 0 else None


    def well_path_targets(self):
        """Well Targets

        Returns:
             List of WellPathTarget
        """
        return self.children("WellPathTargets", WellPathTarget)


class WellPathTarget(PdmObjectBase):
    """
    Class containing the Well Target definition

    Attributes:
        azimuth (float): Azi(deg)
        dogleg1 (float): DL in
        dogleg2 (float): DL out
        inclination (float): Inc(deg)
        target_measured_depth (float): MD
        target_point (str): Relative Coord
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.azimuth = 0
        self.dogleg1 = 3
        self.dogleg2 = 3
        self.inclination = 0
        self.target_measured_depth = 0
        self.target_point = [0, 0, 0]
        PdmObjectBase.__init__(self, pb2_object, channel)
        if WellPathTarget.__custom_init__ is not None:
            WellPathTarget.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class WellPathCollection(PdmObjectBase):
    """
    Collection of Well Paths

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        PdmObjectBase.__init__(self, pb2_object, channel)
        if WellPathCollection.__custom_init__ is not None:
            WellPathCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def well_paths(self):
        """Well Paths

        Returns:
             List of WellPath
        """
        return self.children("WellPaths", WellPath)


def class_dict():
    classes = {}
    classes['Case'] = Case
    classes['CellColors'] = CellColors
    classes['CellFilterCollection'] = CellFilterCollection
    classes['CheckableNamedObject'] = CheckableNamedObject
    classes['CommandRouter'] = CommandRouter
    classes['DataContainerFloat'] = DataContainerFloat
    classes['DataContainerString'] = DataContainerString
    classes['DataContainerTime'] = DataContainerTime
    classes['DepthTrackPlot'] = DepthTrackPlot
    classes['EclipseCase'] = EclipseCase
    classes['EclipseContourMap'] = EclipseContourMap
    classes['EclipseResult'] = EclipseResult
    classes['EclipseView'] = EclipseView
    classes['ElasticProperties'] = ElasticProperties
    classes['ElasticPropertyScaling'] = ElasticPropertyScaling
    classes['ElasticPropertyScalingCollection'] = ElasticPropertyScalingCollection
    classes['EnsembleStatisticsSurface'] = EnsembleStatisticsSurface
    classes['EnsembleSurface'] = EnsembleSurface
    classes['EnsembleWellLogs'] = EnsembleWellLogs
    classes['FaciesInitialPressureConfig'] = FaciesInitialPressureConfig
    classes['FaciesProperties'] = FaciesProperties
    classes['FileSummaryCase'] = FileSummaryCase
    classes['FileWellPath'] = FileWellPath
    classes['FractureTemplate'] = FractureTemplate
    classes['FractureTemplateCollection'] = FractureTemplateCollection
    classes['GeoMechCase'] = GeoMechCase
    classes['GeoMechContourMap'] = GeoMechContourMap
    classes['GeoMechPart'] = GeoMechPart
    classes['GeoMechPartCollection'] = GeoMechPartCollection
    classes['GeoMechView'] = GeoMechView
    classes['GridCaseGroup'] = GridCaseGroup
    classes['GridCaseSurface'] = GridCaseSurface
    classes['GridSummaryCase'] = GridSummaryCase
    classes['ModeledWellPath'] = ModeledWellPath
    classes['MudWeightWindowParameters'] = MudWeightWindowParameters
    classes['NamedObject'] = NamedObject
    classes['NonNetLayers'] = NonNetLayers
    classes['PdmObjectBase'] = PdmObjectBase
    classes['Plot'] = Plot
    classes['PlotCurve'] = PlotCurve
    classes['PlotWindow'] = PlotWindow
    classes['PressureTable'] = PressureTable
    classes['PressureTableItem'] = PressureTableItem
    classes['Project'] = Project
    classes['ResampleData'] = ResampleData
    classes['Reservoir'] = Reservoir
    classes['SimulationWell'] = SimulationWell
    classes['StimPlanFractureTemplate'] = StimPlanFractureTemplate
    classes['StimPlanModel'] = StimPlanModel
    classes['StimPlanModelCollection'] = StimPlanModelCollection
    classes['StimPlanModelPlot'] = StimPlanModelPlot
    classes['StimPlanModelPlotCollection'] = StimPlanModelPlotCollection
    classes['StimPlanModelTemplate'] = StimPlanModelTemplate
    classes['StimPlanModelTemplateCollection'] = StimPlanModelTemplateCollection
    classes['SummaryCase'] = SummaryCase
    classes['SummaryCaseSubCollection'] = SummaryCaseSubCollection
    classes['SummaryPlot'] = SummaryPlot
    classes['SummaryPlotCollection'] = SummaryPlotCollection
    classes['Surface'] = Surface
    classes['SurfaceCollection'] = SurfaceCollection
    classes['SurfaceInterface'] = SurfaceInterface
    classes['View'] = View
    classes['ViewWindow'] = ViewWindow
    classes['WbsParameters'] = WbsParameters
    classes['WellBoreStabilityPlot'] = WellBoreStabilityPlot
    classes['WellLogExtractionCurve'] = WellLogExtractionCurve
    classes['WellLogPlot'] = WellLogPlot
    classes['WellLogPlotCollection'] = WellLogPlotCollection
    classes['WellLogPlotCurve'] = WellLogPlotCurve
    classes['WellLogPlotTrack'] = WellLogPlotTrack
    classes['WellPath'] = WellPath
    classes['WellPathCollection'] = WellPathCollection
    classes['WellPathGeometry'] = WellPathGeometry
    classes['WellPathTarget'] = WellPathTarget
    return classes

def class_from_keyword(class_keyword):
    all_classes = class_dict()
    if class_keyword in all_classes.keys():
        return all_classes[class_keyword]
    return None
