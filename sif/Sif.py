import sys
import usi
import sr_registry
#from usi.registry import module
from usi.shell import start as shell_start
#from usi.systemc import NS as SC_NS
from sr_registry import module
#from sr_registry import USIDelegateBase
from usi.sc_module import USIModule
from usi.tools import elf
#from sr_register import scireg
#from sif import Sif
#import sif

dir(usi.registry.api.load)
usi.registry.api.load('./build/sif/libsr_sif.so')

class BaseSystem(USIModule):
	print "1. Binding of Sockets"
	def __init__(self,name):
		self.initiator = module.Initiator("initiator")
#		print self.sif

		# self.sfrprogrammer = module.SfrProgrammer("sfrprogrammer")
# #		print self.sfrprogrammer, self.sfrprogrammer.sfrInitSocket_

# #		self.sfrprogrammer.sfrInitSocket_.bind(self.sif.sifTargSocket_)
		# self.sfrprogrammer.sfrInitSocket_.socket_bind(self.sif.sifTargSocket_)
		print "2. Binding of Sockets_!"
	def start_of_simulation(self):
		print "3. Binding of Sockets_!!"
		if hasattr(self, '_rom'):
			print self.rom
			elf.load_elf_into_scireg(self._rom, self.rom, 0x00000000)
		if hasattr(self, '_ram'):
			print self.ram
			elf.load_elf_into_scireg(self._ram, self.ram, 0x40000000)
            #if self.use_intrinsics:
			elf.load_elf_intrinsics_to_processor(self._ram, [self.cpu], elf.intrinsic_groups['standard'])
        #shell_start()

basesystem = BaseSystem("basesystem")

#@usi.on('start_of_initialization')


usi.report.set_filter_to_whitelist(True)