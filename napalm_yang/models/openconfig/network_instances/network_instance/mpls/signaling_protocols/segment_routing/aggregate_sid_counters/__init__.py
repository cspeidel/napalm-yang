
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

from . import aggregate_sid_counter
class aggregate_sid_counters(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/segment-routing/aggregate-sid-counters. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Per-SID counters aggregated across all interfaces on the local system
  """
  __slots__ = ('_path_helper', '_extmethods', '__aggregate_sid_counter',)

  _yang_name = 'aggregate-sid-counters'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__aggregate_sid_counter = YANGDynClass(base=YANGListType("mpls_label",aggregate_sid_counter.aggregate_sid_counter, yang_name="aggregate-sid-counter", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-label', extensions=None), is_container='list', yang_name="aggregate-sid-counter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'signaling-protocols', u'segment-routing', u'aggregate-sid-counters']

  def _get_aggregate_sid_counter(self):
    """
    Getter method for aggregate_sid_counter, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/aggregate_sid_counters/aggregate_sid_counter (list)

    YANG Description: Counters aggregated across all of the interfaces of the local
system corresponding to traffic received or forwarded with a
particular SID
    """
    return self.__aggregate_sid_counter
      
  def _set_aggregate_sid_counter(self, v, load=False):
    """
    Setter method for aggregate_sid_counter, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/aggregate_sid_counters/aggregate_sid_counter (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_aggregate_sid_counter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_aggregate_sid_counter() directly.

    YANG Description: Counters aggregated across all of the interfaces of the local
system corresponding to traffic received or forwarded with a
particular SID
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("mpls_label",aggregate_sid_counter.aggregate_sid_counter, yang_name="aggregate-sid-counter", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-label', extensions=None), is_container='list', yang_name="aggregate-sid-counter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """aggregate_sid_counter must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("mpls_label",aggregate_sid_counter.aggregate_sid_counter, yang_name="aggregate-sid-counter", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-label', extensions=None), is_container='list', yang_name="aggregate-sid-counter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__aggregate_sid_counter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_aggregate_sid_counter(self):
    self.__aggregate_sid_counter = YANGDynClass(base=YANGListType("mpls_label",aggregate_sid_counter.aggregate_sid_counter, yang_name="aggregate-sid-counter", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-label', extensions=None), is_container='list', yang_name="aggregate-sid-counter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  aggregate_sid_counter = __builtin__.property(_get_aggregate_sid_counter, _set_aggregate_sid_counter)


  _pyangbind_elements = {'aggregate_sid_counter': aggregate_sid_counter, }


from . import aggregate_sid_counter
class aggregate_sid_counters(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/segment-routing/aggregate-sid-counters. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Per-SID counters aggregated across all interfaces on the local system
  """
  __slots__ = ('_path_helper', '_extmethods', '__aggregate_sid_counter',)

  _yang_name = 'aggregate-sid-counters'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__aggregate_sid_counter = YANGDynClass(base=YANGListType("mpls_label",aggregate_sid_counter.aggregate_sid_counter, yang_name="aggregate-sid-counter", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-label', extensions=None), is_container='list', yang_name="aggregate-sid-counter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'signaling-protocols', u'segment-routing', u'aggregate-sid-counters']

  def _get_aggregate_sid_counter(self):
    """
    Getter method for aggregate_sid_counter, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/aggregate_sid_counters/aggregate_sid_counter (list)

    YANG Description: Counters aggregated across all of the interfaces of the local
system corresponding to traffic received or forwarded with a
particular SID
    """
    return self.__aggregate_sid_counter
      
  def _set_aggregate_sid_counter(self, v, load=False):
    """
    Setter method for aggregate_sid_counter, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/segment_routing/aggregate_sid_counters/aggregate_sid_counter (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_aggregate_sid_counter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_aggregate_sid_counter() directly.

    YANG Description: Counters aggregated across all of the interfaces of the local
system corresponding to traffic received or forwarded with a
particular SID
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("mpls_label",aggregate_sid_counter.aggregate_sid_counter, yang_name="aggregate-sid-counter", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-label', extensions=None), is_container='list', yang_name="aggregate-sid-counter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """aggregate_sid_counter must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("mpls_label",aggregate_sid_counter.aggregate_sid_counter, yang_name="aggregate-sid-counter", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-label', extensions=None), is_container='list', yang_name="aggregate-sid-counter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__aggregate_sid_counter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_aggregate_sid_counter(self):
    self.__aggregate_sid_counter = YANGDynClass(base=YANGListType("mpls_label",aggregate_sid_counter.aggregate_sid_counter, yang_name="aggregate-sid-counter", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mpls-label', extensions=None), is_container='list', yang_name="aggregate-sid-counter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  aggregate_sid_counter = __builtin__.property(_get_aggregate_sid_counter, _set_aggregate_sid_counter)


  _pyangbind_elements = {'aggregate_sid_counter': aggregate_sid_counter, }


