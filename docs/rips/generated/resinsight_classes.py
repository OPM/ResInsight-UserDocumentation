from rips.pdmobject import PdmObjectBase
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
        name_setting (str): Name Setting
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

    def add_property_scaling(self, formation=None, facies=None, property=None, scale=None):
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


class CheckableNamedObject(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        PdmObjectBase.__init__(self, pb2_object, channel)
        if CheckableNamedObject.__custom_init__ is not None:
            CheckableNamedObject.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class ElasticPropertyScaling(CheckableNamedObject):
    """
    Attributes:
        facies (str): Facies
        formation (str): Formation
        property (str): Property
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


class FaciesProperties(PdmObjectBase):
    """
    Attributes:
        color_legend (str): Colors
        file_path (str): File Path
        properties_table (str): Properties Table
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.color_legend = "ColorLegend:2174931122064"
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
        name_setting (str): Name Setting
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


    def resample_values(self, address=None, resampling_period=None):
        """
        
        Arguments:
            address (str): Formatted address specifying the summary vector
            resampling_period (str): Resampling Period
        Returns:
            ResampleData
        """
        return self._call_pdm_method("resampleValues", address=address, resampling_period=resampling_period)


    def summary_vector_values(self, address=None):
        """
        Create a new Summary Plot
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
        self.background_color = "#b0c4de"
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

class GridStatisticsPlotCollection(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        PdmObjectBase.__init__(self, pb2_object, channel)
        if GridStatisticsPlotCollection.__custom_init__ is not None:
            GridStatisticsPlotCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def grid_statistics_plots(self):
        """
        Returns:
             List of GridStatisticsPlot
        """
        return self.children("GridStatisticsPlots", GridStatisticsPlot)


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

class ModeledWellPath(WellPath):
    """
    A Well Path created interactively in ResInsight

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        WellPath.__init__(self, pb2_object, channel)
        if ModeledWellPath.__custom_init__ is not None:
            ModeledWellPath.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def well_path_geometry(self):
        """Trajectory
        Returns:
             WellPathGeometry
        """
        children = self.children("WellPathGeometry", WellPathGeometry)
        return children[0] if len(children) > 0 else None


class ModeledWellPathLateral(WellPath):
    """
    A Well Path Lateral created interactively

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        WellPath.__init__(self, pb2_object, channel)
        if ModeledWellPathLateral.__custom_init__ is not None:
            ModeledWellPathLateral.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def well_path_lateral_geometry(self):
        """Trajectory
        Returns:
             WellPathLateralGeometry
        """
        children = self.children("WellPathLateralGeometry", WellPathLateralGeometry)
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

    def import_summary_case(self, file_name=None):
        """
        Import Summary Case
        Arguments:
            file_name (str): 
        Returns:
            FileSummaryCase
        """
        return self._call_pdm_method("importSummaryCase", file_name=file_name)


    def summary_case(self, case_id=None):
        """
        Find Summary Case
        Arguments:
            case_id (int): 
        Returns:
            FileSummaryCase
        """
        return self._call_pdm_method("summaryCase", case_id=case_id)


    def surface_folder(self, folder_name=None):
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
        flow_tracer_selection_mode (str): Tracers
        phase_selection (str): Phases
        porosity_model_type (str): Porosity
        result_type (str): Type
        result_variable (str): Variable
        selected_injector_tracers (List of str): Injector Tracers
        selected_producer_tracers (List of str): Producer Tracers
        selected_souring_tracers (List of str): Tracers
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

class StimPlanModel(CheckableNamedObject):
    """
    Attributes:
        anchor_position (str): Anchor Position
        auto_compute_barrier (str): Auto Compute Barrier
        azimuth_angle (float): Azimuth Angle
        barrier (str): Barrier
        barrier_annotation (str): Barrier Annotation
        barrier_dip (float): Barrier Dip
        barrier_fault_name (str): Barrier Fault
        barrier_text_annotation (str): Barrier Text Annotation
        bounding_box_horizontal (float): Bounding Box Horizontal
        bounding_box_vertical (float): Bounding Box Vertical
        distance_to_barrier (float): Distance To Barrier [m]
        eclipse_case (str): Case
        extraction_depth_bottom (float): Bottom
        extraction_depth_top (float): Top
        extraction_type (str): Extraction Type
        formation_dip (float): Formation Dip
        fracture_orientation (str): Fracture Orientation
        measured_depth (float): Measured Depth
        perforation_length (float): Perforation Length [m]
        poro_elastic_constant (float): Poro-Elastic Constant
        relative_permeability_factor (float): Relative Permeability Factor
        show_all_faults (str): Show All Faults
        show_only_barrier_fault (str): Show Only Barrier Fault
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
        self.barrier_annotation = ""
        self.barrier_dip = 0
        self.barrier_fault_name = ""
        self.barrier_text_annotation = ""
        self.bounding_box_horizontal = 50
        self.bounding_box_vertical = 100
        self.distance_to_barrier = 0
        self.eclipse_case = ""
        self.extraction_depth_bottom = -1
        self.extraction_depth_top = -1
        self.extraction_type = "TST"
        self.formation_dip = 0
        self.fracture_orientation = "ALONG_WELL_PATH"
        self.measured_depth = 0
        self.perforation_length = 10
        self.poro_elastic_constant = 0
        self.relative_permeability_factor = 0.5
        self.show_all_faults = False
        self.show_only_barrier_fault = False
        self.thermal_expansion_coefficient = 0
        self.thickness_direction = [0, 0, 0]
        self.thickness_direction_well_path = ""
        self.time_step = 0
        self.use_detailed_fluid_loss = True
        self.well_penetration_layer = 2
        CheckableNamedObject.__init__(self, pb2_object, channel)
        if StimPlanModel.__custom_init__ is not None:
            StimPlanModel.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def export_to_file(self, directory_path=None):
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

    def new_stim_plan_model(self, eclipse_case=None, time_step=None, well_path=None, measured_depth=None, stim_plan_model_template=None):
        """
        Create a new StimPlan Model
        Arguments:
            eclipse_case (RimReservoir): Eclipse Case
            time_step (int): Time Step
            well_path (WellPathBase): Well Path
            measured_depth (float): Measured Depth
            stim_plan_model_template (StimPlanModelTemplate): StimPlan Model Template
        Returns:
            StimPlanModel
        """
        return self._call_pdm_method("NewStimPlanModel", eclipse_case=eclipse_case, time_step=time_step, well_path=well_path, measured_depth=measured_depth, stim_plan_model_template=stim_plan_model_template)


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
        axis_title_font_size (str): Axis Title Font Size
        axis_value_font_size (str): Axis Value Font Size
        depth_type (str): Type
        depth_unit (str): Unit
        maximum_depth (float): Max
        minimum_depth (float): Min
        show_depth_grid_lines (str): Show Grid Lines
        show_title_in_plot (str): Show Title
        sub_title_font_size (str): Track Title Font Size
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
        self.show_title_in_plot = False
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

    def new_stim_plan_model_plot(self, stim_plan_model=None):
        """
        Create a new StimPlan Model
        Arguments:
            stim_plan_model (StimPlanModel): StimPlan Model
        Returns:
            StimPlanModelPlot
        """
        return self._call_pdm_method("NewStimPlanModelPlot", stim_plan_model=stim_plan_model)


    def stim_plan_model_plots(self):
        """
        Returns:
             List of StimPlanModelPlot
        """
        return self.children("StimPlanModelPlots", StimPlanModelPlot)


class StimPlanModelTemplate(PdmObjectBase):
    """
    Attributes:
        default_permeability (float): Default Permeability
        default_porosity (float): Default Porosity
        id (int): ID
        overburden_facies (str): Overburden Facies
        overburden_fluid_density (float): Overburden Fluid Density [g/cm^3]
        overburden_formation (str): Overburden Formation
        overburden_height (float): Overburden Height
        overburden_permeability (float): Overburden Permeability
        overburden_porosity (float): Overburden Porosity
        reference_temperature (float): Temperature [C]
        reference_temperature_depth (float): Temperature Depth [m]
        reference_temperature_gradient (float): Temperature Gradient [C/m]
        stress_depth (float): Stress Depth
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
        self.default_permeability = 1e-05
        self.default_porosity = 0
        self.id = -1
        self.overburden_facies = ""
        self.overburden_fluid_density = 1.03
        self.overburden_formation = ""
        self.overburden_height = 50
        self.overburden_permeability = 1e-05
        self.overburden_porosity = 0
        self.reference_temperature = 70
        self.reference_temperature_depth = 2500
        self.reference_temperature_gradient = 0.025
        self.stress_depth = 1000
        self.underburden_facies = ""
        self.underburden_fluid_density = 1.03
        self.underburden_formation = ""
        self.underburden_height = 50
        self.underburden_permeability = 1e-05
        self.underburden_porosity = 0
        self.vertical_stress = 238
        self.vertical_stress_gradient = 0.238
        PdmObjectBase.__init__(self, pb2_object, channel)
        if StimPlanModelTemplate.__custom_init__ is not None:
            StimPlanModelTemplate.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def elastic_properties(self):
        """Elastic Properties
        Returns:
             ElasticProperties
        """
        children = self.children("ElasticProperties", ElasticProperties)
        return children[0] if len(children) > 0 else None


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


class StimPlanModelTemplateCollection(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        PdmObjectBase.__init__(self, pb2_object, channel)
        if StimPlanModelTemplateCollection.__custom_init__ is not None:
            StimPlanModelTemplateCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def new_stim_plan_model_template(self, facies_properties_file_path=None, elastic_properties_file_path=None):
        """
        Create a new StimPlan Model Template
        Arguments:
            facies_properties_file_path (str): Facies Properties File Path
            elastic_properties_file_path (str): Elastic Properties File Path
        Returns:
            StimPlanModelTemplate
        """
        return self._call_pdm_method("NewStimPlanModelTemplate", facies_properties_file_path=facies_properties_file_path, elastic_properties_file_path=elastic_properties_file_path)


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

    def new_summary_plot(self, summary_cases=[], ensemble=None, address=None):
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

class Surface(SurfaceInterface):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        SurfaceInterface.__init__(self, pb2_object, channel)
        if Surface.__custom_init__ is not None:
            Surface.__custom_init__(self, pb2_object=pb2_object, channel=channel)

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

    def add_folder(self, folder_name=None):
        """
        Add a new surface folder
        Arguments:
            folder_name (str): New surface folder name
        Returns:
            SurfaceCollection
        """
        return self._call_pdm_method("AddFolder", folder_name=folder_name)


    def import_surface(self, file_name=None):
        """
        Import a new surface from file
        Arguments:
            file_name (str): Filename to import surface from
        Returns:
            Surface
        """
        return self._call_pdm_method("ImportSurface", file_name=file_name)


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


class WbsParameters(PdmObjectBase):
    """
    Attributes:
        df_source (str): Depletion Factor (DF)
        fg_multiplier (float): SH Multiplier for FG in Shale
        fg_shale_source (str): FG in Shale Calculation
        k0_fg_source (str): K0_FG
        k0_sh_source (str): K0_SH
        obg0_source (str): Initial Overburden Gradient
        poission_ratio_source (str): Poisson Ratio
        pore_pressure_non_reservoir_source (str): Non-Reservoir Pore Pressure
        pore_pressure_reservoir_source (str): Reservoir Pore Pressure
        ucs_source (str): Uniaxial Compressive Strength
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
        md_at_first_target (float): MD at First Target
        reference_point (str): UTM Reference Point
        use_auto_generated_target_at_sea_level (str): Generate Target at Sea Level
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.air_gap = 0
        self.md_at_first_target = 0
        self.reference_point = [0, 0, 0]
        self.use_auto_generated_target_at_sea_level = True
        PdmObjectBase.__init__(self, pb2_object, channel)
        if WellPathGeometry.__custom_init__ is not None:
            WellPathGeometry.__custom_init__(self, pb2_object=pb2_object, channel=channel)

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


class WellPathGroup(WellPath):
    """
    A Group of Well Paths

    Attributes:
        group_name (str): Group Name
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.group_name = ""
        WellPath.__init__(self, pb2_object, channel)
        if WellPathGroup.__custom_init__ is not None:
            WellPathGroup.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def child_well_paths(self):
        """Child Well Paths
        Returns:
             List of WellPath
        """
        return self.children("ChildWellPaths", WellPath)


class WellPathLateralGeometry(PdmObjectBase):
    """
    Class containing the geometry of a modeled Well Path Lateral

    Attributes:
        md_at_connection (float): MD at Well Path Connection
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object=None, channel=None):
        self.md_at_connection = 0
        PdmObjectBase.__init__(self, pb2_object, channel)
        if WellPathLateralGeometry.__custom_init__ is not None:
            WellPathLateralGeometry.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def well_path_targets(self):
        """Well Targets
        Returns:
             List of WellPathTarget
        """
        return self.children("WellPathTargets", WellPathTarget)


def class_dict():
    classes = {}
    classes['Case'] = Case
    classes['CellColors'] = CellColors
    classes['CheckableNamedObject'] = CheckableNamedObject
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
    classes['FaciesProperties'] = FaciesProperties
    classes['FileSummaryCase'] = FileSummaryCase
    classes['FileWellPath'] = FileWellPath
    classes['GeoMechCase'] = GeoMechCase
    classes['GeoMechContourMap'] = GeoMechContourMap
    classes['GeoMechView'] = GeoMechView
    classes['GridCaseGroup'] = GridCaseGroup
    classes['GridStatisticsPlotCollection'] = GridStatisticsPlotCollection
    classes['GridSummaryCase'] = GridSummaryCase
    classes['ModeledWellPath'] = ModeledWellPath
    classes['ModeledWellPathLateral'] = ModeledWellPathLateral
    classes['MudWeightWindowParameters'] = MudWeightWindowParameters
    classes['NonNetLayers'] = NonNetLayers
    classes['PdmObjectBase'] = PdmObjectBase
    classes['Plot'] = Plot
    classes['PlotWindow'] = PlotWindow
    classes['Project'] = Project
    classes['ResampleData'] = ResampleData
    classes['Reservoir'] = Reservoir
    classes['SimulationWell'] = SimulationWell
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
    classes['WellLogPlot'] = WellLogPlot
    classes['WellPath'] = WellPath
    classes['WellPathGeometry'] = WellPathGeometry
    classes['WellPathGroup'] = WellPathGroup
    classes['WellPathLateralGeometry'] = WellPathLateralGeometry
    return classes

def class_from_keyword(class_keyword):
    all_classes = class_dict()
    if class_keyword in all_classes.keys():
        return all_classes[class_keyword]
    return None
