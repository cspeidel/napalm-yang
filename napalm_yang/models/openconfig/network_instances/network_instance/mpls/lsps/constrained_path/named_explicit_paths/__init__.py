
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

from . import named_explicit_path
class named_explicit_paths(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/named-explicit-paths. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for the named explicit paths
  """
  __slots__ = ('_path_helper', '_extmethods', '__named_explicit_path',)

  _yang_name = 'named-explicit-paths'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__named_explicit_path = YANGDynClass(base=YANGListType("name",named_explicit_path.named_explicit_path, yang_name="named-explicit-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="named-explicit-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'constrained-path', u'named-explicit-paths']

  def _get_named_explicit_path(self):
    """
    Getter method for named_explicit_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/named_explicit_paths/named_explicit_path (list)

    YANG Description: A list of explicit paths
    """
    return self.__named_explicit_path
      
  def _set_named_explicit_path(self, v, load=False):
    """
    Setter method for named_explicit_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/named_explicit_paths/named_explicit_path (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_named_explicit_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_named_explicit_path() directly.

    YANG Description: A list of explicit paths
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",named_explicit_path.named_explicit_path, yang_name="named-explicit-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="named-explicit-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """named_explicit_path must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",named_explicit_path.named_explicit_path, yang_name="named-explicit-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="named-explicit-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__named_explicit_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_named_explicit_path(self):
    self.__named_explicit_path = YANGDynClass(base=YANGListType("name",named_explicit_path.named_explicit_path, yang_name="named-explicit-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="named-explicit-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  named_explicit_path = __builtin__.property(_get_named_explicit_path, _set_named_explicit_path)


  _pyangbind_elements = {'named_explicit_path': named_explicit_path, }


from . import named_explicit_path
class named_explicit_paths(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/named-explicit-paths. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for the named explicit paths
  """
  __slots__ = ('_path_helper', '_extmethods', '__named_explicit_path',)

  _yang_name = 'named-explicit-paths'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__named_explicit_path = YANGDynClass(base=YANGListType("name",named_explicit_path.named_explicit_path, yang_name="named-explicit-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="named-explicit-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'constrained-path', u'named-explicit-paths']

  def _get_named_explicit_path(self):
    """
    Getter method for named_explicit_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/named_explicit_paths/named_explicit_path (list)

    YANG Description: A list of explicit paths
    """
    return self.__named_explicit_path
      
  def _set_named_explicit_path(self, v, load=False):
    """
    Setter method for named_explicit_path, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/named_explicit_paths/named_explicit_path (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_named_explicit_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_named_explicit_path() directly.

    YANG Description: A list of explicit paths
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("name",named_explicit_path.named_explicit_path, yang_name="named-explicit-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="named-explicit-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """named_explicit_path must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",named_explicit_path.named_explicit_path, yang_name="named-explicit-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="named-explicit-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__named_explicit_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_named_explicit_path(self):
    self.__named_explicit_path = YANGDynClass(base=YANGListType("name",named_explicit_path.named_explicit_path, yang_name="named-explicit-path", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions=None), is_container='list', yang_name="named-explicit-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  named_explicit_path = __builtin__.property(_get_named_explicit_path, _set_named_explicit_path)


  _pyangbind_elements = {'named_explicit_path': named_explicit_path, }


