# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Definitions.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x44\x65\x66initions.proto\x12\x04rips\"\x07\n\x05\x45mpty\"9\n\x19\x43lientToServerStreamReply\x12\x1c\n\x14\x61\x63\x63\x65pted_value_count\x18\x01 \x01(\x03\"(\n\x05Vec3i\x12\t\n\x01i\x18\x01 \x01(\x05\x12\t\n\x01j\x18\x02 \x01(\x05\x12\t\n\x01k\x18\x03 \x01(\x05\"(\n\x05Vec3d\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\"+\n\x0b\x43\x65llCenters\x12\x1c\n\x07\x63\x65nters\x18\x01 \x03(\x0b\x32\x0b.rips.Vec3d\"\xd5\x01\n\x0b\x43\x65llCorners\x12\x17\n\x02\x63\x30\x18\x01 \x01(\x0b\x32\x0b.rips.Vec3d\x12\x17\n\x02\x63\x31\x18\x02 \x01(\x0b\x32\x0b.rips.Vec3d\x12\x17\n\x02\x63\x32\x18\x03 \x01(\x0b\x32\x0b.rips.Vec3d\x12\x17\n\x02\x63\x33\x18\x04 \x01(\x0b\x32\x0b.rips.Vec3d\x12\x17\n\x02\x63\x34\x18\x05 \x01(\x0b\x32\x0b.rips.Vec3d\x12\x17\n\x02\x63\x35\x18\x06 \x01(\x0b\x32\x0b.rips.Vec3d\x12\x17\n\x02\x63\x36\x18\x07 \x01(\x0b\x32\x0b.rips.Vec3d\x12\x17\n\x02\x63\x37\x18\x08 \x01(\x0b\x32\x0b.rips.Vec3d\"4\n\x10\x43\x65llCornersArray\x12 \n\x05\x63\x65lls\x18\x01 \x03(\x0b\x32\x11.rips.CellCornersb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Definitions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMPTY']._serialized_start=27
  _globals['_EMPTY']._serialized_end=34
  _globals['_CLIENTTOSERVERSTREAMREPLY']._serialized_start=36
  _globals['_CLIENTTOSERVERSTREAMREPLY']._serialized_end=93
  _globals['_VEC3I']._serialized_start=95
  _globals['_VEC3I']._serialized_end=135
  _globals['_VEC3D']._serialized_start=137
  _globals['_VEC3D']._serialized_end=177
  _globals['_CELLCENTERS']._serialized_start=179
  _globals['_CELLCENTERS']._serialized_end=222
  _globals['_CELLCORNERS']._serialized_start=225
  _globals['_CELLCORNERS']._serialized_end=438
  _globals['_CELLCORNERSARRAY']._serialized_start=440
  _globals['_CELLCORNERSARRAY']._serialized_end=492
# @@protoc_insertion_point(module_scope)
