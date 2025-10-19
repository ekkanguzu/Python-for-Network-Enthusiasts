
# templates for access and trunk switch configurations
access_template = [
    "switchport mode access", "switchport access vlan {}",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]

# User prompts based on interface mode
prompts = {"access": "Enter VLAN number:",
           "trunk": "Enter the allowed VLANs:"
           }

# Combine templates into a dictionary for easy access
templates = {
    "access": "\n".join(access_template),
    "trunk": "\n".join(trunk_template)
}

# Get user input
interface_mode = input("Enter interface mode (access/trunk): ")
interface_type_number = input("Enter type and interface number: ")

# Get VLAN number(s) based on interface mode
vlan_number = input(f"{prompts[interface_mode]} ")

# Print the configuration based on user input
print(f"\ninterface {interface_type_number}\n" + templates[interface_mode].format(vlan_number))
