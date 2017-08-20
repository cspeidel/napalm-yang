
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

from . import global_
from . import areas
class ospfv2(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level configuration and operational state for
Open Shortest Path First (OSPF) v2
  """
  __slots__ = ('_path_helper', '_extmethods', '__global_','__areas',)

  _yang_name = 'ospfv2'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__areas = YANGDynClass(base=areas.areas, is_container='container', yang_name="areas", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__global_ = YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2']

  def _get_global_(self):
    """
    Getter method for global_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global (container)

    YANG Description: Configuration and operational state parameters for settings
that are global to the OSPFv2 instance
    """
    return self.__global_
      
  def _set_global_(self, v, load=False):
    """
    Setter method for global_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_() directly.

    YANG Description: Configuration and operational state parameters for settings
that are global to the OSPFv2 instance
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """global_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__global_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_global_(self):
    self.__global_ = YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_areas(self):
    """
    Getter method for areas, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas (container)

    YANG Description: Configuration and operational state relating to an
OSPFv2 area.
    """
    return self.__areas
      
  def _set_areas(self, v, load=False):
    """
    Setter method for areas, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_areas is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_areas() directly.

    YANG Description: Configuration and operational state relating to an
OSPFv2 area.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=areas.areas, is_container='container', yang_name="areas", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """areas must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=areas.areas, is_container='container', yang_name="areas", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__areas = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_areas(self):
    self.__areas = YANGDynClass(base=areas.areas, is_container='container', yang_name="areas", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  global_ = __builtin__.property(_get_global_, _set_global_)
  areas = __builtin__.property(_get_areas, _set_areas)


  _pyangbind_elements = {'global_': global_, 'areas': areas, }


from . import global_
from . import areas
class ospfv2(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level configuration and operational state for
Open Shortest Path First (OSPF) v2
  """
  __slots__ = ('_path_helper', '_extmethods', '__global_','__areas',)

  _yang_name = 'ospfv2'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__areas = YANGDynClass(base=areas.areas, is_container='container', yang_name="areas", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__global_ = YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2']

  def _get_global_(self):
    """
    Getter method for global_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global (container)

    YANG Description: Configuration and operational state parameters for settings
that are global to the OSPFv2 instance
    """
    return self.__global_
      
  def _set_global_(self, v, load=False):
    """
    Setter method for global_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/global (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_() directly.

    YANG Description: Configuration and operational state parameters for settings
that are global to the OSPFv2 instance
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """global_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__global_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_global_(self):
    self.__global_ = YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_areas(self):
    """
    Getter method for areas, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas (container)

    YANG Description: Configuration and operational state relating to an
OSPFv2 area.
    """
    return self.__areas
      
  def _set_areas(self, v, load=False):
    """
    Setter method for areas, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_areas is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_areas() directly.

    YANG Description: Configuration and operational state relating to an
OSPFv2 area.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=areas.areas, is_container='container', yang_name="areas", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """areas must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=areas.areas, is_container='container', yang_name="areas", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__areas = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_areas(self):
    self.__areas = YANGDynClass(base=areas.areas, is_container='container', yang_name="areas", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  global_ = __builtin__.property(_get_global_, _set_global_)
  areas = __builtin__.property(_get_areas, _set_areas)


  _pyangbind_elements = {'global_': global_, 'areas': areas, }


