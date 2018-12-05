#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

from glob import glob

from os import environ
from os import system

from os.path import abspath
from os.path import basename
from os.path import dirname
from os.path import getctime
from os.path import isfile
from os.path import join

from sys import exit


if __name__ == "__main__":
    current = join(dirname(abspath(__file__)))
    root = join(environ["HOME"], "Desktop")

    now = datetime.now()
    date = now.date()

    src = None

    try:
        file_list = glob("{0}/スクリーンショット {1}*".format(root, date))
        latest_file = max(file_list, key=getctime)
        src = latest_file
    except ValueError:
        pass

    if src is None:
        for name in glob("{0}/IMG_*.png".format(root)):
           src = name

    if src is None:
        print('Not found {0}/スクリーンショット {1}* or {0}/IMG_*.png'.format(root, date))
        exit(1)

    number = 0
    for name in glob('{0}/img_chromedevsummitday2/chrome_dev_summit_*.png'.format(current)):
        name = basename(name)
        n = int(name[18:-4])
        if number < n:
            number = n

    number += 1
    path = "img_chromedevsummitday2/chrome_dev_summit_{0}.png".format(number)
    dst = "{0}/{1}".format(current, path)

    system("mv -v \"{0}\" \"{1}\"".format(src, dst))

    system('echo \"{0}\" | pbcopy'.format(path))
