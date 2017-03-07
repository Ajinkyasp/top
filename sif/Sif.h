#ifndef  SIF_H
#define  SIF_H
#include "core/common/base.h"
#include "tlm_utils/simple_target_socket.h"
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
//class Sif: public sc_core::sc_module
class Sif : public BaseModule<DefaultBase>
//class Sif : public BaseModule<tlmsocket>
{
	public :
	tlm_utils::simple_target_socket<Sif, 32, tlm::tlm_base_protocol_types> sifTargSocket_;	
	SC_HAS_PROCESS(Sif);	
	Sif(ModuleName nm);
//	Sif(sc_module_name nm);
	virtual void b_transport(tlm::tlm_generic_payload& trans, sc_core::sc_time& delay);
};

#endif
