#!/usr/bin/env python

import pyeapi
import argparse
import sys


def my_help():
    hlp = '''\nuseage: exercise2.py [-h] [--help] {--name VLAN-ID VLAN-NAME | --remove VLAN-ID}\n'''

    print hlp
    exit(0)


def check_vlan_exist(vlan_id):
    pynet_sw1 = pyeapi.connect_to("pynet-sw1")
    output = pynet_sw1.enable("show vlan brief") 
    if vlan_id in output[0]['result']['vlans'].keys():
        return True

    return False


def create_vlan(vlan):
    pynet_sw1 = pyeapi.connect_to("pynet-sw1")
    cmds = ['vlan ' + vlan[1], 'name ' + vlan[0]]
    try:
        pynet_sw1.config(cmds)
    except pyeapi.eapilib.CommandError as e:
        print "Run into an error during vlan creation:"
        print str(e)
        exit(1)

    print "Vlan-id %s was succesfully created." % vlan[1]
    return True


def delete_vlan(vlan):
    pynet_sw1 = pyeapi.connect_to("pynet-sw1")
    cmds = ['no vlan ' + vlan]
    try:
        pynet_sw1.config(cmds)
    except pyeapi.eapilib.CommandError as e:
        print "Run into an error during vlan deletion:"
        print str(e)
        exit(1)

    print "Vlan-id %s was deleted." % vlan
    return True


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--name', nargs=2, dest="vlan", default=False)
    parser.add_argument('--remove', nargs=1, default=False)
    parser.add_argument('-h', '--help', action="store_true", default=False)
    args = parser.parse_args()

    if len(sys.argv) == 1:
        my_help()

    if (args.vlan is not False) and (args.remove is not False):
        print "Please specify only 1 argument at a time."
        my_help()

    if args.vlan is not False:
        if check_vlan_exist(args.vlan[1]):
            print "Vlan-id %s exists already. No action taken." % args.vlan[1]
            exit(0)
        else:
            create_vlan(args.vlan)
            exit(0)

    if args.remove is not False:
        delete_vlan(args.remove[0])
        exit(0)


if __name__ == "__main__":
    main()
