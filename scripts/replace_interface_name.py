
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
new_nat = nat.replace("FastEthernet", "GigabitEthernet")
print(new_nat)
# Output: ip nat inside source list ACL interface GigabitEthernet0/1 overload
