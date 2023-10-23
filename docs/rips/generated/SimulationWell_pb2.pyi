import Definitions_pb2 as _Definitions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SimulationWellRequest(_message.Message):
    __slots__ = ["case_id", "well_name", "timestep"]
    CASE_ID_FIELD_NUMBER: _ClassVar[int]
    WELL_NAME_FIELD_NUMBER: _ClassVar[int]
    TIMESTEP_FIELD_NUMBER: _ClassVar[int]
    case_id: int
    well_name: str
    timestep: int
    def __init__(self, case_id: _Optional[int] = ..., well_name: _Optional[str] = ..., timestep: _Optional[int] = ...) -> None: ...

class SimulationWellStatus(_message.Message):
    __slots__ = ["well_type", "is_open"]
    WELL_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_OPEN_FIELD_NUMBER: _ClassVar[int]
    well_type: str
    is_open: bool
    def __init__(self, well_type: _Optional[str] = ..., is_open: bool = ...) -> None: ...

class SimulationWellCellInfo(_message.Message):
    __slots__ = ["ijk", "grid_index", "is_open", "branch_id", "segment_id"]
    IJK_FIELD_NUMBER: _ClassVar[int]
    GRID_INDEX_FIELD_NUMBER: _ClassVar[int]
    IS_OPEN_FIELD_NUMBER: _ClassVar[int]
    BRANCH_ID_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ijk: _Definitions_pb2.Vec3i
    grid_index: int
    is_open: bool
    branch_id: int
    segment_id: int
    def __init__(self, ijk: _Optional[_Union[_Definitions_pb2.Vec3i, _Mapping]] = ..., grid_index: _Optional[int] = ..., is_open: bool = ..., branch_id: _Optional[int] = ..., segment_id: _Optional[int] = ...) -> None: ...

class SimulationWellCellInfoArray(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[SimulationWellCellInfo]
    def __init__(self, data: _Optional[_Iterable[_Union[SimulationWellCellInfo, _Mapping]]] = ...) -> None: ...
