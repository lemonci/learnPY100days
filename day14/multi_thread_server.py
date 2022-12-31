from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread

def main():
    # customized thread class
    class FileTransferHandler(Thread):
        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'guido.jpg'
            # JSON is a plain-text format so it cannot carry binary data
            # The image needs to be base6-encoded
            my_dict['filedata'] = data
            # Use function dump to convert the dictionary into JSON string
            json_str = dumps(my_dict)
            # Send JSON string
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    # 1. Create a socket and specify which type of transmission to use
    server = socket()
    # 2. Bind the IP address and port(to distinguish between different services)
    server.bind(('192.168.2.98', 5566))
    # 3. Start listening - listen to the client to connect to the server
    server.listen(512)
    print('Server starts listening')
    with open('guido.jpg', 'rb') as f:
        # Convert binary data into base64 and then decode into string
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        # Start a thread to deal with the request from clinet
        FileTransferHandler(client).start()

if __name__ == '__main__':
    main()