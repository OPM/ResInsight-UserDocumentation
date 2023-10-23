import PdmObject_pb2 as _PdmObject_pb2
import Definitions_pb2 as _Definitions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PorosityModelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    MATRIX_MODEL: _ClassVar[PorosityModelType]
    FRACTURE_MODEL: _ClassVar[PorosityModelType]
MATRIX_MODEL: PorosityModelType
FRACTURE_MODEL: PorosityModelType

class CaseRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class CaseInfo(_message.Message):
    __slots__ = ["id", "group_id", "name", "type"]
    ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    group_id: int
    name: str
    type: str
    def __init__(self, id: _Optional[int] = ..., group_id: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class CaseInfoArray(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[CaseInfo]
    def __init__(self, data: _Optional[_Iterable[_Union[CaseInfo, _Mapping]]] = ...) -> None: ...

class BoundingBox(_message.Message):
    __slots__ = ["min_x", "max_x", "min_y", "max_y", "min_z", "max_z"]
    MIN_X_FIELD_NUMBER: _ClassVar[int]
    MAX_X_FIELD_NUMBER: _ClassVar[int]
    MIN_Y_FIELD_NUMBER: _ClassVar[int]
    MAX_Y_FIELD_NUMBER: _ClassVar[int]
    MIN_Z_FIELD_NUMBER: _ClassVar[int]
    MAX_Z_FIELD_NUMBER: _ClassVar[int]
    min_x: float
    max_x: float
    min_y: float
    max_y: float
    min_z: float
    max_z: float
    def __init__(self, min_x: _Optional[float] = ..., max_x: _Optional[float] = ..., min_y: _Optional[float] = ..., max_y: _Optional[float] = ..., min_z: _Optional[float] = ..., max_z: _Optional[float] = ...) -> None: ...

class CaseGroup(_message.Message):
    __slots__ = ["id", "name"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class CaseGroups(_message.Message):
    __slots__ = ["case_groups"]
    CASE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    case_groups: _containers.RepeatedCompositeFieldContainer[CaseGroup]
    def __init__(self, case_groups: _Optional[_Iterable[_Union[CaseGroup, _Mapping]]] = ...) -> None: ...

class GridCount(_message.Message):
    __slots__ = ["count"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class CellCount(_message.Message):
    __slots__ = ["active_cell_count", "reservoir_cell_count"]
    ACTIVE_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESERVOIR_CELL_COUNT_FIELD_NUMBER: _ClassVar[int]
    active_cell_count: int
    reservoir_cell_count: int
    def __init__(self, active_cell_count: _Optional[int] = ..., reservoir_cell_count: _Optional[int] = ...) -> None: ...

class CellInfoRequest(_message.Message):
    __slots__ = ["case_request", "porosity_model"]
    CASE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    POROSITY_MODEL_FIELD_NUMBER: _ClassVar[int]
    case_request: CaseRequest
    porosity_model: PorosityModelType
    def __init__(self, case_request: _Optional[_Union[CaseRequest, _Mapping]] = ..., porosity_model: _Optional[_Union[PorosityModelType, str]] = ...) -> None: ...

class CellInfoArray(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[CellInfo]
    def __init__(self, data: _Optional[_Iterable[_Union[CellInfo, _Mapping]]] = ...) -> None: ...

class CellInfo(_message.Message):
    __slots__ = ["grid_index", "parent_grid_index", "coarsening_box_index", "local_ijk", "parent_ijk"]
    GRID_INDEX_FIELD_NUMBER: _ClassVar[int]
    PARENT_GRID_INDEX_FIELD_NUMBER: _ClassVar[int]
    COARSENING_BOX_INDEX_FIELD_NUMBER: _ClassVar[int]
    LOCAL_IJK_FIELD_NUMBER: _ClassVar[int]
    PARENT_IJK_FIELD_NUMBER: _ClassVar[int]
    grid_index: int
    parent_grid_index: int
    coarsening_box_index: int
    local_ijk: _Definitions_pb2.Vec3i
    parent_ijk: _Definitions_pb2.Vec3i
    def __init__(self, grid_index: _Optional[int] = ..., parent_grid_index: _Optional[int] = ..., coarsening_box_index: _Optional[int] = ..., local_ijk: _Optional[_Union[_Definitions_pb2.Vec3i, _Mapping]] = ..., parent_ijk: _Optional[_Union[_Definitions_pb2.Vec3i, _Mapping]] = ...) -> None: ...

class CoarseningInfoArray(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[CoarseningInfo]
    def __init__(self, data: _Optional[_Iterable[_Union[CoarseningInfo, _Mapping]]] = ...) -> None: ...

class CoarseningInfo(_message.Message):
    __slots__ = ["min", "max"]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    min: _Definitions_pb2.Vec3i
    max: _Definitions_pb2.Vec3i
    def __init__(self, min: _Optional[_Union[_Definitions_pb2.Vec3i, _Mapping]] = ..., max: _Optional[_Union[_Definitions_pb2.Vec3i, _Mapping]] = ...) -> None: ...

class TimeStepDates(_message.Message):
    __slots__ = ["dates"]
    DATES_FIELD_NUMBER: _ClassVar[int]
    dates: _containers.RepeatedCompositeFieldContainer[TimeStepDate]
    def __init__(self, dates: _Optional[_Iterable[_Union[TimeStepDate, _Mapping]]] = ...) -> None: ...

class TimeStepDate(_message.Message):
    __slots__ = ["year", "month", "day", "hour", "minute", "second"]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    HOUR_FIELD_NUMBER: _ClassVar[int]
    MINUTE_FIELD_NUMBER: _ClassVar[int]
    SECOND_FIELD_NUMBER: _ClassVar[int]
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int
    def __init__(self, year: _Optional[int] = ..., month: _Optional[int] = ..., day: _Optional[int] = ..., hour: _Optional[int] = ..., minute: _Optional[int] = ..., second: _Optional[int] = ...) -> None: ...

class DaysSinceStart(_message.Message):
    __slots__ = ["day_decimals"]
    DAY_DECIMALS_FIELD_NUMBER: _ClassVar[int]
    day_decimals: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, day_decimals: _Optional[_Iterable[float]] = ...) -> None: ...

class SelectedCell(_message.Message):
    __slots__ = ["grid_index", "ijk"]
    GRID_INDEX_FIELD_NUMBER: _ClassVar[int]
    IJK_FIELD_NUMBER: _ClassVar[int]
    grid_index: int
    ijk: _Definitions_pb2.Vec3i
    def __init__(self, grid_index: _Optional[int] = ..., ijk: _Optional[_Union[_Definitions_pb2.Vec3i, _Mapping]] = ...) -> None: ...

class SelectedCells(_message.Message):
    __slots__ = ["cells"]
    CELLS_FIELD_NUMBER: _ClassVar[int]
    cells: _containers.RepeatedCompositeFieldContainer[SelectedCell]
    def __init__(self, cells: _Optional[_Iterable[_Union[SelectedCell, _Mapping]]] = ...) -> None: ...
