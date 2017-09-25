#/usr/bin/env python

from snmp_helper import snmp_extract,snmp_get_oid_v3
import email_helper
import time
import sys
import pygal

SNMP_PORT = 161

if __name__ == "__main__":

    #initialize snmp params
    oids = [
            ('sysName', '1.3.6.1.2.1.1.5.0'),
            ('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5'),
            ('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5'),
            ('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5'),
            ('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
            ('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5')
            ]

    pynet_rtr1 = '184.105.247.70'
    snmp_device = (pynet_rtr1, SNMP_PORT)
    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    snmp_user = (a_user, auth_key, encrypt_key)

    snmp_data = snmp_get_oid_v3(snmp_device, snmp_user, oid=oids[0][1])
    hostname = snmp_extract(snmp_data)

    #initialize data structures
    fa4_in_octets = []
    fa4_out_octets = []
    fa4_in_packets = []
    fa4_out_packets = []
    x_labels = []

    last_in_octets = 0
    last_out_octets = 0
    last_in_packets = 0
    last_out_packets = 0

    for i in range(13):
        try:
            if i == 0:
                snmp_data = snmp_get_oid_v3(snmp_device, snmp_user, oid=oids[2][1])
                last_in_octets = int(snmp_extract(snmp_data), base=10)
                snmp_data = snmp_get_oid_v3(snmp_device, snmp_user,
                        oid=oids[3][1])
                last_in_packets = int(snmp_extract(snmp_data), base=10)

                snmp_data = snmp_get_oid_v3(snmp_device, snmp_user, oid=oids[4][1])
                last_out_octets = int(snmp_extract(snmp_data), base=10)
                snmp_data = snmp_get_oid_v3(snmp_device, snmp_user,
                        oid=oids[5][1])
                last_out_packets = int(snmp_extract(snmp_data), base=10)

                x_labels.append(str(i*5))
                print "Run #%d completed. Sleeping for 15mins." % i
                time.sleep(900)
                continue

            snmp_data = snmp_get_oid_v3(snmp_device, snmp_user, oid=oids[2][1])
            curr_in_octets = int(snmp_extract(snmp_data), base=10)
            snmp_data = snmp_get_oid_v3(snmp_device, snmp_user,
                    oid=oids[3][1])
            curr_in_packets = int(snmp_extract(snmp_data), base=10)

            snmp_data = snmp_get_oid_v3(snmp_device, snmp_user, oid=oids[4][1])
            curr_out_octets = int(snmp_extract(snmp_data), base=10)
            snmp_data = snmp_get_oid_v3(snmp_device, snmp_user,
                    oid=oids[5][1])
            curr_out_packets = int(snmp_extract(snmp_data), base=10)

            fa4_in_octets.append(curr_in_octets - last_in_octets)
            fa4_out_octets.append(curr_out_octets - last_out_octets)
            fa4_in_packets.append(curr_in_packets - last_in_packets)
            fa4_out_packets.append(curr_out_packets - last_out_packets)

            last_in_octets = curr_in_octets
            last_out_octets = curr_out_octets
            last_in_packets = curr_in_packets
            last_out_packets = curr_out_packets

            x_labels.append(str(i*5))
            print "Run #%d completed. Sleeping for 15mins." % i
            time.sleep(900)

        except KeyboardInterrupt:
            print "\nScript interrupted by user. Exiting."
            sys.exit(0)

    #print fa4_in_octets
    #print fa4_out_octets
    #print fa4_in_packets
    #print fa4_out_packets
    #print x_labels

    line_chart = pygal.Line()
    line_chart.title = 'Input/Output Bytes on Fa4, ' + hostname
    line_chart.x_labels = x_labels
    line_chart.add('InBytes', fa4_in_octets)
    line_chart.add('OutBytes', fa4_out_octets)
    line_chart.render_to_file('Fa4-InOut-Bytes.svg')

    line_chart = pygal.Line()
    line_chart.title = 'Input/Output Packets on Fa4, ' + hostname
    line_chart.x_labels = x_labels
    line_chart.add('InBytes', fa4_in_packets)
    line_chart.add('OutBytes', fa4_out_packets)
    line_chart.render_to_file('Fa4-InOut-Packets.svg')
