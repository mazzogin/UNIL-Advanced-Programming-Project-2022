import requests
from bs4 import BeautifulSoup
from random import choice


def get_proxies():
    """
    get_proxies downloads free proxies from a github repo and directly parses them into usable data.

    Calling this function will get you the newest data on the website, since it's updated regularly.
    """
    proxy_url = 'https://github.com/clarketm/proxy-list/blob/master/proxy-list-raw.txt'
    r = requests.get(proxy_url)
    soup = BeautifulSoup(r.content, "html.parser").find_all("td", {"class":"blob-code blob-code-inner js-file-line"})
    proxies = [proxy.text for proxy in soup]
    return proxies

def get_random_proxies(proxies):
    """
    Randomizes the order of the proxies that are downloaded using get_proxies and puts them into
    a dictionary format.
    
    Proxies inside a dictionary can be passed directly into a GET request (similar to the header).
    """
    return {"https": choice(proxies)}

proxies = get_proxies()

def get_working_proxies():
    """
    Will go through 20 proxies in randomized order and check whether the requests_status_code == 200.
    If the status_code is 200 it means that connection to a website (here it is google) was successful.

    Assigning get_working_proxies() to a variable will make the usable proxies callable.
    """
    working = []
    for i in range(20):
        proxy = get_random_proxies(proxies)
        print(f"using {proxy}...")
        try:
            r = requests.get("https://www.google.com" ,proxies = proxy, timeout=3)
            if r.status_code == 200:
                working.append(proxy)
            print(r.status_code)
        except:
            pass
    return working

get_working_proxies()

# proxy = choice(get_working_proxies())

# requests.get(url, proxies = proxy)