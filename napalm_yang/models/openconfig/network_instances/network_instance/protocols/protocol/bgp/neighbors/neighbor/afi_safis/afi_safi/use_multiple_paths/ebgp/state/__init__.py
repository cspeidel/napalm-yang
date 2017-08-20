
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/use-multiple-paths/ebgp/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to eBGP multipath
  """
  __slots__ = ('_path_helper', '_extmethods', '__allow_multiple_as',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__allow_multiple_as = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="allow-multiple-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'neighbors', u'neighbor', u'afi-safis', u'afi-safi', u'use-multiple-paths', u'ebgp', u'state']

  def _get_allow_multiple_as(self):
    """
    Getter method for allow_multiple_as, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/afi_safis/afi_safi/use_multiple_paths/ebgp/state/allow_multiple_as (boolean)

    YANG Description: Allow multipath to use paths from different neighbouring
ASes.  The default is to only consider multiple paths from
the same neighbouring AS.
    """
    return self.__allow_multiple_as
      
  def _set_allow_multiple_as(self, v, load=False):
    """
    Setter method for allow_multiple_as, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/afi_safis/afi_safi/use_multiple_paths/ebgp/state/allow_multiple_as (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_allow_multiple_as is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_allow_multiple_as() directly.

    YANG Description: Allow multipath to use paths from different neighbouring
ASes.  The default is to only consider multiple paths from
the same neighbouring AS.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="allow-multiple-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """allow_multiple_as must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="allow-multiple-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__allow_multiple_as = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_allow_multiple_as(self):
    self.__allow_multiple_as = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="allow-multiple-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

  allow_multiple_as = __builtin__.property(_get_allow_multiple_as)


  _pyangbind_elements = {'allow_multiple_as': allow_multiple_as, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/use-multiple-paths/ebgp/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to eBGP multipath
  """
  __slots__ = ('_path_helper', '_extmethods', '__allow_multiple_as',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__allow_multiple_as = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="allow-multiple-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'neighbors', u'neighbor', u'afi-safis', u'afi-safi', u'use-multiple-paths', u'ebgp', u'state']

  def _get_allow_multiple_as(self):
    """
    Getter method for allow_multiple_as, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/afi_safis/afi_safi/use_multiple_paths/ebgp/state/allow_multiple_as (boolean)

    YANG Description: Allow multipath to use paths from different neighbouring
ASes.  The default is to only consider multiple paths from
the same neighbouring AS.
    """
    return self.__allow_multiple_as
      
  def _set_allow_multiple_as(self, v, load=False):
    """
    Setter method for allow_multiple_as, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/afi_safis/afi_safi/use_multiple_paths/ebgp/state/allow_multiple_as (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_allow_multiple_as is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_allow_multiple_as() directly.

    YANG Description: Allow multipath to use paths from different neighbouring
ASes.  The default is to only consider multiple paths from
the same neighbouring AS.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="allow-multiple-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """allow_multiple_as must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="allow-multiple-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__allow_multiple_as = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_allow_multiple_as(self):
    self.__allow_multiple_as = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="allow-multiple-as", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

  allow_multiple_as = __builtin__.property(_get_allow_multiple_as)


  _pyangbind_elements = {'allow_multiple_as': allow_multiple_as, }


