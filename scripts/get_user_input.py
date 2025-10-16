
# Get user input for interface type/number and VLAN number
interface = input("Enter interface type and number: ")
vlan = input("Enter VLAN number: ")

access_template = ['switchport mode access',
'switchport access vlan {}',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']

# Print a separator line for better readability
print('\n' + '-' * 30)

# Print the interface configuration
print("interface {}".format(interface))
print("\n".join(access_template).format(vlan))
