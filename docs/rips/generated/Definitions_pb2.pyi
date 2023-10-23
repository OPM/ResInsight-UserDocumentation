from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ClientToServerStreamReply(_message.Message):
    __slots__ = ["accepted_value_count"]
    ACCEPTED_VALUE_COUNT_FIELD_NUMBER: _ClassVar[int]
    accepted_value_count: int
    def __init__(self, accepted_value_count: _Optional[int] = ...) -> None: ...

class Vec3i(_message.Message):
    __slots__ = ["i", "j", "k"]
    I_FIELD_NUMBER: _ClassVar[int]
    J_FIELD_NUMBER: _ClassVar[int]
    K_FIELD_NUMBER: _ClassVar[int]
    i: int
    j: int
    k: int
    def __init__(self, i: _Optional[int] = ..., j: _Optional[int] = ..., k: _Optional[int] = ...) -> None: ...

class Vec3d(_message.Message):
    __slots__ = ["x", "y", "z"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class CellCenters(_message.Message):
    __slots__ = ["centers"]
    CENTERS_FIELD_NUMBER: _ClassVar[int]
    centers: _containers.RepeatedCompositeFieldContainer[Vec3d]
    def __init__(self, centers: _Optional[_Iterable[_Union[Vec3d, _Mapping]]] = ...) -> None: ...

class CellCorners(_message.Message):
    __slots__ = ["c0", "c1", "c2", "c3", "c4", "c5", "c6", "c7"]
    C0_FIELD_NUMBER: _ClassVar[int]
    C1_FIELD_NUMBER: _ClassVar[int]
    C2_FIELD_NUMBER: _ClassVar[int]
    C3_FIELD_NUMBER: _ClassVar[int]
    C4_FIELD_NUMBER: _ClassVar[int]
    C5_FIELD_NUMBER: _ClassVar[int]
    C6_FIELD_NUMBER: _ClassVar[int]
    C7_FIELD_NUMBER: _ClassVar[int]
    c0: Vec3d
    c1: Vec3d
    c2: Vec3d
    c3: Vec3d
    c4: Vec3d
    c5: Vec3d
    c6: Vec3d
    c7: Vec3d
    def __init__(self, c0: _Optional[_Union[Vec3d, _Mapping]] = ..., c1: _Optional[_Union[Vec3d, _Mapping]] = ..., c2: _Optional[_Union[Vec3d, _Mapping]] = ..., c3: _Optional[_Union[Vec3d, _Mapping]] = ..., c4: _Optional[_Union[Vec3d, _Mapping]] = ..., c5: _Optional[_Union[Vec3d, _Mapping]] = ..., c6: _Optional[_Union[Vec3d, _Mapping]] = ..., c7: _Optional[_Union[Vec3d, _Mapping]] = ...) -> None: ...

class CellCornersArray(_message.Message):
    __slots__ = ["cells"]
    CELLS_FIELD_NUMBER: _ClassVar[int]
    cells: _containers.RepeatedCompositeFieldContainer[CellCorners]
    def __init__(self, cells: _Optional[_Iterable[_Union[CellCorners, _Mapping]]] = ...) -> None: ...
