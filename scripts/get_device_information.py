
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

# Retrieve device information based on user input || provide default message if device not found
device_information = london_co.get(device_name, "Not Found")

# Print the device information
print(device_information)
