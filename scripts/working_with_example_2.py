
# resulting dictionary should have interface names as keys and their MTU values as values
result = {}

with open('data/sh_ip_interface.txt') as f:
    for line in f:
        # check for lines that contain 'line protocol'
        if 'line protocol' in line:
            
            # extract the interface name
            interface = line.split()[0]
        
        # check for lines that contain 'Internet address'
        elif "Internet address" in line:
            # extract the IP address
            ip_address = line.split()[-1]

            # initialize the dictionary for this interface
            result[interface] = {}

            # store the IP address in the dictionary
            result[interface]['ip'] = ip_address
        
        # check for lines that contain 'MTU is'
        elif 'MTU is' in line:
            # extract the MTU value
            mtu = line.split()[-2]

            # store the MTU value in the dictionary
            result[interface]['mtu'] = mtu

# print the resulting dictionary
print(result)
