import socket

# get the IP and port range from the user
#ip = input("Enter the IP address: ")
#start_port = int(input("Enter the starting port: "))
#end_port = int(input("Enter the ending port: "))



# loop through the port range
for port in range(start_port, end_port+1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except:
        print(f"Port {port} is closed or host is not reachable")

