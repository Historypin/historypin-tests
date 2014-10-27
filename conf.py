
PATH_CRHOME_DRIVER	= '/usr/lib64/chromium-browser/chromedriver'
GO_TIMEOUT = 1

# VERSION = 'v5-europeana-filter'
# VERSION = 'explore-independance'
VERSION = 'v612-beta-5'
# LINK_BASE = 'historypin.org'
LINK_BASE = '{0}.historypin-hrd.appspot.com'.format(VERSION)

URL_BASE = 'http://www.{0}'.format(LINK_BASE)
URL_BLOB = 'http://www.{0}'.format(LINK_BASE)
PROTOCOL = URL_BASE.split('://')[0]


IS_ON_SDK	= not (LINK_BASE.endswith('.appspot.com') or LINK_BASE.endswith('historypin.com'))
IS_LIVE		= LINK_BASE.endswith('historypin.com') or LINK_BASE.endswith('historypin.org')

if IS_LIVE:
	URL_ROOT_JP		= 'http://www.historypin.jp'
	URL_BASE_JP		= 'http://www.historypin.jp/jp'
	URL_ROOT_1989	= 'http://www.europeana1989.eu'
	URL_BASE_1989	= 'http://www.europeana1989.eu/en'
	URL_BASE_FUJI	= '{0}/project/47-fujinomiya-project'.format(URL_BASE_JP)
else:
	URL_ROOT_JP		= URL_BASE
	URL_BASE_JP		= '{0}/jp/project/39-japan-project'.format(URL_BASE)
	URL_ROOT_1989	= URL_BASE
	URL_BASE_1989	= '{0}/en/project/34-1989'.format(URL_BASE)
	URL_BASE_FUJI	= '{0}/jp/project/47-fujinomiya-project'.format(URL_BASE)
	
# URL_ROOT_JP			= 'http://www.historypin.jp' if IS_LIVE else URL_BASE
# URL_BASE_JP			= 'http://www.historypin.jp/jp' if IS_LIVE else URL_BASE + '/jp/project/39-japan-project'
# URL_BASE_1989			= 'http://www.europeana1989.eu' if IS_LIVE else URL_BASE
# URL_BASE_FUJINOMIYA	= '%s/project/47-fujinomiya-project' % URL_BASE_JP if IS_LIVE else URL_BASE + '/jp/project/47-fujinomiya-project'

ID_COLLECTION	= 3033
ID_TOUR			= 1706

ID_COLLECTION_VIEW	= 2967
ID_TOUR_VIEW		= 1989

ID_COLLECTION_IMAGES	= [160180, 149729]

ID_TOUR_IMAGES			= [160180, 149729]


FAVOURITE_CHANNELS			= [26288, 14950, 33328]
FAVOURITE_CHANNELS_IMAGES	= [26288, 14950, 33328]

ID_USER			= 35019
ID_USER_VIEW	= 33283

ID_MAP_ITEM			= 149729
ID_EDIT_ITEM		= 160180
# ID_FAVOURITE_ITEM	= 210086

ID_PROJECTS			= [3, 5, 6, 8, 10, 15, 22, 26, 34, 39, 40, 41, 42, 43, 44, 49, 51]
ID_PROJECTS_IMAGES	= [3, 5, 6, 8, 10, 15, 22, 26, 34, 39, 40, 41, 42, 43, 44, 49, 51]

# TODO change the ids after migration
CHANNELS_EXAMPLES = [6207, 30008, 7673, 11752, 81]

# TODO change the ids after migration
COLLECTION_EXAMPLES	= [21, 44, 498, 1113, 1050]
TOUR_EXAMPLES		= [540, 19, 252, 644, 4]

URL_ATTACH = '{0}/attach/uid{1}'.format(URL_BASE, ID_USER)

