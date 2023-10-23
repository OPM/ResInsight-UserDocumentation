import Definitions_pb2 as _Definitions_pb2
import PdmObject_pb2 as _PdmObject_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplicationTypeEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    GUI_APPLICATION: _ClassVar[ApplicationTypeEnum]
    CONSOLE_APPLICATION: _ClassVar[ApplicationTypeEnum]
GUI_APPLICATION: ApplicationTypeEnum
CONSOLE_APPLICATION: ApplicationTypeEnum

class Version(_message.Message):
    __slots__ = ["major_version", "minor_version", "patch_version"]
    MAJOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    MINOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    PATCH_VERSION_FIELD_NUMBER: _ClassVar[int]
    major_version: int
    minor_version: int
    patch_version: int
    def __init__(self, major_version: _Optional[int] = ..., minor_version: _Optional[int] = ..., patch_version: _Optional[int] = ...) -> None: ...

class RuntimeInfo(_message.Message):
    __slots__ = ["app_type"]
    APP_TYPE_FIELD_NUMBER: _ClassVar[int]
    app_type: ApplicationTypeEnum
    def __init__(self, app_type: _Optional[_Union[ApplicationTypeEnum, str]] = ...) -> None: ...
