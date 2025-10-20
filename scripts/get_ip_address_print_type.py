
# Get an IP address from the user
ip_address = input("Enter an IP address: ")

# Extract the first byte of the IP address
first_byte = int(ip_address.split(".")[0])

# Check for unicast range
if 1 <= first_byte <= 223:
    print("unicast")

# Check for multicast range
elif 224 <= first_byte <= 239:
    print("multicast")

# Check for broadcast
elif ip_address == "255.255.255.255":
    print("local broadcast")

# Check for unassigned address
elif ip_address == "0.0.0.0":
    print("unassigned")

# If none of the above, it's unused
else:
    print("unused")
