# SOCROCKET TESTING FOR SYSTEM-C PYTHON INTERFACING

import sys
import usi
import sr_registry
from usi.shell import start as shell_start
from sr_registry import module
from usi.sc_module import USIModule
from usi.tools import elf
#from usi.registry import module
#from usi.systemc import NS as SC_NS
#from sr_registry import USIDelegateBase
#from sr_register import scireg
#from sif import Sif
#import sif
from usi.api import tlmsocket

# dir(usi.registry.api.load)
# usi.registry.api.load('./build/sif/libsr_sif.so')

class SifTb(USIModule):
	
	def __init__(self, name):
		print "TEST"
		self.usitlminitiatorsocket = tlmsocket.USITLMInitiatorSocket("usitlminitiatorsocket")
		print "\n>>>>>Instance of USITLMInitiatorSocket!<<<<<\n"
		self.usitlminitiatorsocket_ = tlmsocket.USITLMInitiatorSocket("usitlminitiatorsocket_")
		print "\n>>>>>Instance of USITLMTargetSocket!<<<<<\n"
		self.targetsocket_ = tlmsocket.USITLMTargetSocket("targetsocket_")
		# self.usitlminitiatorsocket.iscb_320 = None
		# TLMSocketCheck = self.usitlminitiatorsocket.iscb_320
		# print "\n", self.usitlminitiatorsocket, dir(self.usitlminitiatorsocket)
		# print TLMSocketCheck
		print "\n"
		
class SifTop(USIModule):
    def __init__(self,name):
		self.sif = module.Sif("sif")
		self.sifTb = SifTb("siftb")
		self.sfrprogrammer = module.SfrProgrammer("sfrprogrammer")

		self.sifTb.usitlminitiatorsocket.socket_bind(self.sif.sifTargSocket_)
		print "\n>>>>>First Binding of Sockets_!<<<<<\n"
		
		# self.sifTb.usitlminitiatorsocket.socket_bind(self.sfrprogrammer.sfrInitSocket_)
		# print "\n>>>>>Second Binding of Sockets_!<<<<<\n"
		
		# self.sfrprogrammer.sfrInitSocket_.socket_bind(self.sifTb.targetsocket_)
		# print "\n>>>>>Third Binding of Sockets_!<<<<<\n"
		
		# self.sifTb.usitlmtargetsocket_.socket_bind(self.sfrprogrammer.sfrInitSocket_)
		# print "\n>>>>>Test Binding of Sockets_!<<<<<\n"
		
		# self.sfrprogrammer.sfrInitSocket_.socket_bind(self.sifTb.usitlminitiatorsocket)
		# print "\n>>>>>Fourth Binding of Sockets_!<<<<<\n"
		
		# self.sifTb.usitlminitiatorsocket_.socket_bind(self.sif.sifTargSocket_)
		# print "\n>>>>>Final Binding of Sockets_!<<<<<\n"
		
#class BaseSystem(USIModule):
#	print "\n\n<<<<<-----INSIDE BaseSystem USIModule----->>>>>"
#	# USITLMInitiatorSocket.iscb320 TLMSocketCheck
#	siftb = sifTb("siftb")
#	def __init__(self,name):
#		self.sif = module.Sif("sif")
##		print self.sif
#
#		self.sfrprogrammer = module.SfrProgrammer("sfrprogrammer")
##		print self.sfrprogrammer, self.sfrprogrammer.sfrInitSocket_
#
#		self.sfrprogrammer.sfrInitSocket_.socket_bind(self.sif.sifTargSocket_)
#		print "\n>>>>>Final Binding of Sockets_!<<<<<\n"
#		print "\n"
#		# print self.siftb.TLMSocketCheck
#		print "\n"
#		# self.siftb.TLMSocketCheck.socket_bind(self.sif.sifTargSocket_)
#		print "\n>>>>>_____->->->->->->->->->->->->->->NEW Binding of Sockets_!<<<<<\n"
#
#	# def start_of_simulation(self):
#		# print "Inside of >>>>>>>>>>>>>>>>>>>>>> start_of_simulation!!"
#		# if hasattr(self, '_rom'):
#			# print self.rom
#			# elf.load_elf_into_scireg(self._rom, self.rom, 0x00000000)
#		# if hasattr(self, '_ram'):
#			# print self.ram
#			# elf.load_elf_into_scireg(self._ram, self.ram, 0x40000000)
#            # #if self.use_intrinsics:
#			# elf.load_elf_intrinsics_to_processor(self._ram, [self.cpu], elf.intrinsic_groups['standard'])
#        # #shell_start()

#siftb = sifTb("siftb")
#basesystem = BaseSystem("basesystem")

sifTop = SifTop("Top");

#@usi.on('start_of_initialization')


usi.report.set_filter_to_whitelist(True)