#!/usr/bin/env python
'''
Write a script that connects to the lab pynet-rtr1, logins, and executes the
'show ip int brief' command.

Rewritten to class-based solution
'''

import telnetlib
import time
import socket
import sys
import getpass

TELNET_PORT = 23
TELNET_TIMEOUT = 6

class TelnetNetworkDevice(object):
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password

    def send_command(self, cmd):
        '''
        Send a command down the telnet channel
        Return the response
        '''
        cmd = cmd.rstrip()
        self.remote_conn.write(cmd + '\n')
        time.sleep(1)
        return self.remote_conn.read_very_eager()

    def login(self):
        '''
        Login to network device
        '''
        output = self.remote_conn.read_until("sername:", TELNET_TIMEOUT)
        self.remote_conn.write(self.username + '\n')
        output += self.remote_conn.read_until("ssword:", TELNET_TIMEOUT)
        self.remote_conn.write(self.password + '\n')
        return output

    def disable_paging(self, paging_cmd='terminal length 0'):
        '''
        Disable the paging of output (i.e. --More--)
        '''
        return self.send_command(paging_cmd)

    def telnet_connect(self):
        '''
        Establish telnet connection
        '''
        try:
            self.remote_conn = telnetlib.Telnet(self.ip, TELNET_PORT, TELNET_TIMEOUT)
            return True
        except socket.timeout:
            sys.exit("Connection timed-out")

    def close_conn(self):
        self.remote_conn.close()
        return True


def main():
    '''
    Write a script that connects to the lab pynet-rtr1, logins, and executes the
    'show ip int brief' command.
    '''
    ip_addr = raw_input("IP address: ")
    ip_addr = ip_addr.strip()
    username = 'pyclass'
    password = getpass.getpass()

    rtr = TelnetNetworkDevice(ip_addr, username, password)

    rtr.telnet_connect()
    rtr.login()
    time.sleep(1)

    rtr.disable_paging()

    output = rtr.send_command('show ip int brief')

    print "\n\n"
    print output
    print "\n\n"

    rtr.close_conn()

if __name__ == "__main__":
    main()
