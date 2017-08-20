
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
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/subinterfaces/subinterface/ipv6/autoconf/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data 
  """
  __slots__ = ('_path_helper', '_extmethods', '__create_global_addresses','__create_temporary_addresses','__temporary_valid_lifetime','__temporary_preferred_lifetime',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__temporary_valid_lifetime = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(604800), is_leaf=True, yang_name="temporary-valid-lifetime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip-ext', defining_module='openconfig-if-ip-ext', yang_type='uint32', is_config=False)
    self.__temporary_preferred_lifetime = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(86400), is_leaf=True, yang_name="temporary-preferred-lifetime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip-ext', defining_module='openconfig-if-ip-ext', yang_type='uint32', is_config=False)
    self.__create_temporary_addresses = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="create-temporary-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip-ext', defining_module='openconfig-if-ip-ext', yang_type='boolean', is_config=False)
    self.__create_global_addresses = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="create-global-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip-ext', defining_module='openconfig-if-ip-ext', yang_type='boolean', is_config=False)

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
      return [u'interfaces', u'interface', u'subinterfaces', u'subinterface', u'ipv6', u'autoconf', u'state']

  def _get_create_global_addresses(self):
    """
    Getter method for create_global_addresses, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv6/autoconf/state/create_global_addresses (boolean)

    YANG Description: [adapted from IETF IP model RFC 7277]

If enabled, the host creates global addresses as
described in RFC 4862.
    """
    return self.__create_global_addresses
      
  def _set_create_global_addresses(self, v, load=False):
    """
    Setter method for create_global_addresses, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv6/autoconf/state/create_global_addresses (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_create_global_addresses is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_create_global_addresses() directly.

    YANG Description: [adapted from IETF IP model RFC 7277]

If enabled, the host creates global addresses as
described in RFC 4862.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="create-global-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip-ext', defining_module='openconfig-if-ip-ext', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """create_global_addresses must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="create-global-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip-ext', defining_module='openconfig-if-ip-ext', yang_type='boolean', is_config=False)""",
        })

    self.__create_global_addresses = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_create_global_addresses(self):
    self.__create_global_addresses = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="create-global-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip-ext', defining_module='openconfig-if-ip-ext', yang_type='boolean', is_config=False)


  def _get_create_temporary_addresses(self):
    """
    Getter method for create_temporary_addresses, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv6/autoconf/state/create_temporary_addresses (boolean)

    YANG Description: [adapted from IETF IP model RFC 7277]

If enabled, the host creates temporary addresses as
described in RFC 4941.
    """
    return self.__create_temporary_addresses
      
  def _set_create_temporary_addresses(self, v, load=False):
    """
    Setter method for create_temporary_addresses, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv6/autoconf/state/create_temporary_addresses (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_create_temporary_addresses is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_create_temporary_addresses() directly.

    YANG Description: [adapted from IETF IP model RFC 7277]

If enabled, the host creates temporary addresses as
described in RFC 4941.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="create-temporary-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip-ext', defining_module='openconfig-if-ip-ext', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """create_temporary_addresses must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="create-temporary-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip-ext', defining_module='openconfig-if-ip-ext', yang_type='boolean', is_config=False)""",
        })

    self.__create_temporary_addresses = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_create_temporary_addresses(self):
    self.__create_temporary_addresses = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="create-temporary-addresses", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip-ext', defining_module='openconfig-if-ip-ext', yang_type='boolean', is_config=False)


  def _get_temporary_valid_lifetime(self):
    """
    Getter method for temporary_valid_lifetime, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv6/autoconf/state/temporary_valid_lifetime (uint32)

    YANG Description: [adapted from IETF IP model RFC 7277]

The time period during which the temporary address
is valid.
    """
    return self.__temporary_valid_lifetime
      
  def _set_temporary_valid_lifetime(self, v, load=False):
    """
    Setter method for temporary_valid_lifetime, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv6/autoconf/state/temporary_valid_lifetime (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_temporary_valid_lifetime is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_temporary_valid_lifetime() directly.

    YANG Description: [adapted from IETF IP model RFC 7277]

The time period during which the temporary address
is valid.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(604800), is_leaf=True, yang_name="temporary-valid-lifetime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip-ext', defining_module='openconfig-if-ip-ext', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """temporary_valid_lifetime must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(604800), is_leaf=True, yang_name="temporary-valid-lifetime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip-ext', defining_module='openconfig-if-ip-ext', yang_type='uint32', is_config=False)""",
        })

    self.__temporary_valid_lifetime = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_temporary_valid_lifetime(self):
    self.__temporary_valid_lifetime = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(604800), is_leaf=True, yang_name="temporary-valid-lifetime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip-ext', defining_module='openconfig-if-ip-ext', yang_type='uint32', is_config=False)


  def _get_temporary_preferred_lifetime(self):
    """
    Getter method for temporary_preferred_lifetime, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv6/autoconf/state/temporary_preferred_lifetime (uint32)

    YANG Description: [adapted from IETF IP model RFC 7277]

The time period during which the temporary address is
preferred.
    """
    return self.__temporary_preferred_lifetime
      
  def _set_temporary_preferred_lifetime(self, v, load=False):
    """
    Setter method for temporary_preferred_lifetime, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv6/autoconf/state/temporary_preferred_lifetime (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_temporary_preferred_lifetime is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_temporary_preferred_lifetime() directly.

    YANG Description: [adapted from IETF IP model RFC 7277]

The time period during which the temporary address is
preferred.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(86400), is_leaf=True, yang_name="temporary-preferred-lifetime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip-ext', defining_module='openconfig-if-ip-ext', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """temporary_preferred_lifetime must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(86400), is_leaf=True, yang_name="temporary-preferred-lifetime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip-ext', defining_module='openconfig-if-ip-ext', yang_type='uint32', is_config=False)""",
        })

    self.__temporary_preferred_lifetime = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_temporary_preferred_lifetime(self):
    self.__temporary_preferred_lifetime = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(86400), is_leaf=True, yang_name="temporary-preferred-lifetime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip-ext', defining_module='openconfig-if-ip-ext', yang_type='uint32', is_config=False)

  create_global_addresses = __builtin__.property(_get_create_global_addresses)
  create_temporary_addresses = __builtin__.property(_get_create_temporary_addresses)
  temporary_valid_lifetime = __builtin__.property(_get_temporary_valid_lifetime)
  temporary_preferred_lifetime = __builtin__.property(_get_temporary_preferred_lifetime)


  _pyangbind_elements = {'create_global_addresses': create_global_addresses, 'create_temporary_addresses': create_temporary_addresses, 'temporary_valid_lifetime': temporary_valid_lifetime, 'temporary_preferred_lifetime': temporary_preferred_lifetime, }


