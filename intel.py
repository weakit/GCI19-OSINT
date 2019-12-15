#!/usr/bin/env python3
import requests as r
from random import choice

username = ''
UAs = [  # user agents
    'Mozilla Firefox Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/74.0.3729.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (PlayStation 4 5.55) AppleWebKit/601.2 (KHTML, like Gecko)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
]


def check_response(url):
    response = r.get(url, headers={'User-Agent': choice(UAs)})
    if response.status_code == 200:
        return True
    return False


def instagram(u):
    url = "https://www.instagram.com/" + u
    return check_response(url)


def reddit(u):
    url = "https://www.reddit.com/user/" + u
    return check_response(url)


def github(u):
    url = "https://github.com/" + u
    return check_response(url)


def twitter(u):
    url = "https://twitter.com/" + u
    return check_response(url)


def tumblr(u):
    url = "https://%s.tumblr.com/" % u
    return check_response(url)


def facebook(u):
    url = "https://graph.facebook.com/v5.0/" + u
    response = r.get(url, headers={'User-Agent': choice(UAs)})
    if response.status_code == 404:
        return False
    return True


if __name__ == '__main__':
    username = input("Enter a username: ")
    print("\nInstagram: " + ("Found" if instagram(username) else "Not found"))
    print("Facebook: " + ("Found" if facebook(username) else "Not found"))
    print("Reddit: " + ("Found" if reddit(username) else "Not found"))
    print("Github: " + ("Found" if github(username) else "Not found"))
    print("Twitter: " + ("Found" if twitter(username) else "Not found"))
    print("Tumblr: " + ("Found" if tumblr(username) else "Not found"))

