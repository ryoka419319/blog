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
            'img': join(current, 'img'),
            'output': join(current, 'output'),
            'logo': join(current, 'brutalist', 'logo'),
            }
        self.__generate_sitemap = join(current, 'generate_sitemap.py')

    def __cmd(self, cmd: Text):
        print(cmd)
        Popen(cmd, shell=True).wait()

    def install(self):
        pips: List = [
            'pelican',
            'Markdown',
            'ghp-import',
            'lxml',
            'pytz',
            ]

        pip_txt: Text = ' '.join(pips)

        self.__cmd('pip install --upgrade pip')
        self.__cmd(f'pip install --user {pip_txt}')

    def __get_ad_text(self):
        return '\n'.join([
            '',
            '<!-- Google AdSense -->',
            '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>',
            '<script>',
            '  (adsbygoogle = window.adsbygoogle || []).push({',
            '    google_ad_client: "ca-pub-6379280991526072",',
            '    enable_page_level_ads: true',
            '  });',
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
        self.__cmd('make html')
        self.__cmd(f'cp -rpv {self.__blog["img"]}/img_* {self.__blog["output"]}/')
        self.__cmd(f'cp -fv {self.__blog["logo"]}/favicon.ico {self.__blog["output"]}/')

    def upload(self):
        self.__cmd(f'{self.__generate_sitemap}')
        self.__insert_ad()
        self.__cmd('ghp-import output')
        self.__cmd('git push -f https://github.com/ryoka419319/ryoka419319.github.io.git gh-pages:master')


if __name__ == '__main__':
    def parse_args():
        parser = ArgumentParser(description='Operation for blog.')

        parser.add_argument(
            '--setup', '-s',
            action='store_true',
            default=False,
            help='Setup for this script.'
            )

        parser.add_argument(
            '--prepare', '-p',
            action='store_true',
            default=False,
            help='Make html from markdown.'
            )

        parser.add_argument(
            '--upload', '-u',
            action='store_true',
            default=False,
            help='Upload to GitHub'
            )

        parser.add_argument(
            '--release', '-r',
            action='store_true',
            default=False,
            help='Prepare and Upload'
            )

        return parser.parse_args()

    args = parse_args()
    o = Operator()

    if args.setup:
        o.install()
    elif args.prepare:
        o.prepare()
    elif args.upload:
        o.upload()
    elif args.release:
        o.prepare()
        o.upload()

