
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
vlans_string = config.split()[-1]
vlans_list = vlans_string.split(",")
print(vlans_list)
# Output: ['1', '3', '10', '20', '30', '100']
