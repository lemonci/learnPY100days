from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def main():
    # 1. Create a socket object and specify the type of transmission service
    # family = AF_INET - IPv4 address
    # family = AF_INET6 - PPv6 address
    # type = SOCK_STREAM - TCP socket
    # type = SOCK_DGRAM - UDP socket
    # type = SOCK_RAW - raw socket
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2. Bind IP address and port (port is used to distinguish different services)
    # Only one service can be bound on the same port at the same time otherwise an error is reported
    server.bind(('192.168.2.98', 6789))
    # 3. Start listening - listening the client to connect to the server
    # parameter 512 is the size of the connection queue
    server.listen(512)
    print('Server start listening')
    while True:
        # 4. USe look to collect the connection from client and provide service
        # accept method: If the system call is interrupted and the signal handler does not raise an exception, the method now retries the system call instead of raising an InterruptedError exception.
        # The return value is a pair (conn, address) where conn is a new socket object usable to send and receive data on the connection, and address is the address bound to the socket on the other end of the connection.
        client, addr = server.accept()
        # 5. Send data
        client.send(str(datetime.now()).encode('utf-8'))
        # 6. Close the connection
        client.close()

if __name__ == '__main__':
    main()