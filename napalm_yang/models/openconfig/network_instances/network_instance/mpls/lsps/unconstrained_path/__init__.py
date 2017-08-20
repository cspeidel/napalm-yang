
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

from . import path_setup_protocol
class unconstrained_path(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/lsps/unconstrained-path. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: LSPs that use the IGP-determined path, i.e., non
traffic-engineered, or non constrained-path
  """
  __slots__ = ('_path_helper', '_extmethods', '__path_setup_protocol',)

  _yang_name = 'unconstrained-path'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__path_setup_protocol = YANGDynClass(base=path_setup_protocol.path_setup_protocol, is_container='container', yang_name="path-setup-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'unconstrained-path']

  def _get_path_setup_protocol(self):
    """
    Getter method for path_setup_protocol, mapped from YANG variable /network_instances/network_instance/mpls/lsps/unconstrained_path/path_setup_protocol (container)

    YANG Description: select and configure the signaling method for
 the LSP
    """
    return self.__path_setup_protocol
      
  def _set_path_setup_protocol(self, v, load=False):
    """
    Setter method for path_setup_protocol, mapped from YANG variable /network_instances/network_instance/mpls/lsps/unconstrained_path/path_setup_protocol (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path_setup_protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path_setup_protocol() directly.

    YANG Description: select and configure the signaling method for
 the LSP
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=path_setup_protocol.path_setup_protocol, is_container='container', yang_name="path-setup-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path_setup_protocol must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=path_setup_protocol.path_setup_protocol, is_container='container', yang_name="path-setup-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__path_setup_protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path_setup_protocol(self):
    self.__path_setup_protocol = YANGDynClass(base=path_setup_protocol.path_setup_protocol, is_container='container', yang_name="path-setup-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  path_setup_protocol = __builtin__.property(_get_path_setup_protocol, _set_path_setup_protocol)


  _pyangbind_elements = {'path_setup_protocol': path_setup_protocol, }


from . import path_setup_protocol
class unconstrained_path(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/lsps/unconstrained-path. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: LSPs that use the IGP-determined path, i.e., non
traffic-engineered, or non constrained-path
  """
  __slots__ = ('_path_helper', '_extmethods', '__path_setup_protocol',)

  _yang_name = 'unconstrained-path'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__path_setup_protocol = YANGDynClass(base=path_setup_protocol.path_setup_protocol, is_container='container', yang_name="path-setup-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'unconstrained-path']

  def _get_path_setup_protocol(self):
    """
    Getter method for path_setup_protocol, mapped from YANG variable /network_instances/network_instance/mpls/lsps/unconstrained_path/path_setup_protocol (container)

    YANG Description: select and configure the signaling method for
 the LSP
    """
    return self.__path_setup_protocol
      
  def _set_path_setup_protocol(self, v, load=False):
    """
    Setter method for path_setup_protocol, mapped from YANG variable /network_instances/network_instance/mpls/lsps/unconstrained_path/path_setup_protocol (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path_setup_protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path_setup_protocol() directly.

    YANG Description: select and configure the signaling method for
 the LSP
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=path_setup_protocol.path_setup_protocol, is_container='container', yang_name="path-setup-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path_setup_protocol must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=path_setup_protocol.path_setup_protocol, is_container='container', yang_name="path-setup-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__path_setup_protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path_setup_protocol(self):
    self.__path_setup_protocol = YANGDynClass(base=path_setup_protocol.path_setup_protocol, is_container='container', yang_name="path-setup-protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  path_setup_protocol = __builtin__.property(_get_path_setup_protocol, _set_path_setup_protocol)


  _pyangbind_elements = {'path_setup_protocol': path_setup_protocol, }


