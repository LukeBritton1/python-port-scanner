import socket

def port_scanner(target, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)  # Set a timeout for each connection attempt
    
    result = scanner.connect_ex((target, port))  # Returns 0 if port is open
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    scanner.close()


target = input("Enter target IP or hostname: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: ")) 


for port in range(start_port, end_port + 1):
    port_scanner(target, port)