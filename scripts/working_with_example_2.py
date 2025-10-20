
# resulting dictionary should have interface names as keys and their MTU values as values
result = {}

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
            # add the interface and MTU to the dictionary
            result[interface] = mtu

# print the resulting dictionary
print(result)
