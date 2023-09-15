# Python Resolver
import socket
import platform
import os
import re

def welcome():
    # clear the screen
    os.system("cls")

    # print a welcome banner
    print("RESOLVER" + "\n" + "--------------------------------------------")

def resolve():
    # get the input string from user
    input_string = input("Enter a list of hostnames\n>> ")

    # define the regular expression used to parse the input
    pattern = r'[ \n,]+'

    # split the input string according to the pattern rules
    result = re.split(pattern, input_string)

    # a bit of formatting
    print("\n" + "--------------------------------------------")

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

    # a bit of formatting
    print("\n" + "--------------------------------------------")        

# wanna do it again? 
def repeat():
    answer = input("\nWould you like to run the program again? [Y]/[n]\n>> ")
    if answer == "Y":
        main()
    else:
        exit

# main function
def main():
    welcome()
    resolve()
    repeat()

if __name__ == '__main__':
    main()

