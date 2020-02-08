#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from zipfile import *
import re
import codecs
import traceback
from datetime import datetime
from bs4 import BeautifulSoup


def main():
    cwd = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(cwd)

    tags, all_links, all_images, all_titles = get_all_tags('../../html/tags')

    for tag, links, images, titles in zip(tags, all_links, all_images, all_titles):
        if not os.path.exists(cwd + '\\result'):
            os.makedirs(cwd + '\\result')
        os.chdir(cwd + '\\result')

        print(cwd)
        book_name = '编程随想 - {}'.format(decode_tag(tag))
        epub_file = '{}.epub'.format(book_name)
        if os.path.exists(epub_file) :
            os.remove(epub_file)

        print('\ngenerating {}'.format(epub_file))

        zf = ZipFile(epub_file, 'w', ZIP_DEFLATED)
        os.chdir(cwd)

        for folder in ['./conf/', '../../html/'] :
            os.chdir(os.path.join(cwd, folder))
            add_folder(zf, '.', None, links, images)

        ncx = create_ncx(book_name, links, titles)
        with codecs.open('program-think.ncx', 'w', 'utf-8-sig') as f:
            f.write(ncx)
        zf.write('program-think.ncx')

        opf = create_opf(book_name, links, images)
        with codecs.open('program-think.opf', 'w', 'utf-8-sig') as f:
            f.write(opf)
        zf.write('program-think.opf')

        zf.close()

        print('\n{} OK'.format(epub_file))

    return 0


def get_all_tags(folder):
    tags = []
    all_links = []
    all_images = []
    all_titles = []
    children = os.listdir(folder)

    for name in children:
        tag = '.'.join(name.split('.')[:-1])
        tags.append(tag)

        name = os.path.join(folder, name)

        os.chdir(folder)

        soup = BeautifulSoup(open(name, 'rb'), "html.parser")

        links = []
        images = []
        titles = []
        div = soup.find("div", {"class": "post"})

        for h3 in div("h3"):
            for link in h3("a"):
                titles.append(link.text)
                link = link.get("href")
                images.extend(get_all_images(link))
                link = link.replace('.', '', 1)
                link = link.replace('/', '\\')
                links.append(link)

        all_links.append(links)
        all_images.append(images)
        all_titles.append(titles)

        print("Collect tag {} Done".format(tag))

    return tags, all_links, all_images, all_titles


def get_all_images(file):
    soup = BeautifulSoup(open(file, 'rb'), "html.parser")
    images = soup.findAll('img', {"src" : True})
    all_images = []
    for image in images:
        all_images.append(image['src'])
    return all_images


def decode_tag(tag):
    parts = tag.split('.')
    origin = []
    for part in parts:
        temp = ""
        try:
            temp = bytes.fromhex(part).decode('utf-8')
        except ValueError:
            temp = part
        finally:
            # File name couldn't contain slash
            temp = temp.replace('/', '')
            origin.append(temp)

    return '.'.join(origin)


def add_folder(zf, folder, count, target_files, target_images):
    info = ''

    if re.match(r'^\.(?:/|\\)20\d{2}$', folder):
        info = folder[-4:]
    elif re.match(r'^\.(?:/|\\)(?:archive|images|tags)$', folder):
        info = folder.split(os.sep)[-1]
    if info:
        print("~~~~~~~~~~~"+info)
        count = 0

    children = os.listdir(folder)
    children.sort()
    for name in children:
        name = os.path.join(folder, name)

        if os.path.isdir(name):
            count = add_folder(zf, name, count, target_files, target_images)
        elif name in target_files:
            zf.write(name)
        elif "images" in name and name.replace('\\', '/').replace('.', '../..') in target_images:
            zf.write(name)

            if count is not None:
                count += 1
                if (count % 10) == 0:  # optimize
                    sys.stdout.write(str(count)+' \r')
                    sys.stdout.flush()
        elif "css" in name:
            zf.write(name)
        elif "META-INF" in name or "mimetype" in name:
            zf.write(name)
        elif "cover" in name:
            zf.write(name)
        else:
            pass

    if info :
        print(str(count))
        return None
    else :
        return count


def create_opf(book_name, links, images):
    year = datetime.today().strftime('%Y')
    month = datetime.today().strftime('%m')
    today = datetime.today().strftime('%Y-%m-%d')
    metadata = """
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
    <dc:title>{0}</dc:title>
    <dc:identifier id="BookId" opf:scheme="URI">http://program-think.blogspot.com/{1}/{2}/</dc:identifier>
    <dc:language>zh</dc:language>
    <dc:creator opf:role="aut">编程随想</dc:creator>
    <dc:publisher>编程随想</dc:publisher>
    <dc:description>本书制作于 {3}
    （正常情况下，每个月都会更新，以包含俺博客上的所有博文）。
    要想【自动】获取俺博客的离线版本，请参见本电子书首页上的介绍（基于 BT Sync 自动同步）。
    </dc:description>
    <dc:subject>个人博客</dc:subject>
    <dc:source>http://program-think.blogspot.com/</dc:source>
    <dc:date opf:event="publication">{4}</dc:date>
    <dc:rights>本博客所有的原创文章，作者皆保留版权。转载博文必须包含本声明，保持博文的完整，并以超链接形式注明作者“编程随想”和该博文的原始网址</dc:rights>
    <dc:contributor></dc:contributor>
    <dc:type></dc:type>
    <dc:format></dc:format>
    <dc:relation></dc:relation>
    <dc:coverage></dc:coverage>
    <dc:builder>Script by program.think@gmail.com</dc:builder>
    <meta name="cover" content="cover-image" />
</metadata>
        """.format(book_name, year, month, today, today)

    itemref = ""
    idref = "    <itemref idref=\"post-{0}\" linear=\"yes\"/>\n"

    item = ""
    appli_template = "    <item id=\"post-{0}\" href=\"{1}\" media-type=\"application/xhtml+xml\" />\n"
    image_template = "    <item id=\"{0}\" href=\"{1}\" media-type=\"image/jpeg\" />\n"

    for link in links:
        itemref += idref.format(link[2:].replace("\\", "-").replace(".html", ""))
        item += appli_template.format(link[2:].replace("\\", "-").replace(".html", ""), link)

    for image in images:
        item += image_template.format(image.replace("../", "").replace("/", "-"), image.replace("../", ""))

    manifest = """
<manifest>
    <item id="ncx" href="program-think.ncx" media-type="application/x-dtbncx+xml" />
    <item id="cover-image" href="images/cover.jpg" media-type="image/jpeg" />
    <item id="css" href="css/program-think.css" media-type="text/css" />
{0}
</manifest>
        """.format(item)

    spine = """
<spine toc="ncx">
{}
</spine>
        """.format(itemref)

    opf = """
<?xml version="1.0" encoding="UTF-8" ?>
<package version="2.0" xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId">
{0}
{1}
{2}
<guide>
    <reference type="cover" title="封面" href="index.html" />
</guide>
</package>
        """.format(metadata, manifest, spine)

    return opf


def create_ncx(book_name, links, titles):
    """
    .ncx 文件是目录文件
    """
    year = datetime.today().strftime('%Y')
    month = datetime.today().strftime('%m')
    head = """
<head>
    <meta name="dtb:uid" content="http://program-think.blogspot.com/{0}/{1}/" />
    <meta name="dtb:depth" content="4" />
    <meta name="dtb:totalPageCount" content="0" />
    <meta name="dtb:maxPageNumber" content="0" />
    <meta name="dtb:generator" content="Python script by program.think@gmail.com" />
    <meta name="provider" content="program-think.blogspot.com" />
    <meta name="right" content="本博客所有的原创文章，作者皆保留版权。转载博文必须包含本声明，保持博文的完整，并以超链接形式注明作者“编程随想”和该博文的原始网址" />
</head>
        """.format(year, month)

    navPoint = ""
    navPoint_template = """
    <navPoint id="navPoint-{0}" playOrder="{1}">
        <navLabel>
            <text>{2}</text>
        </navLabel>
        <content src="{3}"/>
    </navPoint>
      """

    play_id = 0
    for link, title in zip(links, titles):
        navPoint += navPoint_template.format(play_id, play_id, title, link)
        play_id = play_id + 1

    ncx = """
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN" "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">
<ncx version="2005-1" xmlns="http://www.daisy.org/z3986/2005/ncx/" xml:lang="zh-CN">
{0}
<docTitle><text>{1}</text></docTitle>
<docAuthor><text>编程随想</text></docAuthor>
<navMap>
{2}
</navMap>
</ncx>
       """.format(head, book_name, navPoint)

    return ncx


if '__main__' == __name__:
    try:
        sys.exit(main())
    except Exception as err:
        print('Error:\n' + str(err))
        traceback.print_exc()
        sys.exit(1)
