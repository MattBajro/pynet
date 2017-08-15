
from ciscoconfparse import CiscoConfParse

parse_cfg = CiscoConfParse("cisco_ipsec.txt")

crypto_objlist = parse_cfg.find_objects(r"^crypto map CRYPTO")

for item in crypto_objlist:
    print item.text
    for child in item.children:
        print child.text

