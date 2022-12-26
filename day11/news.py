import requests
import json


def main():
    resp = requests.get('http://api.tianapi.com/bulletin/?key=9cdf5e4721b060ec2d93eb044cacf553&num=10')
    data_model = json.loads(resp.text)
    # print(data_model)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main()