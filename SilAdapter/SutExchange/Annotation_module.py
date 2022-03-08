# This code was generated automatically. Changes to this file may
# cause incorrect behavior and will be lost if the code is regenerated.

from typing import List
from .._vector_typelib import typelib_data_member as typelib_data_member
from .._vector_typelib import typelib_do as typelib_do
from .._vector_typelib import typelib_common as typelib_common
from .._vector_typelib import typelib_base_datatypes as typelib_base_datatypes
from .._vector_typelib import typelib_encodings as typelib_encodings
from . import Rectangle_module as _0_SutExchange_Rectangle_module


class Annotation(typelib_base_datatypes.StructDataType):

    _struct_member_types = {
        "labelID": typelib_base_datatypes.OptionalDataType(typelib_base_datatypes.Int32DataType),
        "label": typelib_base_datatypes.OptionalDataType(typelib_base_datatypes.StringDataType),
        "confidence": typelib_base_datatypes.FloatDataType,
        "boundingBox": typelib_base_datatypes.OptionalDataType(_0_SutExchange_Rectangle_module.Rectangle),
        }

    def __init__(self, \
                 labelID: int = typelib_base_datatypes.Int32DataType.initial_value(), \
                 label: str = typelib_base_datatypes.StringDataType.initial_value(), \
                 confidence: float = typelib_base_datatypes.FloatDataType.initial_value(), \
                 boundingBox: _0_SutExchange_Rectangle_module.Rectangle = _0_SutExchange_Rectangle_module.Rectangle.initial_value()):
        self.labelID : int = labelID
        self.label : str = label
        self.confidence : float = confidence
        self.boundingBox : _0_SutExchange_Rectangle_module.Rectangle = boundingBox

    @staticmethod
    def initial_value():
        return Annotation()

    @staticmethod
    def serialize(serializer, value, stored_raw):
        typelib_base_datatypes.StructDataType._serialize(Annotation, serializer, value, stored_raw)

    @staticmethod
    def deserialize(deserializer, stored_raw):
        return typelib_base_datatypes.StructDataType._deserialize(Annotation, deserializer, stored_raw)

    @staticmethod
    def deserialize_in_place(deserializer, value, stored_raw):
        return typelib_base_datatypes.StructDataType._deserialize_in_place(Annotation, deserializer, value, stored_raw)


class AnnotationDataObjConsumedProps(typelib_common.DataObjPropsBase):

    @property
    def labelID(self) -> typelib_common.ReadOnlySubmember[int]:
        return self._create_data_obj(typelib_common.ReadOnlySubmember[int], "labelID")

    @property
    def label(self) -> typelib_common.ReadOnlySubmember[str]:
        return self._create_data_obj(typelib_common.ReadOnlySubmember[str], "label")

    @property
    def confidence(self) -> typelib_common.ReadOnlySubmember[float]:
        return self._create_data_obj(typelib_common.ReadOnlySubmember[float], "confidence")

    @property
    def boundingBox(self) -> _0_SutExchange_Rectangle_module.RectangleDataObjConsumed:
        return self._create_data_obj(_0_SutExchange_Rectangle_module.RectangleDataObjConsumed, "boundingBox")


class AnnotationDataObjProvidedProps(typelib_common.DataObjPropsBase, typelib_common.DataObjSetMixin):

    @property
    def labelID(self) -> typelib_common.ReadWriteSubmember[int]:
        return self._create_data_obj(typelib_common.ReadWriteSubmember[int], "labelID")

    @labelID.setter
    def labelID(self, val: int):
        self._set_child_node_value("labelID", val)

    @property
    def label(self) -> typelib_common.ReadWriteSubmember[str]:
        return self._create_data_obj(typelib_common.ReadWriteSubmember[str], "label")

    @label.setter
    def label(self, val: str):
        self._set_child_node_value("label", val)

    @property
    def confidence(self) -> typelib_common.ReadWriteSubmember[float]:
        return self._create_data_obj(typelib_common.ReadWriteSubmember[float], "confidence")

    @confidence.setter
    def confidence(self, val: float):
        self._set_child_node_value("confidence", val)

    @property
    def boundingBox(self) -> _0_SutExchange_Rectangle_module.RectangleDataObjProvided:
        return self._create_data_obj(_0_SutExchange_Rectangle_module.RectangleDataObjProvided, "boundingBox")

    @boundingBox.setter
    def boundingBox(self, val: _0_SutExchange_Rectangle_module.Rectangle):
        self._set_child_node_value("boundingBox", val)


class AnnotationDataObjVeConsumed(AnnotationDataObjConsumedProps):
    def __init__(self):
        self._branch_path = []
        self._value_entity_wrapper = self


class AnnotationDataObjVeProvided(AnnotationDataObjProvidedProps):
    def __init__(self):
        self._branch_path = []
        self._value_entity_wrapper = self


class AnnotationDataObjConsumed(AnnotationDataObjConsumedProps, typelib_common.ComplexSubmember[Annotation]):
    def __init__(self, value_entity_wrapper, branch_path):
        self._branch_path = branch_path
        self._value_entity_wrapper = value_entity_wrapper


class AnnotationDataObjProvided(AnnotationDataObjProvidedProps, typelib_common.ComplexSubmember[Annotation]):
    def __init__(self, value_entity_wrapper, branch_path):
        self._branch_path = branch_path
        self._value_entity_wrapper = value_entity_wrapper
