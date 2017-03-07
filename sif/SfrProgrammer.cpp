#include "SfrProgrammer.h"
SR_HAS_MODULE(SfrProgrammer);
//SfrProgrammer::SfrProgrammer(sc_module_name nm): sc_module(nm), sfrInitSocket_("sfrInitSocket")
SfrProgrammer::SfrProgrammer(ModuleName nm) : BaseModule<DefaultBase>(nm) , sfrInitSocket_("sfrInitSocket_")
{
	SC_THREAD(startTransmission);
}
void SfrProgrammer::startTransmission()
{
  while (1)
  {
    wait(20, SC_NS);
    cout << "\n\nThread: Transmission Started at\t" << sc_time_stamp() <<"\n\n" << endl;
    break;
  }
}
