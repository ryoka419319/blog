#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import *

from argparse import ArgumentParser

from os.path import abspath
from os.path import dirname
from os.path import join

from subprocess import Popen

from sys import exit

from glob import glob

from re import match


class Operator:
    def __init__(self):
        current = dirname(abspath(__file__))

        self.__blog = {
            'src': join('/', 'Users', 'rkamikaw', 'vscode', 'blog'),
            'dst': join(current, 'content'),
            'output': join(current, 'output'),
            'output_orig': join(current, 'output.orig'),
            }

    def __cmd(self, cmd: Text):
        print(cmd)
        Popen(cmd, shell=True).wait()

    def install(self):
        pips: List = [
            'pelican',
            'Markdown',
            'ghp-import',
            ]
    
        pip_txt: Text = ' '.join(pips)
    
        self.__cmd(f'pip install --user {pip_txt}')

    def __get_ad_text(self):
        return '\n'.join([
            '',
            '<!-- Google AdSense -->',
            '<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>',
            '<script>',
            '(adsbygoogle = window.adsbygoogle || []).push({',
            'google_ad_client: "ca-pub-6379280991526072"',
            'enable_page_level_ads: true',
            '});',
            '</script>',
            '<!--/ Google AdSense -->',
            '',
            ])

    def __insert_ad(self):
        for path in glob('{0}/*.html'.format(self.__blog["output"])):
            with open(path) as fd:
                blog = fd.readlines()

            with open(path, 'w') as fd:
                for line in blog:
                    if (match(r'</head>', line)):
                        fd.write(self.__get_ad_text())
                    fd.write(line)

    def prepare(self):
        self.__cmd(f'rm {self.__blog["output"]}/*')
        self.__cmd(f'rm {self.__blog["dst"]}/*')
        self.__cmd(f'cp -v {self.__blog["src"]}/* {self.__blog["dst"]}/')
        self.__cmd('make html')
        self.__cmd(f'cp -rv {self.__blog["src"]}/img_* {self.__blog["output"]}/')

    def upload(self):
        self.__cmd('ghp-import output')
        self.__cmd(f'cp -rv {self.__blog["output_orig"]}/* {self.__blog["output"]}/')
        self.__insert_ad()
        self.__cmd('git push https://github.com/ryoka419319/ryoka419319.github.io.git gh-pages:master')

    def release(self):
        self.prepare()
        self.upload()


if __name__ == '__main__':
    def parse_args():
        parser = ArgumentParser(description='Operation for blog.')

        parser.add_argument(
            'operation',
            action='store',
            help='Operation.'
            )

        return parser.parse_args()

    args = parse_args()
    o = Operator()

    method = getattr(o, args.operation)
    method()

