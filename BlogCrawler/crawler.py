#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : <2020-03-16 Mon 04:18>
# @Author  : Ynjxsjmh
# @Link    : https://github.com/ynjxsjmh
# @Version : v2.1

import os
import re
import json
import time
import datetime
import requests
from bs4 import BeautifulSoup

page_num = 16
dst_dir = "CSDN"
img_dir = "images"
img_link_tml = "https://raw.githubusercontent.com/Ynjxsjmh/ynjxsjmh.github.io/master/img/{0:04d}/{1:02d}/{2}{3}"
headers = {
    "cookie": "",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
}


def request_article_list(page=1):
    """
    获取博客列表
    主要包括博客的id以及发表时间等
    """
    url = f'https://blog-console-api.csdn.net/v1/article/list?page={page}&pageSize=20'

    response = requests.get(url=url, headers=headers)
    response = json.loads(response.text)
    article_list = response["data"]["list"]

    return article_list


def request_md(blog_id, date, status):
    """获取博文的json数据"""

    url = f"https://blog-console-api.csdn.net/v1/editor/getArticle?id={blog_id}"
    response = requests.get(url=url, headers=headers)
    response = json.loads(response.text)

    write_as_md(response, date, status)


def download_img(img_url, img_loc, img_name):
    """
    1. 如果图片没有下载过，下载
    2. 如果图片下载过，什么都不做
    """
    img_suffix = ".error"

    img_suffixs = [".png", ".jpg", ".gif"]
    for suffix in img_suffixs:
        img_path = os.path.join(img_loc, img_name + suffix)

        if os.path.isfile(img_path):
            return suffix

    response = requests.get(img_url)
    img_mime = response.headers["content-type"]
    img_data = response.content

    if img_mime.endswith("png"):
        img_suffix = img_suffixs[0]
    elif img_mime.endswith("jpeg"):
        img_suffix = img_suffixs[1]
    elif img_mime.endswith("gif"):
        img_suffix = img_suffixs[2]
    else:
        pass

    if not ("." in img_name):
        img_name = img_name + img_suffix

    img_path = os.path.join(img_loc, img_name)
    os.makedirs(os.path.dirname(img_path), exist_ok=True)
    with open(img_path, "wb") as handler:
        handler.write(img_data)
        time.sleep(3)

    return img_suffix


def parse_img(content):
    img_links = []

    md_img_regex = "!\[[^\]]*\]\(([^\)]*)\)"
    md_img_links = re.findall(md_img_regex, content)

    img_links.extend(md_img_links)

    soup = BeautifulSoup(content, "html.parser")
    html_imgs = soup.findAll("img")

    for html_img in html_imgs:
        html_img_link = html_img["src"]
        img_links.append(html_img_link)

    for img_link in img_links:
        # 有这么几种link
        # 1. img-blog.csdn.net 的无后缀
        # 2. img-blog.csdnimg.cn 有后缀
        # 3. imgconvert.csdnimg.cn 转换后的，图片名没意义（而且这个api不应该返回它）
        # 4. 已经托管在 github 上的
        # 5. 别人的图

        if "github" in img_link:
            continue

        if not ("csdn" in img_link):
            continue

        if not ("http" in img_link):
            img_link = "http:" + img_link

        no_wm = img_link.split("?")[0]
        print(f"  Parsing {img_link} ...")
        img_name = no_wm.split("/")[-1]

        if "convert" in img_link:
            after_name = img_name
            img_loc = os.path.join(*[dst_dir, img_dir])
        else:
            dt = datetime.datetime.strptime(img_name.split(".")[0], '%Y%m%d%H%M%S%f')
            after_name = "{0:04d}{1:02d}{2:02d}_{3:02d}{4:02d}{5:02d}_{6}".format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond)
            img_loc = os.path.join(*[dst_dir, img_dir, str(dt.year), dt.strftime('%m')])

        img_suffix = download_img(img_link, img_loc, after_name)

        if "convert" in img_link:
            # Only download it
            continue
        else:
            after_img_link = img_link_tml.format(dt.year, dt.month, after_name, img_suffix)

        content = content.replace(img_link, after_img_link)

    return content


def write_as_md(data, date, status):
    """
    将获取的json数据解析为markdown格式
    有markdown 保存为 markdown，没有则保存为HTML
    """
    title = re.sub("[/:\*\?\"<>|]", " ", data["data"]["title"])
    orginal_link = data["data"]["original_link"]
    categories = data["data"]["categories"].replace("#", "").replace(" ", "")
    tags = data["data"]["tags"]
    # 页面唯一标识符，用于统计系统和评论系统
    key = "key" + str(int(datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").timestamp()))

    meta = """---
layout:     post
title:      {0}
subtitle:
date:       {1}
author:     在到处之间找我
header-img: img/post-default-bg.jpg
link:       {2}
category:   [{3}]
tags:       [{4}]
key:        {5}
---\n\n\n""".format(data["data"]["title"], date, orginal_link, categories, tags, key)

    if status == "2":
        atype = "（草稿）"
    elif status == "63":
        atype = "（私密）"
    else:
        atype = ""

    date = date.split(" ")[0].split("-")
    name = f"{date[0]}-{date[1]}-{date[2]}-{atype}{title}"
    markdowncontent = data["data"]["markdowncontent"].replace("@[toc]", "")

    if len(markdowncontent) <= 0:
        content = data["data"]["content"].replace("↵", "\n")
        file_type = "html"
    else:
        content = markdowncontent
        file_type = "md"

    content = parse_img(content)

    file_name = f"{dst_dir}/{name}.{file_type}"

    try:
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(meta + content)

        print(f"写入 {name}")
    except OSError:
        file_error_name = f"{dst_dir}/{date[0]}-{date[1]}-{date[2]}-filename-error.{file_type}"
        os.makedirs(os.path.dirname(file_error_name), exist_ok=True)
        with open(file_error_name, "w", encoding="utf-8") as f:
            f.write(meta + content)

        print(f"写入 {file_error_name}")


def crawl(total_pages, start=1):
    """
    获取博客列表，包括id，时间
    获取博客内容数据
    """
    articles = []

    for page in range(start, total_pages + 1):
        articles.extend(request_article_list(page))

    print(f"You have {len(articles)} posts")

    for article in articles:
        article_id = article["ArticleId"]
        date = article["PostTime"].replace("日", "")
        date = re.sub("[年月]", "-", date)
        # status 64 私密
        # status 2 草稿
        # status 1 公开
        status = article["Status"]
        request_md(article_id, date, status)
        time.sleep(1)


if __name__ == '__main__':
    crawl(page_num)
