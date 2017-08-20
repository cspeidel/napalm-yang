
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/tables/table/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters related to the table
  """
  __slots__ = ('_path_helper', '_extmethods', '__protocol','__address_family',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__protocol = YANGDynClass(base=unicode, is_leaf=True, yang_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__address_family = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-types:L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}},), is_leaf=True, yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)

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
      return [u'network-instances', u'network-instance', u'tables', u'table', u'state']

  def _get_protocol(self):
    """
    Getter method for protocol, mapped from YANG variable /network_instances/network_instance/tables/table/state/protocol (leafref)

    YANG Description: Reference to the protocol that the table is associated with.
    """
    return self.__protocol
      
  def _set_protocol(self, v, load=False):
    """
    Setter method for protocol, mapped from YANG variable /network_instances/network_instance/tables/table/state/protocol (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol() directly.

    YANG Description: Reference to the protocol that the table is associated with.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol(self):
    self.__protocol = YANGDynClass(base=unicode, is_leaf=True, yang_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_address_family(self):
    """
    Getter method for address_family, mapped from YANG variable /network_instances/network_instance/tables/table/state/address_family (identityref)

    YANG Description: The address family (IPv4, IPv6) of the table's entries
    """
    return self.__address_family
      
  def _set_address_family(self, v, load=False):
    """
    Setter method for address_family, mapped from YANG variable /network_instances/network_instance/tables/table/state/address_family (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address_family is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address_family() directly.

    YANG Description: The address family (IPv4, IPv6) of the table's entries
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-types:L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}},), is_leaf=True, yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address_family must be of a type compatible with identityref""",
          'defined-type': "openconfig-network-instance:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-types:L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}},), is_leaf=True, yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)""",
        })

    self.__address_family = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address_family(self):
    self.__address_family = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-types:L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}},), is_leaf=True, yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)

  protocol = __builtin__.property(_get_protocol)
  address_family = __builtin__.property(_get_address_family)


  _pyangbind_elements = {'protocol': protocol, 'address_family': address_family, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/tables/table/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters related to the table
  """
  __slots__ = ('_path_helper', '_extmethods', '__protocol','__address_family',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__protocol = YANGDynClass(base=unicode, is_leaf=True, yang_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    self.__address_family = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-types:L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}},), is_leaf=True, yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)

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
      return [u'network-instances', u'network-instance', u'tables', u'table', u'state']

  def _get_protocol(self):
    """
    Getter method for protocol, mapped from YANG variable /network_instances/network_instance/tables/table/state/protocol (leafref)

    YANG Description: Reference to the protocol that the table is associated with.
    """
    return self.__protocol
      
  def _set_protocol(self, v, load=False):
    """
    Setter method for protocol, mapped from YANG variable /network_instances/network_instance/tables/table/state/protocol (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol() directly.

    YANG Description: Reference to the protocol that the table is associated with.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)""",
        })

    self.__protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol(self):
    self.__protocol = YANGDynClass(base=unicode, is_leaf=True, yang_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=False)


  def _get_address_family(self):
    """
    Getter method for address_family, mapped from YANG variable /network_instances/network_instance/tables/table/state/address_family (identityref)

    YANG Description: The address family (IPv4, IPv6) of the table's entries
    """
    return self.__address_family
      
  def _set_address_family(self, v, load=False):
    """
    Setter method for address_family, mapped from YANG variable /network_instances/network_instance/tables/table/state/address_family (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address_family is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address_family() directly.

    YANG Description: The address family (IPv4, IPv6) of the table's entries
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-types:L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}},), is_leaf=True, yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address_family must be of a type compatible with identityref""",
          'defined-type': "openconfig-network-instance:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-types:L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}},), is_leaf=True, yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)""",
        })

    self.__address_family = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address_family(self):
    self.__address_family = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-types:L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'oc-types:MPLS': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:L2_ETHERNET': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'octypes:IPV6': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}, u'IPV4': {'@namespace': u'http://openconfig.net/yang/openconfig-types', '@module': u'openconfig-types'}},), is_leaf=True, yang_name="address-family", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=False)

  protocol = __builtin__.property(_get_protocol)
  address_family = __builtin__.property(_get_address_family)


  _pyangbind_elements = {'protocol': protocol, 'address_family': address_family, }


