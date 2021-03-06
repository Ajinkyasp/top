"""
    Exposes all registerd module as Python Functions (Constructors)
    This serves as hidden factory because it will look like this module
    magicaly imports all module classes.

    Example:
    >>> import sr_registry
    >>> ahbctrl = sr_registry.module.AHBCtrl("ahbctrl",
    >>>               rrobin=True
    >>>           )
    >>> print ahbctrl.generics.rrobin.get()
    >>> ahbctrl.ahbOUT(apbctrl.ahb)

    Or write a service class for a sc_module:
    >>> '''In gaisler/ahbctrl/ahbctrl.py'''
    >>> from sr_registry import USIDelegateBase
    >>> 
    >>> class AHBCtrl(USIDelegateBase):
    >>>     # Defining the sr_registry category in which AHBCtrl is registered
    >>>     self.__usi_group__ = 'module'
    >>>     # Defining the sc_module name
    >>>     self.__usi_class__ = 'AHBCtrl'
    >>> 
    >>>     def __init__(self, *k, **kw):
    >>>         '''Calling the C++ constructor'''
    >>>         super(AHBCtrl, self).__init__(*k, **kw)
    >>>     def print_slaves(self):
    >>>         '''An external service function which will be attached to any object of the systemc type AHBCtrl.'''
    >>>         print 'dooo'

    To use like:
    >>> from gaisler.ahbctrl.ahbctrl import AHBCtrl
    >>> ahbctrl = AHBCtrl("ahbctrl",
    >>>               rrobin=True
    >>>           )
    >>> print ahbctrl.generics.rrobin.get()
    >>> ahbctrl.ahbOUT(apbctrl.ahb)
"""
def create_module(__name__):
    """
    This function holds all module interna.
    This Python module has dynamic content.
    """
    from builtins import object
    from . import sr_registry as api
    from usi import sc_object
    import abc
    import sys
    print "1. Start"
    def delegate_new(cls, instance, *args, **kw):
        """
        __new__ Method for USIDelegates. Calls undelying C++ constructors and populates CCI parameters.
        Do not call directly. Use USIDelegateMeta.
        """
        obj = api.create_object_by_name(cls.__usi_group__, cls.__usi_class__, instance)
        print "1a. Start"
        if hasattr(obj, 'generics'):
            generics = getattr(obj, 'generics')
            for key, val in kw.items():
                param = generics
                path = key.split("__")
                try:
                    for part in path:
                        param = getattr(param, part)
                    param.cci_write(str(val))
                except AttributeError as e:
                    ei = sys.exc_info()
                    raise AttributeError("""USIDelegate '%s', '%s' has no generic '%s'""" % (cls.__name__, instance, key)), None, ei[2].tb_next
        return obj
    print "1b. Start"
    class USIDelegateMeta(abc.ABCMeta):
        """
        Abstract base meta class for USIDelegates.
        This meta class allows to create SystemC Object like real Python objects by including this Module and instantiating a object from a coresponding class.
        Furthermore allowing the programmer to define a USIDelegateBase class for each SystemC Class which can declare additional Python members accassable in each instance of the class.
        """
        print "1c. Start"
        def __init__(cls, name, bases, nmspc):
		    print "1d. Start"
            if cls.__usi_class__ != "":
			    print "1e. Start"
                for item_name, item in cls.__dict__.items():
                    if not item_name.startswith("_"):
                        sc_object.attach("{}.{}".format(cls.__usi_group__, cls.__usi_class__), item_name, item)
                        print "1f. Start"
            super(USIDelegateMeta, cls).__init__(name, bases, nmspc)
            cls.__new__ = staticmethod(delegate_new)
        def __instancecheck__(cls, instance):
            return api.is_type(cls.__usi_group__, cls.__usi_class__, instance)
			print "1f. Start"
        print "1g. Start"
    if sys.version_info >= (3,3):
        #class USIDelegateBase(metaclass=USIDelegateMeta):
        #    self.__usi_group__ = ""
        #    self.__usi_class__ = ""
        pass
    else:
        class USIDelegateBase(object):
            """
            Abstract Base Class to attach additional Python members to SystemC Classes.
            """
            __metaclass__ = USIDelegateMeta
            __usi_group__ = ""
            __usi_class__ = ""

    class SubModule(object):
        def __init__(self, group):
            self.group = group

        def __dir__(self):
            return list(str(name) for name in api.get_module_names(self.group))+self.__dict__.keys()

        def __getattr__(self, klass):
            if klass in self.__dict__:
                return self.__dict__[group]
            elif klass in list(api.get_module_names(self.group)):
                if sys.version_info >= (3,3):
                    import types
                    return types.new_class(klass, (), {
                        'metaclass': USIDelegateMeta,
                        '__usi_group__': self.group,
                        '__usi_class__': klass
                    })
                else:
                    return USIDelegateMeta(klass, (), {
                        '__usi_group__': self.group,
                        '__usi_class__': klass
                    })
            else:
                return None

    class Module(object):
        def __init__(self, name):
            global __name__
            self.__name__ = __name__ = name
            self.__submodules__ = {}
            self.USIDelegateMeta = USIDelegateMeta
            self.USIDelegateBase = USIDelegateBase
            self.api = api

        def __dir__(self):
            return list(tuple(api.get_group_names())+tuple(self.__dict__.keys()))

        def __getattr__(self, group):
            if group in self.__dict__:
                return self.__dict__[group]
            elif group in list(api.get_group_names()):
                return self.__submodules__.setdefault(group, SubModule(group))
            else:
                return None
        def add_class_to_submodule(self, group, name, cls):
            submodule = self.__submodules__.setdefault(group, SubModule(group))
            submodule.__dict__[name] = cls

    return Module(__name__)

import sys
sys.modules[__name__] = create_module(__name__)
