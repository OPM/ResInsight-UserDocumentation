import Case_pb2 as _Case_pb2
import Definitions_pb2 as _Definitions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NNCPropertyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    NNC_DYNAMIC: _ClassVar[NNCPropertyType]
    NNC_STATIC: _ClassVar[NNCPropertyType]
    NNC_GENERATED: _ClassVar[NNCPropertyType]
NNC_DYNAMIC: NNCPropertyType
NNC_STATIC: NNCPropertyType
NNC_GENERATED: NNCPropertyType

class AvailableNNCProperty(_message.Message):
    __slots__ = ["name", "property_type"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    property_type: NNCPropertyType
    def __init__(self, name: _Optional[str] = ..., property_type: _Optional[_Union[NNCPropertyType, str]] = ...) -> None: ...

class AvailableNNCProperties(_message.Message):
    __slots__ = ["properties"]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    properties: _containers.RepeatedCompositeFieldContainer[AvailableNNCProperty]
    def __init__(self, properties: _Optional[_Iterable[_Union[AvailableNNCProperty, _Mapping]]] = ...) -> None: ...

class NNCConnection(_message.Message):
    __slots__ = ["cell_grid_index1", "cell_grid_index2", "cell1", "cell2"]
    CELL_GRID_INDEX1_FIELD_NUMBER: _ClassVar[int]
    CELL_GRID_INDEX2_FIELD_NUMBER: _ClassVar[int]
    CELL1_FIELD_NUMBER: _ClassVar[int]
    CELL2_FIELD_NUMBER: _ClassVar[int]
    cell_grid_index1: int
    cell_grid_index2: int
    cell1: _Definitions_pb2.Vec3i
    cell2: _Definitions_pb2.Vec3i
    def __init__(self, cell_grid_index1: _Optional[int] = ..., cell_grid_index2: _Optional[int] = ..., cell1: _Optional[_Union[_Definitions_pb2.Vec3i, _Mapping]] = ..., cell2: _Optional[_Union[_Definitions_pb2.Vec3i, _Mapping]] = ...) -> None: ...

class NNCConnections(_message.Message):
    __slots__ = ["connections"]
    CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    connections: _containers.RepeatedCompositeFieldContainer[NNCConnection]
    def __init__(self, connections: _Optional[_Iterable[_Union[NNCConnection, _Mapping]]] = ...) -> None: ...

class NNCValuesRequest(_message.Message):
    __slots__ = ["case_id", "property_name", "property_type", "time_step"]
    CASE_ID_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_STEP_FIELD_NUMBER: _ClassVar[int]
    case_id: int
    property_name: str
    property_type: NNCPropertyType
    time_step: int
    def __init__(self, case_id: _Optional[int] = ..., property_name: _Optional[str] = ..., property_type: _Optional[_Union[NNCPropertyType, str]] = ..., time_step: _Optional[int] = ...) -> None: ...

class NNCValues(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, values: _Optional[_Iterable[float]] = ...) -> None: ...

class NNCValuesInputRequest(_message.Message):
    __slots__ = ["case_id", "property_name", "porosity_model", "time_step"]
    CASE_ID_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_NAME_FIELD_NUMBER: _ClassVar[int]
    POROSITY_MODEL_FIELD_NUMBER: _ClassVar[int]
    TIME_STEP_FIELD_NUMBER: _ClassVar[int]
    case_id: int
    property_name: str
    porosity_model: _Case_pb2.PorosityModelType
    time_step: int
    def __init__(self, case_id: _Optional[int] = ..., property_name: _Optional[str] = ..., porosity_model: _Optional[_Union[_Case_pb2.PorosityModelType, str]] = ..., time_step: _Optional[int] = ...) -> None: ...

class NNCValuesChunk(_message.Message):
    __slots__ = ["params", "values"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    params: NNCValuesInputRequest
    values: NNCValues
    def __init__(self, params: _Optional[_Union[NNCValuesInputRequest, _Mapping]] = ..., values: _Optional[_Union[NNCValues, _Mapping]] = ...) -> None: ...
