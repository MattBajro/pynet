#!/usr/bin/env python

from net_system.models import NetworkDevice, Credentials
import django


def main():

    django.setup()

    temp_rtr1 = NetworkDevice.objects.get(device_name='temp-rtr1')
    temp_rtr1.delete()

    temp_rtr2 = NetworkDevice.objects.get(device_name='temp-rtr2')
    temp_rtr2.delete()


if __name__ == "__main__":
    main()
