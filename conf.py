
PATH_CRHOME_DRIVER	= '/usr/lib64/chromium-browser/chromedriver'
GO_TIMEOUT = 1

VERSION = ''
# VERSION = 'explore-independance'
# VERSION = 'v617-beta-18'
VERSION = 'v628-beta-1'
# VERSION = 'v618-refac-format'
# LINK_BASE = 'historypin.org'
LINK_BASE = '{0}.historypin-hrd.appspot.com'.format(VERSION)

URL_BASE = 'http://www.{0}'.format(LINK_BASE)
URL_BLOB = 'http://www.{0}'.format(LINK_BASE)
PROTOCOL = URL_BASE.split('://')[0]


IS_ON_SDK	= not (LINK_BASE.endswith('.appspot.com') or LINK_BASE.endswith('historypin.com'))
IS_LIVE		= LINK_BASE.endswith('historypin.com') or LINK_BASE.endswith('historypin.org')


ID_USER			= 35019
ID_USER_VIEW	= 33283
ID_USER_EXPLORE	= 62442

