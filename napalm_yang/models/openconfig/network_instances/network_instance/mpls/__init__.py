
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
from . import te_global_attributes
from . import te_interface_attributes
from . import signaling_protocols
from . import lsps
class mpls(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Anchor point for mpls configuration and operational
data
  """
  __slots__ = ('_path_helper', '_extmethods', '__global_','__te_global_attributes','__te_interface_attributes','__signaling_protocols','__lsps',)

  _yang_name = 'mpls'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__lsps = YANGDynClass(base=lsps.lsps, is_container='container', yang_name="lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__signaling_protocols = YANGDynClass(base=signaling_protocols.signaling_protocols, is_container='container', yang_name="signaling-protocols", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__te_global_attributes = YANGDynClass(base=te_global_attributes.te_global_attributes, is_container='container', yang_name="te-global-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__te_interface_attributes = YANGDynClass(base=te_interface_attributes.te_interface_attributes, is_container='container', yang_name="te-interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
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
      return [u'network-instances', u'network-instance', u'mpls']

  def _get_global_(self):
    """
    Getter method for global_, mapped from YANG variable /network_instances/network_instance/mpls/global (container)

    YANG Description: general mpls configuration applicable to any
type of LSP and signaling protocol - label ranges,
entropy label supportmay be added here
    """
    return self.__global_
      
  def _set_global_(self, v, load=False):
    """
    Setter method for global_, mapped from YANG variable /network_instances/network_instance/mpls/global (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_() directly.

    YANG Description: general mpls configuration applicable to any
type of LSP and signaling protocol - label ranges,
entropy label supportmay be added here
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


  def _get_te_global_attributes(self):
    """
    Getter method for te_global_attributes, mapped from YANG variable /network_instances/network_instance/mpls/te_global_attributes (container)

    YANG Description: traffic-engineering global attributes
    """
    return self.__te_global_attributes
      
  def _set_te_global_attributes(self, v, load=False):
    """
    Setter method for te_global_attributes, mapped from YANG variable /network_instances/network_instance/mpls/te_global_attributes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_te_global_attributes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_te_global_attributes() directly.

    YANG Description: traffic-engineering global attributes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=te_global_attributes.te_global_attributes, is_container='container', yang_name="te-global-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """te_global_attributes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=te_global_attributes.te_global_attributes, is_container='container', yang_name="te-global-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__te_global_attributes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_te_global_attributes(self):
    self.__te_global_attributes = YANGDynClass(base=te_global_attributes.te_global_attributes, is_container='container', yang_name="te-global-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_te_interface_attributes(self):
    """
    Getter method for te_interface_attributes, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes (container)

    YANG Description: traffic engineering attributes specific
for interfaces
    """
    return self.__te_interface_attributes
      
  def _set_te_interface_attributes(self, v, load=False):
    """
    Setter method for te_interface_attributes, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_te_interface_attributes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_te_interface_attributes() directly.

    YANG Description: traffic engineering attributes specific
for interfaces
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=te_interface_attributes.te_interface_attributes, is_container='container', yang_name="te-interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """te_interface_attributes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=te_interface_attributes.te_interface_attributes, is_container='container', yang_name="te-interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__te_interface_attributes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_te_interface_attributes(self):
    self.__te_interface_attributes = YANGDynClass(base=te_interface_attributes.te_interface_attributes, is_container='container', yang_name="te-interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_signaling_protocols(self):
    """
    Getter method for signaling_protocols, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols (container)

    YANG Description: top-level signaling protocol configuration
    """
    return self.__signaling_protocols
      
  def _set_signaling_protocols(self, v, load=False):
    """
    Setter method for signaling_protocols, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_signaling_protocols is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_signaling_protocols() directly.

    YANG Description: top-level signaling protocol configuration
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=signaling_protocols.signaling_protocols, is_container='container', yang_name="signaling-protocols", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """signaling_protocols must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=signaling_protocols.signaling_protocols, is_container='container', yang_name="signaling-protocols", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__signaling_protocols = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_signaling_protocols(self):
    self.__signaling_protocols = YANGDynClass(base=signaling_protocols.signaling_protocols, is_container='container', yang_name="signaling-protocols", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_lsps(self):
    """
    Getter method for lsps, mapped from YANG variable /network_instances/network_instance/mpls/lsps (container)

    YANG Description: LSP definitions and configuration
    """
    return self.__lsps
      
  def _set_lsps(self, v, load=False):
    """
    Setter method for lsps, mapped from YANG variable /network_instances/network_instance/mpls/lsps (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsps is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsps() directly.

    YANG Description: LSP definitions and configuration
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=lsps.lsps, is_container='container', yang_name="lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsps must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=lsps.lsps, is_container='container', yang_name="lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__lsps = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsps(self):
    self.__lsps = YANGDynClass(base=lsps.lsps, is_container='container', yang_name="lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  global_ = __builtin__.property(_get_global_, _set_global_)
  te_global_attributes = __builtin__.property(_get_te_global_attributes, _set_te_global_attributes)
  te_interface_attributes = __builtin__.property(_get_te_interface_attributes, _set_te_interface_attributes)
  signaling_protocols = __builtin__.property(_get_signaling_protocols, _set_signaling_protocols)
  lsps = __builtin__.property(_get_lsps, _set_lsps)


  _pyangbind_elements = {'global_': global_, 'te_global_attributes': te_global_attributes, 'te_interface_attributes': te_interface_attributes, 'signaling_protocols': signaling_protocols, 'lsps': lsps, }


from . import global_
from . import te_global_attributes
from . import te_interface_attributes
from . import signaling_protocols
from . import lsps
class mpls(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Anchor point for mpls configuration and operational
data
  """
  __slots__ = ('_path_helper', '_extmethods', '__global_','__te_global_attributes','__te_interface_attributes','__signaling_protocols','__lsps',)

  _yang_name = 'mpls'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__lsps = YANGDynClass(base=lsps.lsps, is_container='container', yang_name="lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__signaling_protocols = YANGDynClass(base=signaling_protocols.signaling_protocols, is_container='container', yang_name="signaling-protocols", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__te_global_attributes = YANGDynClass(base=te_global_attributes.te_global_attributes, is_container='container', yang_name="te-global-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__te_interface_attributes = YANGDynClass(base=te_interface_attributes.te_interface_attributes, is_container='container', yang_name="te-interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
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
      return [u'network-instances', u'network-instance', u'mpls']

  def _get_global_(self):
    """
    Getter method for global_, mapped from YANG variable /network_instances/network_instance/mpls/global (container)

    YANG Description: general mpls configuration applicable to any
type of LSP and signaling protocol - label ranges,
entropy label supportmay be added here
    """
    return self.__global_
      
  def _set_global_(self, v, load=False):
    """
    Setter method for global_, mapped from YANG variable /network_instances/network_instance/mpls/global (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_() directly.

    YANG Description: general mpls configuration applicable to any
type of LSP and signaling protocol - label ranges,
entropy label supportmay be added here
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


  def _get_te_global_attributes(self):
    """
    Getter method for te_global_attributes, mapped from YANG variable /network_instances/network_instance/mpls/te_global_attributes (container)

    YANG Description: traffic-engineering global attributes
    """
    return self.__te_global_attributes
      
  def _set_te_global_attributes(self, v, load=False):
    """
    Setter method for te_global_attributes, mapped from YANG variable /network_instances/network_instance/mpls/te_global_attributes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_te_global_attributes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_te_global_attributes() directly.

    YANG Description: traffic-engineering global attributes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=te_global_attributes.te_global_attributes, is_container='container', yang_name="te-global-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """te_global_attributes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=te_global_attributes.te_global_attributes, is_container='container', yang_name="te-global-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__te_global_attributes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_te_global_attributes(self):
    self.__te_global_attributes = YANGDynClass(base=te_global_attributes.te_global_attributes, is_container='container', yang_name="te-global-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_te_interface_attributes(self):
    """
    Getter method for te_interface_attributes, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes (container)

    YANG Description: traffic engineering attributes specific
for interfaces
    """
    return self.__te_interface_attributes
      
  def _set_te_interface_attributes(self, v, load=False):
    """
    Setter method for te_interface_attributes, mapped from YANG variable /network_instances/network_instance/mpls/te_interface_attributes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_te_interface_attributes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_te_interface_attributes() directly.

    YANG Description: traffic engineering attributes specific
for interfaces
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=te_interface_attributes.te_interface_attributes, is_container='container', yang_name="te-interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """te_interface_attributes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=te_interface_attributes.te_interface_attributes, is_container='container', yang_name="te-interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__te_interface_attributes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_te_interface_attributes(self):
    self.__te_interface_attributes = YANGDynClass(base=te_interface_attributes.te_interface_attributes, is_container='container', yang_name="te-interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_signaling_protocols(self):
    """
    Getter method for signaling_protocols, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols (container)

    YANG Description: top-level signaling protocol configuration
    """
    return self.__signaling_protocols
      
  def _set_signaling_protocols(self, v, load=False):
    """
    Setter method for signaling_protocols, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_signaling_protocols is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_signaling_protocols() directly.

    YANG Description: top-level signaling protocol configuration
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=signaling_protocols.signaling_protocols, is_container='container', yang_name="signaling-protocols", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """signaling_protocols must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=signaling_protocols.signaling_protocols, is_container='container', yang_name="signaling-protocols", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__signaling_protocols = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_signaling_protocols(self):
    self.__signaling_protocols = YANGDynClass(base=signaling_protocols.signaling_protocols, is_container='container', yang_name="signaling-protocols", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_lsps(self):
    """
    Getter method for lsps, mapped from YANG variable /network_instances/network_instance/mpls/lsps (container)

    YANG Description: LSP definitions and configuration
    """
    return self.__lsps
      
  def _set_lsps(self, v, load=False):
    """
    Setter method for lsps, mapped from YANG variable /network_instances/network_instance/mpls/lsps (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsps is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsps() directly.

    YANG Description: LSP definitions and configuration
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=lsps.lsps, is_container='container', yang_name="lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsps must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=lsps.lsps, is_container='container', yang_name="lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__lsps = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsps(self):
    self.__lsps = YANGDynClass(base=lsps.lsps, is_container='container', yang_name="lsps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  global_ = __builtin__.property(_get_global_, _set_global_)
  te_global_attributes = __builtin__.property(_get_te_global_attributes, _set_te_global_attributes)
  te_interface_attributes = __builtin__.property(_get_te_interface_attributes, _set_te_interface_attributes)
  signaling_protocols = __builtin__.property(_get_signaling_protocols, _set_signaling_protocols)
  lsps = __builtin__.property(_get_lsps, _set_lsps)


  _pyangbind_elements = {'global_': global_, 'te_global_attributes': te_global_attributes, 'te_interface_attributes': te_interface_attributes, 'signaling_protocols': signaling_protocols, 'lsps': lsps, }


