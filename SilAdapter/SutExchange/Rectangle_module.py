# This code was generated automatically. Changes to this file may
# cause incorrect behavior and will be lost if the code is regenerated.

from typing import List
from .._vector_typelib import typelib_data_member as typelib_data_member
from .._vector_typelib import typelib_do as typelib_do
from .._vector_typelib import typelib_common as typelib_common
from .._vector_typelib import typelib_base_datatypes as typelib_base_datatypes
from .._vector_typelib import typelib_encodings as typelib_encodings


class Rectangle(typelib_base_datatypes.StructDataType):

    _struct_member_types = {
        "xMin": typelib_base_datatypes.UInt32DataType,
        "xMax": typelib_base_datatypes.UInt32DataType,
        "yMin": typelib_base_datatypes.UInt32DataType,
        "yMax": typelib_base_datatypes.UInt32DataType,
        }

    def __init__(self, \
                 xMin: int = typelib_base_datatypes.UInt32DataType.initial_value(), \
                 xMax: int = typelib_base_datatypes.UInt32DataType.initial_value(), \
                 yMin: int = typelib_base_datatypes.UInt32DataType.initial_value(), \
                 yMax: int = typelib_base_datatypes.UInt32DataType.initial_value()):
        self.xMin : int = xMin
        self.xMax : int = xMax
        self.yMin : int = yMin
        self.yMax : int = yMax

    @staticmethod
    def initial_value():
        return Rectangle()

    @staticmethod
    def serialize(serializer, value, stored_raw):
        typelib_base_datatypes.StructDataType._serialize(Rectangle, serializer, value, stored_raw)

    @staticmethod
    def deserialize(deserializer, stored_raw):
        return typelib_base_datatypes.StructDataType._deserialize(Rectangle, deserializer, stored_raw)

    @staticmethod
    def deserialize_in_place(deserializer, value, stored_raw):
        return typelib_base_datatypes.StructDataType._deserialize_in_place(Rectangle, deserializer, value, stored_raw)


class RectangleDataObjConsumedProps(typelib_common.DataObjPropsBase):

    @property
    def xMin(self) -> typelib_common.ReadOnlySubmember[int]:
        return self._create_data_obj(typelib_common.ReadOnlySubmember[int], "xMin")

    @property
    def xMax(self) -> typelib_common.ReadOnlySubmember[int]:
        return self._create_data_obj(typelib_common.ReadOnlySubmember[int], "xMax")

    @property
    def yMin(self) -> typelib_common.ReadOnlySubmember[int]:
        return self._create_data_obj(typelib_common.ReadOnlySubmember[int], "yMin")

    @property
    def yMax(self) -> typelib_common.ReadOnlySubmember[int]:
        return self._create_data_obj(typelib_common.ReadOnlySubmember[int], "yMax")


class RectangleDataObjProvidedProps(typelib_common.DataObjPropsBase, typelib_common.DataObjSetMixin):

    @property
    def xMin(self) -> typelib_common.ReadWriteSubmember[int]:
        return self._create_data_obj(typelib_common.ReadWriteSubmember[int], "xMin")

    @xMin.setter
    def xMin(self, val: int):
        self._set_child_node_value("xMin", val)

    @property
    def xMax(self) -> typelib_common.ReadWriteSubmember[int]:
        return self._create_data_obj(typelib_common.ReadWriteSubmember[int], "xMax")

    @xMax.setter
    def xMax(self, val: int):
        self._set_child_node_value("xMax", val)

    @property
    def yMin(self) -> typelib_common.ReadWriteSubmember[int]:
        return self._create_data_obj(typelib_common.ReadWriteSubmember[int], "yMin")

    @yMin.setter
    def yMin(self, val: int):
        self._set_child_node_value("yMin", val)

    @property
    def yMax(self) -> typelib_common.ReadWriteSubmember[int]:
        return self._create_data_obj(typelib_common.ReadWriteSubmember[int], "yMax")

    @yMax.setter
    def yMax(self, val: int):
        self._set_child_node_value("yMax", val)


class RectangleDataObjVeConsumed(RectangleDataObjConsumedProps):
    def __init__(self):
        self._branch_path = []
        self._value_entity_wrapper = self


class RectangleDataObjVeProvided(RectangleDataObjProvidedProps):
    def __init__(self):
        self._branch_path = []
        self._value_entity_wrapper = self


class RectangleDataObjConsumed(RectangleDataObjConsumedProps, typelib_common.ComplexSubmember[Rectangle]):
    def __init__(self, value_entity_wrapper, branch_path):
        self._branch_path = branch_path
        self._value_entity_wrapper = value_entity_wrapper


class RectangleDataObjProvided(RectangleDataObjProvidedProps, typelib_common.ComplexSubmember[Rectangle]):
    def __init__(self, value_entity_wrapper, branch_path):
        self._branch_path = branch_path
        self._value_entity_wrapper = value_entity_wrapper
