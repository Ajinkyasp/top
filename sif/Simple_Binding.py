# SOCROCKET TESTING FOR SYSTEM-C PYTHON INTERFACING

# import usi
# import sr_registry

from sr_registry import module

print dir(module)
sif = module.Sif("sif")
sfrprogrammer = module.SfrProgrammer("sfrprogrammer")
sfrprogrammer.sfrInitSocket_.socket_bind(sif.sifTargSocket_)
