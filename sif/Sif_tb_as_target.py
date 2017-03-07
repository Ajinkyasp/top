# SOCROCKET TESTING FOR SYSTEM-C PYTHON INTERFACING

import sys
import usi
import sr_registry
from usi.shell import start as shell_start
from sr_registry import module
from usi.sc_module import USIModule
from usi.tools import elf
from usi.api import tlmsocket

# class testModule():
	# def __init__(self,name):
		# self.nm = name

# class sifTb(USIModule):
	# def __init__(self, name):
		# print "TEST"
		# self.tlmSocket = create_tlm_inititor_socket
		# self.usitlmtargetsocket = tlmsocket.USITLMTargetSocket("usitlmtargetsocket", )
		# print "", self.usitlmtargetsocket

class BaseSystem(USIModule):
	
	def __init__(self,name):
		# self.sif = module.Sif("sif")
		self.initiator = module.Initiator("initiator")
		# self.siftb = sifTb("siftb")
		#self.initiator.sfrInitSocket_.socket_bind(self.siftb.usitlmtargetsocket)
		# self.testObj = testModule("testModule")
		#sc_module_(sc_core::sc_module_name mn, PyObject *cls, PyObject *args, PyObject *kw):
		# self.testScObj = usi.create_sc_module("TestObjSc",self.testObj)
		print "Just a casual print"		
		# print "name", self.testScObj.name()

		


# siftb = sifTb("siftb")

basesystem = BaseSystem("basesystem")

usi.report.set_filter_to_whitelist(True)