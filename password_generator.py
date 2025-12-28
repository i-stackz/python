#!/usr/bin/env python3

# Description: Password Generator script
# Author: istackz

######################################################

# requirements:
# - Length
# - should contain upppercase
# - should contain special
# - should contain digits

# create/get all available characters
# randomly pick characters up to the length
# ensure we have atleast one of each character type
# ensure length is valid


#######################################################

# modules
import random
import string

# function
def generate_password():
    # local variables
    length = int(input("Enter the desired password length: ").strip());
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower();
    include_special = input("Include special characters? (yes/no): ").strip().lower();
    include_digits = input("Include digits? (yes/no): ").strip().lower();

    
    if length < 4:
        print("Password length must be at least 4 characters.")
        return

    lowercase = string.ascii_lowercase

    if include_uppercase == 'yes':
        uppercase = string.ascii_uppercase
    else:
        uppercase = "";

    if include_special == 'yes':
        special = string.punctuation;
    else:
        special = "";

    if include_digits == 'yes':
        digits = string.digits;
    else:
        digits = "";

    all_characters = lowercase + uppercase + special + digits;

    required_characters = [];

    if include_uppercase == "yes":
        required_characters.append(random.choice(uppercase));

    if include_special == 'yes':
        required_characters.append(random.choice(special));

    if include_digits == 'yes':
        required_characters.append(random.choice(digits));

    remaining_length = length - len(required_characters);

    password = required_characters;

    for _ in range(remaining_length):
        character = random.choice(all_characters);
        password.append(character);

    random.shuffle(password);

    str_password = "".join(password);

    return print(str_password);

# call function
generate_password();
