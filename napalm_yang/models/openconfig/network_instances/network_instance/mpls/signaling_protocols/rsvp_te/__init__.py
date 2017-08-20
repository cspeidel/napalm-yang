
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

from . import sessions
from . import neighbors
from . import global_
from . import interface_attributes
class rsvp_te(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: RSVP-TE global signaling protocol configuration
  """
  __slots__ = ('_path_helper', '_extmethods', '__sessions','__neighbors','__global_','__interface_attributes',)

  _yang_name = 'rsvp-te'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__neighbors = YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__interface_attributes = YANGDynClass(base=interface_attributes.interface_attributes, is_container='container', yang_name="interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__global_ = YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__sessions = YANGDynClass(base=sessions.sessions, is_container='container', yang_name="sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'signaling-protocols', u'rsvp-te']

  def _get_sessions(self):
    """
    Getter method for sessions, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions (container)

    YANG Description: Enclosing container for sessions
    """
    return self.__sessions
      
  def _set_sessions(self, v, load=False):
    """
    Setter method for sessions, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sessions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sessions() directly.

    YANG Description: Enclosing container for sessions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=sessions.sessions, is_container='container', yang_name="sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sessions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=sessions.sessions, is_container='container', yang_name="sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__sessions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sessions(self):
    self.__sessions = YANGDynClass(base=sessions.sessions, is_container='container', yang_name="sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_neighbors(self):
    """
    Getter method for neighbors, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/neighbors (container)

    YANG Description: Configuration and state for RSVP neighbors connecting
to the device
    """
    return self.__neighbors
      
  def _set_neighbors(self, v, load=False):
    """
    Setter method for neighbors, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/neighbors (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbors is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbors() directly.

    YANG Description: Configuration and state for RSVP neighbors connecting
to the device
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbors must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__neighbors = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbors(self):
    self.__neighbors = YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_global_(self):
    """
    Getter method for global_, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global (container)

    YANG Description: Platform wide RSVP configuration and state
    """
    return self.__global_
      
  def _set_global_(self, v, load=False):
    """
    Setter method for global_, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_() directly.

    YANG Description: Platform wide RSVP configuration and state
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


  def _get_interface_attributes(self):
    """
    Getter method for interface_attributes, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes (container)

    YANG Description: Attributes relating to RSVP-TE enabled interfaces
    """
    return self.__interface_attributes
      
  def _set_interface_attributes(self, v, load=False):
    """
    Setter method for interface_attributes, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_attributes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_attributes() directly.

    YANG Description: Attributes relating to RSVP-TE enabled interfaces
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface_attributes.interface_attributes, is_container='container', yang_name="interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_attributes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_attributes.interface_attributes, is_container='container', yang_name="interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__interface_attributes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_attributes(self):
    self.__interface_attributes = YANGDynClass(base=interface_attributes.interface_attributes, is_container='container', yang_name="interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  sessions = __builtin__.property(_get_sessions, _set_sessions)
  neighbors = __builtin__.property(_get_neighbors, _set_neighbors)
  global_ = __builtin__.property(_get_global_, _set_global_)
  interface_attributes = __builtin__.property(_get_interface_attributes, _set_interface_attributes)


  _pyangbind_elements = {'sessions': sessions, 'neighbors': neighbors, 'global_': global_, 'interface_attributes': interface_attributes, }


from . import sessions
from . import neighbors
from . import global_
from . import interface_attributes
class rsvp_te(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: RSVP-TE global signaling protocol configuration
  """
  __slots__ = ('_path_helper', '_extmethods', '__sessions','__neighbors','__global_','__interface_attributes',)

  _yang_name = 'rsvp-te'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__neighbors = YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__interface_attributes = YANGDynClass(base=interface_attributes.interface_attributes, is_container='container', yang_name="interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__global_ = YANGDynClass(base=global_.global_, is_container='container', yang_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__sessions = YANGDynClass(base=sessions.sessions, is_container='container', yang_name="sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'signaling-protocols', u'rsvp-te']

  def _get_sessions(self):
    """
    Getter method for sessions, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions (container)

    YANG Description: Enclosing container for sessions
    """
    return self.__sessions
      
  def _set_sessions(self, v, load=False):
    """
    Setter method for sessions, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/sessions (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sessions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sessions() directly.

    YANG Description: Enclosing container for sessions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=sessions.sessions, is_container='container', yang_name="sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sessions must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=sessions.sessions, is_container='container', yang_name="sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__sessions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sessions(self):
    self.__sessions = YANGDynClass(base=sessions.sessions, is_container='container', yang_name="sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_neighbors(self):
    """
    Getter method for neighbors, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/neighbors (container)

    YANG Description: Configuration and state for RSVP neighbors connecting
to the device
    """
    return self.__neighbors
      
  def _set_neighbors(self, v, load=False):
    """
    Setter method for neighbors, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/neighbors (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbors is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbors() directly.

    YANG Description: Configuration and state for RSVP neighbors connecting
to the device
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbors must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__neighbors = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbors(self):
    self.__neighbors = YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_global_(self):
    """
    Getter method for global_, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global (container)

    YANG Description: Platform wide RSVP configuration and state
    """
    return self.__global_
      
  def _set_global_(self, v, load=False):
    """
    Setter method for global_, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_() directly.

    YANG Description: Platform wide RSVP configuration and state
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


  def _get_interface_attributes(self):
    """
    Getter method for interface_attributes, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes (container)

    YANG Description: Attributes relating to RSVP-TE enabled interfaces
    """
    return self.__interface_attributes
      
  def _set_interface_attributes(self, v, load=False):
    """
    Setter method for interface_attributes, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_attributes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_attributes() directly.

    YANG Description: Attributes relating to RSVP-TE enabled interfaces
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface_attributes.interface_attributes, is_container='container', yang_name="interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_attributes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_attributes.interface_attributes, is_container='container', yang_name="interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__interface_attributes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_attributes(self):
    self.__interface_attributes = YANGDynClass(base=interface_attributes.interface_attributes, is_container='container', yang_name="interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  sessions = __builtin__.property(_get_sessions, _set_sessions)
  neighbors = __builtin__.property(_get_neighbors, _set_neighbors)
  global_ = __builtin__.property(_get_global_, _set_global_)
  interface_attributes = __builtin__.property(_get_interface_attributes, _set_interface_attributes)


  _pyangbind_elements = {'sessions': sessions, 'neighbors': neighbors, 'global_': global_, 'interface_attributes': interface_attributes, }


