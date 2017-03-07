#include "Sif.h"
SR_HAS_MODULE(Sif);
//Sif::Sif(sc_module_name nm) : sc_module(nm), sifTargSocket_("sifTargSocket")
Sif::Sif(ModuleName nm) : BaseModule<DefaultBase>(nm) , sifTargSocket_("sifTargSocket_")
{
	sifTargSocket_.register_b_transport(this, &Sif::b_transport);
	std::cout<<"Sif::b_transport()"<<std::endl;
}
void Sif::b_transport(tlm::tlm_generic_payload& trans, sc_core::sc_time& delay)
{
	std::cout<<"Sif::b_transport5()"<<std::endl;
} 