#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : <2020-03-16 Mon 04:18>
# @Author  : Ynjxsjmh
# @Link    : https://github.com/ynjxsjmh
# @Version : v1.0

import os
import re
import json
import time
import datetime
import requests


page_num = 16
dst_dir = "CSDN"
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

    meta = """
---
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
---\n
    """.format(title, date, orginal_link, categories, tags, key)

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

    file_name = f"{dst_dir}/{name}.{file_type}"

    try:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(meta + content)

        print(f"写入 {name}")
    except OSError:
        file_error_name = f"{dst_dir}/{date[0]}-{date[1]}-{date[2]}-filename-error.{file_type}"
        with open(file_error_name, "w", encoding="utf-8") as f:
            f.write(meta + content)

        print(f"写入 {file_error_name}")


def crawl(total_pages):
    """
    获取博客列表，包括id，时间
    获取博客内容数据
    """
    articles = []

    for page in range(1, total_pages + 1):
        articles.extend(request_article_list(page))

    print(f"You have {len(articles)} posts");

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
    if not os.path.isdir(dst_dir):
        os.mkdir(dst_dir)
    crawl(page_num)
