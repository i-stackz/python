#!/usr/bin/env python3

"""
    Description: This script will create a HEREDOC bash script on the system.
    Author: istackz
    Date: 12/24/25
"""

# Modules
import sys # for arguments and system stuff
import subprocess # to run bash cli commands

# variables
file = open("./testfile.sh", "w");
file.write(f"""
#!/usr/bin/env bash

# Description: This is test

echo -e 'Test was successfull';

""");
file.close;

print(subprocess.run(['/usr/bin/bash ./testfile.sh'], capture_output=True, shell=True, check=True).stdout.decode('utf-8'));
