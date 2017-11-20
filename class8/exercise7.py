#!/usr/bin/env python

from net_system.models import NetworkDevice, Credentials
from netmiko import ConnectHandler
from datetime import datetime
from multiprocessing import Process, current_process
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

    procs = []
    for device in devices:
        my_proc = Process(target=show_ver, args=(device,))
        my_proc.start()
        procs.append(my_proc)

    for a_proc in procs:
        # print a_proc
        a_proc.join()

    print "Elapsed time {}".format(datetime.now() - start_time)


if __name__ == "__main__":
    main()
