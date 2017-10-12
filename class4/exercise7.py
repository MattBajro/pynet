#!/usr/bin/env python


from netmiko import ConnectHandler
from getpass import getpass

def main():
    pynet2 = {
        'device_type': 'cisco_ios',
        'ip': '184.105.247.71',
        'username': 'pyclass',
        'password': '88newclass',
        'port': 22,
    }

    pyrtr2 = ConnectHandler(**pynet2)

    pyrtr2.config_mode()
    pyrtr2.send_command("logging buffered 31313")
    pyrtr2.exit_config_mode()
    print pyrtr2.send_command("show run | i logging buffered")

    pyrtr2.disconnect()

if __name__ == "__main__":
    main()
