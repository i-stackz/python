#!/usr/bin/env python3 

"""
    Description: This script will gather information on the host. Works on Unix (RHEL) hosts
    Author: istackz
    Date: 12/23/2026
"""
# Modules
import sys # system module
import re # regular expression module
import os # operating system module
import platform # similar to the sys module
import subprocess # cli commands module 

# Variables
operating_system = sys.platform;
operating_system1 = platform.system(); # alternatively platform.system().system
user = subprocess.run(['id -un'], capture_output=True, shell=True, text=True).stdout;
hostname = subprocess.run('hostname -f', capture_output=True, shell=True, text=True).stdout.strip();

# check if system = 'linux'
if operating_system != "linux":
    print(f"Current Host's OS: {operating_system}");
    sys.exit("Error! Host's OS is not 'linux'");

if operating_system == "linux":
    print(f"\nCurrent Host's OS: {operating_system}");
    print(f"Current Host's OS (alt): {operating_system1}\n");

# multi-line comment
""" 
#print(f"{re.findall('root', user)[0]}");
#print(f"{subprocess.run(['id -un'], capture_output=True, shell=True, text=True).stdout}");

if user != 'root':
    sys.exit("Error! Commands must be ran as root");
else:
    continue;
""" 
# end of multi-line comment

# run unix commands
#print(subprocess.run(["cat", '/etc/os-release'], capture_output=True, text=True));
print(subprocess.run(["hostnamectl", 'status'], capture_output=True, text=True).stdout); # new way to convert byte output to string
print(subprocess.run('echo -e "Local IPv4: $(ip -4 -brief addr | grep -vi lo | grep -iv down | awk \'{print $3}\')"', capture_output=True, shell=True).stdout.decode('utf-8'));
print(subprocess.run('echo -e Public IPv4: $(dig +short myip.opendns.com @resolver1.opendns.com)', capture_output=True, shell=True, text=True).stdout); # print public ip ** requires dig binary/package **
print(subprocess.run(["free", "-h"], capture_output=True, text=True, check=True).stdout);
print(subprocess.run(["lspci | grep -i vga"], capture_output=True, shell=True).stdout.decode('utf-8')); # alternate way to run bash commands
print(f"{subprocess.run(['ss', '-tunl'], capture_output=True, text=True).stdout}");
print(subprocess.run('lsblk', capture_output=True, shell=True, text=True, check=True).stdout); 

# create a file and write output to it
with open(f"./{hostname}.log", "w") as file: # best practice as it automatically closes the file
    file.write(f"\nSystem Info:\n");
    file.write(f"\n{subprocess.run(['hostnamectl status'], capture_output=True, shell=True, text=True).stdout}\n");
    file.write(f"\nLocal IPv4:\n");
    file.write(f'\n{subprocess.run(["ip -4 -brief addr"], capture_output=True, shell=True, text=True).stdout}\n');
    file.write(f"\nPublic IPv4:\n");
    file.write(f"\n{subprocess.run('dig +short myip.opendns.com @resolver1.opendns.com', capture_output=True, shell=True, text=True).stdout}\n");
    file.write("\nHost's Memory:\n");
    file.write(f"\n{subprocess.run(['free -h'], capture_output=True, shell=True).stdout.decode('utf-8')}\n");
    file.write(f"\nHost's GPU Info:\n");
    file.write(f"\n{subprocess.run(['lspci | grep -i vga'], capture_output=True, shell=True, text=True).stdout}\n");
    file.write(f"\nHost's Listening Network Connections:\n");
    file.write(f"\n{subprocess.run(['ss -tunl'], capture_output=True, shell=True, text=True).stdout}\n");
    file.write(f"\nHost's Block Devices:\n");
    file.write(f"\n{subprocess.run('lsblk', capture_output=True, shell=True, text=True).stdout}\n\n");
    file.close();

"""

    alternative method:
    
    file = open("./get_sys_info.log", "w"); # create and open file for writing
    file.write(f"{subprocess.run(['hostname status'], capture_output=True, shell=True, text=True).stdout}"); # write to file has to be a string
    file.close(); # closes the file

"""
