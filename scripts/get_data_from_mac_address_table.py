
# script works with data/CAM_table.txt
# extract VLAN, MAC address, and port from the MAC address table

# open the MAC address table file
with open('data/CAM_table.txt') as f:
    for line in f:
        # remove leading and trailing space in the line
        line = line.strip()

        # skip empty lines
        if line == '':
            continue
        
        # get the first character of the line
        first_character = line.split()[0][0]

        # process only lines that start with a digit
        if first_character.isdigit():
            
            # split the line into components and unpack into variables
            vlan, mac, _, port = line.split()

            # print the extracted information in a formatted way
            print(f'{vlan:<10} {mac:<18} {port:<18}')
