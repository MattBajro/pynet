#!/usr/bin/env python

from net_system.models import NetworkDevice, Credentials
import django

vendors = {'cisco_ios': 'Cisco Systems',
           'arista_eos': 'Arista Netowrks',
           'juniper': 'Juniper Networks'}


def main():

    django.setup()

    devices = NetworkDevice.objects.all()

    for device in devices:
        device.vendor = vendors[device.device_type]
        device.save()


if __name__ == "__main__":
    main()
