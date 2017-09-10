#/usr/bin/env python

import time
from snmp_helper import snmp_extract,snmp_get_oid_v3
import email_helper
import time
import sys

SNMP_PORT = 161
OID_SYS_NAME = '1.3.6.1.2.1.1.5.0'
OID_RUN_LAST_CHNG = '1.3.6.1.4.1.9.9.43.1.1.1.0'
OID_RUN_LAST_SAVE = '1.3.6.1.4.1.9.9.43.1.1.2.0'
OID_START_LAST_CHNG = '1.3.6.1.4.1.9.9.43.1.1.3.0'

if __name__ == "__main__":

    #initialize snmp params
    pynet_rtr2 = '184.105.247.71'

    snmp_device = (pynet_rtr2, SNMP_PORT)
    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    snmp_user = (a_user, auth_key, encrypt_key)

    snmp_data = snmp_get_oid_v3(snmp_device, snmp_user, oid=OID_SYS_NAME)
    hostname = snmp_extract(snmp_data)

    #initialize email
    recipient = 'matus.biro@marlink.com'
    sender = 'mbiro@twb-tech.com'
    subject = 'Class3 - exercise1'
    template_message = '''

    Notification message for Class3 - exercise1.
    {} config was changed.
    '''.format(hostname)

    #initialize snmp_init_last_chng for next comparisons
    snmp_data = snmp_get_oid_v3(snmp_device, snmp_user, oid=OID_RUN_LAST_CHNG)
    init_time = time.time()
    snmp_init_last_chng = int(snmp_extract(snmp_data), base=10) / 100.0
    #keep copy of this time for calculating time of last change
    snmp_init_time = snmp_init_last_chng

    for i in range(6):
        try:
            time.sleep(20)
            snmp_data = snmp_get_oid_v3(snmp_device, snmp_user, oid=OID_RUN_LAST_CHNG)
            snmp_run_last_chng = int(snmp_extract(snmp_data), base=10) / 100.0

            if snmp_init_last_chng < snmp_run_last_chng:
                #calculate and convert time of last change
                gm_time = time.gmtime(init_time + (snmp_run_last_chng -
                    snmp_init_time))
                str_change_time = "Time of last change: " + time.strftime("%a, %d %b %Y %H:%M:%S +0000",
                        gm_time)

                message = template_message + str_change_time
                email_helper.send_mail(recipient, subject, message, sender)
                print "%d: %s config was changed and email was sent" % (i, hostname)
                #update last change time for next comparisons
                snmp_init_last_chng = snmp_run_last_chng
                continue

            print "%d: config was NOT changed" % i
        except KeyboardInterrupt:
            print "\nScript interrupted by user. Exiting."
            sys.exit(0)
