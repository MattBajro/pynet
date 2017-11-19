#!/usr/bin/env python

from net_system.models import NetworkDevice, Credentials
import django


def main():

    django.setup()
    creds = Credentials.objects.all()

    temp_rtr1 = NetworkDevice(
        device_type='cisco_ios',
        device_name='temp-rtr1',
        ip_address='192.168.0.254',
        port='22',
        vendor='Cisco Systems')
    print temp_rtr1
    temp_rtr1.credentials = creds[0]
    temp_rtr1.save()

    temp_rtr2 = NetworkDevice.objects.get_or_create(
        device_type='cisco_ios',
        device_name='temp-rtr2',
        ip_address='192.168.0.253',
        port='22',
        vendor='Cisco Systems')
    print temp_rtr2
    temp_rtr2[0].credentials = creds[0]
    temp_rtr2[0].save()


if __name__ == "__main__":
    main()
