
# script works with the file data/sh_ip_interface.txt
# data/sh_ip_interface.txt contains the output of the "show ip interface" command from a router
# script extracts the interface names and their MTU values

# open the file sh_ip_interface.txt and read it line by line
with open('data/sh_ip_interface.txt') as f:
    for line in f:

        # check for lines that contain 'line protocol'
        if 'line protocol' in line:
            # extract the interface name
            interface = line.split()[0]

        # check for lines that contain 'MTU is'
        elif 'MTU is' in line:
            # extract the MTU value
            mtu = line.split()[-2]
            print('{:15}{}'.format(interface, mtu))
