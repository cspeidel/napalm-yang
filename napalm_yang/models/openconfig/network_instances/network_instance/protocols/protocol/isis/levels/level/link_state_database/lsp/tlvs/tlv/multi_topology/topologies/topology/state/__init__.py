
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/multi-topology/topologies/topology/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of IS multi-topology TLV 229.
  """
  __slots__ = ('_path_helper', '_extmethods', '__MT_ID','__attributes',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__MT_ID = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0 .. 4095']}), is_leaf=True, yang_name="MT-ID", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    self.__attributes = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ATTACHED': {}, u'OVERLOAD': {}},), is_leaf=True, yang_name="attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'multi-topology', u'topologies', u'topology', u'state']

  def _get_MT_ID(self):
    """
    Getter method for MT_ID, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/multi_topology/topologies/topology/state/MT_ID (uint16)

    YANG Description: Multi-topology ID.
    """
    return self.__MT_ID
      
  def _set_MT_ID(self, v, load=False):
    """
    Setter method for MT_ID, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/multi_topology/topologies/topology/state/MT_ID (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_MT_ID is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_MT_ID() directly.

    YANG Description: Multi-topology ID.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0 .. 4095']}), is_leaf=True, yang_name="MT-ID", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """MT_ID must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0 .. 4095']}), is_leaf=True, yang_name="MT-ID", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)""",
        })

    self.__MT_ID = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_MT_ID(self):
    self.__MT_ID = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0 .. 4095']}), is_leaf=True, yang_name="MT-ID", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)


  def _get_attributes(self):
    """
    Getter method for attributes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/multi_topology/topologies/topology/state/attributes (enumeration)

    YANG Description: Attributes of the LSP for the associated topology.
    """
    return self.__attributes
      
  def _set_attributes(self, v, load=False):
    """
    Setter method for attributes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/multi_topology/topologies/topology/state/attributes (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attributes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attributes() directly.

    YANG Description: Attributes of the LSP for the associated topology.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ATTACHED': {}, u'OVERLOAD': {}},), is_leaf=True, yang_name="attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attributes must be of a type compatible with enumeration""",
          'defined-type': "openconfig-network-instance:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ATTACHED': {}, u'OVERLOAD': {}},), is_leaf=True, yang_name="attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)""",
        })

    self.__attributes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attributes(self):
    self.__attributes = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ATTACHED': {}, u'OVERLOAD': {}},), is_leaf=True, yang_name="attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)

  MT_ID = __builtin__.property(_get_MT_ID)
  attributes = __builtin__.property(_get_attributes)


  _pyangbind_elements = {'MT_ID': MT_ID, 'attributes': attributes, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/multi-topology/topologies/topology/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of IS multi-topology TLV 229.
  """
  __slots__ = ('_path_helper', '_extmethods', '__MT_ID','__attributes',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__MT_ID = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0 .. 4095']}), is_leaf=True, yang_name="MT-ID", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    self.__attributes = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ATTACHED': {}, u'OVERLOAD': {}},), is_leaf=True, yang_name="attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'multi-topology', u'topologies', u'topology', u'state']

  def _get_MT_ID(self):
    """
    Getter method for MT_ID, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/multi_topology/topologies/topology/state/MT_ID (uint16)

    YANG Description: Multi-topology ID.
    """
    return self.__MT_ID
      
  def _set_MT_ID(self, v, load=False):
    """
    Setter method for MT_ID, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/multi_topology/topologies/topology/state/MT_ID (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_MT_ID is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_MT_ID() directly.

    YANG Description: Multi-topology ID.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0 .. 4095']}), is_leaf=True, yang_name="MT-ID", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """MT_ID must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0 .. 4095']}), is_leaf=True, yang_name="MT-ID", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)""",
        })

    self.__MT_ID = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_MT_ID(self):
    self.__MT_ID = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0 .. 4095']}), is_leaf=True, yang_name="MT-ID", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)


  def _get_attributes(self):
    """
    Getter method for attributes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/multi_topology/topologies/topology/state/attributes (enumeration)

    YANG Description: Attributes of the LSP for the associated topology.
    """
    return self.__attributes
      
  def _set_attributes(self, v, load=False):
    """
    Setter method for attributes, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/multi_topology/topologies/topology/state/attributes (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attributes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attributes() directly.

    YANG Description: Attributes of the LSP for the associated topology.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ATTACHED': {}, u'OVERLOAD': {}},), is_leaf=True, yang_name="attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attributes must be of a type compatible with enumeration""",
          'defined-type': "openconfig-network-instance:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ATTACHED': {}, u'OVERLOAD': {}},), is_leaf=True, yang_name="attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)""",
        })

    self.__attributes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attributes(self):
    self.__attributes = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ATTACHED': {}, u'OVERLOAD': {}},), is_leaf=True, yang_name="attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)

  MT_ID = __builtin__.property(_get_MT_ID)
  attributes = __builtin__.property(_get_attributes)


  _pyangbind_elements = {'MT_ID': MT_ID, 'attributes': attributes, }


