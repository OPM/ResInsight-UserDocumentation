import Definitions_pb2 as _Definitions_pb2
import Case_pb2 as _Case_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GridRequest(_message.Message):
    __slots__ = ["case_request", "grid_index"]
    CASE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GRID_INDEX_FIELD_NUMBER: _ClassVar[int]
    case_request: _Case_pb2.CaseRequest
    grid_index: int
    def __init__(self, case_request: _Optional[_Union[_Case_pb2.CaseRequest, _Mapping]] = ..., grid_index: _Optional[int] = ...) -> None: ...

class GridDimensions(_message.Message):
    __slots__ = ["dimensions"]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    dimensions: _Definitions_pb2.Vec3i
    def __init__(self, dimensions: _Optional[_Union[_Definitions_pb2.Vec3i, _Mapping]] = ...) -> None: ...
