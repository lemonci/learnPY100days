from socket import socket

def main():
    # 1. Create a socket to use IPv4 and TCP
    client = socket()
    # 2. Connect to server (with IP address and port specified)
    client.connect(('192.168.2.98', 6789))
    # 3. Get data from server
    print(client.recv(1024).decode('utf-8'))
    client.close()

if __name__ == '__main__':
    main()