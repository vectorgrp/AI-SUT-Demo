# This code was generated automatically. Changes to this file may
# cause incorrect behavior and will be lost if the code is regenerated.

from . import IInputImage_module as _0_SutExchange_IInputImage_module
from . import IImageAnnotation_module as _0_SutExchange_IImageAnnotation_module
from canoe_sil_adapter_runtime.cla import TxTrigger_OnChange, TxTrigger_OnUpdate
import atexit

InputImage = _0_SutExchange_IInputImage_module.IInputImage(
    'SutExchange::InputImage',
    tx_trigger={
    })
ImageAnnotation = _0_SutExchange_IImageAnnotation_module.IImageAnnotation(
    'SutExchange::ImageAnnotation',
    tx_trigger={
    })

_distributed_objects = (
  InputImage,
  ImageAnnotation,
)

def _setup_DO_initial_values():
  pass

def _typelib_shutdown():
  for pyDo in _distributed_objects:
    pyDo._release()
    del pyDo._do

_setup_DO_initial_values()

atexit.register(_typelib_shutdown)
