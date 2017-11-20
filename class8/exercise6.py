#!/usr/bin/env python

from net_system.models import NetworkDevice, Credentials
from netmiko import ConnectHandler
from datetime import datetime
import threading
import django


def show_ver(device):

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


def main():

    django.setup()

    start_time = datetime.now()
    devices = NetworkDevice.objects.all()

    for device in devices:
        my_thread = threading.Thread(target=show_ver, args=(device,))
        my_thread.start()

    main_thread = threading.currentThread()
    for a_thread in threading.enumerate():
        if a_thread != main_thread:
            # print a_thread
            a_thread.join()

    print "Elapsed time {}".format(datetime.now() - start_time)


if __name__ == "__main__":
    main()
