
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

from . import afi
class igp_shortcuts(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/global/igp-shortcuts. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines IGP shortcuts configuration and state
information.
  """
  __slots__ = ('_path_helper', '_extmethods', '__afi',)

  _yang_name = 'igp-shortcuts'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__afi = YANGDynClass(base=YANGListType("afi_name",afi.afi, yang_name="afi", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-name', extensions=None), is_container='list', yang_name="afi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'global', u'igp-shortcuts']

  def _get_afi(self):
    """
    Getter method for afi, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/igp_shortcuts/afi (list)

    YANG Description: Address-family list.
    """
    return self.__afi
      
  def _set_afi(self, v, load=False):
    """
    Setter method for afi, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/igp_shortcuts/afi (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_afi is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_afi() directly.

    YANG Description: Address-family list.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("afi_name",afi.afi, yang_name="afi", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-name', extensions=None), is_container='list', yang_name="afi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """afi must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("afi_name",afi.afi, yang_name="afi", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-name', extensions=None), is_container='list', yang_name="afi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__afi = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_afi(self):
    self.__afi = YANGDynClass(base=YANGListType("afi_name",afi.afi, yang_name="afi", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-name', extensions=None), is_container='list', yang_name="afi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  afi = __builtin__.property(_get_afi, _set_afi)


  _pyangbind_elements = {'afi': afi, }


from . import afi
class igp_shortcuts(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/global/igp-shortcuts. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines IGP shortcuts configuration and state
information.
  """
  __slots__ = ('_path_helper', '_extmethods', '__afi',)

  _yang_name = 'igp-shortcuts'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__afi = YANGDynClass(base=YANGListType("afi_name",afi.afi, yang_name="afi", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-name', extensions=None), is_container='list', yang_name="afi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'global', u'igp-shortcuts']

  def _get_afi(self):
    """
    Getter method for afi, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/igp_shortcuts/afi (list)

    YANG Description: Address-family list.
    """
    return self.__afi
      
  def _set_afi(self, v, load=False):
    """
    Setter method for afi, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/igp_shortcuts/afi (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_afi is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_afi() directly.

    YANG Description: Address-family list.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("afi_name",afi.afi, yang_name="afi", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-name', extensions=None), is_container='list', yang_name="afi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """afi must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("afi_name",afi.afi, yang_name="afi", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-name', extensions=None), is_container='list', yang_name="afi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__afi = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_afi(self):
    self.__afi = YANGDynClass(base=YANGListType("afi_name",afi.afi, yang_name="afi", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='afi-name', extensions=None), is_container='list', yang_name="afi", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  afi = __builtin__.property(_get_afi, _set_afi)


  _pyangbind_elements = {'afi': afi, }


