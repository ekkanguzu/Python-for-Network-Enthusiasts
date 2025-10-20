
# this script gets data from the data/sh_ip_int_br.txt
# data/sh_ip_int_br.txt contains the output of the "show ip interface brief" command from a router

# initialize empty dictionary to store results
result = {}

# open the file and read line by line
with open("data/sh_ip_int_br.txt") as f:
    for line in f:
        # split the line into words
        line = line.split()

        # check if the line has enough elements and the second element and at index 0 is a digit
        if line and line[1][0].isdigit():
            # unpack the line into interace and address variables
            interface, address, *other = line

            # store the interface and address in the result dictionary
            result[interface] = address

# print the result dictionary
print(result)
