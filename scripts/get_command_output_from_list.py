
access_template = ['switchport mode access',
'switchport access vlan {}',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']

# this line prints the template and adds VLAN 5 to the second line of the template
print('\n'.join(access_template).format(5))

