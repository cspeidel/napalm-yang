
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

class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/interface-attributes/interface/protection/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State for link-protection
  """
  __slots__ = ('_path_helper', '_extmethods', '__link_protection_style_requested','__bypass_optimize_interval',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__bypass_optimize_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="bypass-optimize-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    self.__link_protection_style_requested = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-mplst:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}},), default=unicode("oc-mplst:LINK_NODE_PROTECTION_REQUESTED"), is_leaf=True, yang_name="link-protection-style-requested", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)

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
      return [u'network-instances', u'network-instance', u'mpls', u'signaling-protocols', u'rsvp-te', u'interface-attributes', u'interface', u'protection', u'state']

  def _get_link_protection_style_requested(self):
    """
    Getter method for link_protection_style_requested, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/protection/state/link_protection_style_requested (identityref)

    YANG Description: Style of mpls frr protection desired:
link, link-node, or unprotected
    """
    return self.__link_protection_style_requested
      
  def _set_link_protection_style_requested(self, v, load=False):
    """
    Setter method for link_protection_style_requested, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/protection/state/link_protection_style_requested (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_protection_style_requested is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_protection_style_requested() directly.

    YANG Description: Style of mpls frr protection desired:
link, link-node, or unprotected
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-mplst:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}},), default=unicode("oc-mplst:LINK_NODE_PROTECTION_REQUESTED"), is_leaf=True, yang_name="link-protection-style-requested", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_protection_style_requested must be of a type compatible with identityref""",
          'defined-type': "openconfig-network-instance:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-mplst:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}},), default=unicode("oc-mplst:LINK_NODE_PROTECTION_REQUESTED"), is_leaf=True, yang_name="link-protection-style-requested", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)""",
        })

    self.__link_protection_style_requested = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_protection_style_requested(self):
    self.__link_protection_style_requested = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-mplst:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}},), default=unicode("oc-mplst:LINK_NODE_PROTECTION_REQUESTED"), is_leaf=True, yang_name="link-protection-style-requested", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)


  def _get_bypass_optimize_interval(self):
    """
    Getter method for bypass_optimize_interval, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/protection/state/bypass_optimize_interval (uint16)

    YANG Description: interval between periodic optimization
of the bypass LSPs
    """
    return self.__bypass_optimize_interval
      
  def _set_bypass_optimize_interval(self, v, load=False):
    """
    Setter method for bypass_optimize_interval, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/protection/state/bypass_optimize_interval (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bypass_optimize_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bypass_optimize_interval() directly.

    YANG Description: interval between periodic optimization
of the bypass LSPs
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="bypass-optimize-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bypass_optimize_interval must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="bypass-optimize-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)""",
        })

    self.__bypass_optimize_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bypass_optimize_interval(self):
    self.__bypass_optimize_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="bypass-optimize-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)

  link_protection_style_requested = __builtin__.property(_get_link_protection_style_requested)
  bypass_optimize_interval = __builtin__.property(_get_bypass_optimize_interval)


  _pyangbind_elements = {'link_protection_style_requested': link_protection_style_requested, 'bypass_optimize_interval': bypass_optimize_interval, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/interface-attributes/interface/protection/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State for link-protection
  """
  __slots__ = ('_path_helper', '_extmethods', '__link_protection_style_requested','__bypass_optimize_interval',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__bypass_optimize_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="bypass-optimize-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    self.__link_protection_style_requested = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-mplst:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}},), default=unicode("oc-mplst:LINK_NODE_PROTECTION_REQUESTED"), is_leaf=True, yang_name="link-protection-style-requested", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)

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
      return [u'network-instances', u'network-instance', u'mpls', u'signaling-protocols', u'rsvp-te', u'interface-attributes', u'interface', u'protection', u'state']

  def _get_link_protection_style_requested(self):
    """
    Getter method for link_protection_style_requested, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/protection/state/link_protection_style_requested (identityref)

    YANG Description: Style of mpls frr protection desired:
link, link-node, or unprotected
    """
    return self.__link_protection_style_requested
      
  def _set_link_protection_style_requested(self, v, load=False):
    """
    Setter method for link_protection_style_requested, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/protection/state/link_protection_style_requested (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_protection_style_requested is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_protection_style_requested() directly.

    YANG Description: Style of mpls frr protection desired:
link, link-node, or unprotected
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-mplst:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}},), default=unicode("oc-mplst:LINK_NODE_PROTECTION_REQUESTED"), is_leaf=True, yang_name="link-protection-style-requested", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_protection_style_requested must be of a type compatible with identityref""",
          'defined-type': "openconfig-network-instance:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-mplst:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}},), default=unicode("oc-mplst:LINK_NODE_PROTECTION_REQUESTED"), is_leaf=True, yang_name="link-protection-style-requested", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)""",
        })

    self.__link_protection_style_requested = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_protection_style_requested(self):
    self.__link_protection_style_requested = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-mplst:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mplst:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-types:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:UNPROTECTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'oc-mpls-t:LINK_NODE_PROTECTION_REQUESTED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}, u'LINK_PROTECTION_REQUIRED': {'@namespace': u'http://openconfig.net/yang/mpls-types', '@module': u'openconfig-mpls-types'}},), default=unicode("oc-mplst:LINK_NODE_PROTECTION_REQUESTED"), is_leaf=True, yang_name="link-protection-style-requested", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)


  def _get_bypass_optimize_interval(self):
    """
    Getter method for bypass_optimize_interval, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/protection/state/bypass_optimize_interval (uint16)

    YANG Description: interval between periodic optimization
of the bypass LSPs
    """
    return self.__bypass_optimize_interval
      
  def _set_bypass_optimize_interval(self, v, load=False):
    """
    Setter method for bypass_optimize_interval, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/protection/state/bypass_optimize_interval (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bypass_optimize_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bypass_optimize_interval() directly.

    YANG Description: interval between periodic optimization
of the bypass LSPs
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="bypass-optimize-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bypass_optimize_interval must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="bypass-optimize-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)""",
        })

    self.__bypass_optimize_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bypass_optimize_interval(self):
    self.__bypass_optimize_interval = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="bypass-optimize-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)

  link_protection_style_requested = __builtin__.property(_get_link_protection_style_requested)
  bypass_optimize_interval = __builtin__.property(_get_bypass_optimize_interval)


  _pyangbind_elements = {'link_protection_style_requested': link_protection_style_requested, 'bypass_optimize_interval': bypass_optimize_interval, }


