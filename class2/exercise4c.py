#/usr/bin/env python

from snmp_helper import snmp_get_oid,snmp_extract

COMM_STRING = 'galileo'
SNMP_PORT = 161
pynet_rtr1 = ('184.105.247.70', COMM_STRING, SNMP_PORT)
pynet_rtr2 = ('184.105.247.71', COMM_STRING, SNMP_PORT)

#get sysName
snmp_data = snmp_get_oid(pynet_rtr1, oid='1.3.6.1.2.1.1.5.0', display_errors=True)
output = snmp_extract(snmp_data)
print output

#get sysDesc
snmp_data = snmp_get_oid(pynet_rtr1, oid='1.3.6.1.2.1.1.1.0', display_errors=True)
output = snmp_extract(snmp_data)
print output

print "\n"

#get sysName
snmp_data = snmp_get_oid(pynet_rtr2, oid='1.3.6.1.2.1.1.5.0', display_errors=True)
output = snmp_extract(snmp_data)
print output

#get sysDesc
snmp_data = snmp_get_oid(pynet_rtr2, oid='1.3.6.1.2.1.1.1.0', display_errors=True)
output = snmp_extract(snmp_data)
print output

