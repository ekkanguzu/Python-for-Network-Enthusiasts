
# script works with data/ospf.txt

# open the OSPF routing table file
with open('data/ospf.txt') as f:
    for line in f:
        # clean and split the line into components
        line = line.strip().split()

        # extract ip address, ad/metric, next hop, last update, and outbound interface
        ip_address = line[1]
        ad_metric = line[2].strip('[]')
        next_hop = line[4].strip(',')
        last_update = line[5].strip(',')
        outbound_interface = line[6]

        # print the extracted information in a formatted way
        print(f"""
Prefix {ip_address:<15}
AD/Metric {ad_metric:<15} 
Next hop {next_hop:<15} 
Last update {last_update:<15} 
Outbound interface {outbound_interface:<15}
""")
