
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

from . import state
from . import unknown_subtlv
from . import unreserved_bandwidths
from . import administrative_groups
class sub_tlv(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/traffic-engineering/tlvs/tlv/link/sub-tlvs/sub-tlv. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The Sub-TLVs included within the Traffic Engineering
LSA's sub-TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__state','__unknown_subtlv','__unreserved_bandwidths','__administrative_groups',)

  _yang_name = 'sub-tlv'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__unreserved_bandwidths = YANGDynClass(base=unreserved_bandwidths.unreserved_bandwidths, is_container='container', yang_name="unreserved-bandwidths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__unknown_subtlv = YANGDynClass(base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__administrative_groups = YANGDynClass(base=administrative_groups.administrative_groups, is_container='container', yang_name="administrative-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'opaque-lsa', u'traffic-engineering', u'tlvs', u'tlv', u'link', u'sub-tlvs', u'sub-tlv']

  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/state (container)

    YANG Description: State parameters of the Link Sub-TLV
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters of the Link Sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_unknown_subtlv(self):
    """
    Getter method for unknown_subtlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/unknown_subtlv (container)

    YANG Description: An unknown SubTLV within the context. Unknown Sub-TLV
are defined to be the set of SubTLVs that are not modelled
by the OpenConfig schema, or are unknown to the local system
such that it cannot decode their value.
    """
    return self.__unknown_subtlv
      
  def _set_unknown_subtlv(self, v, load=False):
    """
    Setter method for unknown_subtlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/unknown_subtlv (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unknown_subtlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unknown_subtlv() directly.

    YANG Description: An unknown SubTLV within the context. Unknown Sub-TLV
are defined to be the set of SubTLVs that are not modelled
by the OpenConfig schema, or are unknown to the local system
such that it cannot decode their value.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unknown_subtlv must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__unknown_subtlv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unknown_subtlv(self):
    self.__unknown_subtlv = YANGDynClass(base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_unreserved_bandwidths(self):
    """
    Getter method for unreserved_bandwidths, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/unreserved_bandwidths (container)

    YANG Description: The unreserved link bandwidths for the Traffic
Engineering LSA - utilised when the sub-TLV type
indicates that the sub-TLV describes unreserved
bandwidth
    """
    return self.__unreserved_bandwidths
      
  def _set_unreserved_bandwidths(self, v, load=False):
    """
    Setter method for unreserved_bandwidths, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/unreserved_bandwidths (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unreserved_bandwidths is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unreserved_bandwidths() directly.

    YANG Description: The unreserved link bandwidths for the Traffic
Engineering LSA - utilised when the sub-TLV type
indicates that the sub-TLV describes unreserved
bandwidth
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unreserved_bandwidths.unreserved_bandwidths, is_container='container', yang_name="unreserved-bandwidths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unreserved_bandwidths must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=unreserved_bandwidths.unreserved_bandwidths, is_container='container', yang_name="unreserved-bandwidths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__unreserved_bandwidths = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unreserved_bandwidths(self):
    self.__unreserved_bandwidths = YANGDynClass(base=unreserved_bandwidths.unreserved_bandwidths, is_container='container', yang_name="unreserved-bandwidths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_administrative_groups(self):
    """
    Getter method for administrative_groups, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/administrative_groups (container)

    YANG Description: The administrative groups that are set for the
Traffic Engineering LSA - utilised when the sub-TLV type
indicates that the sub-TLV describes administrative
groups
    """
    return self.__administrative_groups
      
  def _set_administrative_groups(self, v, load=False):
    """
    Setter method for administrative_groups, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/administrative_groups (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_administrative_groups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_administrative_groups() directly.

    YANG Description: The administrative groups that are set for the
Traffic Engineering LSA - utilised when the sub-TLV type
indicates that the sub-TLV describes administrative
groups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=administrative_groups.administrative_groups, is_container='container', yang_name="administrative-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """administrative_groups must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=administrative_groups.administrative_groups, is_container='container', yang_name="administrative-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__administrative_groups = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_administrative_groups(self):
    self.__administrative_groups = YANGDynClass(base=administrative_groups.administrative_groups, is_container='container', yang_name="administrative-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  state = __builtin__.property(_get_state)
  unknown_subtlv = __builtin__.property(_get_unknown_subtlv)
  unreserved_bandwidths = __builtin__.property(_get_unreserved_bandwidths)
  administrative_groups = __builtin__.property(_get_administrative_groups)


  _pyangbind_elements = {'state': state, 'unknown_subtlv': unknown_subtlv, 'unreserved_bandwidths': unreserved_bandwidths, 'administrative_groups': administrative_groups, }


from . import state
from . import unknown_subtlv
from . import unreserved_bandwidths
from . import administrative_groups
class sub_tlv(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/traffic-engineering/tlvs/tlv/link/sub-tlvs/sub-tlv. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The Sub-TLVs included within the Traffic Engineering
LSA's sub-TLV
  """
  __slots__ = ('_path_helper', '_extmethods', '__state','__unknown_subtlv','__unreserved_bandwidths','__administrative_groups',)

  _yang_name = 'sub-tlv'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__unreserved_bandwidths = YANGDynClass(base=unreserved_bandwidths.unreserved_bandwidths, is_container='container', yang_name="unreserved-bandwidths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__unknown_subtlv = YANGDynClass(base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    self.__administrative_groups = YANGDynClass(base=administrative_groups.administrative_groups, is_container='container', yang_name="administrative-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types', u'lsa-type', u'lsas', u'lsa', u'opaque-lsa', u'traffic-engineering', u'tlvs', u'tlv', u'link', u'sub-tlvs', u'sub-tlv']

  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/state (container)

    YANG Description: State parameters of the Link Sub-TLV
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters of the Link Sub-TLV
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_unknown_subtlv(self):
    """
    Getter method for unknown_subtlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/unknown_subtlv (container)

    YANG Description: An unknown SubTLV within the context. Unknown Sub-TLV
are defined to be the set of SubTLVs that are not modelled
by the OpenConfig schema, or are unknown to the local system
such that it cannot decode their value.
    """
    return self.__unknown_subtlv
      
  def _set_unknown_subtlv(self, v, load=False):
    """
    Setter method for unknown_subtlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/unknown_subtlv (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unknown_subtlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unknown_subtlv() directly.

    YANG Description: An unknown SubTLV within the context. Unknown Sub-TLV
are defined to be the set of SubTLVs that are not modelled
by the OpenConfig schema, or are unknown to the local system
such that it cannot decode their value.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unknown_subtlv must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__unknown_subtlv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unknown_subtlv(self):
    self.__unknown_subtlv = YANGDynClass(base=unknown_subtlv.unknown_subtlv, is_container='container', yang_name="unknown-subtlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_unreserved_bandwidths(self):
    """
    Getter method for unreserved_bandwidths, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/unreserved_bandwidths (container)

    YANG Description: The unreserved link bandwidths for the Traffic
Engineering LSA - utilised when the sub-TLV type
indicates that the sub-TLV describes unreserved
bandwidth
    """
    return self.__unreserved_bandwidths
      
  def _set_unreserved_bandwidths(self, v, load=False):
    """
    Setter method for unreserved_bandwidths, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/unreserved_bandwidths (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unreserved_bandwidths is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unreserved_bandwidths() directly.

    YANG Description: The unreserved link bandwidths for the Traffic
Engineering LSA - utilised when the sub-TLV type
indicates that the sub-TLV describes unreserved
bandwidth
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unreserved_bandwidths.unreserved_bandwidths, is_container='container', yang_name="unreserved-bandwidths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """unreserved_bandwidths must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=unreserved_bandwidths.unreserved_bandwidths, is_container='container', yang_name="unreserved-bandwidths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__unreserved_bandwidths = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_unreserved_bandwidths(self):
    self.__unreserved_bandwidths = YANGDynClass(base=unreserved_bandwidths.unreserved_bandwidths, is_container='container', yang_name="unreserved-bandwidths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)


  def _get_administrative_groups(self):
    """
    Getter method for administrative_groups, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/administrative_groups (container)

    YANG Description: The administrative groups that are set for the
Traffic Engineering LSA - utilised when the sub-TLV type
indicates that the sub-TLV describes administrative
groups
    """
    return self.__administrative_groups
      
  def _set_administrative_groups(self, v, load=False):
    """
    Setter method for administrative_groups, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/traffic_engineering/tlvs/tlv/link/sub_tlvs/sub_tlv/administrative_groups (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_administrative_groups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_administrative_groups() directly.

    YANG Description: The administrative groups that are set for the
Traffic Engineering LSA - utilised when the sub-TLV type
indicates that the sub-TLV describes administrative
groups
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=administrative_groups.administrative_groups, is_container='container', yang_name="administrative-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """administrative_groups must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=administrative_groups.administrative_groups, is_container='container', yang_name="administrative-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
        })

    self.__administrative_groups = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_administrative_groups(self):
    self.__administrative_groups = YANGDynClass(base=administrative_groups.administrative_groups, is_container='container', yang_name="administrative-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)

  state = __builtin__.property(_get_state)
  unknown_subtlv = __builtin__.property(_get_unknown_subtlv)
  unreserved_bandwidths = __builtin__.property(_get_unreserved_bandwidths)
  administrative_groups = __builtin__.property(_get_administrative_groups)


  _pyangbind_elements = {'state': state, 'unknown_subtlv': unknown_subtlv, 'unreserved_bandwidths': unreserved_bandwidths, 'administrative_groups': administrative_groups, }


