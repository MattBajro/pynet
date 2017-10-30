#!/usr/bin/env python

import pexpect
from getpass import getpass
import re

def main():

    ip_addr = '184.105.247.71'
    username = 'pyclass'
    port = 22
    password = getpass()

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)

    ssh_conn.expect(r'#')
    phostname = re.escape(ssh_conn.before.strip())
    #print phostname
    cfg = re.escape('(config)#')

    ssh_conn.sendline('configure terminal')
    ssh_conn.expect(phostname + cfg)
    print ssh_conn.before
    print ssh_conn.after

    ssh_conn.sendline('logging buffered 33008')
    ssh_conn.expect(phostname + cfg)
    print ssh_conn.before
    print ssh_conn.after

    ssh_conn.sendline('end')
    ssh_conn.expect(phostname + r'#')
    print ssh_conn.before
    print ssh_conn.after

    ssh_conn.sendline('show run | include logging buffered')
    ssh_conn.expect(phostname + r'#')
    print ssh_conn.before
    print ssh_conn.after

    ssh_conn.close()

if __name__ == '__main__':
    main()
