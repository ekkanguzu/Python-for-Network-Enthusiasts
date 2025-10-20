
# list of MAC addresses in original format
mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]

# list to hold converted MAC addresses
result = []

# Convert each MAC address to Cisco format
for address in mac:
    # replace colons with dots
    converted_mac = address.replace(":", ".")

    # append converted MAC address to result list
    result.append(converted_mac)

# print the list of converted MAC addresses
print(result)
