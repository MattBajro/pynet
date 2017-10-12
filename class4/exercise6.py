#!/usr/bin/env python


from netmiko import ConnectHandler
from getpass import getpass

def main():
    pynet1 = {
        'device_type': 'cisco_ios',
        'ip': '184.105.247.70',
        'username': 'pyclass',
        'password': '88newclass',
    }
    pynet2 = {
        'device_type': 'cisco_ios',
        'ip': '184.105.247.71',
        'username': 'pyclass',
        'password': '88newclass',
        'port': 22,
    }
    juniper = {
        'device_type': 'juniper',
        'ip': '184.105.247.76',
        'username': 'pyclass',
        'password': '88newclass',
        'port': 22,
    }

    pyrtr1 = ConnectHandler(**pynet1)
    pyrtr2 = ConnectHandler(**pynet2)
    srx = ConnectHandler(**juniper)

    cmds = ['show arp']

    for device in [pyrtr1, pyrtr2, srx]:
        print device.find_prompt()
        for cmd in cmds:
            print device.send_command(cmd)

    pyrtr1.disconnect()
    pyrtr2.disconnect()
    srx.disconnect()

if __name__ == "__main__":
    main()
