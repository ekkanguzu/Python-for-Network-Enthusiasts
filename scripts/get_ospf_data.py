
# Process the ospf_route string and print the information to the stdout as follows:
#  Prefix 10.0.24.0/24
#  AD/Metric 110/41
#  Next-Hop 10.0.13.3
#  Last update 3d18h
#  Outbound Interface FastEthernet0/0


ospf_route = " 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

# this line removes leading space from the string
clean_ospf_route = ospf_route.strip()

prefix = clean_ospf_route.split()[0]
ad_metric = clean_ospf_route.split()[1].strip("[]")
next_hop = clean_ospf_route.split()[3].strip(",")
last_update = clean_ospf_route.split()[4].strip(",")
outbound_interface = clean_ospf_route.split()[5]

print(f"""
Prefix \t\t\t{prefix}
AD/Metric \t\t{ad_metric}
Next-Hop \t\t{next_hop}
Last update \t\t{last_update}
Outbound Interface \t{outbound_interface}
""")
