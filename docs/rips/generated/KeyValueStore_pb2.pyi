import Definitions_pb2 as _Definitions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeyValueStoreInputChunk(_message.Message):
    __slots__ = ("parameters", "values")
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    parameters: KeyValueInputParameters
    values: KeyValueStoreChunk
    def __init__(self, parameters: _Optional[_Union[KeyValueInputParameters, _Mapping]] = ..., values: _Optional[_Union[KeyValueStoreChunk, _Mapping]] = ...) -> None: ...

class KeyValueInputParameters(_message.Message):
    __slots__ = ("name", "num_elements")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    num_elements: int
    def __init__(self, name: _Optional[str] = ..., num_elements: _Optional[int] = ...) -> None: ...

class KeyValueStoreChunk(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, values: _Optional[_Iterable[float]] = ...) -> None: ...

class KeyValueStoreOutputRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class KeyValueStoreOutputChunk(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, values: _Optional[_Iterable[float]] = ...) -> None: ...

class KeyValueStoreRemoveRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
