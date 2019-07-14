#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Maarten Tegelaers'
COPYRIGHT = 'Maarten Tegelaers'
SITENAME = "Monty's Blog"
SITEURL = 'http://localhost:8000'

PATH = 'content'
THEME='theme/rubber-squid/'
ARTICLE_PATHS = ['articles']

TIMEZONE = 'Europe/Paris'

DIRECT_TEMPLATES = ['index']

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('https://nl.linkedin.com/in/maartentegelaers', 'fa-linkedin-in'),
          ('https://github.com/BeardedPlatypus',          'fa-github'),
          ('https://www.youtube.com/user/Month3d',        'fa-youtube')
         )

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

OUTPUT_PATH = 'preview/'

PLUGIN_PATHS = ["./plugins/",]
PLUGINS = ["summary.summary",
          ]

# Currently not supported, as such we do not want to generate them.
AUTHOR_SAVE_AS = ''
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''

SUMMARY_USE_FIRST_PARAGRAPH = True
