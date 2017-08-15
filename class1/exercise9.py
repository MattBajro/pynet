
from ciscoconfparse import CiscoConfParse

parse_cfg = CiscoConfParse("cisco_ipsec.txt")

pfs2crypto = parse_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO",
                                            childspec=r"pfs group2")

for item in pfs2crypto:
    print item.text

