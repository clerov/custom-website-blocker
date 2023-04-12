import os
import time
import pandas as pd
from datetime import datetime as dt

hosts = {
    "windows": "C:\\Windows\\System32\\drivers\\etc\\hosts",
    "linux_or_mac": "/etc/hosts"
}

if os.name == "nt":
    host_path = hosts["windows"]
else:
    host_path = hosts["linux_or_mac"]

# Testing host file
# host_temp = "hosts"

# Please include the websites in websites.txt and separate new links with ,
websites = list(pd.read_csv('websites.txt', sep=","))

redirect = "127.0.0.1"

# Defines the blocking hours

blocking_hours = {
    "start": 16,
    "end": 18
}

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, blocking_hours['start']) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, blocking_hours['end']):
        print('Working hours...')
        with open(host_path, 'r+') as file:
            content = file.read()
            # print(content)
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(f"{redirect}  {website}\n")
                    print(f'{website} has been blocked')
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
                file.truncate()
        for website in websites:
            print(f'{website} has been unblocked')
        print('Fun hours')
    time.sleep(5)
