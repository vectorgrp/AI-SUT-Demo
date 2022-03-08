# This code was generated automatically. Changes to this file may
# cause incorrect behavior and will be lost if the code is regenerated.

from typing import List, Dict
from .._vector_typelib import typelib_data_member as typelib_data_member
from .._vector_typelib import typelib_do as typelib_do
from .._vector_typelib import typelib_common as typelib_common
from .._vector_typelib import typelib_base_datatypes as typelib_base_datatypes
from .._vector_typelib import typelib_encodings as typelib_encodings
from . import Annotation_module as _0_SutExchange_Annotation_module


class anno_list(typelib_base_datatypes.List_Base[_0_SutExchange_Annotation_module.Annotation]):
    def __init__(self, \
                 full_values: List[_0_SutExchange_Annotation_module.Annotation] = None, \
                 sparse_values: Dict[int, _0_SutExchange_Annotation_module.Annotation] = None):
        super().__init__(3, 100, _0_SutExchange_Annotation_module.Annotation, False)

        if full_values is not None:
            for value in full_values:
                self.append(value)

        if sparse_values is not None:
            for key, value in sparse_values.items():
                if len(self.data) < key:
                    self.resize(key)
                self.__setitem__(key, value)

    @staticmethod
    def initial_value():
        return anno_list()

    @staticmethod 
    def serialize(serializer, values, stored_raw):
        typelib_base_datatypes.List_Base._serialize(serializer, values, _0_SutExchange_Annotation_module.Annotation, stored_raw)

    @staticmethod 
    def deserialize(deserializer, stored_raw):
        return typelib_base_datatypes.List_Base._deserialize(deserializer, anno_list, _0_SutExchange_Annotation_module.Annotation, stored_raw)

    @staticmethod 
    def deserialize_in_place(deserializer, value, stored_raw):
        typelib_base_datatypes.List_Base._deserialize_in_place(deserializer, _0_SutExchange_Annotation_module.Annotation, value, stored_raw)


class anno_listDataObjConsumedProps(typelib_common.DataObjPropsBase):
    def __getitem__(self, i) -> _0_SutExchange_Annotation_module.AnnotationDataObjConsumed:
        return self._create_data_obj(_0_SutExchange_Annotation_module.AnnotationDataObjConsumed, i)


class anno_listDataObjProvidedProps(typelib_common.DataObjPropsBase, typelib_common.DataObjSetMixin):
    def __getitem__(self, i) -> _0_SutExchange_Annotation_module.AnnotationDataObjProvided:
        return self._create_data_obj(_0_SutExchange_Annotation_module.AnnotationDataObjProvided, i)

    def __setitem__(self, i, item: _0_SutExchange_Annotation_module.Annotation):
        self._set_child_node_value(i, item)


class anno_listDataObjVeConsumed(anno_listDataObjConsumedProps):
    def __init__(self):
        self._branch_path = []
        self._value_entity_wrapper = self


class anno_listDataObjVeProvided(anno_listDataObjProvidedProps):
    def __init__(self):
        self._branch_path = []
        self._value_entity_wrapper = self


class anno_listDataObjConsumed(anno_listDataObjConsumedProps, typelib_common.ComplexSubmember[anno_list]):
    def __init__(self, value_entity_wrapper, branch_path):
        self._branch_path = branch_path
        self._value_entity_wrapper = value_entity_wrapper


class anno_listDataObjProvided(anno_listDataObjProvidedProps, typelib_common.ComplexSubmember[anno_list]):
    def __init__(self, value_entity_wrapper, branch_path):
        self._branch_path = branch_path
        self._value_entity_wrapper = value_entity_wrapper

