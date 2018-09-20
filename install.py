#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import abspath
from os.path import dirname
from os.path import join

from subprocess import Popen


def cmd(cmd):
    Popen(cmd, shell=True).wait()


if __name__ == "__main__":
    pips = ["pelican", "Markdown", "ghp-import"]

    cmd("pip install {0}".format(" ".join(pips)))
