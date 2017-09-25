#!/usr/bin/env python

import paramiko
import time

p2 = {
    'device_type': 'cisco_ios',
	'ip': '184.105.247.71',
	'username': 'pyclass',
	'password': '88newclass',
	'port': 22,
}

def main():
    rcon_pre = paramiko.SSHClient()
    #rcon_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    rcon_pre.load_system_host_keys()
    rcon_pre.connect(p2['ip'], username=p2['username'],
    password=p2['password'],
            look_for_keys=False, allow_agent=False, port=p2['port'])

    rcon = rcon_pre.invoke_shell()
    rcon.settimeout(4.0)

    rcon.send("terminal length 0\n")
    rcon.send("configure terminal\n")
    time.sleep(0.5)
    rcon.send("logging buffered 33333\n")
    rcon.send("end\n")
    time.sleep(0.5)
    outp = rcon.recv(5000)

    print outp
    rcon.close()

if __name__ == "__main__":
    main()
