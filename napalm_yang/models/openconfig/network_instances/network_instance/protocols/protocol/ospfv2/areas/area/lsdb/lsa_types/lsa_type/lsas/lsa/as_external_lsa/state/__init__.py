
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/as-external-lsa/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters for the AS external LSA
  """
  __slots__ = ('_path_helper', '_extmethods', '__mask','__metric_type','__metric','__forwarding_address','__external_route_tag',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__metric_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'TYPE_2': {}, u'TYPE_1': {}},), is_leaf=True, yang_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    self.__external_route_tag = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="external-route-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:ospf-metric', is_config=False)
    self.__mask = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..32']}), is_leaf=True, yang_name="mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    self.__forwarding_address = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': u'[0-9\\.]*'}), is_leaf=True, yang_name="forwarding-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'as-external-lsa', u'state']

  def _get_mask(self):
    """
    Getter method for mask, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/as_external_lsa/state/mask (uint8)

    YANG Description: The subnet mask for the advertised destination
    """
    return self.__mask
      
  def _set_mask(self, v, load=False):
    """
    Setter method for mask, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/as_external_lsa/state/mask (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mask is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mask() directly.

    YANG Description: The subnet mask for the advertised destination
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..32']}), is_leaf=True, yang_name="mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mask must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..32']}), is_leaf=True, yang_name="mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__mask = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mask(self):
    self.__mask = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..32']}), is_leaf=True, yang_name="mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)


  def _get_metric_type(self):
    """
    Getter method for metric_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/as_external_lsa/state/metric_type (enumeration)

    YANG Description: The type of metric included within the AS External LSA.
    """
    return self.__metric_type
      
  def _set_metric_type(self, v, load=False):
    """
    Setter method for metric_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/as_external_lsa/state/metric_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric_type() directly.

    YANG Description: The type of metric included within the AS External LSA.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'TYPE_2': {}, u'TYPE_1': {}},), is_leaf=True, yang_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric_type must be of a type compatible with enumeration""",
          'defined-type': "openconfig-network-instance:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'TYPE_2': {}, u'TYPE_1': {}},), is_leaf=True, yang_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)""",
        })

    self.__metric_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric_type(self):
    self.__metric_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'TYPE_2': {}, u'TYPE_1': {}},), is_leaf=True, yang_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)


  def _get_metric(self):
    """
    Getter method for metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/as_external_lsa/state/metric (oc-ospf-types:ospf-metric)

    YANG Description: The cost to reach the external network specified. The exact
interpretation of this cost is dependent on the type of
metric specified
    """
    return self.__metric
      
  def _set_metric(self, v, load=False):
    """
    Setter method for metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/as_external_lsa/state/metric (oc-ospf-types:ospf-metric)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric() directly.

    YANG Description: The cost to reach the external network specified. The exact
interpretation of this cost is dependent on the type of
metric specified
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:ospf-metric', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric must be of a type compatible with oc-ospf-types:ospf-metric""",
          'defined-type': "oc-ospf-types:ospf-metric",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:ospf-metric', is_config=False)""",
        })

    self.__metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric(self):
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:ospf-metric', is_config=False)


  def _get_forwarding_address(self):
    """
    Getter method for forwarding_address, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/as_external_lsa/state/forwarding_address (inet:ipv4-address-no-zone)

    YANG Description: The destination to which traffic for the external prefix
should be advertised. When this value is set to 0.0.0.0 then
traffic should be forwarded to the LSA's originator
    """
    return self.__forwarding_address
      
  def _set_forwarding_address(self, v, load=False):
    """
    Setter method for forwarding_address, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/as_external_lsa/state/forwarding_address (inet:ipv4-address-no-zone)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_forwarding_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_forwarding_address() directly.

    YANG Description: The destination to which traffic for the external prefix
should be advertised. When this value is set to 0.0.0.0 then
traffic should be forwarded to the LSA's originator
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': u'[0-9\\.]*'}), is_leaf=True, yang_name="forwarding-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """forwarding_address must be of a type compatible with inet:ipv4-address-no-zone""",
          'defined-type': "inet:ipv4-address-no-zone",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': u'[0-9\\.]*'}), is_leaf=True, yang_name="forwarding-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=False)""",
        })

    self.__forwarding_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_forwarding_address(self):
    self.__forwarding_address = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': u'[0-9\\.]*'}), is_leaf=True, yang_name="forwarding-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=False)


  def _get_external_route_tag(self):
    """
    Getter method for external_route_tag, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/as_external_lsa/state/external_route_tag (uint32)

    YANG Description: An opaque tag that set by the LSA originator to carry
information relating to the external route
    """
    return self.__external_route_tag
      
  def _set_external_route_tag(self, v, load=False):
    """
    Setter method for external_route_tag, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/as_external_lsa/state/external_route_tag (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_external_route_tag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_external_route_tag() directly.

    YANG Description: An opaque tag that set by the LSA originator to carry
information relating to the external route
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="external-route-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """external_route_tag must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="external-route-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__external_route_tag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_external_route_tag(self):
    self.__external_route_tag = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="external-route-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  mask = __builtin__.property(_get_mask)
  metric_type = __builtin__.property(_get_metric_type)
  metric = __builtin__.property(_get_metric)
  forwarding_address = __builtin__.property(_get_forwarding_address)
  external_route_tag = __builtin__.property(_get_external_route_tag)


  _pyangbind_elements = {'mask': mask, 'metric_type': metric_type, 'metric': metric, 'forwarding_address': forwarding_address, 'external_route_tag': external_route_tag, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/as-external-lsa/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters for the AS external LSA
  """
  __slots__ = ('_path_helper', '_extmethods', '__mask','__metric_type','__metric','__forwarding_address','__external_route_tag',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__metric_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'TYPE_2': {}, u'TYPE_1': {}},), is_leaf=True, yang_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    self.__external_route_tag = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="external-route-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:ospf-metric', is_config=False)
    self.__mask = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..32']}), is_leaf=True, yang_name="mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    self.__forwarding_address = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': u'[0-9\\.]*'}), is_leaf=True, yang_name="forwarding-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'as-external-lsa', u'state']

  def _get_mask(self):
    """
    Getter method for mask, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/as_external_lsa/state/mask (uint8)

    YANG Description: The subnet mask for the advertised destination
    """
    return self.__mask
      
  def _set_mask(self, v, load=False):
    """
    Setter method for mask, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/as_external_lsa/state/mask (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mask is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mask() directly.

    YANG Description: The subnet mask for the advertised destination
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..32']}), is_leaf=True, yang_name="mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mask must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..32']}), is_leaf=True, yang_name="mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
        })

    self.__mask = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mask(self):
    self.__mask = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0..32']}), is_leaf=True, yang_name="mask", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)


  def _get_metric_type(self):
    """
    Getter method for metric_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/as_external_lsa/state/metric_type (enumeration)

    YANG Description: The type of metric included within the AS External LSA.
    """
    return self.__metric_type
      
  def _set_metric_type(self, v, load=False):
    """
    Setter method for metric_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/as_external_lsa/state/metric_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric_type() directly.

    YANG Description: The type of metric included within the AS External LSA.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'TYPE_2': {}, u'TYPE_1': {}},), is_leaf=True, yang_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric_type must be of a type compatible with enumeration""",
          'defined-type': "openconfig-network-instance:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'TYPE_2': {}, u'TYPE_1': {}},), is_leaf=True, yang_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)""",
        })

    self.__metric_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric_type(self):
    self.__metric_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'TYPE_2': {}, u'TYPE_1': {}},), is_leaf=True, yang_name="metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)


  def _get_metric(self):
    """
    Getter method for metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/as_external_lsa/state/metric (oc-ospf-types:ospf-metric)

    YANG Description: The cost to reach the external network specified. The exact
interpretation of this cost is dependent on the type of
metric specified
    """
    return self.__metric
      
  def _set_metric(self, v, load=False):
    """
    Setter method for metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/as_external_lsa/state/metric (oc-ospf-types:ospf-metric)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric() directly.

    YANG Description: The cost to reach the external network specified. The exact
interpretation of this cost is dependent on the type of
metric specified
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:ospf-metric', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric must be of a type compatible with oc-ospf-types:ospf-metric""",
          'defined-type': "oc-ospf-types:ospf-metric",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:ospf-metric', is_config=False)""",
        })

    self.__metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric(self):
    self.__metric = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-ospf-types:ospf-metric', is_config=False)


  def _get_forwarding_address(self):
    """
    Getter method for forwarding_address, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/as_external_lsa/state/forwarding_address (inet:ipv4-address-no-zone)

    YANG Description: The destination to which traffic for the external prefix
should be advertised. When this value is set to 0.0.0.0 then
traffic should be forwarded to the LSA's originator
    """
    return self.__forwarding_address
      
  def _set_forwarding_address(self, v, load=False):
    """
    Setter method for forwarding_address, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/as_external_lsa/state/forwarding_address (inet:ipv4-address-no-zone)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_forwarding_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_forwarding_address() directly.

    YANG Description: The destination to which traffic for the external prefix
should be advertised. When this value is set to 0.0.0.0 then
traffic should be forwarded to the LSA's originator
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': u'[0-9\\.]*'}), is_leaf=True, yang_name="forwarding-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """forwarding_address must be of a type compatible with inet:ipv4-address-no-zone""",
          'defined-type': "inet:ipv4-address-no-zone",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': u'[0-9\\.]*'}), is_leaf=True, yang_name="forwarding-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=False)""",
        })

    self.__forwarding_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_forwarding_address(self):
    self.__forwarding_address = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': u'[0-9\\.]*'}), is_leaf=True, yang_name="forwarding-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='inet:ipv4-address-no-zone', is_config=False)


  def _get_external_route_tag(self):
    """
    Getter method for external_route_tag, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/as_external_lsa/state/external_route_tag (uint32)

    YANG Description: An opaque tag that set by the LSA originator to carry
information relating to the external route
    """
    return self.__external_route_tag
      
  def _set_external_route_tag(self, v, load=False):
    """
    Setter method for external_route_tag, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/as_external_lsa/state/external_route_tag (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_external_route_tag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_external_route_tag() directly.

    YANG Description: An opaque tag that set by the LSA originator to carry
information relating to the external route
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="external-route-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """external_route_tag must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="external-route-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__external_route_tag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_external_route_tag(self):
    self.__external_route_tag = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="external-route-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  mask = __builtin__.property(_get_mask)
  metric_type = __builtin__.property(_get_metric_type)
  metric = __builtin__.property(_get_metric)
  forwarding_address = __builtin__.property(_get_forwarding_address)
  external_route_tag = __builtin__.property(_get_external_route_tag)


  _pyangbind_elements = {'mask': mask, 'metric_type': metric_type, 'metric': metric, 'forwarding_address': forwarding_address, 'external_route_tag': external_route_tag, }


