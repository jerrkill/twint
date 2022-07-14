import time
import requests

def get_ip():
    # 获取ip地址的网站
    url = 'https://api.ipify.org?format=json'
    # 9050端口是tor的端口，我们通过tor访问网站
    proxies = {'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'}

    r = requests.get(url, proxies=proxies)
    print('当前ip: %s' % r.text)


def main():
    # 一直循环
    while True:
        # 获取ip
        get_ip()
        # 等待10秒
        time.sleep(10)

if __name__ == "__main__":
    main()