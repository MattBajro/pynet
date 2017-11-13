#!/usr/bin/env python

import pyeapi


def main():

    pynet_sw1 = pyeapi.connect_to("pynet-sw1")

    output = pynet_sw1.enable("show interfaces")
    dict_sh_int = output[0]['result']['interfaces']

    for intf in sorted(dict_sh_int.keys()):
        if 'Vlan' in intf:
            print intf + " - has no counters"
            continue
        icounters = dict_sh_int[intf]['interfaceCounters']
        intf_stats = '{}, outOctets: {}, inOctets:{}'.format(intf,
                                                             icounters['outOctets'],
                                                             icounters['inOctets'])

        print intf_stats


if __name__ == "__main__":
    main()
