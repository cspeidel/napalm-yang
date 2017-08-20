
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
  unicode = str
elif six.PY2:
  import __builtin__

from . import temperature
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform - based on the path /components/component/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for each component
  """
  __slots__ = ('_path_helper', '_extmethods', '__name','__type','__id','__description','__mfg_name','__version','__serial_no','__part_no','__temperature',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__description = YANGDynClass(base=unicode, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)
    self.__part_no = YANGDynClass(base=unicode, is_leaf=True, yang_name="part-no", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)
    self.__serial_no = YANGDynClass(base=unicode, is_leaf=True, yang_name="serial-no", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)
    self.__mfg_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="mfg-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)
    self.__version = YANGDynClass(base=unicode, is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)
    self.__temperature = YANGDynClass(base=temperature.temperature, is_container='container', yang_name="temperature", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='container', is_config=False)
    self.__type = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'PORT': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'TRANSCEIVER': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:SENSOR': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'CPU': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:LINECARD': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:CPU': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'FAN': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:POWER_SUPPLY': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:PORT': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:FAN': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-opt-types:OPTICAL_CHANNEL': {'@namespace': u'http://openconfig.net/yang/transport-types', '@module': u'openconfig-transport-types'}, u'oc-platform-types:TRANSCEIVER': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:CHASSIS': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'MODULE': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'BACKPLANE': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'LINECARD': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'SENSOR': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:MODULE': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:BACKPLANE': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'CHASSIS': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'POWER_SUPPLY': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'OPTICAL_CHANNEL': {'@namespace': u'http://openconfig.net/yang/transport-types', '@module': u'openconfig-transport-types'}},),RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-platform-types:OPERATING_SYSTEM': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'OPERATING_SYSTEM': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}},),], is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='union', is_config=False)
    self.__id = YANGDynClass(base=unicode, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'components', u'component', u'state']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /components/component/state/name (string)

    YANG Description: Device name for the component -- this will not be a
configurable parameter on many implementations
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /components/component/state/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Device name for the component -- this will not be a
configurable parameter on many implementations
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)


  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /components/component/state/type (union)

    YANG Description: Type of component as identified by the system
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /components/component/state/type (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: Type of component as identified by the system
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'PORT': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'TRANSCEIVER': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:SENSOR': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'CPU': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:LINECARD': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:CPU': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'FAN': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:POWER_SUPPLY': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:PORT': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:FAN': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-opt-types:OPTICAL_CHANNEL': {'@namespace': u'http://openconfig.net/yang/transport-types', '@module': u'openconfig-transport-types'}, u'oc-platform-types:TRANSCEIVER': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:CHASSIS': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'MODULE': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'BACKPLANE': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'LINECARD': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'SENSOR': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:MODULE': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:BACKPLANE': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'CHASSIS': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'POWER_SUPPLY': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'OPTICAL_CHANNEL': {'@namespace': u'http://openconfig.net/yang/transport-types', '@module': u'openconfig-transport-types'}},),RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-platform-types:OPERATING_SYSTEM': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'OPERATING_SYSTEM': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}},),], is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with union""",
          'defined-type': "openconfig-platform:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'PORT': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'TRANSCEIVER': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:SENSOR': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'CPU': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:LINECARD': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:CPU': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'FAN': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:POWER_SUPPLY': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:PORT': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:FAN': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-opt-types:OPTICAL_CHANNEL': {'@namespace': u'http://openconfig.net/yang/transport-types', '@module': u'openconfig-transport-types'}, u'oc-platform-types:TRANSCEIVER': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:CHASSIS': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'MODULE': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'BACKPLANE': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'LINECARD': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'SENSOR': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:MODULE': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:BACKPLANE': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'CHASSIS': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'POWER_SUPPLY': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'OPTICAL_CHANNEL': {'@namespace': u'http://openconfig.net/yang/transport-types', '@module': u'openconfig-transport-types'}},),RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-platform-types:OPERATING_SYSTEM': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'OPERATING_SYSTEM': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}},),], is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='union', is_config=False)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'PORT': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'TRANSCEIVER': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:SENSOR': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'CPU': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:LINECARD': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:CPU': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'FAN': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:POWER_SUPPLY': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:PORT': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:FAN': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-opt-types:OPTICAL_CHANNEL': {'@namespace': u'http://openconfig.net/yang/transport-types', '@module': u'openconfig-transport-types'}, u'oc-platform-types:TRANSCEIVER': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:CHASSIS': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'MODULE': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'BACKPLANE': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'LINECARD': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'SENSOR': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:MODULE': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'oc-platform-types:BACKPLANE': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'CHASSIS': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'POWER_SUPPLY': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'OPTICAL_CHANNEL': {'@namespace': u'http://openconfig.net/yang/transport-types', '@module': u'openconfig-transport-types'}},),RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-platform-types:OPERATING_SYSTEM': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}, u'OPERATING_SYSTEM': {'@namespace': u'http://openconfig.net/yang/platform-types', '@module': u'openconfig-platform-types'}},),], is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='union', is_config=False)


  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /components/component/state/id (string)

    YANG Description: Unique identifier assigned by the system for the
component
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /components/component/state/id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.

    YANG Description: Unique identifier assigned by the system for the
component
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=unicode, is_leaf=True, yang_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)


  def _get_description(self):
    """
    Getter method for description, mapped from YANG variable /components/component/state/description (string)

    YANG Description: System-supplied description of the component
    """
    return self.__description
      
  def _set_description(self, v, load=False):
    """
    Setter method for description, mapped from YANG variable /components/component/state/description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description() directly.

    YANG Description: System-supplied description of the component
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)""",
        })

    self.__description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description(self):
    self.__description = YANGDynClass(base=unicode, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)


  def _get_mfg_name(self):
    """
    Getter method for mfg_name, mapped from YANG variable /components/component/state/mfg_name (string)

    YANG Description: System-supplied identifier for the manufacturer of the
component.  This data is particularly useful when a
component manufacturer is different than the overall
device vendor.
    """
    return self.__mfg_name
      
  def _set_mfg_name(self, v, load=False):
    """
    Setter method for mfg_name, mapped from YANG variable /components/component/state/mfg_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mfg_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mfg_name() directly.

    YANG Description: System-supplied identifier for the manufacturer of the
component.  This data is particularly useful when a
component manufacturer is different than the overall
device vendor.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mfg-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mfg_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mfg-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)""",
        })

    self.__mfg_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mfg_name(self):
    self.__mfg_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="mfg-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)


  def _get_version(self):
    """
    Getter method for version, mapped from YANG variable /components/component/state/version (string)

    YANG Description: System-defined version string for a hardware, firmware,
or software component.
    """
    return self.__version
      
  def _set_version(self, v, load=False):
    """
    Setter method for version, mapped from YANG variable /components/component/state/version (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_version is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_version() directly.

    YANG Description: System-defined version string for a hardware, firmware,
or software component.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """version must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)""",
        })

    self.__version = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_version(self):
    self.__version = YANGDynClass(base=unicode, is_leaf=True, yang_name="version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)


  def _get_serial_no(self):
    """
    Getter method for serial_no, mapped from YANG variable /components/component/state/serial_no (string)

    YANG Description: System-assigned serial number of the component.
    """
    return self.__serial_no
      
  def _set_serial_no(self, v, load=False):
    """
    Setter method for serial_no, mapped from YANG variable /components/component/state/serial_no (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_serial_no is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_serial_no() directly.

    YANG Description: System-assigned serial number of the component.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="serial-no", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """serial_no must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="serial-no", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)""",
        })

    self.__serial_no = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_serial_no(self):
    self.__serial_no = YANGDynClass(base=unicode, is_leaf=True, yang_name="serial-no", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)


  def _get_part_no(self):
    """
    Getter method for part_no, mapped from YANG variable /components/component/state/part_no (string)

    YANG Description: System-assigned part number for the component.  This should
be present in particular if the component is also an FRU
(field replacable unit)
    """
    return self.__part_no
      
  def _set_part_no(self, v, load=False):
    """
    Setter method for part_no, mapped from YANG variable /components/component/state/part_no (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_part_no is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_part_no() directly.

    YANG Description: System-assigned part number for the component.  This should
be present in particular if the component is also an FRU
(field replacable unit)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="part-no", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """part_no must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="part-no", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)""",
        })

    self.__part_no = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_part_no(self):
    self.__part_no = YANGDynClass(base=unicode, is_leaf=True, yang_name="part-no", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='string', is_config=False)


  def _get_temperature(self):
    """
    Getter method for temperature, mapped from YANG variable /components/component/state/temperature (container)

    YANG Description: Temperature in degrees Celsius of the component. Values include
the instantaneous, average, minimum, and maximum statistics. If
avg/min/max statistics are not supported, the target is expected
to just supply the instant value
    """
    return self.__temperature
      
  def _set_temperature(self, v, load=False):
    """
    Setter method for temperature, mapped from YANG variable /components/component/state/temperature (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_temperature is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_temperature() directly.

    YANG Description: Temperature in degrees Celsius of the component. Values include
the instantaneous, average, minimum, and maximum statistics. If
avg/min/max statistics are not supported, the target is expected
to just supply the instant value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=temperature.temperature, is_container='container', yang_name="temperature", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """temperature must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=temperature.temperature, is_container='container', yang_name="temperature", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='container', is_config=False)""",
        })

    self.__temperature = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_temperature(self):
    self.__temperature = YANGDynClass(base=temperature.temperature, is_container='container', yang_name="temperature", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/platform', defining_module='openconfig-platform', yang_type='container', is_config=False)

  name = __builtin__.property(_get_name)
  type = __builtin__.property(_get_type)
  id = __builtin__.property(_get_id)
  description = __builtin__.property(_get_description)
  mfg_name = __builtin__.property(_get_mfg_name)
  version = __builtin__.property(_get_version)
  serial_no = __builtin__.property(_get_serial_no)
  part_no = __builtin__.property(_get_part_no)
  temperature = __builtin__.property(_get_temperature)


  _pyangbind_elements = {'name': name, 'type': type, 'id': id, 'description': description, 'mfg_name': mfg_name, 'version': version, 'serial_no': serial_no, 'part_no': part_no, 'temperature': temperature, }


