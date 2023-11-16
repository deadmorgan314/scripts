import requests
from conf import *
import time

def request(url, proxies, headers):
    response = requests.get(url=url, proxies=proxies, headers=headers, verify=False)
    print(response.status_code)
    time.sleep(2)


for i in range(iterations):
    request(url, proxies, headers)

