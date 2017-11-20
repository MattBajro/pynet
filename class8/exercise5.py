#!/usr/bin/env python

from net_system.models import NetworkDevice, Credentials
from netmiko import ConnectHandler
from datetime import datetime
import django


def main():

    django.setup()

    start_time = datetime.now()
    devices = NetworkDevice.objects.all()

    for device in devices:
        creds = device.credentials
        conn_dev = ConnectHandler(
            device_type=device.device_type,
            ip=device.ip_address,
            username=creds.username,
            password=creds.password,
            port=device.port)

        outp = conn_dev.send_command("show version")
        # print outp
        conn_dev.disconnect()

    print "Elapsed time {}".format(datetime.now() - start_time)


if __name__ == "__main__":
    main()
