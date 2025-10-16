
# device information dictionary
london_co = {
"r1": {
"location": "21 New Globe Walk",
"vendor": "Cisco",
"model": "4451",
"ios": "15.4",
"ip": "10.255.0.1"
},
"r2": {
"location": "21 New Globe Walk",
"vendor": "Cisco",
"model": "4451",
"ios": "15.4",
"ip": "10.255.0.2"
},
"sw1": {
"location": "21 New Globe Walk",
"vendor": "Cisco",
"model": "3850",
"ios": "3.6.XE",
"ip": "10.255.0.101",
"vlans": "10,20,30",
"routing": True
}
}

# Get user input for device name
device_name = input("Enter device name: ")

# Create a string of available parameters for the chosen device
parameter_string  = ", ".join(london_co.get(device_name, {}).keys())

# Get user input for device parameter
device_parameter = input(f"Enter parameter name ({parameter_string}): ").lower()

# Retrieve device information based on user input || provide default message if device not found
device_information = london_co.get(device_name, "Not Found")

# Retrieve specific device parameter information || provide default message if parameter not found
device_parameter_information = device_information.get(device_parameter, "No such parameter")

# Print the device parameter information
print(device_parameter_information)
