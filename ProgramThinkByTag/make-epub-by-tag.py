#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from zipfile import *
import re
import traceback
from bs4 import BeautifulSoup


def main() :
    cwd = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(cwd)

    tags, all_links, all_images = get_all_tags('../../html/tags')

    for tag, links, images in zip(tags, all_links, all_images):
        if not os.path.exists(cwd + '\\result'):
            os.makedirs(cwd + '\\result')
        os.chdir(cwd + '\\result')

        print(cwd)

        epub_file = '编程随想 - {}.epub'.format(decode_tag(tag))
        if os.path.exists(epub_file) :
            os.remove(epub_file)

        print('\ngenerating {}'.format(epub_file))

        zf = ZipFile(epub_file, 'w', ZIP_DEFLATED)
        os.chdir(cwd)
        
        for folder in ['./conf/', '../../html/'] :
            os.chdir(os.path.join(cwd, folder))
            add_folder(zf, '.', None, links, images)
        zf.close()

        print('\n{} OK'.format(epub_file))

    return 0


def get_all_tags(folder):
    tags = []
    all_links = []
    all_images = []
    children = os.listdir(folder)

    for name in children:
        tag = '.'.join(name.split('.')[:-1])
        tags.append(tag)

        name = os.path.join(folder, name)

        os.chdir(folder)

        soup = BeautifulSoup(open(name, 'rb'), "html.parser")

        links = []
        images = []
        div = soup.find("div", {"class": "post"})

        for h3 in div("h3"):
            for link in h3("a"):
                link = link.get("href")
                images.extend(get_all_images(link))
                link = link.replace('.', '', 1)
                link = link.replace('/', '\\')
                links.append(link)

        all_links.append(links)
        all_images.append(images)

        print("Collect tag {} Done".format(tag))

    return tags, all_links, all_images


def get_all_images(file):
    soup = BeautifulSoup(open(file, 'rb'), "html.parser")
    images = soup.findAll('img', {"src":True})
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


def add_folder(zf, folder, count, target_files, target_images) :
    info = ''

    if re.match(r'^\.(?:/|\\)20\d{2}$', folder) :
        info = folder[-4:]
    elif re.match(r'^\.(?:/|\\)(?:archive|images|tags)$', folder) :
        info = folder.split(os.sep)[-1]
    if info :
        print("~~~~~~~~~~~"+info)
        count = 0

    children = os.listdir(folder)
    children.sort()
    for name in children :
        name = os.path.join(folder, name)

        if os.path.isdir(name) :
            count = add_folder(zf, name, count, target_files, target_images)
        elif name in target_files :
            zf.write(name)
        elif "images" in name and name.replace('\\', '/').replace('.', '../..') in target_images:
            zf.write(name)

            if count is not None :
                count += 1
                if (count % 10) == 0 :  # optimize
                    sys.stdout.write(str(count)+' \r')
                    sys.stdout.flush()
        elif "css" in name:
            zf.write(name)
        elif "META-INF" in name or "mimetype" in name:
            zf.write(name)
        else:
            pass

    if info :
        print(str(count))
        return None
    else :
        return count


if '__main__' == __name__ :
    try :
        sys.exit(main())
    except Exception as err :
        print('Error:\n' + str(err))
        traceback.print_exc()
        sys.exit(1)

