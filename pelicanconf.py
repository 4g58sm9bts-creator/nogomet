AUTHOR = 'Ante Paro'
SITENAME = 'Nogomet iznutra'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Zagreb'
DEFAULT_LANG = 'hr'

THEME = 'theme'

ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

STATIC_PATHS = ['images']

DEFAULT_PAGINATION = 6

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = [
    ('Početna', '/'),
    ('Taktika', '/pages/taktika.html'),
    ('Zašto trener', '/pages/zasto-trener.html'),
    ('Greške', '/pages/greske.html'),
    ('Rječnik', '/pages/rjecnik.html'),
]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}

RELATIVE_URLS = True
