import socket

def scan_ports(ip_address, start_port, end_port):
    """Scan the specified range of ports for a given IP address"""
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            # create a TCP socket and attempt to connect to the specified port
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.error:
            pass
    return open_ports

# Example usage:
# open_ports = scan_ports("127.0.0.1", 1, 100)
# print("Open ports:", open_ports)
