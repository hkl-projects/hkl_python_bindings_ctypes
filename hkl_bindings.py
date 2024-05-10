from ctypes import *
#from inspect import getmembers, isfunction

lib_hkl = cdll.LoadLibrary("/usr/local/lib/libhkl.so")
# or
lib_hkl = CDLL("/usr/local/lib/libhkl.so")
lib_hkl

detector = lib_hkl.hkl_detector_factory_new(lib_hkl.hkl_detector_type_get_type(0))
print(help(lib_hkl.hkl_factories))
factory = lib_hkl.hkl_factories()['K6C']
geometry = factory.create_new_geometry()



print(getmembers(lib_hkl, isfunction))
# doesnt work, returns empty list

# trying to see what functions are in this shared library instance
