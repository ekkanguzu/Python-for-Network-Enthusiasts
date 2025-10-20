
# Get IP address from user
ip_address = input("Enter an IP address: ")

# Validate IP address format
if ip_address.count(".") != 3:
    print("Invalid IP address")

else:
    # Split IP address into its four bytes
    first_byte = ip_address.split(".")[0]
    second_byte = ip_address.split(".")[1]
    third_byte = ip_address.split(".")[2]
    fourth_byte = ip_address.split(".")[3]

    # Validate that each byte is a number between 0 and 255
    if not (first_byte.isdigit() and second_byte.isdigit() and third_byte.isdigit() and fourth_byte.isdigit()):
        print("Invalid IP address")

    # Validate byte ranges
    elif not (0 <= int(first_byte) <= 255) and (0 <= int(second_byte) <= 255) and (0 <= int(third_byte) <= 255) and (0 <= int(first_byte) <= 255):
        print("Invalid IP address")

    # Check for unicast range
    elif 1 <= int(first_byte) <= 223:
        print("unicast")

    # Check for multicast range
    elif 224 <= int(first_byte) <= 239:
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

