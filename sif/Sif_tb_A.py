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

dir(usi.registry.api.load)
usi.registry.api.load('./build/sif/libsr_sif.so')

class SifTb(USIModule):
	
	def __init__(self, name):
		print "TEST"
		self.usitlmtargetsocket = tlmsocket.USITLMTargetSocket("usitlmtargetsocket")
		# self.usitlminitiatorsocket = tlmsocket.USITLMInitiatorSocket("usitlminitiatorsocket")
		print "\n"
		
class SifTop(USIModule):
    def __init__(self, name):
		self.sfrprogrammer = module.SfrProgrammer("sfrprogrammer")
		# self.sif = module.Sif("sif")
		self.sifTb = SifTb("siftb")
		
		self.sfrprogrammer.sfrInitSocket_.socket_bind(self.sifTb.usitlmtargetsocket)
		# self.sifTb.usitlminitiatorsocket.socket_bind(self.sif.sifTargSocket_)
		print "\n>>>>>Final Binding of Sockets_!<<<<<\n"
		
sifTop = SifTop("Top");

#@usi.on('start_of_initialization')


usi.report.set_filter_to_whitelist(True)