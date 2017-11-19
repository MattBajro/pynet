#!/usr/bin/env python

from net_system.models import NetworkDevice, Credentials
import django


def main():

    django.setup()

    devices = NetworkDevice.objects.all()
    creds = Credentials.objects.all()
    std_creds = creds[0]
    arista_creds = creds[1]

    for device in devices:
        if 'pynet-sw' in device.device_name:
            device.credentials = arista_creds
        else:
            device.credentials = std_creds
        device.save()


if __name__ == "__main__":
    main()
