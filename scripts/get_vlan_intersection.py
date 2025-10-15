
# Script to find the intersection of VLANs from two switchport trunk allowed vlan commands

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

command1_vlans = command1.split()[-1].split(",")
command2_vlans = command2.split()[-1].split(",")

intersection = set(command1_vlans) & set(command2_vlans)
print(intersection)
# Output: {'1', '3', '8'}
