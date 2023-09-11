# Python Resolver


import socket
import platform
import os

# clear the screen
os.system("cls")

# list of hostnames
hostname_list = ['HCV591MDOTPDC17', 'HCV591MDOTTDC08']

# resolve hostnames to IP addresses
print("Resolving\n-----------------------------------------------")
for hostname in hostname_list:
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f'{hostname} - {ip_address}')
    except socket.gaierror as error:
        print(f'Error resolving {hostname}: {error}')


