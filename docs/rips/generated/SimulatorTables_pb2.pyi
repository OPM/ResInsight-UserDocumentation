from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SimulatorTableRequest(_message.Message):
    __slots__ = ("wellpath_name", "case_id")
    WELLPATH_NAME_FIELD_NUMBER: _ClassVar[int]
    CASE_ID_FIELD_NUMBER: _ClassVar[int]
    wellpath_name: str
    case_id: int
    def __init__(self, wellpath_name: _Optional[str] = ..., case_id: _Optional[int] = ...) -> None: ...

class SimulatorTableUnifiedRequest(_message.Message):
    __slots__ = ("wellpath_names", "case_id")
    WELLPATH_NAMES_FIELD_NUMBER: _ClassVar[int]
    CASE_ID_FIELD_NUMBER: _ClassVar[int]
    wellpath_names: _containers.RepeatedScalarFieldContainer[str]
    case_id: int
    def __init__(self, wellpath_names: _Optional[_Iterable[str]] = ..., case_id: _Optional[int] = ...) -> None: ...

class SimulatorCompdatEntry(_message.Message):
    __slots__ = ("well_name", "grid_i", "grid_j", "upper_k", "lower_k", "open_shut_flag", "saturation", "transmissibility", "diameter", "kh", "skin_factor", "d_factor", "direction", "start_md", "end_md", "comment", "grid_name", "completion_number")
    WELL_NAME_FIELD_NUMBER: _ClassVar[int]
    GRID_I_FIELD_NUMBER: _ClassVar[int]
    GRID_J_FIELD_NUMBER: _ClassVar[int]
    UPPER_K_FIELD_NUMBER: _ClassVar[int]
    LOWER_K_FIELD_NUMBER: _ClassVar[int]
    OPEN_SHUT_FLAG_FIELD_NUMBER: _ClassVar[int]
    SATURATION_FIELD_NUMBER: _ClassVar[int]
    TRANSMISSIBILITY_FIELD_NUMBER: _ClassVar[int]
    DIAMETER_FIELD_NUMBER: _ClassVar[int]
    KH_FIELD_NUMBER: _ClassVar[int]
    SKIN_FACTOR_FIELD_NUMBER: _ClassVar[int]
    D_FACTOR_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    START_MD_FIELD_NUMBER: _ClassVar[int]
    END_MD_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    GRID_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    well_name: str
    grid_i: int
    grid_j: int
    upper_k: int
    lower_k: int
    open_shut_flag: str
    saturation: float
    transmissibility: float
    diameter: float
    kh: float
    skin_factor: float
    d_factor: float
    direction: str
    start_md: float
    end_md: float
    comment: str
    grid_name: str
    completion_number: int
    def __init__(self, well_name: _Optional[str] = ..., grid_i: _Optional[int] = ..., grid_j: _Optional[int] = ..., upper_k: _Optional[int] = ..., lower_k: _Optional[int] = ..., open_shut_flag: _Optional[str] = ..., saturation: _Optional[float] = ..., transmissibility: _Optional[float] = ..., diameter: _Optional[float] = ..., kh: _Optional[float] = ..., skin_factor: _Optional[float] = ..., d_factor: _Optional[float] = ..., direction: _Optional[str] = ..., start_md: _Optional[float] = ..., end_md: _Optional[float] = ..., comment: _Optional[str] = ..., grid_name: _Optional[str] = ..., completion_number: _Optional[int] = ...) -> None: ...

class SimulatorWelspecsEntry(_message.Message):
    __slots__ = ("well_name", "group_name", "grid_i", "grid_j", "bhp_depth", "phase", "drainage_radius", "inflow_equation", "auto_shut_in", "cross_flow", "pvt_num", "hydrostatic_density_calc", "fip_region", "grid_name")
    WELL_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    GRID_I_FIELD_NUMBER: _ClassVar[int]
    GRID_J_FIELD_NUMBER: _ClassVar[int]
    BHP_DEPTH_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    DRAINAGE_RADIUS_FIELD_NUMBER: _ClassVar[int]
    INFLOW_EQUATION_FIELD_NUMBER: _ClassVar[int]
    AUTO_SHUT_IN_FIELD_NUMBER: _ClassVar[int]
    CROSS_FLOW_FIELD_NUMBER: _ClassVar[int]
    PVT_NUM_FIELD_NUMBER: _ClassVar[int]
    HYDROSTATIC_DENSITY_CALC_FIELD_NUMBER: _ClassVar[int]
    FIP_REGION_FIELD_NUMBER: _ClassVar[int]
    GRID_NAME_FIELD_NUMBER: _ClassVar[int]
    well_name: str
    group_name: str
    grid_i: int
    grid_j: int
    bhp_depth: float
    phase: str
    drainage_radius: float
    inflow_equation: str
    auto_shut_in: str
    cross_flow: str
    pvt_num: int
    hydrostatic_density_calc: str
    fip_region: int
    grid_name: str
    def __init__(self, well_name: _Optional[str] = ..., group_name: _Optional[str] = ..., grid_i: _Optional[int] = ..., grid_j: _Optional[int] = ..., bhp_depth: _Optional[float] = ..., phase: _Optional[str] = ..., drainage_radius: _Optional[float] = ..., inflow_equation: _Optional[str] = ..., auto_shut_in: _Optional[str] = ..., cross_flow: _Optional[str] = ..., pvt_num: _Optional[int] = ..., hydrostatic_density_calc: _Optional[str] = ..., fip_region: _Optional[int] = ..., grid_name: _Optional[str] = ...) -> None: ...

class SimulatorWelsegsHeaderEntry(_message.Message):
    __slots__ = ("well_name", "top_depth", "top_length", "wellbore_volume", "info_type", "pressure_components", "flow_model")
    WELL_NAME_FIELD_NUMBER: _ClassVar[int]
    TOP_DEPTH_FIELD_NUMBER: _ClassVar[int]
    TOP_LENGTH_FIELD_NUMBER: _ClassVar[int]
    WELLBORE_VOLUME_FIELD_NUMBER: _ClassVar[int]
    INFO_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRESSURE_COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    FLOW_MODEL_FIELD_NUMBER: _ClassVar[int]
    well_name: str
    top_depth: float
    top_length: float
    wellbore_volume: float
    info_type: str
    pressure_components: str
    flow_model: str
    def __init__(self, well_name: _Optional[str] = ..., top_depth: _Optional[float] = ..., top_length: _Optional[float] = ..., wellbore_volume: _Optional[float] = ..., info_type: _Optional[str] = ..., pressure_components: _Optional[str] = ..., flow_model: _Optional[str] = ...) -> None: ...

class SimulatorWelsegsRowEntry(_message.Message):
    __slots__ = ("segment_1", "segment_2", "branch", "join_segment", "length", "depth", "diameter", "roughness", "description")
    SEGMENT_1_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_2_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    JOIN_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    DIAMETER_FIELD_NUMBER: _ClassVar[int]
    ROUGHNESS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    segment_1: int
    segment_2: int
    branch: int
    join_segment: int
    length: float
    depth: float
    diameter: float
    roughness: float
    description: str
    def __init__(self, segment_1: _Optional[int] = ..., segment_2: _Optional[int] = ..., branch: _Optional[int] = ..., join_segment: _Optional[int] = ..., length: _Optional[float] = ..., depth: _Optional[float] = ..., diameter: _Optional[float] = ..., roughness: _Optional[float] = ..., description: _Optional[str] = ...) -> None: ...

class SimulatorWelsegsEntry(_message.Message):
    __slots__ = ("header", "row")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    header: SimulatorWelsegsHeaderEntry
    row: _containers.RepeatedCompositeFieldContainer[SimulatorWelsegsRowEntry]
    def __init__(self, header: _Optional[_Union[SimulatorWelsegsHeaderEntry, _Mapping]] = ..., row: _Optional[_Iterable[_Union[SimulatorWelsegsRowEntry, _Mapping]]] = ...) -> None: ...

class SimulatorCompsegsEntry(_message.Message):
    __slots__ = ("i", "j", "k", "branch", "distance_start", "distance_end", "grid_name")
    I_FIELD_NUMBER: _ClassVar[int]
    J_FIELD_NUMBER: _ClassVar[int]
    K_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_START_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_END_FIELD_NUMBER: _ClassVar[int]
    GRID_NAME_FIELD_NUMBER: _ClassVar[int]
    i: int
    j: int
    k: int
    branch: int
    distance_start: float
    distance_end: float
    grid_name: str
    def __init__(self, i: _Optional[int] = ..., j: _Optional[int] = ..., k: _Optional[int] = ..., branch: _Optional[int] = ..., distance_start: _Optional[float] = ..., distance_end: _Optional[float] = ..., grid_name: _Optional[str] = ...) -> None: ...

class SimulatorWsegvalvEntry(_message.Message):
    __slots__ = ("well_name", "segment_number", "cv", "area", "extra_length", "pipe_d", "roughness", "pipe_a", "status", "max_a")
    WELL_NAME_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CV_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    EXTRA_LENGTH_FIELD_NUMBER: _ClassVar[int]
    PIPE_D_FIELD_NUMBER: _ClassVar[int]
    ROUGHNESS_FIELD_NUMBER: _ClassVar[int]
    PIPE_A_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MAX_A_FIELD_NUMBER: _ClassVar[int]
    well_name: str
    segment_number: int
    cv: float
    area: float
    extra_length: float
    pipe_d: float
    roughness: float
    pipe_a: float
    status: str
    max_a: float
    def __init__(self, well_name: _Optional[str] = ..., segment_number: _Optional[int] = ..., cv: _Optional[float] = ..., area: _Optional[float] = ..., extra_length: _Optional[float] = ..., pipe_d: _Optional[float] = ..., roughness: _Optional[float] = ..., pipe_a: _Optional[float] = ..., status: _Optional[str] = ..., max_a: _Optional[float] = ...) -> None: ...

class SimulatorWsegaicdEntry(_message.Message):
    __slots__ = ("well_name", "segment_1", "segment_2", "strength", "length", "density_cali", "viscosity_cali", "critical_value", "width_trans", "max_visc_ratio", "method_scaling_factor", "max_abs_rate", "flow_rate_exponent", "visc_exponent", "status", "oil_flow_fraction", "water_flow_fraction", "gas_flow_fraction", "oil_visc_fraction", "water_visc_fraction", "gas_visc_fraction", "description")
    WELL_NAME_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_1_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_2_FIELD_NUMBER: _ClassVar[int]
    STRENGTH_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    DENSITY_CALI_FIELD_NUMBER: _ClassVar[int]
    VISCOSITY_CALI_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    WIDTH_TRANS_FIELD_NUMBER: _ClassVar[int]
    MAX_VISC_RATIO_FIELD_NUMBER: _ClassVar[int]
    METHOD_SCALING_FACTOR_FIELD_NUMBER: _ClassVar[int]
    MAX_ABS_RATE_FIELD_NUMBER: _ClassVar[int]
    FLOW_RATE_EXPONENT_FIELD_NUMBER: _ClassVar[int]
    VISC_EXPONENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OIL_FLOW_FRACTION_FIELD_NUMBER: _ClassVar[int]
    WATER_FLOW_FRACTION_FIELD_NUMBER: _ClassVar[int]
    GAS_FLOW_FRACTION_FIELD_NUMBER: _ClassVar[int]
    OIL_VISC_FRACTION_FIELD_NUMBER: _ClassVar[int]
    WATER_VISC_FRACTION_FIELD_NUMBER: _ClassVar[int]
    GAS_VISC_FRACTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    well_name: str
    segment_1: int
    segment_2: int
    strength: float
    length: float
    density_cali: float
    viscosity_cali: float
    critical_value: float
    width_trans: float
    max_visc_ratio: float
    method_scaling_factor: int
    max_abs_rate: float
    flow_rate_exponent: float
    visc_exponent: float
    status: str
    oil_flow_fraction: float
    water_flow_fraction: float
    gas_flow_fraction: float
    oil_visc_fraction: float
    water_visc_fraction: float
    gas_visc_fraction: float
    description: str
    def __init__(self, well_name: _Optional[str] = ..., segment_1: _Optional[int] = ..., segment_2: _Optional[int] = ..., strength: _Optional[float] = ..., length: _Optional[float] = ..., density_cali: _Optional[float] = ..., viscosity_cali: _Optional[float] = ..., critical_value: _Optional[float] = ..., width_trans: _Optional[float] = ..., max_visc_ratio: _Optional[float] = ..., method_scaling_factor: _Optional[int] = ..., max_abs_rate: _Optional[float] = ..., flow_rate_exponent: _Optional[float] = ..., visc_exponent: _Optional[float] = ..., status: _Optional[str] = ..., oil_flow_fraction: _Optional[float] = ..., water_flow_fraction: _Optional[float] = ..., gas_flow_fraction: _Optional[float] = ..., oil_visc_fraction: _Optional[float] = ..., water_visc_fraction: _Optional[float] = ..., gas_visc_fraction: _Optional[float] = ..., description: _Optional[str] = ...) -> None: ...

class SimulatorWpimultEntry(_message.Message):
    __slots__ = ("well_name", "pimult", "i", "j", "k", "grid_name")
    WELL_NAME_FIELD_NUMBER: _ClassVar[int]
    PIMULT_FIELD_NUMBER: _ClassVar[int]
    I_FIELD_NUMBER: _ClassVar[int]
    J_FIELD_NUMBER: _ClassVar[int]
    K_FIELD_NUMBER: _ClassVar[int]
    GRID_NAME_FIELD_NUMBER: _ClassVar[int]
    well_name: str
    pimult: float
    i: int
    j: int
    k: int
    grid_name: str
    def __init__(self, well_name: _Optional[str] = ..., pimult: _Optional[float] = ..., i: _Optional[int] = ..., j: _Optional[int] = ..., k: _Optional[int] = ..., grid_name: _Optional[str] = ...) -> None: ...

class SimulatorTableData(_message.Message):
    __slots__ = ("compdat", "welspecs", "welsegs", "compsegs", "wsegvalv", "wsegaicd", "wpimult")
    COMPDAT_FIELD_NUMBER: _ClassVar[int]
    WELSPECS_FIELD_NUMBER: _ClassVar[int]
    WELSEGS_FIELD_NUMBER: _ClassVar[int]
    COMPSEGS_FIELD_NUMBER: _ClassVar[int]
    WSEGVALV_FIELD_NUMBER: _ClassVar[int]
    WSEGAICD_FIELD_NUMBER: _ClassVar[int]
    WPIMULT_FIELD_NUMBER: _ClassVar[int]
    compdat: _containers.RepeatedCompositeFieldContainer[SimulatorCompdatEntry]
    welspecs: _containers.RepeatedCompositeFieldContainer[SimulatorWelspecsEntry]
    welsegs: _containers.RepeatedCompositeFieldContainer[SimulatorWelsegsEntry]
    compsegs: _containers.RepeatedCompositeFieldContainer[SimulatorCompsegsEntry]
    wsegvalv: _containers.RepeatedCompositeFieldContainer[SimulatorWsegvalvEntry]
    wsegaicd: _containers.RepeatedCompositeFieldContainer[SimulatorWsegaicdEntry]
    wpimult: _containers.RepeatedCompositeFieldContainer[SimulatorWpimultEntry]
    def __init__(self, compdat: _Optional[_Iterable[_Union[SimulatorCompdatEntry, _Mapping]]] = ..., welspecs: _Optional[_Iterable[_Union[SimulatorWelspecsEntry, _Mapping]]] = ..., welsegs: _Optional[_Iterable[_Union[SimulatorWelsegsEntry, _Mapping]]] = ..., compsegs: _Optional[_Iterable[_Union[SimulatorCompsegsEntry, _Mapping]]] = ..., wsegvalv: _Optional[_Iterable[_Union[SimulatorWsegvalvEntry, _Mapping]]] = ..., wsegaicd: _Optional[_Iterable[_Union[SimulatorWsegaicdEntry, _Mapping]]] = ..., wpimult: _Optional[_Iterable[_Union[SimulatorWpimultEntry, _Mapping]]] = ...) -> None: ...
