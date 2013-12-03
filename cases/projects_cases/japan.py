# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_Japan(HPTestCase, Attach):
	
	PROJECT_URL = '/project/39-japan-project'
	ATTACH_URL = '/jp/attach'
	
	ATTACH_TABS = [
		['%s/photos/index/' % (PROJECT_URL), '%s/photos/gallery/' % PROJECT_URL],
	]
	
	test_attach_tabs	= Attach.attach_tabs
	test_tab_map		= Attach.attach_tab_map
	test_tab_gallery	= Attach.attach_tab_gallery
