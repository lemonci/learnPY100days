from time import time
from threading import Thread

import requests

# Inherit Class Thread to define a new thread class
class DownloadHanlder(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/Users/Lemonci/Pictures/' + filename, 'wb') as f:
            f.write(resp.content)

def main():
    # Use get in requests module to get the network resource
    # Use TianAPI to get data
    resp = requests.get(
        'https://apis.tianapi.com/dongman/index?key=5eee6da2e246f73ce2cc94c7d0ee3587&num=10'
    )
    # Parse the JSON data returned by the server into a dictionary
    data_model = resp.json()
    #print(data_model) # check the JSON format
    for mm_dict in data_model['result']['newslist']:
        url = mm_dict['picUrl']
        # use multithread to download
        DownloadHanlder(url).start()

if __name__ == '__main__':
    main()