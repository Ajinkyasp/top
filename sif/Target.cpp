#include "tlm_utils/simple_target_socket.h"
using namespace sc_core;

class Sif: public sc_core::sc_module
{
	public :
	tlm_utils::simple_target_socket<Sif, 32, tlm::tlm_base_protocol_types> sifTargSocket_;
	SC_HAS_PROCESS(Sif);
	Sif(sc_module_name nm) : sc_module(nm), sifTargSocket_("sifTargSocket")
	{
		sifTargSocket_.register_b_transport(this, &Sif::b_transport);
		std::cout<<"Sif::b_transport()"<<std::endl;
	}
	virtual void b_transport(tlm::tlm_generic_payload& trans, sc_core::sc_time& delay)
	{
		std::cout<<"Sif::b_transport7()"<<std::endl;
	} 
};

