import Definitions_pb2 as _Definitions_pb2
import Case_pb2 as _Case_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PropertyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DYNAMIC_NATIVE: _ClassVar[PropertyType]
    STATIC_NATIVE: _ClassVar[PropertyType]
    SOURSIMRL: _ClassVar[PropertyType]
    GENERATED: _ClassVar[PropertyType]
    INPUT_PROPERTY: _ClassVar[PropertyType]
    FORMATION_NAMES: _ClassVar[PropertyType]
    FLOW_DIAGNOSTICS: _ClassVar[PropertyType]
    INJECTION_FLOODING: _ClassVar[PropertyType]
    REMOVED: _ClassVar[PropertyType]
    UNDEFINED: _ClassVar[PropertyType]
DYNAMIC_NATIVE: PropertyType
STATIC_NATIVE: PropertyType
SOURSIMRL: PropertyType
GENERATED: PropertyType
INPUT_PROPERTY: PropertyType
FORMATION_NAMES: PropertyType
FLOW_DIAGNOSTICS: PropertyType
INJECTION_FLOODING: PropertyType
REMOVED: PropertyType
UNDEFINED: PropertyType

class AvailablePropertiesRequest(_message.Message):
    __slots__ = ["case_request", "property_type", "porosity_model"]
    CASE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_TYPE_FIELD_NUMBER: _ClassVar[int]
    POROSITY_MODEL_FIELD_NUMBER: _ClassVar[int]
    case_request: _Case_pb2.CaseRequest
    property_type: PropertyType
    porosity_model: _Case_pb2.PorosityModelType
    def __init__(self, case_request: _Optional[_Union[_Case_pb2.CaseRequest, _Mapping]] = ..., property_type: _Optional[_Union[PropertyType, str]] = ..., porosity_model: _Optional[_Union[_Case_pb2.PorosityModelType, str]] = ...) -> None: ...

class AvailableProperties(_message.Message):
    __slots__ = ["property_names"]
    PROPERTY_NAMES_FIELD_NUMBER: _ClassVar[int]
    property_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, property_names: _Optional[_Iterable[str]] = ...) -> None: ...

class PropertyRequest(_message.Message):
    __slots__ = ["case_request", "property_type", "property_name", "time_step", "grid_index", "porosity_model"]
    CASE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_STEP_FIELD_NUMBER: _ClassVar[int]
    GRID_INDEX_FIELD_NUMBER: _ClassVar[int]
    POROSITY_MODEL_FIELD_NUMBER: _ClassVar[int]
    case_request: _Case_pb2.CaseRequest
    property_type: PropertyType
    property_name: str
    time_step: int
    grid_index: int
    porosity_model: _Case_pb2.PorosityModelType
    def __init__(self, case_request: _Optional[_Union[_Case_pb2.CaseRequest, _Mapping]] = ..., property_type: _Optional[_Union[PropertyType, str]] = ..., property_name: _Optional[str] = ..., time_step: _Optional[int] = ..., grid_index: _Optional[int] = ..., porosity_model: _Optional[_Union[_Case_pb2.PorosityModelType, str]] = ...) -> None: ...

class TimeStep(_message.Message):
    __slots__ = ["index"]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    index: int
    def __init__(self, index: _Optional[int] = ...) -> None: ...

class PropertyInputChunk(_message.Message):
    __slots__ = ["params", "values"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    params: PropertyRequest
    values: PropertyChunk
    def __init__(self, params: _Optional[_Union[PropertyRequest, _Mapping]] = ..., values: _Optional[_Union[PropertyChunk, _Mapping]] = ...) -> None: ...

class PropertyChunk(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, values: _Optional[_Iterable[float]] = ...) -> None: ...
