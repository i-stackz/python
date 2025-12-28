#!/usr/bin/env python3

# Description: This script will prompt user for filename if its not given one as an argument and prints out it's contents.
# Author: istackz

import sys # module that contains Python IDE functions (argv, platform)

# Original Code

#if len(sys.argv) < 2:
#    filename = input('Enter a filename: ');
#    file = open("./{}".format(str(filename)), "r");
#
#    for line in file:
#        print(line);
#
#    file.close();
#
#elif len(sys.argv) == 2:
#    filename = sys.argv[1];
#    file = open("./{}".format(str(filename)), "r");
#
#    for line in file:
#        print(line);
#
#    file.close();
### End ###

## Version 2.0 ##

# check for arguments
if len(sys.argv) < 2:
    filename = input("Enter a filename: ");
    with open(f"./{filename}", "r") as file:
        data = file.read();
        print(data)
elif len(sys.argv) == 2:
    filename = sys.argv[1];
    with open(f"./{filename}", "r") as file:
        data = file.read();
        print(data);

