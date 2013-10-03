
PATH_CRHOME_DRIVER	= '/usr/lib64/chromium-browser/chromedriver'

VERSION = 'v4-sql'
LINK_BASE = '%s.historypin-hrd.appspot.com' % (VERSION)
# LINK_BASE = 'historypin.com'

URL_BASE = 'http://www.%s' % LINK_BASE

IS_ON_SDK = not (LINK_BASE.endswith('.appspot.com') or LINK_BASE.endswith('.historypin.com'))

if VERSION == 'v4-sql':
	ID_COLLECTION	= 6399
	ID_TOUR			= 1706
	
	ID_COLLECTION_VIEW	= 22782015  # SQL
	ID_TOUR_VIEW		= 22354015  # SQL
	
	ID_COLLECTION_IMAGES	= [322003, 2090034, 22363018, 26162010]
	# HP - 322003 - Morden College east elevation and chapel, 2090034- Pinner High St from Church, 22363018 - National Theatre in Sofia, Bulgaria, 26162010 - Bulgarian Army Theater [322003, 2090034, 22363018, 26162010]
	# SQL - - Morden College east elevation and chapel, - Pinner High St from Church, - National Theatre in Sofia, Bulgaria, - Bulgarian Army Theater [ids from SQL]
	
	ID_TOUR_IMAGES			= [322003, 2090034, 22363018, 26162010]
	
	# HP - 322003 - Morden College east elevation and chapel, 2090034- Pinner High St from Church, 22363018 - National Theatre in Sofia, Bulgaria, 26162010 - Bulgarian Army Theater [322003, 2090034, 22363018, 26162010]
	# SQL - - Morden College east elevation and chapel, - Pinner High St from Church, - National Theatre in Sofia, Bulgaria, - Bulgarian Army Theater [ids from SQL]
	
	FAVOURITE_CHANNELS			= [7947312, 6994288, 10668143]  # SQL -
	FAVOURITE_CHANNELS_IMAGES	= [7947312, 6994288, 10668143]  # SQL -
	
	ID_USER			= 84568
	ID_USER_VIEW	= 82832
	
	ID_MAP_ITEM		= 22363018  # SQl
	ID_EDIT_ITEM	= 26162010  # SQl
	
	ID_PROJECTS			= [3, 5, 6, 8, 10, 15, 22, 26, 34, 39, 41]
	ID_PROJECTS_IMAGES	= [11461010, 11462012, 11483012, 11499008, 11886013, 13388066, 13839007, 15742010, 16690005, 23580013, 30128133]  # SQL
else:
	ID_COLLECTION	= 26157007
	ID_TOUR			= 16502051
	
	ID_COLLECTION_VIEW	= 22782015  # when not logged in
	ID_TOUR_VIEW		= 22354015
	
	ID_COLLECTION_IMAGES	= [322003, 2090034, 22363018, 26162010]
	# HP - 322003 - Morden College east elevation and chapel, 2090034- Pinner High St from Church, 22363018 - National Theatre in Sofia, Bulgaria, 26162010 - Bulgarian Army Theater [322003, 2090034, 22363018, 26162010]
	# SQL - - Morden College east elevation and chapel, - Pinner High St from Church, - National Theatre in Sofia, Bulgaria, - Bulgarian Army Theater [ids from SQL]
	
	ID_TOUR_IMAGES			= [322003, 2090034, 22363018, 26162010]
	
	# HP - 322003 - Morden College east elevation and chapel, 2090034- Pinner High St from Church, 22363018 - National Theatre in Sofia, Bulgaria, 26162010 - Bulgarian Army Theater [322003, 2090034, 22363018, 26162010]
	# SQL - - Morden College east elevation and chapel, - Pinner High St from Church, - National Theatre in Sofia, Bulgaria, - Bulgarian Army Theater [ids from SQL]
	
	FAVOURITE_CHANNELS			= [7947312, 6994288, 10668143]
	FAVOURITE_CHANNELS_IMAGES	= [7947312, 6994288, 10668143]
	
	ID_USER			= 11675544
	ID_USER_VIEW	= 10649049
	
	ID_MAP_ITEM		= 22363018
	ID_EDIT_ITEM	= 26162010
	
	ID_PROJECTS			= [11461010, 11483012, 11499008, 11886013, 13388066, 13839007, 15742010, 16690005, 23580013, 39, 30128133]
	ID_PROJECTS_IMAGES	= [11462012, 11483012, 11499008, 11886013, 13388066, 13839007, 15742010, 16690005, 23580013, 30128133]


URL_ATTACH = URL_BASE + '/attach/uid%d' % ID_USER
