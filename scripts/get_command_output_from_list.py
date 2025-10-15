
from sys import argv
# this script prints a switchport access template and adds a VLAN number to the second line of the template
# the VLAN number is provided as a command line argument

interface = argv[1]
vlan = argv[2]

access_template = ['switchport mode access',
'switchport access vlan {}',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']

print("interface {}".format(interface))
print("\n".join(access_template).format(vlan))
