import json

from selenium import webdriver
from bs4 import BeautifulSoup as bs


def build(single_proxy=None):
    # init profile
    profile = webdriver.FirefoxProfile()
    ipv4 = single_proxy.split(':')[0]
    port = int(single_proxy.split(':')[1])
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.socks", ipv4)
    profile.set_preference("network.proxy.socks_port", port)
    profile.set_preference("network.proxy.socks_version", 4)
    profile.update_preferences()

    # You would also like to block flash
    profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', False)
    profile.set_preference("media.peerconnection.enabled", False)

    # save to FF profile
    profile.update_preferences()
    driver = webdriver.Firefox(profile, executable_path=r"/home/nubonix/webdrivers/firefox/geckodriver")
    return driver


def url_generator():
    with open('urls.txt', 'r') as reader:
        for line in reader:
            url = line.replace('\n', '')
            # print(url)
            yield url


def parse(url, html):
    filename = 'data/' + url.split('/')[-1].replace('\n', '') + '.json'
    soup = bs(html, 'html.parser')
    res = soup.find(attrs={'id': 'item', 'class': ['tb-optimized'], 'type': 'application/json'})
    try:
        data = json.loads(res.contents[0])
    except AttributeError:
        return
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)


def main():
    driver = build()
    # driver.get('http://ipv4.icanhazip.com')
    for url in url_generator():
        driver.get(url)
        source = driver.page_source
        parse(url=url, html=source)


if __name__ == "__main__":
    main()
