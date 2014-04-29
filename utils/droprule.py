import pf

class DropRule(pf.PFRule):

    def __init__(self, **kw):
        
	d = {"action":pf.PF_DROP, "af":socket.AF_INET, "proto":socket.IPPROTO_TCP, "flags":"S", "flagset":"SA","keep_state":pf.PF_STATE_NORMAL}
	d.update(kw)
	super(PassRule,self).__init__(**d)


