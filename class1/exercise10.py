
from ciscoconfparse import CiscoConfParse

parse_cfg = CiscoConfParse("cisco_ipsec.txt")

crypto_list = parse_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO",
                                            childspec=r"AES")

for item in crypto_list:
    print item.text
    for child in item.children:
        if 'transform-set' in child.text:
            print child.text.split(' ')[-2]

