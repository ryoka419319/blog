#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import *

from argparse import ArgumentParser

from os.path import abspath
from os.path import dirname
from os.path import join

from subprocess import Popen

from sys import exit


class Operator:
    def __init__(self):
        current = dirname(abspath(__file__))

        self.__blog = {
            "src": join("/", "Users", "rkamikaw", "vscode", "blog"),
            "dst": join(current, "content"),
            }

    def __cmd(self, cmd: Text):
        print(cmd)
        Popen(cmd, shell=True).wait()

    def install(self):
        pips: List = [
            "pelican",
            "Markdown",
            "ghp-import",
            ]
    
        pip_txt: Text = " ".join(pips)
    
        self.__cmd(f"pip install --user {pip_txt}")

    def update(self):
        self.__cmd(f"rm {self.__blog['dst']}/*")
        self.__cmd(f"cp -v {self.__blog['src']}/* {self.__blog['dst']}/")
        self.__cmd("make html")
        self.__cmd("ghp-import output")
        self.__cmd("git push https://github.com/ryoka419319/ryoka419319.github.io.git gh-pages:master")


if __name__ == "__main__":
    def parse_args():
        parser = ArgumentParser(description="Operation for blog.")

        parser.add_argument(
            "operation",
            action="store",
            help="Operation."
            )

        return parser.parse_args()

    args = parse_args()
    o = Operator()

    method = getattr(o, args.operation)
    method()
