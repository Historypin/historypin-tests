
PATH_CRHOME_DRIVER	= '/usr/lib64/chromium-browser/chromedriver'
GO_TIMEOUT = 1

# VERSION = 'v5-europeana-filter'
# VERSION = 'v5-01-07'
# VERSION = 'http://www.historypin.com'
# LINK_BASE = '%s.historypin-hrd.appspot.com' % (VERSION)
LINK_BASE = 'historypin.dev'

URL_BASE = 'http://www.%s' % LINK_BASE

URL_BLOB = 'http://v5-blob.historypin-hrd.appspot.com'

IS_ON_SDK = not (LINK_BASE.endswith('.appspot.com') or LINK_BASE.endswith('.historypin.com'))

ID_COLLECTION	= 3033
ID_TOUR			= 1706

ID_COLLECTION_VIEW	= 2967
ID_TOUR_VIEW		= 2995

ID_COLLECTION_IMAGES		= [160180, 149729]
ID_COLLECTION_IMAGES_BLOB	= ['AMIfv97BxDC3KgRVI9L-A9fGaB8xSYMHSHNEozcXaKK6ou2jaoH7YATeoXhvssu7BiJfd1oi_luVHeht-P_-I_v0AIKisr7nVBHRSBfV8TJNDWkI7EttyQ1kJb315oV6yG8jDvA6z0QBif4oIlwW19RrB0Utj7hTkh3aGW4FVibtNAHdgwLz2w0',
			'AMIfv97wumUW0cEPpZEKoM6-7E1LA3MAqhCicEtBuPmiFKZCgnO2KBsNDvL1qnRgz_5TAe6-hgdPXw8EpLzOYnqDwILvEltSIV-zxpkzj95JMnOBgwdQakl0UoRM4Sa1AFOZJ_m_awrwKi9IlQgZ6_KDHobqSPDTs_hD--sSGhi-6o5OUFFmZIc']

ID_TOUR_IMAGES		= [160180, 149729]
ID_TOUR_IMAGES_BLOB	= ['AMIfv97BxDC3KgRVI9L-A9fGaB8xSYMHSHNEozcXaKK6ou2jaoH7YATeoXhvssu7BiJfd1oi_luVHeht-P_-I_v0AIKisr7nVBHRSBfV8TJNDWkI7EttyQ1kJb315oV6yG8jDvA6z0QBif4oIlwW19RrB0Utj7hTkh3aGW4FVibtNAHdgwLz2w0',
			'AMIfv97wumUW0cEPpZEKoM6-7E1LA3MAqhCicEtBuPmiFKZCgnO2KBsNDvL1qnRgz_5TAe6-hgdPXw8EpLzOYnqDwILvEltSIV-zxpkzj95JMnOBgwdQakl0UoRM4Sa1AFOZJ_m_awrwKi9IlQgZ6_KDHobqSPDTs_hD--sSGhi-6o5OUFFmZIc']


FAVOURITE_CHANNELS			= [26288, 14950, 33328]
FAVOURITE_CHANNELS_IMAGES	= [26288, 14950, 33328]

ID_USER			= 35019
ID_USER_VIEW	= 33283

ID_MAP_ITEM		= 149729
ID_EDIT_ITEM	= 160180

ID_PROJECTS			= [3, 5, 6, 8, 10, 15, 22, 26, 34, 39, 41, 42, 43, 44, 49]
ID_PROJECTS_IMAGES	= [3, 5, 6, 8, 10, 15, 22, 26, 34, 39, 41, 42, 43, 44, 49]

# TODO change the ids after migration
CHANNELS_EXAMPLES = [2238022, 8721093, 2662022, 6487189, 1042029]

# TODO change the ids after migration
COLLECTION_EXAMPLES	= [3762008, 6600998, 7700038, 8798159, 8691041]
TOUR_EXAMPLES		= [8279489, 6631649, 7764038, 8748071, 6605903]

URL_ATTACH = '%s/attach/uid%d' % (URL_BASE, ID_USER)

