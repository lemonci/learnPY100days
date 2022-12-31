from socket import socket
from json import loads
from base64 import b64decode

def main():
    client = socket()
    client.connect(('192.168.2.98', 5566))
    # define an object to save binary data
    in_data = bytes()
    # Receive 1024 bytes each time, since we don't know how much data the server is sending
    data = client.recv(1024)
    while data:
        # concatenate the data received
        in_data += data
        data = client.recv(1024)
    # convert the binary data into JSON then into dictionary
    # The function loads is used to convert a JSON string into a dictionary object
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('/Users/Lemonci/Pictures/'+filename, 'wb') as f:
        # Decode the base64 file into binary and write into a file
        f.write(b64decode(filedata))
    print('The image is saved.')

if __name__ == '__main__':
    main()