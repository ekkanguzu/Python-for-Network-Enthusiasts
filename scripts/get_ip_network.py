
# Get IP Network from user
ip_network = input("Enter IP Network in the format (10.1.1.0/24): ")

# split input into network and mask
network = ip_network.split("/")[0]
mask = ip_network.split("/")[1]

# convert mask to integer
mask = int(mask)

# split network into octets
oct1, oct2, oct3, oct4 = network.split('.')

# create binary string for mask
mask_binary = "1" * mask + "0" * (32 - mask)

# grab each mask per octet
mask_octet1_bin = mask_binary[0:8]
mask_octet2_bin = mask_binary[8:16]
mask_octet3_bin = mask_binary[16:24]
mask_octet4_bin = mask_binary[24:32]

# convert each octet to decimal
mask_octet1_decimal = int(mask_octet1_bin, 2)
mask_octet2_decimal = int(mask_octet2_bin, 2)
mask_octet3_decimal = int(mask_octet3_bin, 2)
mask_octet4_decimal = int(mask_octet4_bin, 2)

# Convert each octet to binary and pad to 8 bits
network_binary_output = f"""
network:
{oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}
{int(oct1):08b} {int(oct2):08b} {int(oct3):08b} {int(oct4):08b}

Mask:
/{mask}
{mask_octet1_decimal:<3} {mask_octet2_decimal:<3} {mask_octet3_decimal:<3} {mask_octet4_decimal}
{mask_octet1_bin} {mask_octet2_bin} {mask_octet3_bin} {mask_octet4_bin}
"""

# remove leading and trailing space from string
network_binary_output = network_binary_output.strip()

# print the fully formatted output
print(network_binary_output)
