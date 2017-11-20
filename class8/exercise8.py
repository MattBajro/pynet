#!/usr/bin/env python

from net_system.models import NetworkDevice, Credentials
from netmiko import ConnectHandler
from datetime import datetime
from multiprocessing import Process, current_process, Queue
import django


def show_ver_q(device, q):
    output_dict = {}
    creds = device.credentials
    conn_dev = ConnectHandler(
        device_type=device.device_type,
        ip=device.ip_address,
        username=creds.username,
        password=creds.password,
        port=device.port)

    outp = ('#' * 80) + "\n"
    outp += conn_dev.send_command("show version") + "\n"
    outp += ('#' * 80) + "\n"
    output_dict[device.device_name] = outp
    q.put(output_dict)

    conn_dev.disconnect()


def main():

    django.setup()

    start_time = datetime.now()
    q = Queue(maxsize=20)
    devices = NetworkDevice.objects.all()

    procs = []
    for device in devices:
        my_proc = Process(target=show_ver_q, args=(device, q))
        my_proc.start()
        procs.append(my_proc)

    for a_proc in procs:
        # print a_proc
        a_proc.join()

    while not q.empty():
        my_dict = q.get()
        for h, o in my_dict.iteritems():
            print h
            print o

    print "Elapsed time {}".format(datetime.now() - start_time)


if __name__ == "__main__":
    main()
