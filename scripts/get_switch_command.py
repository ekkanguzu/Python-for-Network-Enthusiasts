
# script works with data/config_sw1.txt

from sys import argv

# get the file name from command line argument and construct the full path
file_name = 'data/' + argv[1]

# open the switch configuration file
with open(file_name) as f:
    for line in f:
        line = line.strip()
        
        # skip lines that start with "!"
        if line.startswith("!"):
            continue

        # print the remaining lines
        print(line)
