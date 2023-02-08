import os
import sys

# get the subnet from the command line argument
subnet = sys.argv[1]

# list to store the online IPs
online_ips = []

# loop through the first 10 IPs in the subnet
for i in range(1, 11):
    ip = subnet + '.' + str(i)
    response = os.system("ping -c 1 " + ip + " > /dev/null")

    # check the response code
    if response == 0:
        online_ips.append(ip)

# print the online IPs
if online_ips:
    print("Online IPs:")
    for ip in online_ips:
        print(ip)
else:
    print("No online IPs found.")

