
# script works with data/config_sw1.txt
# script is executed as: python get_switch_command.py config_sw1.txt
# file name is provided as a command line argument

from sys import argv

# script will skip lines that inlcude these words
ignore_list = ["duplex", "alias", "Current configuration"]

# get the file name from command line argument and construct the full path
file_name = 'data/' + argv[1]

# open the switch configuration file
with open(file_name) as f:
    for line in f:
        line = line.strip()
        
        # skip lines that start with "!"
        if line.startswith("!"):
            continue
        
        # Check each word in ignore_list
        skip_line = False
        for word in ignore_list:
            if word in line:
                skip_line = True
                break  # Exit loop early if match found
        
        # If skip_line is True, skip this line
        if skip_line:
            continue

        # print the remaining lines
        print(line)
