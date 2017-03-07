#include "tlm_utils/simple_initiator_socket.h"
using namespace sc_core;
class SfrProgrammer: public sc_core::sc_module 
{ 
	public :
	tlm_utils::simple_initiator_socket<SfrProgrammer, 32, tlm::tlm_base_protocol_types> sfrInitSocket_; 
	SC_HAS_PROCESS(SfrProgrammer);
	SfrProgrammer(sc_module_name nm): sc_module(nm), sfrInitSocket_("sfrInitSocket")
	{
		SC_THREAD(startTransmission);
	}
	void startTransmission()
	{
		cout<<"Transmission Started"<<endl;
		wait();
	}
};


