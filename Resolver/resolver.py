# Python Resolver
import socket
import platform
import os
import re

def resolve():
    # get the input string from user
    input_string = input("Enter a list of hostnames\n>>")

    # define the regular expression used to parse the input
    pattern = r'[ \n,]+'

    # split the input string according to the pattern rules
    result = re.split(pattern, input_string)

    # iterates over the newly formatted list
    for hostname in result:
        try:
            ip_address = socket.gethostbyname(hostname)
            operating_system = platform.system()
            
            # output format
            print(f'{hostname} - {ip_address} - {operating_system}')

        # error handling
        except socket.gaierror as error:
            print(f'Error resolving {hostname}: {error}')            

# main function
def main():
    os.system("cls")
    resolve()

if __name__ == '__main__':
    main()


