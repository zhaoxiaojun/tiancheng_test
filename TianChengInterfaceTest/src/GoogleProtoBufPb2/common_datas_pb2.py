# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common_datas.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common_datas.proto',
  package='common_datas',
  serialized_pb=_b('\n\x12\x63ommon_datas.proto\x12\x0c\x63ommon_datas\x1a\x0c\x63ommon.proto\"\'\n\nmenu_items\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\r\n\x05title\x18\x02 \x01(\x0c\"\x83\x01\n\x0emenu_items_ask\x12.\n\tenum_type\x18\x01 \x01(\x0e\x32\x1b.common_datas.item_api_type\x12\x12\n\nos_version\x18\x02 \x01(\x0c\x12-\n\nask_header\x18\x03 \x01(\x0b\x32\x19.common.common_ask_header\"]\n\x0emenu_items_ans\x12&\n\x04item\x18\x01 \x03(\x0b\x32\x18.common_datas.menu_items\x12#\n\x06result\x18\x02 \x01(\x0b\x32\x13.common.result_info*)\n\ritem_api_type\x12\x18\n\x14TerminalVersionItems\x10\x01')
  ,
  dependencies=[common_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ITEM_API_TYPE = _descriptor.EnumDescriptor(
  name='item_api_type',
  full_name='common_datas.item_api_type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TerminalVersionItems', index=0, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=320,
  serialized_end=361,
)
_sym_db.RegisterEnumDescriptor(_ITEM_API_TYPE)

item_api_type = enum_type_wrapper.EnumTypeWrapper(_ITEM_API_TYPE)
TerminalVersionItems = 1



_MENU_ITEMS = _descriptor.Descriptor(
  name='menu_items',
  full_name='common_datas.menu_items',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='common_datas.menu_items.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='common_datas.menu_items.title', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=89,
)


_MENU_ITEMS_ASK = _descriptor.Descriptor(
  name='menu_items_ask',
  full_name='common_datas.menu_items_ask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enum_type', full_name='common_datas.menu_items_ask.enum_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='os_version', full_name='common_datas.menu_items_ask.os_version', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ask_header', full_name='common_datas.menu_items_ask.ask_header', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=223,
)


_MENU_ITEMS_ANS = _descriptor.Descriptor(
  name='menu_items_ans',
  full_name='common_datas.menu_items_ans',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='common_datas.menu_items_ans.item', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='common_datas.menu_items_ans.result', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=225,
  serialized_end=318,
)

_MENU_ITEMS_ASK.fields_by_name['enum_type'].enum_type = _ITEM_API_TYPE
_MENU_ITEMS_ASK.fields_by_name['ask_header'].message_type = common_pb2._COMMON_ASK_HEADER
_MENU_ITEMS_ANS.fields_by_name['item'].message_type = _MENU_ITEMS
_MENU_ITEMS_ANS.fields_by_name['result'].message_type = common_pb2._RESULT_INFO
DESCRIPTOR.message_types_by_name['menu_items'] = _MENU_ITEMS
DESCRIPTOR.message_types_by_name['menu_items_ask'] = _MENU_ITEMS_ASK
DESCRIPTOR.message_types_by_name['menu_items_ans'] = _MENU_ITEMS_ANS
DESCRIPTOR.enum_types_by_name['item_api_type'] = _ITEM_API_TYPE

menu_items = _reflection.GeneratedProtocolMessageType('menu_items', (_message.Message,), dict(
  DESCRIPTOR = _MENU_ITEMS,
  __module__ = 'common_datas_pb2'
  # @@protoc_insertion_point(class_scope:common_datas.menu_items)
  ))
_sym_db.RegisterMessage(menu_items)

menu_items_ask = _reflection.GeneratedProtocolMessageType('menu_items_ask', (_message.Message,), dict(
  DESCRIPTOR = _MENU_ITEMS_ASK,
  __module__ = 'common_datas_pb2'
  # @@protoc_insertion_point(class_scope:common_datas.menu_items_ask)
  ))
_sym_db.RegisterMessage(menu_items_ask)

menu_items_ans = _reflection.GeneratedProtocolMessageType('menu_items_ans', (_message.Message,), dict(
  DESCRIPTOR = _MENU_ITEMS_ANS,
  __module__ = 'common_datas_pb2'
  # @@protoc_insertion_point(class_scope:common_datas.menu_items_ans)
  ))
_sym_db.RegisterMessage(menu_items_ans)


# @@protoc_insertion_point(module_scope)
