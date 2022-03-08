# This code was generated automatically. Changes to this file may
# cause incorrect behavior and will be lost if the code is regenerated.

from .._vector_typelib import typelib_data_member as typelib_data_member
from .._vector_typelib import typelib_event_member as typelib_event_member
from .._vector_typelib import typelib_field_member as typelib_field_member
from .._vector_typelib import typelib_do as typelib_do
from .._vector_typelib import typelib_base_datatypes as typelib_base_datatypes
from .._vector_typelib import typelib_encodings as typelib_encodings

from . import TransmittedImage_module as _0_SutExchange_TransmittedImage_module
from . import OperationMode_module as _0_SutExchange_OperationMode_module

from canoe_sil_adapter_runtime.cla import TxTrigger_OnChange, TxTrigger_OnUpdate


class _c_inputImage(typelib_data_member.ConsumedData[_0_SutExchange_TransmittedImage_module.TransmittedImage], _0_SutExchange_TransmittedImage_module.TransmittedImageDataObjVeConsumed):
    def __init__(self, do_interface_impl, embedded_prefix, do_member_name, dt):
        typelib_data_member.ConsumedData.__init__(self, do_interface_impl, embedded_prefix, do_member_name, dt)
        _0_SutExchange_TransmittedImage_module.TransmittedImageDataObjVeConsumed.__init__(self)

class IInputImage(typelib_do.DoInterfaceImpl):
    def __init__(self, identifier, embedded_prefix="", do=None, tx_trigger: dict = {}):
        super().__init__(identifier, embedded_prefix, do)
        self._operationMode = typelib_data_member.ConsumedData(self, self._embedded_prefix, 'operationMode', typelib_base_datatypes.EnumDataType(_0_SutExchange_OperationMode_module.OperationMode,  _0_SutExchange_OperationMode_module.OperationMode.DetectionAndClassification, 8))
        self._inputImage = _c_inputImage(self, self._embedded_prefix, 'inputImage', _0_SutExchange_TransmittedImage_module.TransmittedImage)

        self.__setup_initial_values()

    @property
    def operationMode(self) -> typelib_data_member.ConsumedData[_0_SutExchange_OperationMode_module.OperationMode]:
        return self._operationMode

    @property
    def inputImage(self) -> _c_inputImage:
        return self._inputImage

    def __setup_initial_values(self):
        pass

    def _get_members(self):
        members = [self._operationMode, self._inputImage]
        return members

