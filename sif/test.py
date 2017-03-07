# SOCROCKET TESTING FOR SYSTEM-C PYTHON INTERFACING
import usi
from sr_registry import module
from usi.sc_module import USIModule
# import sys
# import sr_registry
# from usi.tools import elf
# from usi.shell import start as shell_start

dir(usi.registry.api.load)
usi.registry.api.load('./build/sif/libsr_sif.so')

# class SfrProgrammer : public BaseModule<DefaultBase>
# //class SfrProgrammer : public BaseModule<tlmsocket>
# { 
	# public :
	# tlm_utils::simple_initiator_socket<SfrProgrammer, 32, tlm::tlm_base_protocol_types> sfrInitSocket_; 
	# SC_HAS_PROCESS(SfrProgrammer);
	# SfrProgrammer(ModuleName nm);
# //	SfrProgrammer(sc_module_name nm);
	# void startTransmission();
# };

# class Siftb(BaseSystem):
    # def __init__(self, name):
        # print " * Creating Siftb:"
        # super(BaseSystem, self).__init__(name)
        # self.cpu = module.Leon3("cpu", hindex = 1)
        # #self.cpu.cpu.historyEnabled.cci_write("true")
        # #self.cpu.gdb.cci_write("2000")
        # self.connect_cpu()

class BaseSystem(USIModule):
    def __init__(name):
            sif = module.Sif("sif")
            self.sfrprogrammer = module.SfrProgrammer("sfrprogrammer")
            self.sfrprogrammer.sfrInitSocket_.socket_bind(self.sif.sifTargSocket_)
    def start_of_simulation(self):
            if hasattr(self, '_rom'):
                    print self.rom
                    elf.load_elf_into_scireg(self._rom, self.rom, 0x00000000)
            if hasattr(self, '_ram'):
                    print self.ram
                    elf.load_elf_into_scireg(self._ram, self.ram, 0x40000000)
                    elf.load_elf_intrinsics_to_processor(self._ram, [self.cpu], elf.intrinsic_groups['standard'])

#basesystem = BaseSystem("basesystem")
# sif = module.Sif("sif")
# sfrprogrammer = module.SfrProgrammer("sfrprogrammer")
# sfrprogrammer.sfrInitSocket_.socket_bind(sif.sifTargSocket_)

#@usi.on("start_of_simulation")
# def simulation(*k, **kw):
        # print "3. Binding of Sockets_!!"
        # if hasattr(self, '_rom'):
                # print self.rom
                # elf.load_elf_into_scireg(self._rom, self.rom, 0x00000000)
        # if hasattr(self, '_ram'):
                # print self.ram
                # elf.load_elf_into_scireg(self._ram, self.ram, 0x40000000)
                # elf.load_elf_intrinsics_to_processor(self._ram, [self.cpu], elf.intrinsic_groups['standard'])
				
# @usi.on('start_of_initialization')
# def class_systems(*k, **kw):
    # siftb = Siftb("siftb")
# usi.report.set_filter_to_whitelist(True)