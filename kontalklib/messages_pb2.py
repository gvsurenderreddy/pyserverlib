# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='messages.proto',
  package='',
  serialized_pb='\n\x0emessages.proto\"v\n\nServerInfo\x12\x0f\n\x07version\x18\x01 \x02(\t\x12\x17\n\x0f\x63lient_protocol\x18\x02 \x02(\r\x12\x17\n\x0fserver_protocol\x18\x03 \x02(\r\x12\x13\n\x0b\x66ingerprint\x18\x04 \x02(\t\x12\x10\n\x08supports\x18\x05 \x03(\t\"<\n\x0fPhoneValidation\x12\x17\n\x06status\x18\x01 \x02(\x0e\x32\x07.Status\x12\x10\n\x08sms_from\x18\x02 \x01(\t\"8\n\x0e\x41uthentication\x12\x17\n\x06status\x18\x01 \x02(\x0e\x32\x07.Status\x12\r\n\x05token\x18\x02 \x01(\t\")\n\x08Received\x12\x1d\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x0e.ReceivedEntry\"<\n\rReceivedEntry\x12\x17\n\x06status\x18\x01 \x02(\x0e\x32\x07.Status\x12\x12\n\nmessage_id\x18\x02 \x02(\t\"/\n\x0bMessageSent\x12 \n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x11.MessageSentEntry\"P\n\x10MessageSentEntry\x12\x17\n\x06status\x18\x01 \x02(\x0e\x32\x07.Status\x12\x0f\n\x07user_id\x18\x02 \x02(\t\x12\x12\n\nmessage_id\x18\x03 \x01(\t\" \n\rLookupRequest\x12\x0f\n\x07user_id\x18\x01 \x03(\t\"5\n\x0eLookupResponse\x12#\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x14.LookupResponseEntry\"9\n\x13LookupResponseEntry\x12\x0f\n\x07user_id\x18\x01 \x02(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\"I\n\x0bNewMessages\x12\x17\n\x06status\x18\x01 \x02(\x0e\x32\x07.Status\x12!\n\x07message\x18\x02 \x03(\x0b\x32\x10.NewMessageEntry\"\x98\x01\n\x0fNewMessageEntry\x12\x12\n\nmessage_id\x18\x01 \x02(\t\x12\x0e\n\x06sender\x18\x02 \x02(\t\x12\r\n\x05group\x18\x03 \x03(\t\x12\x13\n\x0boriginal_id\x18\x04 \x01(\t\x12\x0c\n\x04mime\x18\x05 \x02(\t\x12\x11\n\tencrypted\x18\x06 \x02(\x08\x12\x0f\n\x07\x63ontent\x18\x07 \x02(\x0c\x12\x0b\n\x03url\x18\x08 \x01(\t*\xcf\x01\n\x06Status\x12\x12\n\x0eSTATUS_SUCCESS\x10\x00\x12\x10\n\x0cSTATUS_ERROR\x10\x01\x12\x0f\n\x0bSTATUS_BUSY\x10\x02\x12\x1e\n\x1aSTATUS_VERIFICATION_FAILED\x10\x03\x12\x1f\n\x1bSTATUS_INVALID_PHONE_NUMBER\x10\x04\x12\x16\n\x12STATUS_TTL_EXPIRED\x10\x05\x12\x18\n\x14STATUS_USER_NOTFOUND\x10\x06\x12\x1b\n\x17STATUS_MESSAGE_NOTFOUND\x10\x07\x42 \n\x12org.kontalk.clientB\x08ProtocolH\x03')

_STATUS = descriptor.EnumDescriptor(
  name='Status',
  full_name='Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='STATUS_SUCCESS', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STATUS_ERROR', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STATUS_BUSY', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STATUS_VERIFICATION_FAILED', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STATUS_INVALID_PHONE_NUMBER', index=4, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STATUS_TTL_EXPIRED', index=5, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STATUS_USER_NOTFOUND', index=6, number=6,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STATUS_MESSAGE_NOTFOUND', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=873,
  serialized_end=1080,
)


STATUS_SUCCESS = 0
STATUS_ERROR = 1
STATUS_BUSY = 2
STATUS_VERIFICATION_FAILED = 3
STATUS_INVALID_PHONE_NUMBER = 4
STATUS_TTL_EXPIRED = 5
STATUS_USER_NOTFOUND = 6
STATUS_MESSAGE_NOTFOUND = 7



_SERVERINFO = descriptor.Descriptor(
  name='ServerInfo',
  full_name='ServerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='version', full_name='ServerInfo.version', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='client_protocol', full_name='ServerInfo.client_protocol', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='server_protocol', full_name='ServerInfo.server_protocol', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='fingerprint', full_name='ServerInfo.fingerprint', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='supports', full_name='ServerInfo.supports', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=18,
  serialized_end=136,
)


_PHONEVALIDATION = descriptor.Descriptor(
  name='PhoneValidation',
  full_name='PhoneValidation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='status', full_name='PhoneValidation.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sms_from', full_name='PhoneValidation.sms_from', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=138,
  serialized_end=198,
)


_AUTHENTICATION = descriptor.Descriptor(
  name='Authentication',
  full_name='Authentication',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='status', full_name='Authentication.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='token', full_name='Authentication.token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=200,
  serialized_end=256,
)


_RECEIVED = descriptor.Descriptor(
  name='Received',
  full_name='Received',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='entry', full_name='Received.entry', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=258,
  serialized_end=299,
)


_RECEIVEDENTRY = descriptor.Descriptor(
  name='ReceivedEntry',
  full_name='ReceivedEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='status', full_name='ReceivedEntry.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message_id', full_name='ReceivedEntry.message_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=301,
  serialized_end=361,
)


_MESSAGESENT = descriptor.Descriptor(
  name='MessageSent',
  full_name='MessageSent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='entry', full_name='MessageSent.entry', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=363,
  serialized_end=410,
)


_MESSAGESENTENTRY = descriptor.Descriptor(
  name='MessageSentEntry',
  full_name='MessageSentEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='status', full_name='MessageSentEntry.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_id', full_name='MessageSentEntry.user_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message_id', full_name='MessageSentEntry.message_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=412,
  serialized_end=492,
)


_LOOKUPREQUEST = descriptor.Descriptor(
  name='LookupRequest',
  full_name='LookupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='user_id', full_name='LookupRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=494,
  serialized_end=526,
)


_LOOKUPRESPONSE = descriptor.Descriptor(
  name='LookupResponse',
  full_name='LookupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='entry', full_name='LookupResponse.entry', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=528,
  serialized_end=581,
)


_LOOKUPRESPONSEENTRY = descriptor.Descriptor(
  name='LookupResponseEntry',
  full_name='LookupResponseEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='user_id', full_name='LookupResponseEntry.user_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timestamp', full_name='LookupResponseEntry.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=583,
  serialized_end=640,
)


_NEWMESSAGES = descriptor.Descriptor(
  name='NewMessages',
  full_name='NewMessages',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='status', full_name='NewMessages.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='NewMessages.message', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=642,
  serialized_end=715,
)


_NEWMESSAGEENTRY = descriptor.Descriptor(
  name='NewMessageEntry',
  full_name='NewMessageEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message_id', full_name='NewMessageEntry.message_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sender', full_name='NewMessageEntry.sender', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='group', full_name='NewMessageEntry.group', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='original_id', full_name='NewMessageEntry.original_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mime', full_name='NewMessageEntry.mime', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='encrypted', full_name='NewMessageEntry.encrypted', index=5,
      number=6, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='content', full_name='NewMessageEntry.content', index=6,
      number=7, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='url', full_name='NewMessageEntry.url', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=718,
  serialized_end=870,
)

_PHONEVALIDATION.fields_by_name['status'].enum_type = _STATUS
_AUTHENTICATION.fields_by_name['status'].enum_type = _STATUS
_RECEIVED.fields_by_name['entry'].message_type = _RECEIVEDENTRY
_RECEIVEDENTRY.fields_by_name['status'].enum_type = _STATUS
_MESSAGESENT.fields_by_name['entry'].message_type = _MESSAGESENTENTRY
_MESSAGESENTENTRY.fields_by_name['status'].enum_type = _STATUS
_LOOKUPRESPONSE.fields_by_name['entry'].message_type = _LOOKUPRESPONSEENTRY
_NEWMESSAGES.fields_by_name['status'].enum_type = _STATUS
_NEWMESSAGES.fields_by_name['message'].message_type = _NEWMESSAGEENTRY
DESCRIPTOR.message_types_by_name['ServerInfo'] = _SERVERINFO
DESCRIPTOR.message_types_by_name['PhoneValidation'] = _PHONEVALIDATION
DESCRIPTOR.message_types_by_name['Authentication'] = _AUTHENTICATION
DESCRIPTOR.message_types_by_name['Received'] = _RECEIVED
DESCRIPTOR.message_types_by_name['ReceivedEntry'] = _RECEIVEDENTRY
DESCRIPTOR.message_types_by_name['MessageSent'] = _MESSAGESENT
DESCRIPTOR.message_types_by_name['MessageSentEntry'] = _MESSAGESENTENTRY
DESCRIPTOR.message_types_by_name['LookupRequest'] = _LOOKUPREQUEST
DESCRIPTOR.message_types_by_name['LookupResponse'] = _LOOKUPRESPONSE
DESCRIPTOR.message_types_by_name['LookupResponseEntry'] = _LOOKUPRESPONSEENTRY
DESCRIPTOR.message_types_by_name['NewMessages'] = _NEWMESSAGES
DESCRIPTOR.message_types_by_name['NewMessageEntry'] = _NEWMESSAGEENTRY

class ServerInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SERVERINFO
  
  # @@protoc_insertion_point(class_scope:ServerInfo)

class PhoneValidation(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PHONEVALIDATION
  
  # @@protoc_insertion_point(class_scope:PhoneValidation)

class Authentication(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUTHENTICATION
  
  # @@protoc_insertion_point(class_scope:Authentication)

class Received(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RECEIVED
  
  # @@protoc_insertion_point(class_scope:Received)

class ReceivedEntry(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RECEIVEDENTRY
  
  # @@protoc_insertion_point(class_scope:ReceivedEntry)

class MessageSent(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MESSAGESENT
  
  # @@protoc_insertion_point(class_scope:MessageSent)

class MessageSentEntry(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MESSAGESENTENTRY
  
  # @@protoc_insertion_point(class_scope:MessageSentEntry)

class LookupRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOOKUPREQUEST
  
  # @@protoc_insertion_point(class_scope:LookupRequest)

class LookupResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOOKUPRESPONSE
  
  # @@protoc_insertion_point(class_scope:LookupResponse)

class LookupResponseEntry(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOOKUPRESPONSEENTRY
  
  # @@protoc_insertion_point(class_scope:LookupResponseEntry)

class NewMessages(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NEWMESSAGES
  
  # @@protoc_insertion_point(class_scope:NewMessages)

class NewMessageEntry(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NEWMESSAGEENTRY
  
  # @@protoc_insertion_point(class_scope:NewMessageEntry)

# @@protoc_insertion_point(module_scope)
