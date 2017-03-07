#ifndef  SFR_PROGRAMMER_H
#define  SFR_PROGRAMMER_H
#include "core/common/base.h"
#include "tlm_utils/simple_initiator_socket.h"
#include <stdint.h>
#include "core/common/sr_param.h"
#include <tlm.h>
#include <map>
#include "core/common/sr_registry.h"
#include "core/common/clkdevice.h"
#include "core/common/sr_signal.h"
//#include "core/common/msclogger.h"
#include "core/common/socrocket.h"
#include ".waf/playground/dynamic_headers/src/module.h"
#include "usi.h"

using namespace sc_core;
//class SfrProgrammer: public sc_core::sc_module
class SfrProgrammer : public BaseModule<DefaultBase>
//class SfrProgrammer : public BaseModule<tlmsocket>
{ 
	public :
	tlm_utils::simple_initiator_socket<SfrProgrammer, 32, tlm::tlm_base_protocol_types> sfrInitSocket_; 
	SC_HAS_PROCESS(SfrProgrammer);
	SfrProgrammer(ModuleName nm);
//	SfrProgrammer(sc_module_name nm);
	void startTransmission();
};

#endif
