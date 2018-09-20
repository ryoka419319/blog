#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import abspath
from os.path import dirname
from os.path import join

from subprocess import Popen


def cmd(cmd):
    Popen(cmd, shell=True).wait()


if __name__ == "__main__":
    current = dirname(abspath(__file__))

    src = join("/", "Users", "rkamikaw", "vscode", "blog")
    dst = join(current, "content")

    cmd("cp -v {0}/* {1}/".format(src, dst))
    cmd("make html")
    cmd("ghp-import output")
    cmd("git push https://github.com/ryoka419319/ryoka419319.github.io.git gh-pages:master")
