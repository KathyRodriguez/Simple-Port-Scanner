import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def parse_arguments():
    parser = argparse.ArgumentParser(description="A simple port scanner.")
    parser.add_argument("target", help="Target IP or hostname to scan.")
    parser.add_argument("-p", "--ports", nargs=2, type=int, metavar=("start", "end"),
                        help="Port range to scan (default is 1-1024).",
                        default=(1, 1024))
    return parser.parse_args()

def is_port_open(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((target, port))
        sock.close()
        return True
    except Exception:
        return False

def scan_port(target, port):
    if is_port_open(target, port):
        print(f"[+] Port {port} is open")
    else:
        print(f"[-] Port {port} is closed")

def main():
    args = parse_arguments()
    target = args.target
    start_port, end_port = args.ports

    print(f"Scanning {target} for open ports...")
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target, port)

    print("Scan complete.")

if __name__ == "__main__":
    main()
