import os

PATH_CRHOME_DRIVER	= '/usr/lib64/chromium-browser/chromedriver'


KEY_COLLECTION		= '26157007'
KEY_TOUR			= '16502051'
# ID_TOUR			= 16502051
ID_USER = 11675544  # USER on HP - 84568


LINK_BASE = 'historypin.com'  #'v4-sql.historypin-hrd.appspot.com'
URL_BASE = 'http://www.%s' % LINK_BASE
URL_ATTACH = URL_BASE + '/attach/uid%d' % ID_USER
IS_ON_SDK = not (LINK_BASE.endswith('.appspot.com') or LINK_BASE.endswith('.historypin.com'))


# ID_USER = 11675544
