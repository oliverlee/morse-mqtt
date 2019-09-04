#!/usr/bin/env python
# -*- coding: utf-8 -*-
from queue import Queue
from threading import Thread
from time import sleep

from morse_mqtt.mqtt_recevier import MqttReceiver


def receiver(host, topic, queue):
    mqtt_recevier = MqttReceiver(host, topic, queue)
    mqtt_recevier.connect_loop()


# SAMPLE READER
def reader(timeout, queue):
    print("Reader started")
    while True:
        timestamps = queue.get()
        print(timestamps)


def main():
    host = '192.168.1.103'
    topic = '+/CAR/#'
    read_timeout = 2
    queue = Queue()

    receiver_thread = Thread(target=receiver, args=(host, topic, queue))
    receiver_thread.start()

    reader_thread = Thread(target=reader, args=(read_timeout, queue))
    reader_thread.start()

    receiver_thread.join()
    reader_thread.join()


main()
