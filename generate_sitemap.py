#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

from lxml import etree

from os import walk
from os import stat

from os.path import abspath
from os.path import dirname
from os.path import join

from pytz import timezone

from re import match


class Generator:
    def __init__(self):
        current = dirname(abspath(__file__))

        self.__content_path = join(current, 'content')
        self.__output_path = join(current, 'output')
        self.__sitemap_path = join(self.__output_path, 'sitemap.xml')
        self.__base_url = 'https://ryoka419319.github.io'
        self.__changefreq = 'monthly'
        self.__tree = None
        self.__urlset = None

    def __find(self, dirpath):
        for curDir, dirs, filenames in walk(dirpath):
            for filename in filenames:
                yield join(curDir, filename)

    def __add_header(self):
        urlset_nsmap = {'xsi' : 'http://www.w3.org/2001/XMLSchema-instance'}

        self.__urlset = etree.Element('urlset', nsmap = urlset_nsmap)
        self.__urlset.attrib['xmlns'] = 'http://www.sitemaps.org/schemas/sitemap/0.9'

        self.__tree = etree.ElementTree(element=self.__urlset)

    def __add_url(self, loc, priority, lastmod, changefreq):
        url_elm = etree.SubElement(self.__urlset, 'url')

        loc_elm = etree.SubElement(url_elm, 'loc')
        loc_elm.text = loc

        priority_elm = etree.SubElement(url_elm, 'priority')
        priority_elm.text = str(priority)

        lastmod_elm = etree.SubElement(url_elm, 'lastmod')
        lastmod_elm.text = lastmod

        changefreq_elm = etree.SubElement(url_elm, 'changefreq')
        changefreq_elm.text = changefreq

    def generate(self):
        self.__add_header()
        jst = timezone('Japan')

        for path in self.__find(self.__output_path):
            if not match(r'.*\.html$', path):
                continue
            rel_path = path[len(self.__output_path):]

            if rel_path == '/index.html':
                url = '{0}/'.format(self.__base_url)
                priority = 1.0
            else:
                url = '{0}{1}'.format(self.__base_url, rel_path)
                priority = 0.8

            dt = datetime.fromtimestamp(stat(path).st_mtime).replace(tzinfo=timezone('Asia/Tokyo'))
            lastmod = dt.isoformat()

            self.__add_url(url, priority, lastmod, self.__changefreq)

        self.__tree.write(self.__sitemap_path, encoding='utf-8', xml_declaration=True, pretty_print=True)


if __name__ == '__main__':
    g = Generator()
    g.generate()

