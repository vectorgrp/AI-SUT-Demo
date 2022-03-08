# This code was generated automatically. Changes to this file may
# cause incorrect behavior and will be lost if the code is regenerated.

from .._vector_typelib import typelib_data_member as typelib_data_member
from .._vector_typelib import typelib_event_member as typelib_event_member
from .._vector_typelib import typelib_field_member as typelib_field_member
from .._vector_typelib import typelib_do as typelib_do
from .._vector_typelib import typelib_base_datatypes as typelib_base_datatypes
from .._vector_typelib import typelib_encodings as typelib_encodings

from . import TransmittedImage_module as _0_SutExchange_TransmittedImage_module
from . import anno_list_module as _0_SutExchange_anno_list_module

from canoe_sil_adapter_runtime.cla import TxTrigger_OnChange, TxTrigger_OnUpdate


class _p_outputImage(typelib_data_member.ProvidedData[_0_SutExchange_TransmittedImage_module.TransmittedImage], _0_SutExchange_TransmittedImage_module.TransmittedImageDataObjVeProvided):
    def __init__(self, do_interface_impl, embedded_prefix, do_member_name, dt, stored_raw, tx_trigger):
        typelib_data_member.ProvidedData.__init__(self, do_interface_impl, embedded_prefix, do_member_name, dt, stored_raw, tx_trigger)
        _0_SutExchange_TransmittedImage_module.TransmittedImageDataObjVeProvided.__init__(self)


class _p_annotations(typelib_data_member.ProvidedData[_0_SutExchange_anno_list_module.anno_list], _0_SutExchange_anno_list_module.anno_listDataObjVeProvided):
    def __init__(self, do_interface_impl, embedded_prefix, do_member_name, dt, stored_raw, tx_trigger):
        typelib_data_member.ProvidedData.__init__(self, do_interface_impl, embedded_prefix, do_member_name, dt, stored_raw, tx_trigger)
        _0_SutExchange_anno_list_module.anno_listDataObjVeProvided.__init__(self)

class IImageAnnotation(typelib_do.DoInterfaceImpl):
    def __init__(self, identifier, embedded_prefix="", do=None, tx_trigger: dict = {}):
        super().__init__(identifier, embedded_prefix, do)
        self._outputImage = _p_outputImage(self, self._embedded_prefix, 'outputImage', _0_SutExchange_TransmittedImage_module.TransmittedImage, False, tx_trigger.get('outputImage', TxTrigger_OnUpdate))
        self._annotations = _p_annotations(self, self._embedded_prefix, 'annotations', _0_SutExchange_anno_list_module.anno_list, False, tx_trigger.get('annotations', TxTrigger_OnUpdate))

        self.__setup_initial_values()

    @property
    def outputImage(self) -> _p_outputImage:
        return self._outputImage

    @outputImage.setter
    def outputImage(self, value: _0_SutExchange_TransmittedImage_module.TransmittedImage):
        self._outputImage._set_value(value)

    @property
    def annotations(self) -> _p_annotations:
        return self._annotations

    @annotations.setter
    def annotations(self, value: _0_SutExchange_anno_list_module.anno_list):
        self._annotations._set_value(value)

    def __setup_initial_values(self):
        pass

    def _get_members(self):
        members = [self._outputImage, self._annotations]
        return members

