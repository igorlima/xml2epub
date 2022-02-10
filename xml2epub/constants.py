#!usr/bin/python3
# -*- coding: utf-8 -*-

import os

SUPPORTED_TAGS = {
    'a': ['href', 'id', 'name', 'class'],
    'b': ['id'],
    'big': [],
    'blockquote': ['id'],
    'body': [],
    'br': ['id'],
    'center': [],
    'cite': [],
    'code': [],
    'dd': ['id', 'title'],
    'del': [],
    'dfn': [],
    'div': ['align', 'id', 'bgcolor', 'class'],
    'em': ['id', 'title'],
    'font': ['color', 'face', 'id', 'size'],
    'head': [],
    'h1': ['id'],
    'h2': ['id'],
    'h3': ['id'],
    'h4': ['id'],
    'h5': ['id'],
    'h6': ['id'],
    'hr /': ['color', 'id', 'width'],
    'html': [],
    'i': ['class', 'id'],
    'img': ['align', 'border', 'height', 'id', 'src', 'width'],
    'img /': ['align', 'border', 'height', 'id', 'src', 'width'],
    'li': ['class', 'id', 'title'],
    'link': ['type', 'rel', 'href'],
    'ol': ['id'],
    'p': ['align', 'id', 'title'],
    'pre': ['class'],
    's': ['id', 'style', 'title'],
    'small': ['id'],
    'span': ['bgcolor', 'title', 'class'],
    'strike': ['class', 'id'],
    'strong': ['class', 'id'],
    'sub': ['id'],
    'sup': ['class', 'id'],
    'table': ['class', 'id', 'title'],
    'tbody': [],
    'td': [],
    'th': [],
    'thead': ['id'],
    'title': [],
    'tr': [],
    'u': ['id'],
    'ul': ['class', 'id'],
    'var': []
}
SINGLETON_TAG_LIST = [
    'area',
    'base',
    'br',
    'col',
    'command',
    'embed',
    'hr',
    'img',
    'input',
    'link',
    'meta',
    'param',
    'source',
]
CLASS_INCLUDE_LIST = [
    'side'
    'nav',
    'hidden',
    'hide',
    'edit',
    'audio',
    'video',
]
TAG_DELETE_LIST = [
    'aside',
    'nav',
    'link',
]
COVER_TITLE_LIST = [
    'cover', 'cover-image', 'ci', '封面', 'カバー', 'couverture',
    'Startseite', 'trải ra', 'ปิดบัง', '씌우다', 'обложка', 'التغطية'
]
xhtml_doctype_string = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">'
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
EPUB_TEMPLATES_DIR = os.path.join(BASE_DIR, 'epub_templates')
ANIMAL_PIC_DIR = os.path.join(BASE_DIR, "epub_cover/animals")
COVER_FONT_PATH = os.path.join(BASE_DIR, "epub_cover/LXGWWenKai-Regular.ttf")
COVER_COLOR_LIST = [
    '#c04851',
    '#5a1216',
    '#f1939c',
    '#7a7374',
    '#ee4866',
    '#621d34',
    '#681752',
    '#ad6598',
    '#1e131d',
    '#525288',
    '#2177b8',
    '#619ac3',
    '#baccd9',
    '#2f90b9',
    '#1ba784',
    '#57c3c2',
    '#2bae85',
    '#1a6840',
    '#add5a2',
    '#5e5314',
    '#fbda41',
    '#d2b42c',
    '#fecc11',
    '#f8d86a',
    '#b78d12',
    '#daa45a',
    '#fa7e23',
    '#f8b37f',
    '#f2481b',
    '#f33b1f',
    '#ac1f18',
    '#483332',
    '#4b2e2b',
]
