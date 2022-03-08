# This code was generated automatically. Changes to this file may
# cause incorrect behavior and will be lost if the code is regenerated.

from typing import List
from .._vector_typelib import typelib_data_member as typelib_data_member
from .._vector_typelib import typelib_do as typelib_do
from .._vector_typelib import typelib_common as typelib_common
from .._vector_typelib import typelib_base_datatypes as typelib_base_datatypes
from .._vector_typelib import typelib_encodings as typelib_encodings


class TransmittedImage(typelib_base_datatypes.StructDataType):

    _struct_member_types = {
        "imageName": typelib_base_datatypes.StringDataType,
        "timestamp": typelib_base_datatypes.StringDataType,
        "format": typelib_base_datatypes.StringDataType,
        "dataArray": typelib_base_datatypes.BytesDataType,
        "height": typelib_base_datatypes.UInt16DataType,
        "width": typelib_base_datatypes.UInt16DataType,
        }

    def __init__(self, \
                 imageName: str = typelib_base_datatypes.StringDataType.initial_value(), \
                 timestamp: str = typelib_base_datatypes.StringDataType.initial_value(), \
                 format: str = typelib_base_datatypes.StringDataType.initial_value(), \
                 dataArray: bytearray = typelib_base_datatypes.BytesDataType.initial_value(), \
                 height: int = typelib_base_datatypes.UInt16DataType.initial_value(), \
                 width: int = typelib_base_datatypes.UInt16DataType.initial_value()):
        self.imageName : str = imageName
        self.timestamp : str = timestamp
        self.format : str = format
        self.dataArray : bytearray = dataArray
        self.height : int = height
        self.width : int = width

    @staticmethod
    def initial_value():
        return TransmittedImage()

    @staticmethod
    def serialize(serializer, value, stored_raw):
        typelib_base_datatypes.StructDataType._serialize(TransmittedImage, serializer, value, stored_raw)

    @staticmethod
    def deserialize(deserializer, stored_raw):
        return typelib_base_datatypes.StructDataType._deserialize(TransmittedImage, deserializer, stored_raw)

    @staticmethod
    def deserialize_in_place(deserializer, value, stored_raw):
        return typelib_base_datatypes.StructDataType._deserialize_in_place(TransmittedImage, deserializer, value, stored_raw)


class TransmittedImageDataObjConsumedProps(typelib_common.DataObjPropsBase):

    @property
    def imageName(self) -> typelib_common.ReadOnlySubmember[str]:
        return self._create_data_obj(typelib_common.ReadOnlySubmember[str], "imageName")

    @property
    def timestamp(self) -> typelib_common.ReadOnlySubmember[str]:
        return self._create_data_obj(typelib_common.ReadOnlySubmember[str], "timestamp")

    @property
    def format(self) -> typelib_common.ReadOnlySubmember[str]:
        return self._create_data_obj(typelib_common.ReadOnlySubmember[str], "format")

    @property
    def dataArray(self) -> typelib_common.ReadOnlySubmember[bytearray]:
        return self._create_data_obj(typelib_common.ReadOnlySubmember[bytearray], "dataArray")

    @property
    def height(self) -> typelib_common.ReadOnlySubmember[int]:
        return self._create_data_obj(typelib_common.ReadOnlySubmember[int], "height")

    @property
    def width(self) -> typelib_common.ReadOnlySubmember[int]:
        return self._create_data_obj(typelib_common.ReadOnlySubmember[int], "width")


class TransmittedImageDataObjProvidedProps(typelib_common.DataObjPropsBase, typelib_common.DataObjSetMixin):

    @property
    def imageName(self) -> typelib_common.ReadWriteSubmember[str]:
        return self._create_data_obj(typelib_common.ReadWriteSubmember[str], "imageName")

    @imageName.setter
    def imageName(self, val: str):
        self._set_child_node_value("imageName", val)

    @property
    def timestamp(self) -> typelib_common.ReadWriteSubmember[str]:
        return self._create_data_obj(typelib_common.ReadWriteSubmember[str], "timestamp")

    @timestamp.setter
    def timestamp(self, val: str):
        self._set_child_node_value("timestamp", val)

    @property
    def format(self) -> typelib_common.ReadWriteSubmember[str]:
        return self._create_data_obj(typelib_common.ReadWriteSubmember[str], "format")

    @format.setter
    def format(self, val: str):
        self._set_child_node_value("format", val)

    @property
    def dataArray(self) -> typelib_common.ReadWriteSubmember[bytearray]:
        return self._create_data_obj(typelib_common.ReadWriteSubmember[bytearray], "dataArray")

    @dataArray.setter
    def dataArray(self, val: bytearray):
        self._set_child_node_value("dataArray", val)

    @property
    def height(self) -> typelib_common.ReadWriteSubmember[int]:
        return self._create_data_obj(typelib_common.ReadWriteSubmember[int], "height")

    @height.setter
    def height(self, val: int):
        self._set_child_node_value("height", val)

    @property
    def width(self) -> typelib_common.ReadWriteSubmember[int]:
        return self._create_data_obj(typelib_common.ReadWriteSubmember[int], "width")

    @width.setter
    def width(self, val: int):
        self._set_child_node_value("width", val)


class TransmittedImageDataObjVeConsumed(TransmittedImageDataObjConsumedProps):
    def __init__(self):
        self._branch_path = []
        self._value_entity_wrapper = self


class TransmittedImageDataObjVeProvided(TransmittedImageDataObjProvidedProps):
    def __init__(self):
        self._branch_path = []
        self._value_entity_wrapper = self


class TransmittedImageDataObjConsumed(TransmittedImageDataObjConsumedProps, typelib_common.ComplexSubmember[TransmittedImage]):
    def __init__(self, value_entity_wrapper, branch_path):
        self._branch_path = branch_path
        self._value_entity_wrapper = value_entity_wrapper


class TransmittedImageDataObjProvided(TransmittedImageDataObjProvidedProps, typelib_common.ComplexSubmember[TransmittedImage]):
    def __init__(self, value_entity_wrapper, branch_path):
        self._branch_path = branch_path
        self._value_entity_wrapper = value_entity_wrapper
