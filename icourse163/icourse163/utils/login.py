# -*- coding: utf-8 -*-
"""
This model help you to login the site,And the main function : login_session() will return a requests.session to do next.
"""
import requests
from http.cookies import SimpleCookie


def cookies_raw2jar(raw: str) -> dict:
    """
    Arrange Cookies from raw using SimpleCookies
    """
    cookie = SimpleCookie(raw)
    cookies = {}

    for key, morsel in cookie.items():
        cookies[key] = morsel.value

    return cookies


def get_login_session() -> requests.session():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        # 'Accept-Encoding': 'gzip, deflate',
        # 'Accept-Language': 'zh-CN,zh;q=0.8',
        # 'Content-Type': 'text/plain',
    }

    login_session = requests.Session()
    login_session.headers.update(headers)

    cookies = cookies_raw2jar(get_cookie_from_file())
    login_session.cookies.update(cookies)

    return login_session


def get_cookie_from_file():
    with open("cookie.txt", "r", encoding="utf-8-sig") as f:
        return f.readline()


if __name__ == "__main__":
    print(get_login_session())
