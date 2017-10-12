#!/usr/bin/env python


from netmiko import ConnectHandler
import time

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

    pyrtr1 = ConnectHandler(**pynet1)
    pyrtr2 = ConnectHandler(**pynet2)

    for device in [pyrtr1, pyrtr2]:
        print device.find_prompt()
        device.send_config_from_file(config_file='config_file.txt')
        time.sleep(0.3)
        print device.send_command("show run | i logging")

    pyrtr1.disconnect()
    pyrtr2.disconnect()

if __name__ == "__main__":
    main()
