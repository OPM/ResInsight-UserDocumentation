import Definitions_pb2 as _Definitions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PdmDescendantObjectRequest(_message.Message):
    __slots__ = ["object", "child_keyword"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    CHILD_KEYWORD_FIELD_NUMBER: _ClassVar[int]
    object: PdmObject
    child_keyword: str
    def __init__(self, object: _Optional[_Union[PdmObject, _Mapping]] = ..., child_keyword: _Optional[str] = ...) -> None: ...

class PdmChildObjectRequest(_message.Message):
    __slots__ = ["object", "child_field"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    CHILD_FIELD_FIELD_NUMBER: _ClassVar[int]
    object: PdmObject
    child_field: str
    def __init__(self, object: _Optional[_Union[PdmObject, _Mapping]] = ..., child_field: _Optional[str] = ...) -> None: ...

class CreatePdmChildObjectRequest(_message.Message):
    __slots__ = ["object", "child_field", "class_keyword"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    CHILD_FIELD_FIELD_NUMBER: _ClassVar[int]
    CLASS_KEYWORD_FIELD_NUMBER: _ClassVar[int]
    object: PdmObject
    child_field: str
    class_keyword: str
    def __init__(self, object: _Optional[_Union[PdmObject, _Mapping]] = ..., child_field: _Optional[str] = ..., class_keyword: _Optional[str] = ...) -> None: ...

class PdmParentObjectRequest(_message.Message):
    __slots__ = ["object", "parent_keyword"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    PARENT_KEYWORD_FIELD_NUMBER: _ClassVar[int]
    object: PdmObject
    parent_keyword: str
    def __init__(self, object: _Optional[_Union[PdmObject, _Mapping]] = ..., parent_keyword: _Optional[str] = ...) -> None: ...

class PdmObject(_message.Message):
    __slots__ = ["class_keyword", "address", "parameters", "visible", "persistent"]
    class ParametersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CLASS_KEYWORD_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_FIELD_NUMBER: _ClassVar[int]
    class_keyword: str
    address: int
    parameters: _containers.ScalarMap[str, str]
    visible: bool
    persistent: bool
    def __init__(self, class_keyword: _Optional[str] = ..., address: _Optional[int] = ..., parameters: _Optional[_Mapping[str, str]] = ..., visible: bool = ..., persistent: bool = ...) -> None: ...

class PdmObjectArray(_message.Message):
    __slots__ = ["objects"]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[PdmObject]
    def __init__(self, objects: _Optional[_Iterable[_Union[PdmObject, _Mapping]]] = ...) -> None: ...

class PdmObjectGetterRequest(_message.Message):
    __slots__ = ["object", "method"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    object: PdmObject
    method: str
    def __init__(self, object: _Optional[_Union[PdmObject, _Mapping]] = ..., method: _Optional[str] = ...) -> None: ...

class PdmObjectSetterRequest(_message.Message):
    __slots__ = ["request", "data_count"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    DATA_COUNT_FIELD_NUMBER: _ClassVar[int]
    request: PdmObjectGetterRequest
    data_count: int
    def __init__(self, request: _Optional[_Union[PdmObjectGetterRequest, _Mapping]] = ..., data_count: _Optional[int] = ...) -> None: ...

class PdmObjectSetterChunk(_message.Message):
    __slots__ = ["set_request", "doubles", "ints", "strings"]
    SET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DOUBLES_FIELD_NUMBER: _ClassVar[int]
    INTS_FIELD_NUMBER: _ClassVar[int]
    STRINGS_FIELD_NUMBER: _ClassVar[int]
    set_request: PdmObjectSetterRequest
    doubles: DoubleArray
    ints: IntArray
    strings: StringArray
    def __init__(self, set_request: _Optional[_Union[PdmObjectSetterRequest, _Mapping]] = ..., doubles: _Optional[_Union[DoubleArray, _Mapping]] = ..., ints: _Optional[_Union[IntArray, _Mapping]] = ..., strings: _Optional[_Union[StringArray, _Mapping]] = ...) -> None: ...

class DoubleArray(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, data: _Optional[_Iterable[float]] = ...) -> None: ...

class IntArray(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, data: _Optional[_Iterable[int]] = ...) -> None: ...

class StringArray(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, data: _Optional[_Iterable[str]] = ...) -> None: ...

class PdmObjectGetterReply(_message.Message):
    __slots__ = ["doubles", "ints", "strings"]
    DOUBLES_FIELD_NUMBER: _ClassVar[int]
    INTS_FIELD_NUMBER: _ClassVar[int]
    STRINGS_FIELD_NUMBER: _ClassVar[int]
    doubles: DoubleArray
    ints: IntArray
    strings: StringArray
    def __init__(self, doubles: _Optional[_Union[DoubleArray, _Mapping]] = ..., ints: _Optional[_Union[IntArray, _Mapping]] = ..., strings: _Optional[_Union[StringArray, _Mapping]] = ...) -> None: ...

class PdmObjectMethodRequest(_message.Message):
    __slots__ = ["object", "method", "params"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    object: PdmObject
    method: str
    params: PdmObject
    def __init__(self, object: _Optional[_Union[PdmObject, _Mapping]] = ..., method: _Optional[str] = ..., params: _Optional[_Union[PdmObject, _Mapping]] = ...) -> None: ...
