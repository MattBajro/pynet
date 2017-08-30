#/usr/bin/env python

import telnetlib
from pprint import pprint

DEBUG = 0
TELNET_PORT = 23
TELNET_TIMEOUT = 5
READ_TIMEOUT = 2

def normalize_output(output):
    '''
    Remove 1st and last line from output,
    remove any blank chars and normalize newline
    '''
    raw_output = output.split('\n')[1:-1]
    pretty_list = []
    for item in raw_output:
        pretty_list.append(item.strip())
    return '\n'.join(pretty_list)


if __name__ == '__main__':
    ip_addr = '184.105.247.70'
    usr = 'pyclass'
    passwd = '88newclass'

    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    output = remote_conn.read_until('sername:', READ_TIMEOUT)
    #print output
    remote_conn.write(usr + '\n')

    output = remote_conn.read_until('assword:', READ_TIMEOUT)
    #print output
    remote_conn.write(passwd + '\n')

    output = remote_conn.read_until('#', READ_TIMEOUT)
    hostname = output.strip()

    remote_conn.write('terminal length 0' + '\n')
    output = remote_conn.read_until(hostname, READ_TIMEOUT)

    remote_conn.write('show ip int brief' + '\n')
    output = remote_conn.read_until(hostname, READ_TIMEOUT)
    #print output
    print normalize_output(output)

    remote_conn.close()
