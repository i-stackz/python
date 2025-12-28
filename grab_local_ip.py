#!/usr/bin/env python3

"""
    Description: This script will utilize the ip command in order to grab the IPv4 address of NIC's that are in the 'UP' state
                 I found this solution either online or with the help of ChatGPT
    Date: 12/25/2024
    Author: istackz
"""

# import python modules/code libraries
import os


# variables
#grab_ipv4 : list  = os.popen("ip addr | grep -A 2 'state UP' | grep -w 'inet' | awk '{print $2}' | cut -d '/' -f 1 | tr -d '\n'").readlines() # bash command that will grab active NIC's IPv4 address and store it in an array variable

grab_ipv4 : list = os.popen("ip addr | grep -E -w '^[[:digit:]]' -A 2 | grep 'inet' | awk '{print $2}' | cut -d '/' -f 1").readlines() # bash command to grab IPv4 addresses of ALL NICs on the system

# iterate through array variable and print out its contents
for ip in grab_ipv4:
    print(ip.strip())
    

## test c style loop to iterate through array and print out its contents ##
#counter : int = 0; # loop initializer variable
#list_items : int = len(grab_ipv4); # grabs the number of items within the array (length)

## while loop to iterate through array
#while counter < list_items:
#    print(grab_ipv4[counter].strip()); # print out each item within the array
#    counter = counter + 1; # increment counter by one
