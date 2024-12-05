from __future__ import annotations
from rips.pdmobject import PdmObjectBase
import PdmObject_pb2
import grpc
from typing import Optional, Dict, List, Type

class CellFilterCollection(PdmObjectBase):
    """
    Attributes:
        active (bool): Active
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.active: bool = True
        PdmObjectBase.__init__(self, pb2_object, channel)
        if CellFilterCollection.__custom_init__ is not None:
            CellFilterCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class ColorLegend(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        PdmObjectBase.__init__(self, pb2_object, channel)
        if ColorLegend.__custom_init__ is not None:
            ColorLegend.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class CurveIntersection(PdmObjectBase):
    """
    Attributes:
        name (str): Name
        points (List[List[float]]): Points
        simulation_well (Optional[SimulationWell]): Simulation Well
        type (str): One of [CS_WELL_PATH, CS_SIMULATION_WELL, CS_POLYLINE, CS_AZIMUTHLINE, CS_POLYGON]
        well_path (Optional[WellPath]): Well Path        
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.name: str = "Intersection Name"
        self.points: List[List[float]] = []
        self.simulation_well: Optional[SimulationWell] = None
        self.type: str = "CS_POLYLINE"
        self.well_path: Optional[WellPath] = None
        PdmObjectBase.__init__(self, pb2_object, channel)
        if CurveIntersection.__custom_init__ is not None:
            CurveIntersection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def geometry(self, geometry_type: str="FULL_3D") -> TriangleGeometry:
        """
        

        Arguments:
            geometry_type (str): One of [FULL_3D, PROJECTED_TO_PLANE]
        Returns:
            TriangleGeometry
        """
        return self._call_pdm_method_return_value("geometry", TriangleGeometry, geometry_type=geometry_type)


    def geometry_result(self, geometry_type: str="FULL_3D") -> DataContainerFloat:
        """
        

        Arguments:
            geometry_type (str): One of [FULL_3D, PROJECTED_TO_PLANE]
        Returns:
            DataContainerFloat
        """
        return self._call_pdm_method_return_value("geometryResult", DataContainerFloat, geometry_type=geometry_type)


class DataContainerFloat(PdmObjectBase):
    """
    Attributes:
        values (List[float]): Float Values
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.values: List[float] = []
        PdmObjectBase.__init__(self, pb2_object, channel)
        if DataContainerFloat.__custom_init__ is not None:
            DataContainerFloat.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class DataContainerString(PdmObjectBase):
    """
    Attributes:
        values (List[str]): String Values
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.values: List[str] = []
        PdmObjectBase.__init__(self, pb2_object, channel)
        if DataContainerString.__custom_init__ is not None:
            DataContainerString.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class DataContainerTime(PdmObjectBase):
    """
    Attributes:
        values (List[int]): Time Values
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.values: List[int] = []
        PdmObjectBase.__init__(self, pb2_object, channel)
        if DataContainerTime.__custom_init__ is not None:
            DataContainerTime.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class Case(PdmObjectBase):
    """
    The ResInsight base class for Cases

    Attributes:
        file_path (Optional[str]): Case File Name
        id (int): Case ID
        name (str): Case Name
        name_setting (str): One of [FULL_CASE_NAME, SHORT_CASE_NAME, CUSTOM_NAME]
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.file_path: Optional[str] = None
        self.id: int = -1
        self.name: str = ""
        self.name_setting: str = "FULL_CASE_NAME"
        PdmObjectBase.__init__(self, pb2_object, channel)
        if Case.__custom_init__ is not None:
            Case.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class Reservoir(Case):
    """
    Abstract base class for Eclipse Cases

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        Case.__init__(self, pb2_object, channel)
        if Reservoir.__custom_init__ is not None:
            Reservoir.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def import_properties(self, file_names: List[str]=[]) -> None:
        """
        Import Properties

        Arguments:
            file_names (List[str]): 
        Returns:
            
        """
        self._call_pdm_method_void("import_properties", file_names=file_names)


class EclipseCase(Reservoir):
    """
    The Regular Eclipse Results Case

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        Reservoir.__init__(self, pb2_object, channel)
        if EclipseCase.__custom_init__ is not None:
            EclipseCase.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class ElasticProperties(PdmObjectBase):
    """
    Attributes:
        file_path (Optional[str]): File Path
        properties_table (str): Properties Table
        show_scaled_properties (bool): Show Scaled Properties
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.file_path: Optional[str] = None
        self.properties_table: str = ""
        self.show_scaled_properties: bool = True
        PdmObjectBase.__init__(self, pb2_object, channel)
        if ElasticProperties.__custom_init__ is not None:
            ElasticProperties.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def add_property_scaling(self, formation: str="", facies: str="", property: str="", scale: float=1) -> ElasticPropertyScaling:
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
        return self._call_pdm_method_return_value("AddPropertyScaling", ElasticPropertyScaling, formation=formation, facies=facies, property=property, scale=scale)


    def property_scaling_collection(self) -> Optional[ElasticPropertyScalingCollection]:
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

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.name: str = ""
        PdmObjectBase.__init__(self, pb2_object, channel)
        if NamedObject.__custom_init__ is not None:
            NamedObject.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class CheckableNamedObject(NamedObject):
    """
    Attributes:
        is_checked (bool): Active
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.is_checked: bool = True
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

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.facies: str = ""
        self.formation: str = ""
        self.property: str = "YOUNGS_MODULUS"
        self.scale: float = 1
        CheckableNamedObject.__init__(self, pb2_object, channel)
        if ElasticPropertyScaling.__custom_init__ is not None:
            ElasticPropertyScaling.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class ElasticPropertyScalingCollection(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        PdmObjectBase.__init__(self, pb2_object, channel)
        if ElasticPropertyScalingCollection.__custom_init__ is not None:
            ElasticPropertyScalingCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def elastic_property_scalings(self) -> List[ElasticPropertyScaling]:
        """Elastic Property Scalings

        Returns:
             List[ElasticPropertyScaling]
        """
        return self.children("ElasticPropertyScalings", ElasticPropertyScaling)


class SurfaceInterface(PdmObjectBase):
    """
    Attributes:
        depth_offset (float): Depth Offset
        surface_user_decription (str): Name
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.depth_offset: float = 0
        self.surface_user_decription: str = ""
        PdmObjectBase.__init__(self, pb2_object, channel)
        if SurfaceInterface.__custom_init__ is not None:
            SurfaceInterface.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def export_to_file(self, file_name: str="") -> Optional[DataContainerString]:
        """
        Export a surface to file

        Arguments:
            file_name (str): Filename to export surface to
        Returns:
            DataContainerString
        """
        return self._call_pdm_method_return_optional_value("ExportToFile", DataContainerString, file_name=file_name)


class EnsembleStatisticsSurface(SurfaceInterface):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        SurfaceInterface.__init__(self, pb2_object, channel)
        if EnsembleStatisticsSurface.__custom_init__ is not None:
            EnsembleStatisticsSurface.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class SurfaceCollection(PdmObjectBase):
    """
    Attributes:
        surface_user_decription (str): Name
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.surface_user_decription: str = "Surfaces"
        PdmObjectBase.__init__(self, pb2_object, channel)
        if SurfaceCollection.__custom_init__ is not None:
            SurfaceCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def add_folder(self, folder_name: str="Surfaces") -> Optional[SurfaceCollection]:
        """
        Add a new surface folder

        Arguments:
            folder_name (str): New surface folder name
        Returns:
            SurfaceCollection
        """
        return self._call_pdm_method_return_optional_value("AddFolder", SurfaceCollection, folder_name=folder_name)


    def import_surface(self, file_name: str="") -> Optional[Surface]:
        """
        Import a new surface from file

        Arguments:
            file_name (str): Filename to import surface from
        Returns:
            Surface
        """
        return self._call_pdm_method_return_optional_value("ImportSurface", Surface, file_name=file_name)


    def new_surface(self, case: Optional[Case]=None, k_index: int=0) -> Optional[GridCaseSurface]:
        """
        Create a new surface

        Arguments:
            case (Optional[Case]): 
            k_index (int): 
        Returns:
            GridCaseSurface
        """
        return self._call_pdm_method_return_optional_value("NewSurface", GridCaseSurface, case=case, k_index=k_index)


    def sub_collections(self) -> List[SurfaceCollection]:
        """Surfaces

        Returns:
             List[SurfaceCollection]
        """
        return self.children("SubCollections", SurfaceCollection)


    def surfaces_field(self) -> List[SurfaceInterface]:
        """Surfaces

        Returns:
             List[SurfaceInterface]
        """
        return self.children("SurfacesField", SurfaceInterface)


class EnsembleSurface(SurfaceCollection):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        SurfaceCollection.__init__(self, pb2_object, channel)
        if EnsembleSurface.__custom_init__ is not None:
            EnsembleSurface.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class EnsembleWellLogs(NamedObject):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        NamedObject.__init__(self, pb2_object, channel)
        if EnsembleWellLogs.__custom_init__ is not None:
            EnsembleWellLogs.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class FaciesInitialPressureConfig(PdmObjectBase):
    """
    Attributes:
        facies_name (str): Facies
        facies_value (int): Value
        fraction (float): Δ Pressure Fraction
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.facies_name: str = ""
        self.facies_value: int = -1
        self.fraction: float = 1
        PdmObjectBase.__init__(self, pb2_object, channel)
        if FaciesInitialPressureConfig.__custom_init__ is not None:
            FaciesInitialPressureConfig.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class FaciesProperties(PdmObjectBase):
    """
    Attributes:
        color_legend (Optional[ColorLegend]): Colors
        file_path (Optional[str]): File Path
        properties_table (str): Properties Table
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.color_legend: Optional[ColorLegend] = None
        self.file_path: Optional[str] = None
        self.properties_table: str = ""
        PdmObjectBase.__init__(self, pb2_object, channel)
        if FaciesProperties.__custom_init__ is not None:
            FaciesProperties.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def facies_definition(self) -> Optional[EclipseResult]:
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
        auto_shorty_name (bool): Use Auto Display Name
        id (int): Case ID
        name_setting (str): One of [FULL_CASE_NAME, SHORT_CASE_NAME, CUSTOM_NAME]
        short_name (str): Display Name
        show_sub_nodes_in_tree (bool): Show Summary Data Sub-Tree
        summary_header_filename (Optional[str]): Summary Header File
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.auto_shorty_name: bool = False
        self.id: int = -1
        self.name_setting: str = "FULL_CASE_NAME"
        self.short_name: str = ""
        self.show_sub_nodes_in_tree: bool = True
        self.summary_header_filename: Optional[str] = None
        PdmObjectBase.__init__(self, pb2_object, channel)
        if SummaryCase.__custom_init__ is not None:
            SummaryCase.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def available_addresses(self, ) -> DataContainerString:
        """
        

        Arguments:
            
        Returns:
            DataContainerString
        """
        return self._call_pdm_method_return_value("availableAddresses", DataContainerString)


    def available_time_steps(self, ) -> DataContainerTime:
        """
        

        Arguments:
            
        Returns:
            DataContainerTime
        """
        return self._call_pdm_method_return_value("availableTimeSteps", DataContainerTime)


    def resample_values(self, address: str="", resampling_period: str="") -> ResampleData:
        """
        

        Arguments:
            address (str): Formatted address specifying the summary vector
            resampling_period (str): Resampling Period
        Returns:
            ResampleData
        """
        return self._call_pdm_method_return_value("resampleValues", ResampleData, address=address, resampling_period=resampling_period)


    def set_summary_values(self, address: str="", unit: str="", values: List[float]=[]) -> None:
        """
        

        Arguments:
            address (str): Formatted address specifying the summary vector
            unit (str): Unit
            values (List[float]): Values
        Returns:
            
        """
        self._call_pdm_method_void("setSummaryValues", address=address, unit=unit, values=values)


    def summary_vector_values(self, address: str="") -> DataContainerFloat:
        """
        Get all values for a summary vector

        Arguments:
            address (str): Formatted address specifying the summary vector
        Returns:
            DataContainerFloat
        """
        return self._call_pdm_method_return_value("summaryVectorValues", DataContainerFloat, address=address)


class FileSummaryCase(SummaryCase):
    """
    A Summary Case based on SMSPEC files

    Attributes:
        include_restart_files (bool): Include Restart Files
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.include_restart_files: bool = False
        SummaryCase.__init__(self, pb2_object, channel)
        if FileSummaryCase.__custom_init__ is not None:
            FileSummaryCase.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class FractureTemplateCollection(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        PdmObjectBase.__init__(self, pb2_object, channel)
        if FractureTemplateCollection.__custom_init__ is not None:
            FractureTemplateCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def append_fracture_template(self, file_path: str="") -> StimPlanFractureTemplate:
        """
        Create a new StimPlan Fracture Template

        Arguments:
            file_path (str): File Path to StimPlan Countour File
        Returns:
            StimPlanFractureTemplate
        """
        return self._call_pdm_method_return_value("AppendFractureTemplate", StimPlanFractureTemplate, file_path=file_path)


    def append_thermal_fracture_template(self, file_path: str="") -> ThermalFractureTemplate:
        """
        Create a new Thermal Fracture Template

        Arguments:
            file_path (str): File Path to Thermal Fracture CSV File
        Returns:
            ThermalFractureTemplate
        """
        return self._call_pdm_method_return_value("AppendThermalFractureTemplate", ThermalFractureTemplate, file_path=file_path)


class GeoMechPart(CheckableNamedObject):
    """
    Attributes:
        part_id (int): Part Id
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.part_id: int = -1
        CheckableNamedObject.__init__(self, pb2_object, channel)
        if GeoMechPart.__custom_init__ is not None:
            GeoMechPart.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class GeoMechPartCollection(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        PdmObjectBase.__init__(self, pb2_object, channel)
        if GeoMechPartCollection.__custom_init__ is not None:
            GeoMechPartCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def parts(self) -> List[GeoMechPart]:
        """Parts

        Returns:
             List[GeoMechPart]
        """
        return self.children("Parts", GeoMechPart)


class ViewWindow(PdmObjectBase):
    """
    The Base Class for all Views and Plots in ResInsight

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        PdmObjectBase.__init__(self, pb2_object, channel)
        if ViewWindow.__custom_init__ is not None:
            ViewWindow.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class View(ViewWindow):
    """
    Attributes:
        background_color (str): Background
        current_time_step (int): Current Time Step
        disable_lighting (bool): Disable Results Lighting
        grid_z_scale (float): Z Scale
        id (int): View ID
        perspective_projection (bool): Perspective Projection
        show_grid_box (bool): Show Grid Box
        show_z_scale (bool): Show Z Scale Label
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.background_color: str = "#b0c4de"
        self.current_time_step: int = 0
        self.disable_lighting: bool = False
        self.grid_z_scale: float = 5
        self.id: int = -1
        self.perspective_projection: bool = True
        self.show_grid_box: bool = True
        self.show_z_scale: bool = True
        ViewWindow.__init__(self, pb2_object, channel)
        if View.__custom_init__ is not None:
            View.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class GeoMechView(View):
    """
    The Geomechanical 3d View

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        View.__init__(self, pb2_object, channel)
        if GeoMechView.__custom_init__ is not None:
            GeoMechView.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class GridCaseSurface(SurfaceInterface):
    """
    Attributes:
        include_inactive_cells (bool): Include Inactive Cells
        slice_index (int): Slice Index (K)
        source_case (Optional[Case]): Source Case
        watertight (bool): Watertight Surface (fill gaps)
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.include_inactive_cells: bool = False
        self.slice_index: int = 1
        self.source_case: Optional[Case] = None
        self.watertight: bool = False
        SurfaceInterface.__init__(self, pb2_object, channel)
        if GridCaseSurface.__custom_init__ is not None:
            GridCaseSurface.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class GridSummaryCase(SummaryCase):
    """
    A Summary Case based on extracting grid data.

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        SummaryCase.__init__(self, pb2_object, channel)
        if GridSummaryCase.__custom_init__ is not None:
            GridSummaryCase.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class IntersectionCollection(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        PdmObjectBase.__init__(self, pb2_object, channel)
        if IntersectionCollection.__custom_init__ is not None:
            IntersectionCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class WellPath(PdmObjectBase):
    """
    A ResInsight Well Path

    Attributes:
        name (str): Name
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.name: str = ""
        PdmObjectBase.__init__(self, pb2_object, channel)
        if WellPath.__custom_init__ is not None:
            WellPath.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def add_fracture(self, measured_depth: float=0, stim_plan_fracture_template: Optional[StimPlanFractureTemplate]=None, align_dip: bool=False, eclipse_case: Optional[Reservoir]=None) -> WellPathFracture:
        """
        Add StimPlan Fracture

        Arguments:
            measured_depth (float): 
            stim_plan_fracture_template (Optional[StimPlanFractureTemplate]): StimPlan Fracture Template
            align_dip (bool): 
            eclipse_case (Optional[Reservoir]): Eclipse Case
        Returns:
            WellPathFracture
        """
        return self._call_pdm_method_return_value("AddFracture", WellPathFracture, measured_depth=measured_depth, stim_plan_fracture_template=stim_plan_fracture_template, align_dip=align_dip, eclipse_case=eclipse_case)


    def add_thermal_fracture(self, measured_depth: float=0, fracture_template: Optional[ThermalFractureTemplate]=None, place_using_template_data: bool=True) -> WellPathFracture:
        """
        Add Thermal Fracture

        Arguments:
            measured_depth (float): 
            fracture_template (Optional[ThermalFractureTemplate]): Thermal Fracture Template
            place_using_template_data (bool): 
        Returns:
            WellPathFracture
        """
        return self._call_pdm_method_return_value("AddThermalFracture", WellPathFracture, measured_depth=measured_depth, fracture_template=fracture_template, place_using_template_data=place_using_template_data)


    def append_perforation_interval(self, start_md: float=0, end_md: float=0, diameter: float=0, skin_factor: float=0) -> Perforation:
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
        return self._call_pdm_method_return_value("AppendPerforationInterval", Perforation, start_md=start_md, end_md=end_md, diameter=diameter, skin_factor=skin_factor)


    def completion_settings(self) -> Optional[WellPathCompletionSettings]:
        """Completion Settings

        Returns:
             WellPathCompletionSettings
        """
        children = self.children("CompletionSettings", WellPathCompletionSettings)
        return children[0] if len(children) > 0 else None


    def completions(self) -> Optional[WellPathCompletions]:
        """Completions

        Returns:
             WellPathCompletions
        """
        children = self.children("Completions", WellPathCompletions)
        return children[0] if len(children) > 0 else None


    def msw_settings(self, ) -> Optional[MswSettings]:
        """
        Multi Segment Well Settings

        Arguments:
            
        Returns:
            RimMswCompletionParameters
        """
        return self._call_pdm_method_return_optional_value("MswSettings", MswSettings)


class ModeledWellPath(WellPath):
    """
    A Well Path created interactively in ResInsight

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        WellPath.__init__(self, pb2_object, channel)
        if ModeledWellPath.__custom_init__ is not None:
            ModeledWellPath.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def append_lateral(self, tie_in_depth: float=0, lateral_name: str="") -> ModeledWellPath:
        """
        Append Well Path Lateral

        Arguments:
            tie_in_depth (float): Measured Depth on the Parent Well Path
            lateral_name (str): Lateral Name
        Returns:
            ModeledWellPath
        """
        return self._call_pdm_method_return_value("AppendLateral", ModeledWellPath, tie_in_depth=tie_in_depth, lateral_name=lateral_name)


    def well_path_geometry(self) -> Optional[WellPathGeometry]:
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

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.cutoff: float = 0
        self.facies: str = ""
        PdmObjectBase.__init__(self, pb2_object, channel)
        if NonNetLayers.__custom_init__ is not None:
            NonNetLayers.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def facies_definition(self) -> Optional[EclipseResult]:
        """

        Returns:
             EclipseResult
        """
        children = self.children("FaciesDefinition", EclipseResult)
        return children[0] if len(children) > 0 else None


class OsduWellPath(WellPath):
    """
    Well Path Loaded From Osdu

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        WellPath.__init__(self, pb2_object, channel)
        if OsduWellPath.__custom_init__ is not None:
            OsduWellPath.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class Perforation(CheckableNamedObject):
    """
    Attributes:
        diameter (float): Diameter
        end_measured_depth (float): End MD
        skin_factor (float): Skin Factor
        start_measured_depth (float): Start MD
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.diameter: float = 0.216
        self.end_measured_depth: float = 0
        self.skin_factor: float = 0
        self.start_measured_depth: float = 0
        CheckableNamedObject.__init__(self, pb2_object, channel)
        if Perforation.__custom_init__ is not None:
            Perforation.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class PerforationCollection(CheckableNamedObject):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        CheckableNamedObject.__init__(self, pb2_object, channel)
        if PerforationCollection.__custom_init__ is not None:
            PerforationCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def perforations(self) -> List[Perforation]:
        """Perforations

        Returns:
             List[Perforation]
        """
        return self.children("Perforations", Perforation)


class PressureTable(PdmObjectBase):
    """
    Attributes:
        pressure_date (str): Pressure Date
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.pressure_date: str = ""
        PdmObjectBase.__init__(self, pb2_object, channel)
        if PressureTable.__custom_init__ is not None:
            PressureTable.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def add_pressure(self, depth: float=0, initial_pressure: float=0, pressure: float=0) -> PressureTableItem:
        """
        Add pressure data to pressure table.

        Arguments:
            depth (float): Depth: TVDMSL [m]
            initial_pressure (float): Initial Pressure [Bar]
            pressure (float): Pressure [Bar]
        Returns:
            PressureTableItem
        """
        return self._call_pdm_method_return_value("AddPressure", PressureTableItem, depth=depth, initial_pressure=initial_pressure, pressure=pressure)


    def items(self) -> List[PressureTableItem]:
        """Pressure Table Items

        Returns:
             List[PressureTableItem]
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

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.depth: float = 0
        self.initial_pressure: float = 0
        self.pressure: float = 0
        PdmObjectBase.__init__(self, pb2_object, channel)
        if PressureTableItem.__custom_init__ is not None:
            PressureTableItem.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class GeoMechCase(Case):
    """
    The Abaqus Based GeoMech Case

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        Case.__init__(self, pb2_object, channel)
        if GeoMechCase.__custom_init__ is not None:
            GeoMechCase.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def views(self) -> List[GeoMechView]:
        """All GeoMech Views in the Case

        Returns:
             List[GeoMechView]
        """
        return self.children("Views", GeoMechView)


class Project(PdmObjectBase):
    """
    The ResInsight Project

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        PdmObjectBase.__init__(self, pb2_object, channel)
        if Project.__custom_init__ is not None:
            Project.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def import_summary_case(self, file_name: str="") -> Optional[FileSummaryCase]:
        """
        Import Summary Case

        Arguments:
            file_name (str): 
        Returns:
            FileSummaryCase
        """
        return self._call_pdm_method_return_optional_value("importSummaryCase", FileSummaryCase, file_name=file_name)


    def summary_case(self, case_id: int=-1) -> Optional[FileSummaryCase]:
        """
        Find Summary Case

        Arguments:
            case_id (int): 
        Returns:
            FileSummaryCase
        """
        return self._call_pdm_method_return_optional_value("summaryCase", FileSummaryCase, case_id=case_id)


    def surface_folder(self, folder_name: str="") -> Optional[SurfaceCollection]:
        """
        Get Surface Folder

        Arguments:
            folder_name (str): 
        Returns:
            SurfaceCollection
        """
        return self._call_pdm_method_return_optional_value("surfaceFolder", SurfaceCollection, folder_name=folder_name)


class ResampleData(PdmObjectBase):
    """
    Attributes:
        time_steps (List[int]): Time Steps
        values (List[float]): Values
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.time_steps: List[int] = []
        self.values: List[float] = []
        PdmObjectBase.__init__(self, pb2_object, channel)
        if ResampleData.__custom_init__ is not None:
            ResampleData.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class EclipseView(View):
    """
    The Eclipse 3d Reservoir View

    Attributes:
        eclipse_case (Optional[Reservoir]): Eclipse Case
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.eclipse_case: Optional[Reservoir] = None
        View.__init__(self, pb2_object, channel)
        if EclipseView.__custom_init__ is not None:
            EclipseView.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def cell_result(self) -> Optional[CellColors]:
        """Cell Result

        Returns:
             CellColors
        """
        children = self.children("CellResult", CellColors)
        return children[0] if len(children) > 0 else None


    def cell_result_data(self) -> List[float]:
        """Current Eclipse Cell Result

        Returns:
             List[float]
        """
        return self._call_get_method("CellResultData")


    def set_cell_result_data(self, values : List[float]) -> None:
        """Set Current Eclipse Cell Result

        Arguments:
            values (List[float]): data
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
        selected_injector_tracers (List[str]): Injector Tracers
        selected_producer_tracers (List[str]): Producer Tracers
        selected_souring_tracers (List[str]): Tracers
        show_only_visible_categories_in_legend (bool): Show Only Visible Categories In Legend
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.flow_tracer_selection_mode: str = "FLOW_TR_INJ_AND_PROD"
        self.phase_selection: str = "PHASE_ALL"
        self.porosity_model_type: str = "MATRIX_MODEL"
        self.result_type: str = "DYNAMIC_NATIVE"
        self.result_variable: str = "None"
        self.selected_injector_tracers: List[str] = []
        self.selected_producer_tracers: List[str] = []
        self.selected_souring_tracers: List[str] = []
        self.show_only_visible_categories_in_legend: bool = True
        PdmObjectBase.__init__(self, pb2_object, channel)
        if EclipseResult.__custom_init__ is not None:
            EclipseResult.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class CellColors(EclipseResult):
    """
    Eclipse Cell Colors class

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        EclipseResult.__init__(self, pb2_object, channel)
        if CellColors.__custom_init__ is not None:
            CellColors.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class CommandRouter(PdmObjectBase):
    """
    The CommandRouter is used to call code independent to the project

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        PdmObjectBase.__init__(self, pb2_object, channel)
        if CommandRouter.__custom_init__ is not None:
            CommandRouter.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def extract_surfaces(self, grid_model_filename: str="", layers: List[int]=[], minimum_i: int=-1, maximum_i: int=-1, minimum_j: int=-1, maximum_j: int=-1) -> None:
        """
        Extract Layer Surface

        Arguments:
            grid_model_filename (str): 
            layers (List[int]): 
            minimum_i (int): 
            maximum_i (int): 
            minimum_j (int): 
            maximum_j (int): 
        Returns:
            
        """
        self._call_pdm_method_void("ExtractSurfaces", grid_model_filename=grid_model_filename, layers=layers, minimum_i=minimum_i, maximum_i=maximum_i, minimum_j=minimum_j, maximum_j=maximum_j)


class EclipseContourMap(EclipseView):
    """
    A contour map for Eclipse cases

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        EclipseView.__init__(self, pb2_object, channel)
        if EclipseContourMap.__custom_init__ is not None:
            EclipseContourMap.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class RimDepthSurface(SurfaceInterface):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        SurfaceInterface.__init__(self, pb2_object, channel)
        if RimDepthSurface.__custom_init__ is not None:
            RimDepthSurface.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class EclipseCaseEnsemble(NamedObject):
    """
    Grid Ensemble

    Attributes:
        id (int): Id
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.id: int = -1
        NamedObject.__init__(self, pb2_object, channel)
        if EclipseCaseEnsemble.__custom_init__ is not None:
            EclipseCaseEnsemble.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class RimEmCase(Reservoir):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        Reservoir.__init__(self, pb2_object, channel)
        if RimEmCase.__custom_init__ is not None:
            RimEmCase.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class GeoMechContourMap(GeoMechView):
    """
    A contour map for GeoMech cases

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
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

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.group_id: int = -1
        self.user_description: str = "Grid Case Group"
        PdmObjectBase.__init__(self, pb2_object, channel)
        if GridCaseGroup.__custom_init__ is not None:
            GridCaseGroup.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def create_statistics_case(self, ) -> RimStatisticalCalculation:
        """
        The Abstract Base Class for the Project Data Model

        Arguments:
            
        Returns:
            RimStatisticalCalculation
        """
        return self._call_pdm_method_return_value("create_statistics_case", RimStatisticalCalculation)


class MswSettings(PdmObjectBase):
    """
    Multi Segment Well Completion Settings

    Attributes:
        custom_values_for_lateral (bool): Custom Values for Lateral
        enforce_max_segment_length (bool): Enforce Max Segment Length
        length_and_depth (str): One of [INC, ABS]
        liner_diameter (float): Liner Inner Diameter
        max_segment_length (float): Max Segment Length
        pressure_drop (str): One of [H--, HF-, HFA]
        reference_md_type (str): One of [GridEntryPoint, UserDefined]
        roughness_factor (float): Roughness Factor
        user_defined_reference_md (float): User Defined Reference MD
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.custom_values_for_lateral: bool = False
        self.enforce_max_segment_length: bool = False
        self.length_and_depth: str = "ABS"
        self.liner_diameter: float = 0.152
        self.max_segment_length: float = 200
        self.pressure_drop: str = "HF-"
        self.reference_md_type: str = "GridEntryPoint"
        self.roughness_factor: float = 1e-05
        self.user_defined_reference_md: float = 0
        PdmObjectBase.__init__(self, pb2_object, channel)
        if MswSettings.__custom_init__ is not None:
            MswSettings.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class MudWeightWindowParameters(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        PdmObjectBase.__init__(self, pb2_object, channel)
        if MudWeightWindowParameters.__custom_init__ is not None:
            MudWeightWindowParameters.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class RimRoffCase(Reservoir):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        Reservoir.__init__(self, pb2_object, channel)
        if RimRoffCase.__custom_init__ is not None:
            RimRoffCase.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class RimStatisticalCalculation(Reservoir):
    """
    Attributes:
        calculate_percentiles (bool): Calculate Percentiles
        dynamic_properties_to_calculate (List[str]): Dyn Prop
        fracture_dynamic_properties_to_calculate (List[str]): 
        fracture_generated_properties_to_calculate (List[str]): 
        fracture_input_properties_to_calculate (List[str]): 
        fracture_static_properties_to_calculate (List[str]): 
        generated_properties_to_calculate (List[str]): 
        high_percentile (float): High
        input_properties_to_calculate (List[str]): 
        low_percentile (float): Low
        mid_percentile (float): Mid
        percentile_calculation_type (str): One of [NearestObservationPercentile, HistogramEstimatedPercentile, InterpolatedObservationPercentile]
        porosity_model (str): One of [MATRIX_MODEL, FRACTURE_MODEL]
        result_type (str): One of [DYNAMIC_NATIVE, STATIC_NATIVE, SOURSIMRL, GENERATED, INPUT_PROPERTY, FORMATION_NAMES, ALLAN_DIAGRAMS, FLOW_DIAGNOSTICS, INJECTION_FLOODING]
        selected_time_steps (List[int]): Time Step Selection
        static_properties_to_calculate (List[str]): Stat Prop
        use_zero_as_inactive_cell_value (bool): Use Zero as Inactive Cell Value
        well_data_source_case (str): Well Data Source Case
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.calculate_percentiles: bool = True
        self.dynamic_properties_to_calculate: List[str] = []
        self.fracture_dynamic_properties_to_calculate: List[str] = []
        self.fracture_generated_properties_to_calculate: List[str] = []
        self.fracture_input_properties_to_calculate: List[str] = []
        self.fracture_static_properties_to_calculate: List[str] = []
        self.generated_properties_to_calculate: List[str] = []
        self.high_percentile: float = 90
        self.input_properties_to_calculate: List[str] = []
        self.low_percentile: float = 10
        self.mid_percentile: float = 50
        self.percentile_calculation_type: str = "InterpolatedObservationPercentile"
        self.porosity_model: str = "MATRIX_MODEL"
        self.result_type: str = "DYNAMIC_NATIVE"
        self.selected_time_steps: List[int] = []
        self.static_properties_to_calculate: List[str] = []
        self.use_zero_as_inactive_cell_value: bool = False
        self.well_data_source_case: str = "None"
        Reservoir.__init__(self, pb2_object, channel)
        if RimStatisticalCalculation.__custom_init__ is not None:
            RimStatisticalCalculation.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def clear_source_properties(self, ) -> None:
        """
        The Abstract Base Class for the Project Data Model

        Arguments:
            
        Returns:
            
        """
        self._call_pdm_method_void("clear_source_properties")


    def compute_statistics(self, ) -> None:
        """
        The Abstract Base Class for the Project Data Model

        Arguments:
            
        Returns:
            
        """
        self._call_pdm_method_void("compute_statistics")


    def set_source_properties(self, property_type: str="", property_names: List[str]=[]) -> None:
        """
        

        Arguments:
            property_type (str): 
            property_names (List[str]): 
        Returns:
            
        """
        self._call_pdm_method_void("set_source_properties", property_type=property_type, property_names=property_names)


class RimSummaryCaseSumo(SummaryCase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        SummaryCase.__init__(self, pb2_object, channel)
        if RimSummaryCaseSumo.__custom_init__ is not None:
            RimSummaryCaseSumo.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class RimTextAnnotation(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        PdmObjectBase.__init__(self, pb2_object, channel)
        if RimTextAnnotation.__custom_init__ is not None:
            RimTextAnnotation.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class FractureTemplate(PdmObjectBase):
    """
    Attributes:
        azimuth_angle (float): Azimuth Angle
        conductivity_factor (float): Conductivity
        conductivity_type (str): One of [InfiniteConductivity, FiniteConductivity, FiniteConductivityInfiniteWellPI]
        d_factor_scale_factor (float): D-factor
        height_scale_factor (float): Height
        orientation (str): One of [Azimuth, Longitudinal, Transverse]
        perforation_length (float): Perforation Length
        user_defined_perforation_length (bool): User-defined Perforation Length
        user_description (str): Name
        width_scale_factor (float): Half Length
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.azimuth_angle: float = 0
        self.conductivity_factor: float = 1
        self.conductivity_type: str = "FiniteConductivity"
        self.d_factor_scale_factor: float = 1
        self.height_scale_factor: float = 1
        self.orientation: str = "Transverse"
        self.perforation_length: float = 1
        self.user_defined_perforation_length: bool = False
        self.user_description: str = "Fracture Template"
        self.width_scale_factor: float = 1
        PdmObjectBase.__init__(self, pb2_object, channel)
        if FractureTemplate.__custom_init__ is not None:
            FractureTemplate.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def set_scale_factors(self, half_length: float=1, height: float=1, d_factor: float=1, conductivity: float=1) -> None:
        """
        Set Fracture Template Scale Factors.

        Arguments:
            half_length (float): 
            height (float): 
            d_factor (float): 
            conductivity (float): 
        Returns:
            
        """
        self._call_pdm_method_void("SetScaleFactors", half_length=half_length, height=height, d_factor=d_factor, conductivity=conductivity)


class MeshFractureTemplate(FractureTemplate):
    """
    Attributes:
        active_time_step_index (int): Active TimeStep Index
        conductivity_result_name (str): Active Conductivity Result Name
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.active_time_step_index: int = 0
        self.conductivity_result_name: str = ""
        FractureTemplate.__init__(self, pb2_object, channel)
        if MeshFractureTemplate.__custom_init__ is not None:
            MeshFractureTemplate.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class StimPlanFractureTemplate(MeshFractureTemplate):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        MeshFractureTemplate.__init__(self, pb2_object, channel)
        if StimPlanFractureTemplate.__custom_init__ is not None:
            StimPlanFractureTemplate.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class StimPlanModel(CheckableNamedObject):
    """
    Attributes:
        anchor_position (List[float]): Anchor Position
        auto_compute_barrier (bool): Auto Compute Barrier
        azimuth_angle (float): Azimuth Angle
        barrier (bool): Barrier
        barrier_dip (float): Barrier Dip
        barrier_fault_name (str): Barrier Fault
        barrier_text_annotation (Optional[RimTextAnnotation]): Barrier Text Annotation
        bounding_box_horizontal (float): Bounding Box Horizontal
        bounding_box_vertical (float): Bounding Box Vertical
        distance_to_barrier (float): Distance To Barrier [m]
        eclipse_case (Optional[Reservoir]): Dynamic Case
        extraction_depth_bottom (float): Depth
        extraction_depth_top (float): Depth
        extraction_offset_bottom (float): Bottom Offset
        extraction_offset_top (float): Top Offset
        extraction_type (str): One of [TVT, TST]
        formation_dip (float): Formation Dip
        fracture_orientation (str): One of [Longitudinal, Transverse, Azimuth]
        initial_pressure_eclipse_case (Optional[Reservoir]): Initial Pressure Case
        measured_depth (float): Measured Depth
        original_thickness_direction (List[float]): Original Thickness Direction
        perforation_interval (Optional[Perforation]): Perforation Interval
        perforation_length (float): Perforation Length [m]
        poro_elastic_constant (float): Poro-Elastic Constant
        relative_permeability_factor (float): Relative Permeability Factor
        show_all_faults (bool): Show All Faults
        show_only_barrier_fault (bool): Show Only Barrier Fault
        static_eclipse_case (Optional[Reservoir]): Static Case
        thermal_expansion_coefficient (float): Thermal Expansion Coefficient [1/C]
        thickness_direction (List[float]): Thickness Direction
        thickness_direction_well_path (Optional[ModeledWellPath]): Thickness Direction Well Path
        time_step (int): Time Step
        use_detailed_fluid_loss (bool): Use Detailed Fluid Loss
        well_penetration_layer (int): Well Penetration Layer
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.anchor_position: List[float] = [0, 0, 0]
        self.auto_compute_barrier: bool = True
        self.azimuth_angle: float = 0
        self.barrier: bool = True
        self.barrier_dip: float = 0
        self.barrier_fault_name: str = ""
        self.barrier_text_annotation: Optional[RimTextAnnotation] = None
        self.bounding_box_horizontal: float = 50
        self.bounding_box_vertical: float = 100
        self.distance_to_barrier: float = 0
        self.eclipse_case: Optional[Reservoir] = None
        self.extraction_depth_bottom: float = -1
        self.extraction_depth_top: float = -1
        self.extraction_offset_bottom: float = -1
        self.extraction_offset_top: float = -1
        self.extraction_type: str = "TST"
        self.formation_dip: float = 0
        self.fracture_orientation: str = "Longitudinal"
        self.initial_pressure_eclipse_case: Optional[Reservoir] = None
        self.measured_depth: float = 0
        self.original_thickness_direction: List[float] = [0, 0, 0]
        self.perforation_interval: Optional[Perforation] = None
        self.perforation_length: float = 10
        self.poro_elastic_constant: float = 0
        self.relative_permeability_factor: float = 0.5
        self.show_all_faults: bool = False
        self.show_only_barrier_fault: bool = False
        self.static_eclipse_case: Optional[Reservoir] = None
        self.thermal_expansion_coefficient: float = 0
        self.thickness_direction: List[float] = [0, 0, 0]
        self.thickness_direction_well_path: Optional[ModeledWellPath] = None
        self.time_step: int = 0
        self.use_detailed_fluid_loss: bool = True
        self.well_penetration_layer: int = 2
        CheckableNamedObject.__init__(self, pb2_object, channel)
        if StimPlanModel.__custom_init__ is not None:
            StimPlanModel.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def export_to_file(self, directory_path: str="") -> Optional[StimPlanModel]:
        """
        Export StimPlan Model Plot to File

        Arguments:
            directory_path (str): Directory Path
        Returns:
            StimPlanModel
        """
        return self._call_pdm_method_return_optional_value("ExportToFile", StimPlanModel, directory_path=directory_path)


class StimPlanModelCollection(CheckableNamedObject):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        CheckableNamedObject.__init__(self, pb2_object, channel)
        if StimPlanModelCollection.__custom_init__ is not None:
            StimPlanModelCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def append_stim_plan_model(self, well_path: Optional[WellPath]=None, measured_depth: float=0, stim_plan_model_template: Optional[StimPlanModelTemplate]=None) -> StimPlanModel:
        """
        Create a new StimPlan Model

        Arguments:
            well_path (Optional[WellPath]): Well Path
            measured_depth (float): 
            stim_plan_model_template (Optional[StimPlanModelTemplate]): StimPlan Model Template
        Returns:
            StimPlanModel
        """
        return self._call_pdm_method_return_value("AppendStimPlanModel", StimPlanModel, well_path=well_path, measured_depth=measured_depth, stim_plan_model_template=stim_plan_model_template)


    def stim_plan_models(self) -> List[StimPlanModel]:
        """

        Returns:
             List[StimPlanModel]
        """
        return self.children("StimPlanModels", StimPlanModel)


class PlotWindow(ViewWindow):
    """
    The Abstract base class for all MDI Windows in the Plot Window

    Attributes:
        id (int): View ID
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.id: int = -1
        ViewWindow.__init__(self, pb2_object, channel)
        if PlotWindow.__custom_init__ is not None:
            PlotWindow.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class DepthTrackPlot(PlotWindow):
    """
    Attributes:
        auto_scale_depth_enabled (bool): Auto Scale
        auto_zoom_max_depth_factor (float): Auto Zoom Maximum Factor
        auto_zoom_min_depth_factor (float): Auto Zoom Minimum Factor
        axis_title_font_size (str): One of [XX_Small, X_Small, Small, Medium, Large, X_Large, XX_Large]
        axis_value_font_size (str): One of [XX_Small, X_Small, Small, Medium, Large, X_Large, XX_Large]
        depth_type (str): One of [MEASURED_DEPTH, TRUE_VERTICAL_DEPTH, PSEUDO_LENGTH, CONNECTION_NUMBER, TRUE_VERTICAL_DEPTH_RKB]
        depth_unit (str): One of [UNIT_METER, UNIT_FEET, UNIT_NONE]
        maximum_depth (float): Max
        minimum_depth (float): Min
        show_depth_grid_lines (str): One of [GRID_X_NONE, GRID_X_MAJOR, GRID_X_MAJOR_AND_MINOR]
        show_depth_marker_line (bool): Show Depth Marker Line
        sub_title_font_size (str): One of [XX_Small, X_Small, Small, Medium, Large, X_Large, XX_Large]
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.auto_scale_depth_enabled: bool = True
        self.auto_zoom_max_depth_factor: float = 0
        self.auto_zoom_min_depth_factor: float = 0
        self.axis_title_font_size: str = "Medium"
        self.axis_value_font_size: str = "Medium"
        self.depth_type: str = "MEASURED_DEPTH"
        self.depth_unit: str = "UNIT_METER"
        self.maximum_depth: float = 1000
        self.minimum_depth: float = 0
        self.show_depth_grid_lines: str = "GRID_X_MAJOR"
        self.show_depth_marker_line: bool = False
        self.sub_title_font_size: str = "Medium"
        PlotWindow.__init__(self, pb2_object, channel)
        if DepthTrackPlot.__custom_init__ is not None:
            DepthTrackPlot.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class StimPlanModelPlot(DepthTrackPlot):
    """
    A fracture model plot

    Attributes:
        eclipse_case (Optional[Reservoir]): Case
        stim_plan_model (Optional[StimPlanModel]): StimPlan Model
        time_step (int): Time Step
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.eclipse_case: Optional[Reservoir] = None
        self.stim_plan_model: Optional[StimPlanModel] = None
        self.time_step: int = 0
        DepthTrackPlot.__init__(self, pb2_object, channel)
        if StimPlanModelPlot.__custom_init__ is not None:
            StimPlanModelPlot.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class StimPlanModelPlotCollection(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        PdmObjectBase.__init__(self, pb2_object, channel)
        if StimPlanModelPlotCollection.__custom_init__ is not None:
            StimPlanModelPlotCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def append_stim_plan_model_plot(self, stim_plan_model: Optional[StimPlanModel]=None) -> StimPlanModelPlot:
        """
        Create a new StimPlan Model

        Arguments:
            stim_plan_model (Optional[StimPlanModel]): StimPlan Model
        Returns:
            StimPlanModelPlot
        """
        return self._call_pdm_method_return_value("AppendStimPlanModelPlot", StimPlanModelPlot, stim_plan_model=stim_plan_model)


    def stim_plan_model_plots(self) -> List[StimPlanModelPlot]:
        """

        Returns:
             List[StimPlanModelPlot]
        """
        return self.children("StimPlanModelPlots", StimPlanModelPlot)


class StimPlanModelTemplate(NamedObject):
    """
    Attributes:
        default_facies (str): Default Facies
        default_permeability (float): Default Permeability
        default_porosity (float): Default Porosity
        dynamic_eclipse_case (Optional[Reservoir]): Dynamic Case
        id (int): ID
        initial_pressure_eclipse_case (Optional[Reservoir]): Initial Pressure Case
        overburden_facies (str): Overburden Facies
        overburden_fluid_density (float): Overburden Fluid Density [g/cm^3]
        overburden_formation (str): Overburden Formation
        overburden_height (float): Overburden Height
        overburden_permeability (float): Overburden Permeability
        overburden_porosity (float): Overburden Porosity
        reference_temperature (float): Temperature [C]
        reference_temperature_depth (float): Temperature Depth [m]
        reference_temperature_gradient (float): Temperature Gradient [C/m]
        static_eclipse_case (Optional[Reservoir]): Static Case
        stress_depth (float): Stress Depth
        time_step (int): Time Step
        underburden_facies (str): Underburden Facies
        underburden_fluid_density (float): Underburden Fluid Density [g/cm^3]
        underburden_formation (str): Underburden Formation
        underburden_height (float): Underburden Height
        underburden_permeability (float): Underburden Permeability
        underburden_porosity (float): Underburden Porosity
        use_eql_num_for_pressure_interpolation (bool): Use EQLNUM For Pressure Interpolation
        use_pressure_table_for_initial_pressure (bool): Use Pressure Table For Initial Pressure
        use_pressure_table_for_pressure (bool): Use Pressure Table For Pressure
        vertical_stress (float): Vertical Stress
        vertical_stress_gradient (float): Vertical Stress Gradient
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.default_facies: str = ""
        self.default_permeability: float = 0.0001
        self.default_porosity: float = 0.01
        self.dynamic_eclipse_case: Optional[Reservoir] = None
        self.id: int = -1
        self.initial_pressure_eclipse_case: Optional[Reservoir] = None
        self.overburden_facies: str = ""
        self.overburden_fluid_density: float = 1.03
        self.overburden_formation: str = ""
        self.overburden_height: float = 50
        self.overburden_permeability: float = 1e-05
        self.overburden_porosity: float = 0
        self.reference_temperature: float = 70
        self.reference_temperature_depth: float = 2500
        self.reference_temperature_gradient: float = 0.025
        self.static_eclipse_case: Optional[Reservoir] = None
        self.stress_depth: float = 1000
        self.time_step: int = 0
        self.underburden_facies: str = ""
        self.underburden_fluid_density: float = 1.03
        self.underburden_formation: str = ""
        self.underburden_height: float = 50
        self.underburden_permeability: float = 1e-05
        self.underburden_porosity: float = 0
        self.use_eql_num_for_pressure_interpolation: bool = True
        self.use_pressure_table_for_initial_pressure: bool = False
        self.use_pressure_table_for_pressure: bool = False
        self.vertical_stress: float = 238
        self.vertical_stress_gradient: float = 0.238
        NamedObject.__init__(self, pb2_object, channel)
        if StimPlanModelTemplate.__custom_init__ is not None:
            StimPlanModelTemplate.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def elastic_properties(self) -> Optional[ElasticProperties]:
        """Elastic Properties

        Returns:
             ElasticProperties
        """
        children = self.children("ElasticProperties", ElasticProperties)
        return children[0] if len(children) > 0 else None


    def facies_initial_pressure_configs(self) -> List[FaciesInitialPressureConfig]:
        """Facies Initial Pressure Configs

        Returns:
             List[FaciesInitialPressureConfig]
        """
        return self.children("FaciesInitialPressureConfigs", FaciesInitialPressureConfig)


    def facies_properties(self) -> Optional[FaciesProperties]:
        """Facies Properties

        Returns:
             FaciesProperties
        """
        children = self.children("FaciesProperties", FaciesProperties)
        return children[0] if len(children) > 0 else None


    def non_net_layers(self) -> Optional[NonNetLayers]:
        """Non-Net Layers

        Returns:
             NonNetLayers
        """
        children = self.children("NonNetLayers", NonNetLayers)
        return children[0] if len(children) > 0 else None


    def pressure_table(self) -> Optional[PressureTable]:
        """Pressure Table

        Returns:
             PressureTable
        """
        children = self.children("PressureTable", PressureTable)
        return children[0] if len(children) > 0 else None


class StimPlanModelTemplateCollection(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        PdmObjectBase.__init__(self, pb2_object, channel)
        if StimPlanModelTemplateCollection.__custom_init__ is not None:
            StimPlanModelTemplateCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def append_stim_plan_model_template(self, eclipse_case: Optional[Reservoir]=None, time_step: int=0, facies_properties_file_path: str="", elastic_properties_file_path: str="") -> StimPlanModelTemplate:
        """
        Create a new StimPlan Model Template

        Arguments:
            eclipse_case (Optional[Reservoir]): Eclipse Case
            time_step (int): Time Step
            facies_properties_file_path (str): Facies Properties File Path
            elastic_properties_file_path (str): Elastic Properties File Path
        Returns:
            StimPlanModelTemplate
        """
        return self._call_pdm_method_return_value("AppendStimPlanModelTemplate", StimPlanModelTemplate, eclipse_case=eclipse_case, time_step=time_step, facies_properties_file_path=facies_properties_file_path, elastic_properties_file_path=elastic_properties_file_path)


    def stim_plan_model_templates(self) -> List[StimPlanModelTemplate]:
        """StimPlan Model Templates

        Returns:
             List[StimPlanModelTemplate]
        """
        return self.children("StimPlanModelTemplates", StimPlanModelTemplate)


class SummaryCaseSubCollection(PdmObjectBase):
    """
    Attributes:
        create_auto_name (bool): Auto Name
        id (int): Ensemble ID
        is_ensemble (bool): Is Ensemble
        name_count (str): Name
        summary_collection_name (str): Name
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.create_auto_name: bool = True
        self.id: int = -1
        self.is_ensemble: bool = False
        self.name_count: str = "Group"
        self.summary_collection_name: str = "Group"
        PdmObjectBase.__init__(self, pb2_object, channel)
        if SummaryCaseSubCollection.__custom_init__ is not None:
            SummaryCaseSubCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class Plot(PlotWindow):
    """
    The Abstract Base Class for all Plot Objects

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        PlotWindow.__init__(self, pb2_object, channel)
        if Plot.__custom_init__ is not None:
            Plot.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class SummaryPlot(Plot):
    """
    A Summary Plot

    Attributes:
        is_using_auto_name (bool): Auto Title
        normalize_curve_y_values (bool): Normalize all curves
        plot_description (str): Name
        use_qt_charts_plot (bool): Use Qt Charts
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.is_using_auto_name: bool = True
        self.normalize_curve_y_values: bool = False
        self.plot_description: str = "Summary Plot"
        self.use_qt_charts_plot: bool = False
        Plot.__init__(self, pb2_object, channel)
        if SummaryPlot.__custom_init__ is not None:
            SummaryPlot.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class SummaryPlotCollection(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        PdmObjectBase.__init__(self, pb2_object, channel)
        if SummaryPlotCollection.__custom_init__ is not None:
            SummaryPlotCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def new_summary_plot(self, summary_cases: List[SummaryCase]=[], ensemble: Optional[SummaryCaseSubCollection]=None, address: str="") -> SummaryPlot:
        """
        Create a new Summary Plot

        Arguments:
            summary_cases (List[SummaryCase]): Summary Cases
            ensemble (Optional[SummaryCaseSubCollection]): Ensemble
            address (str): Formatted address string specifying the plot options
        Returns:
            SummaryPlot
        """
        return self._call_pdm_method_return_value("NewSummaryPlot", SummaryPlot, summary_cases=summary_cases, ensemble=ensemble, address=address)


class Surface(SurfaceInterface):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        SurfaceInterface.__init__(self, pb2_object, channel)
        if Surface.__custom_init__ is not None:
            Surface.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class ThermalFractureTemplate(MeshFractureTemplate):
    """
    Attributes:
        filter_cake_pressure_drop (str): One of [None, Relative, Absolute]
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.filter_cake_pressure_drop: str = "Relative"
        MeshFractureTemplate.__init__(self, pb2_object, channel)
        if ThermalFractureTemplate.__custom_init__ is not None:
            ThermalFractureTemplate.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def export_to_file(self, file_path: str="", time_step: int=0) -> Optional[ThermalFractureTemplate]:
        """
        Export Thermal Fracture Template to File

        Arguments:
            file_path (str): File Path
            time_step (int): 
        Returns:
            ThermalFractureTemplate
        """
        return self._call_pdm_method_return_optional_value("ExportToFile", ThermalFractureTemplate, file_path=file_path, time_step=time_step)


    def time_steps(self, ) -> Optional[DataContainerString]:
        """
        Get Thermal Fracture Template Time Steps

        Arguments:
            
        Returns:
            DataContainerString
        """
        return self._call_pdm_method_return_optional_value("TimeSteps", DataContainerString)


class TriangleGeometry(PdmObjectBase):
    """
    Attributes:
        connections (List[int]): Indices to triangle vertices
        display_model_offset (List[float]): Display Model Offset
        fault_mesh_x_coords (List[float]): Fault Mesh X coords
        fault_mesh_y_coords (List[float]): Fault Mesh Y coords
        fault_mesh_z_coords (List[float]): Fault Mesh Z coords
        mesh_x_coords (List[float]): Mesh X coords
        mesh_y_coords (List[float]): Mesh Y coords
        mesh_z_coords (List[float]): Mesh Z coords
        x_coords (List[float]): X coords
        y_coords (List[float]): Y coords
        z_coords (List[float]): Z coords
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.connections: List[int] = []
        self.display_model_offset: List[float] = [0, 0, 0]
        self.fault_mesh_x_coords: List[float] = []
        self.fault_mesh_y_coords: List[float] = []
        self.fault_mesh_z_coords: List[float] = []
        self.mesh_x_coords: List[float] = []
        self.mesh_y_coords: List[float] = []
        self.mesh_z_coords: List[float] = []
        self.x_coords: List[float] = []
        self.y_coords: List[float] = []
        self.z_coords: List[float] = []
        PdmObjectBase.__init__(self, pb2_object, channel)
        if TriangleGeometry.__custom_init__ is not None:
            TriangleGeometry.__custom_init__(self, pb2_object=pb2_object, channel=channel)

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

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.df_source: str = "LAS_FILE"
        self.fg_multiplier: float = 1.05
        self.fg_shale_source: str = "DERIVED_FROM_K0FG"
        self.k0_fg_source: str = "LAS_FILE"
        self.k0_sh_source: str = "LAS_FILE"
        self.obg0_source: str = "GRID"
        self.poission_ratio_source: str = "LAS_FILE"
        self.pore_pressure_non_reservoir_source: str = "LAS_FILE"
        self.pore_pressure_reservoir_source: str = "GRID"
        self.ucs_source: str = "LAS_FILE"
        self.user_df: float = 0.7
        self.user_k0_fg: float = 0.75
        self.user_k0_sh: float = 0.65
        self.user_poisson_ratio: float = 0.35
        self.user_pp_non_reservoir: float = 1
        self.user_ucs: float = 100
        self.water_density: float = 1.03
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

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.name: str = ""
        PdmObjectBase.__init__(self, pb2_object, channel)
        if SimulationWell.__custom_init__ is not None:
            SimulationWell.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class WellLogPlot(DepthTrackPlot):
    """
    A Well Log Plot With a shared Depth Axis and Multiple Tracks

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        DepthTrackPlot.__init__(self, pb2_object, channel)
        if WellLogPlot.__custom_init__ is not None:
            WellLogPlot.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def new_well_log_track(self, title: str="", case: Optional[Reservoir]=None, well_path: Optional[WellPath]=None) -> WellLogPlotTrack:
        """
        Create a new well log track

        Arguments:
            title (str): Title
            case (Optional[Reservoir]): Case
            well_path (Optional[WellPath]): Well Path
        Returns:
            WellLogPlotTrack
        """
        return self._call_pdm_method_return_value("NewWellLogTrack", WellLogPlotTrack, title=title, case=case, well_path=well_path)


class WellBoreStabilityPlot(WellLogPlot):
    """
    A GeoMechanical Well Bore Stability Plot

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        WellLogPlot.__init__(self, pb2_object, channel)
        if WellBoreStabilityPlot.__custom_init__ is not None:
            WellBoreStabilityPlot.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def parameters(self) -> Optional[WbsParameters]:
        """Well Bore Stability Parameters

        Returns:
             WbsParameters
        """
        children = self.children("Parameters", WbsParameters)
        return children[0] if len(children) > 0 else None


class PlotCurve(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        PdmObjectBase.__init__(self, pb2_object, channel)
        if PlotCurve.__custom_init__ is not None:
            PlotCurve.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class WellLogPlotCurve(PlotCurve):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        PlotCurve.__init__(self, pb2_object, channel)
        if WellLogPlotCurve.__custom_init__ is not None:
            WellLogPlotCurve.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class WellLogExtractionCurve(WellLogPlotCurve):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        WellLogPlotCurve.__init__(self, pb2_object, channel)
        if WellLogExtractionCurve.__custom_init__ is not None:
            WellLogExtractionCurve.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class WellLogPlotCollection(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        PdmObjectBase.__init__(self, pb2_object, channel)
        if WellLogPlotCollection.__custom_init__ is not None:
            WellLogPlotCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def new_well_log_plot(self, case: Optional[Reservoir]=None, well_path: Optional[WellPath]=None, property_type: str="", property_name: str="", time_step: int=0) -> WellLogPlot:
        """
        Create a new well log plot

        Arguments:
            case (Optional[Reservoir]): Case
            well_path (Optional[WellPath]): Well Path
            property_type (str): Property Type
            property_name (str): Property Name
            time_step (int): Time Step
        Returns:
            WellLogPlot
        """
        return self._call_pdm_method_return_value("NewWellLogPlot", WellLogPlot, case=case, well_path=well_path, property_type=property_type, property_name=property_name, time_step=time_step)


    def well_log_plots(self) -> List[WellLogPlot]:
        """

        Returns:
             List[WellLogPlot]
        """
        return self.children("WellLogPlots", WellLogPlot)


class WellLogPlotTrack(Plot):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        Plot.__init__(self, pb2_object, channel)
        if WellLogPlotTrack.__custom_init__ is not None:
            WellLogPlotTrack.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def add_extraction_curve(self, case: Optional[Reservoir]=None, well_path: Optional[WellPath]=None, property_type: str="", property_name: str="", time_step: int=0) -> WellLogExtractionCurve:
        """
        Create a well log extraction curve

        Arguments:
            case (Optional[Reservoir]): Case
            well_path (Optional[WellPath]): Well Path
            property_type (str): Property Type
            property_name (str): Property Name
            time_step (int): Time Step
        Returns:
            WellLogExtractionCurve
        """
        return self._call_pdm_method_return_value("AddExtractionCurve", WellLogExtractionCurve, case=case, well_path=well_path, property_type=property_type, property_name=property_name, time_step=time_step)


class FileWellPath(WellPath):
    """
    Well Paths Loaded From File

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        WellPath.__init__(self, pb2_object, channel)
        if FileWellPath.__custom_init__ is not None:
            FileWellPath.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class WellPathCompletionSettings(PdmObjectBase):
    """
    Attributes:
        allow_well_cross_flow (bool): Allow Well Cross-Flow
        auto_well_shut_in (str): One of [SHUT, STOP]
        drainage_radius_for_pi (str): Drainage Radius for PI
        fluid_in_place_region (int): Fluid In-Place Region
        gas_inflow_eq (str): One of [STD, R-G, P-P, GPP]
        group_name_for_export (str): Group Name
        hydrostatic_density (str): One of [SEG, AVG]
        msw_liner_diameter (float): MSW Liner Diameter
        msw_roughness (float): MSW Roughness
        reference_depth_for_export (str): Reference Depth for BHP
        well_bore_fluid_pvt_table (int): Wellbore Fluid PVT table
        well_name_for_export (str): Well Name
        well_type_for_export (str): One of [OIL, GAS, WATER, LIQUID]
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.allow_well_cross_flow: bool = True
        self.auto_well_shut_in: str = "STOP"
        self.drainage_radius_for_pi: str = "0.0"
        self.fluid_in_place_region: int = 0
        self.gas_inflow_eq: str = "STD"
        self.group_name_for_export: str = ""
        self.hydrostatic_density: str = "SEG"
        self.msw_liner_diameter: float = 0.152
        self.msw_roughness: float = 1e-05
        self.reference_depth_for_export: str = ""
        self.well_bore_fluid_pvt_table: int = 0
        self.well_name_for_export: str = ""
        self.well_type_for_export: str = "OIL"
        PdmObjectBase.__init__(self, pb2_object, channel)
        if WellPathCompletionSettings.__custom_init__ is not None:
            WellPathCompletionSettings.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class WellPathCompletions(PdmObjectBase):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        PdmObjectBase.__init__(self, pb2_object, channel)
        if WellPathCompletions.__custom_init__ is not None:
            WellPathCompletions.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def perforations(self) -> Optional[PerforationCollection]:
        """Perforations

        Returns:
             PerforationCollection
        """
        children = self.children("Perforations", PerforationCollection)
        return children[0] if len(children) > 0 else None


class Fracture(CheckableNamedObject):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        CheckableNamedObject.__init__(self, pb2_object, channel)
        if Fracture.__custom_init__ is not None:
            Fracture.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class WellPathFracture(Fracture):
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        Fracture.__init__(self, pb2_object, channel)
        if WellPathFracture.__custom_init__ is not None:
            WellPathFracture.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class WellPathGeometry(PdmObjectBase):
    """
    Class containing the geometry of a modeled Well Path

    Attributes:
        air_gap (float): Air Gap
        attached_to_parent_well (bool): Attached to Parent Well
        link_reference_point_updates (bool): Link Reference Point
        md_at_first_target (float): MD at First Target
        reference_point (List[float]): UTM Reference Point
        show_spheres (bool): Spheres
        use_auto_generated_target_at_sea_level (bool): Generate Target at Sea Level
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.air_gap: float = 0
        self.attached_to_parent_well: bool = False
        self.link_reference_point_updates: bool = False
        self.md_at_first_target: float = 0
        self.reference_point: List[float] = [0, 0, 0]
        self.show_spheres: bool = True
        self.use_auto_generated_target_at_sea_level: bool = True
        PdmObjectBase.__init__(self, pb2_object, channel)
        if WellPathGeometry.__custom_init__ is not None:
            WellPathGeometry.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def append_well_target(self, coordinate: List[float]=[0, 0, 0], absolute: bool=False, use_fixed_azimuth: bool=False, use_fixed_inclination: bool=False, fixed_azimuth_value: float=0, fixed_inclination_value: float=0) -> WellPathTarget:
        """
        Create and Add New Well Target

        Arguments:
            coordinate (List[float]): Coordinate
            absolute (bool): Relative or Absolute Coordinate
            use_fixed_azimuth (bool): 
            use_fixed_inclination (bool): 
            fixed_azimuth_value (float): [Degrees]
            fixed_inclination_value (float): [Degrees]
        Returns:
            WellPathTarget
        """
        return self._call_pdm_method_return_value("AppendWellTarget", WellPathTarget, coordinate=coordinate, absolute=absolute, use_fixed_azimuth=use_fixed_azimuth, use_fixed_inclination=use_fixed_inclination, fixed_azimuth_value=fixed_azimuth_value, fixed_inclination_value=fixed_inclination_value)


    def auto_generated_target(self) -> Optional[WellPathTarget]:
        """Auto Generated Target

        Returns:
             WellPathTarget
        """
        children = self.children("AutoGeneratedTarget", WellPathTarget)
        return children[0] if len(children) > 0 else None


    def well_path_targets(self) -> List[WellPathTarget]:
        """Well Targets

        Returns:
             List[WellPathTarget]
        """
        return self.children("WellPathTargets", WellPathTarget)


class WellPathTarget(PdmObjectBase):
    """
    Class containing the Well Target definition

    Attributes:
        azimuth (float): Azi(deg)
        dogleg1 (float): DL in
        dogleg2 (float): DL out
        estimated_azimuth (float): Est Azi(deg)
        estimated_dogleg1 (float): Est DL in
        estimated_dogleg2 (float): Est DL out
        estimated_inclination (float): Est Inc(deg)
        inclination (float): Inc(deg)
        target_measured_depth (float): MD
        target_point (List[float]): Relative Coord
        use_fixed_azimuth (bool): Azi
        use_fixed_inclination (bool): Inc
    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        self.azimuth: float = 0
        self.dogleg1: float = 3
        self.dogleg2: float = 3
        self.estimated_azimuth: float = 0
        self.estimated_dogleg1: float = 0
        self.estimated_dogleg2: float = 0
        self.estimated_inclination: float = 0
        self.inclination: float = 0
        self.target_measured_depth: float = 0
        self.target_point: List[float] = [0, 0, 0]
        self.use_fixed_azimuth: bool = False
        self.use_fixed_inclination: bool = False
        PdmObjectBase.__init__(self, pb2_object, channel)
        if WellPathTarget.__custom_init__ is not None:
            WellPathTarget.__custom_init__(self, pb2_object=pb2_object, channel=channel)

class WellPathCollection(PdmObjectBase):
    """
    Collection of Well Paths

    """
    __custom_init__ = None #: Assign a custom init routine to be run at __init__

    def __init__(self, pb2_object: Optional[PdmObject_pb2.PdmObject]=None, channel: Optional[grpc.Channel]=None) -> None:
        PdmObjectBase.__init__(self, pb2_object, channel)
        if WellPathCollection.__custom_init__ is not None:
            WellPathCollection.__custom_init__(self, pb2_object=pb2_object, channel=channel)

    def well_paths(self) -> List[FileWellPath]:
        """Well Paths

        Returns:
             List[FileWellPath]
        """
        return self.children("WellPaths", FileWellPath)


def class_dict() -> Dict[str, Type[PdmObjectBase]]:
    classes : Dict[str, Type[PdmObjectBase]] = {}
    classes['Case'] = Case
    classes['CellColors'] = CellColors
    classes['CellFilterCollection'] = CellFilterCollection
    classes['CheckableNamedObject'] = CheckableNamedObject
    classes['ColorLegend'] = ColorLegend
    classes['CommandRouter'] = CommandRouter
    classes['CurveIntersection'] = CurveIntersection
    classes['DataContainerFloat'] = DataContainerFloat
    classes['DataContainerString'] = DataContainerString
    classes['DataContainerTime'] = DataContainerTime
    classes['DepthTrackPlot'] = DepthTrackPlot
    classes['EclipseCase'] = EclipseCase
    classes['EclipseCaseEnsemble'] = EclipseCaseEnsemble
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
    classes['Fracture'] = Fracture
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
    classes['IntersectionCollection'] = IntersectionCollection
    classes['MeshFractureTemplate'] = MeshFractureTemplate
    classes['ModeledWellPath'] = ModeledWellPath
    classes['MswSettings'] = MswSettings
    classes['MudWeightWindowParameters'] = MudWeightWindowParameters
    classes['NamedObject'] = NamedObject
    classes['NonNetLayers'] = NonNetLayers
    classes['OsduWellPath'] = OsduWellPath
    classes['PdmObjectBase'] = PdmObjectBase
    classes['Perforation'] = Perforation
    classes['PerforationCollection'] = PerforationCollection
    classes['Plot'] = Plot
    classes['PlotCurve'] = PlotCurve
    classes['PlotWindow'] = PlotWindow
    classes['PressureTable'] = PressureTable
    classes['PressureTableItem'] = PressureTableItem
    classes['Project'] = Project
    classes['ResampleData'] = ResampleData
    classes['Reservoir'] = Reservoir
    classes['RimDepthSurface'] = RimDepthSurface
    classes['RimEmCase'] = RimEmCase
    classes['RimRoffCase'] = RimRoffCase
    classes['RimStatisticalCalculation'] = RimStatisticalCalculation
    classes['RimSummaryCaseSumo'] = RimSummaryCaseSumo
    classes['RimTextAnnotation'] = RimTextAnnotation
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
    classes['ThermalFractureTemplate'] = ThermalFractureTemplate
    classes['TriangleGeometry'] = TriangleGeometry
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
    classes['WellPathCompletionSettings'] = WellPathCompletionSettings
    classes['WellPathCompletions'] = WellPathCompletions
    classes['WellPathFracture'] = WellPathFracture
    classes['WellPathGeometry'] = WellPathGeometry
    classes['WellPathTarget'] = WellPathTarget
    return classes

def class_from_keyword(class_keyword : str) -> Optional[Type[PdmObjectBase]]:
    all_classes = class_dict()
    if class_keyword in all_classes.keys():
        return all_classes[class_keyword]
    return None
