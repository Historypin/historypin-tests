# -*- coding: utf-8 -*-

from base import *

class Map(HPTestCase):
	
	@url('/map/')
	def test_index(self):
		self.assertTitle('Historypin | Map')
		
		self.assertEqual('Search\nby place'										, self.e('.main-panel h1').text)
		self.assertIsInstance(self.e('#search-filters .input-container input')	, WebElement)
		
		button		= self.e('a#photo_search_submit')
		self.assertEqual('{0}/map/#'.format(URL_BASE), button.get_attribute('href'))
		self.assertEqual('Go'						, button.text)
		
		nav			= self.e('.filter-nav')
		self.assertEqual('Narrow down'				, nav.e('h2').text)
		self.assertEqual('by date'					, nav.e('p a.date').text)
		self.assertEqual('by subject'				, nav.e('p a.subject').text)
		
		check_cnt	= self.e('.check_container')
		self.assertIsInstance(check_cnt.e('input')	, WebElement)
		self.assertEqual('show thumbnails'			, check_cnt.e('label').text)
		
		fullscr		= self.e('#fullscreen-on a')
		self.assertEqual('Full\nScreen'				, fullscr.text)
		self.assertIn('ss-icon'						, fullscr.e('span').get_attribute('class'))
		self.assertIn('ss-scaleup'					, fullscr.e('span').get_attribute('class'))
		
		self.assertIsInstance(self.e('#map-canvas')	, WebElement)
	
	@url('/map/')
	def test_search_by_place(self):
		
		input_cnt = self.e('#search-filters .input-container input')
		input_cnt.click()
		sleep(1)
		
		input_cnt.send_keys('Sofia')
		sleep(1)
		
		self.e('.button.left').click()
		sleep(1)
		
		self.assertIn('42.697839,23.32167', '{0}/map/#!/geo:42.697839,23.32167/zoom:10/location:Sofia, Bulgaria/'.format(URL_BASE))
	
	@url('/map/')
	def test_search_by_date(self):
		
		self.e('a.date').click()
		
		search_bar = self.e_wait('.search-bar.by_date')
		self.assertIsInstance(search_bar	, WebElement)
		self.assertEqual('Refine by date'	, search_bar.e('h3').text)
		
		icons = self.es('.search-bar.by_date a span')
		self.assertIn('ss-icon'		, icons[0].get_attribute('class'))
		self.assertIn('ss-location'	, icons[0].get_attribute('class'))
		self.assertIn('ss-icon'		, icons[1].get_attribute('class'))
		self.assertIn('ss-location'	, icons[1].get_attribute('class'))
		
		self.assertEqual('1840', self.e('#from span').text)
		self.assertEqual('2015', self.e('#to span').text)
		
		labels		= ['1840', '1850', '1860', '1870', '1880', '1890', '1900', '1910', '1920', '1930', '1940', '1950', '1960', '1970', '1980', '1990', '2000']
		
		link_label	= self.es('#date-slider-labels a')
		
		for n in range(len(labels)): self.assertEqual(labels[n], link_label[n].text)
		
		date_from	= self.e_wait('#date-slider-labels li:nth-of-type(3) a')
		# date_to		= self.e_wait('#date-slider-labels li:nth-of-type(7) a')
		date_from.click()
		self.assertEqual('1860', date_from.text)
		# date_to.click()
		# self.assertEqual('1990', date_to.text)
		
		# TODO
		# set a date from(e.g. 1887) and date to (e.g. 2005)
		# check if the id='from' and span class has the 1887 value
		# check if the id='to' and span class has the 2005 value
		# assert that the date slider icon is on 1887
		# assert that the date slider icon is on 2005
		# assert if the URL is changing with selected years
		
		reset = self.e('a.reset')
		self.assertEqual('Some content is hidden (reset)', reset.text)
		self.double_click(reset)
	
	@url('/map/')
	def test_search_by_subject(self):
		
		self.e_wait('p a.subject').click()
		tag = self.e('.by_tag')
		self.assertEqual('Refine your results by subject'	, tag.e('h3').text)
		self.assertEqual('Search by keyword'				, tag.e('label').text)
		
		tag.e('.input-container input').send_keys('transport')
		
		refine = tag.e('.button.right')
		self.assertEqual('Refine', refine.text)
		refine.click()
		self.assertIn('tags:transport', '{0}/map/#!/geo:51.6,0.05/zoom:7/tags:transport/'.format(URL_BASE))
		
		reset = self.e('a.reset')
		self.assertEqual('Some content is hidden (reset)', reset.text)
		self.double_click(reset)
		
		# click on a photo cluster
		# - in "Details' tab, assert that in Tags section there is transport keyword
		# close the dialogue
		# click on a single photo marker
		# - in "Details' tab, assert that in Tags section there is transport keyword
		# close the dialogue
	
	@url('/map/')
	def test_fullscreen_map(self):
		
		self.e('#fullscreen-on a').click()
		
		main_panel = self.e('.main-panel a')
		self.assertEqual('{0}/'.format(URL_BASE), main_panel.get_attribute('href'))
		self.assertIn('fullscreen_logo', main_panel.get_attribute('class'))
		
		search_filters = self.e('#search-filters')
		self.assertEqual('Location'									, search_filters.e('label').text)
		self.assertIsInstance(search_filters.e('input')				, WebElement)
		self.assertIsInstance(self.e('#photo_search_submit span')	, WebElement)
		
		self.assertEqual('Narrow down'		, self.e('.filter-nav h2').text)
		
		fullscr_off = self.e('#fullscreen-off')
		self.assertEqual('Exit fullscreen'	, fullscr_off.text)
		self.assertIn('ss-icon'				, fullscr_off.e('span').get_attribute('class'))
		self.assertIn('ss-scaledown'		, fullscr_off.e('span').get_attribute('class'))
		
		fullscr_off.click()
	
	@url('/map/#!/geo:42.697839,23.32167/zoom:10/dialog:{0}/tab:details/'.format(ID_MAP_ITEM))
	def test_dialog_details(self):  # this test case fails only in the test suite
		sleep(15)  # ajax on success
		dlg = self.e('#info-dialog')
		self.assertEqual('{0}/services/thumb/phid/{1}/dim/2000x440/quality/80/'.format(URL_BASE, ID_MAP_ITEM), dlg.e('#details_cnt .image .main-img').get_attribute('src'))
		
		info = self.e('#details_cnt .info')
		self.assertEqual('National Theatre in Sofia, Bulgaria'				, info.e('h2.photo-title').text)
		sleep(3)
		self.assertEqual('ulitsa "Kuzman Shapkarev" 1-3, 1000 Sofia, Bulgaria', info.e('.photo-address').text)
		self.assertEqual('2 August 2012'							, info.e('.photo-date').text)
		
		# sleep(4) this element does not exist in the Details Tab
		# details_link = dlg.e('.open-tab-dialog')
		# self.assertEqual('{0}/map/#write-story_cnt' % URL_BASE	, details_link.get_attribute('href'))
		# self.assertEqual('Suggest more accurate details'		, details_link.text )
		
		about = dlg.e('.about')
		self.assertEqual('{0}/channels/img/{1}/logo/1/dim/46x46/'.format(URL_BASE, ID_USER_VIEW), about.e('img').get_attribute('src'))
		self.assertEqual('Pinned by\nGabss'														, about.e('p.pinned').text)
		self.assertEqual('{0}/channels/view/{1}/'				.format(URL_BASE, ID_USER_VIEW)	, about.e('p.pinned a').get_attribute('href'))
		self.assertEqual('This is a photo of National Theatre in Sofia, Bulgaria'				, about.e('p.photo-story-copy').text)
		
		self.assertEqual('Tags: national, theatre', dlg.e('.tags').text)
		keyword = dlg.es('.tags .photo-keywords a')
		self.assertEqual('{0}/map/#!/geo:42.697839,23.32167/zoom:10/dialog:{1}/tab:details/tags:national/'.format(URL_BASE, ID_MAP_ITEM), keyword[0].get_attribute('href'))
		self.assertEqual('{0}/map/#!/geo:42.697839,23.32167/zoom:10/dialog:{1}/tab:details/tags: theatre/'.format(URL_BASE, ID_MAP_ITEM), keyword[1].get_attribute('href'))
		
		actions = dlg.e('.bottom-actions')
		
		favourite = actions.e('.action.favourite span')
		self.assertIn('ss-icon', favourite.get_attribute('class'))
		self.assertIn('ss-heart', favourite.get_attribute('class'))
		
		report = actions.e('.action.report')
		self.assertEqual('{0}/contact-us/?report/#!/geo:42.697839,23.32167/zoom:10/dialog:{1}/tab:details/'.format(URL_BASE, ID_MAP_ITEM), report.get_attribute('href'))
		self.assertIn('ss-icon'	, report.e('span').get_attribute('class'))
		self.assertIn('ss-alert', report.e('span').get_attribute('class'))
		
		streetview = actions.e('.action.photo-view-on-streetview.sv-marker')
		self.assertEqual('{0}/map/#streetview_cnt'.format(URL_BASE), streetview.get_attribute('href'))
		self.assertEqual('Street View'						, streetview.text)
		
		fullscr = actions.e('.action.fullscr.right')
		self.assertEqual('  See Bigger', fullscr.text)
		self.assertIn('ss-icon'		, fullscr.e('span').get_attribute('class'))
		self.assertIn('ss-scaleup'	, fullscr.e('span').get_attribute('class'))
		fullscr.click()
		self.assertEqual('{0}/services/thumb/phid/{1}/dim/3000x500/quality/80/'.format(URL_BASE, ID_MAP_ITEM), self.e('#preview_cnt .image img').get_attribute('src'))
		
		self.assertEqual('Share:', dlg.e('h3').text)
		social_buttons = dlg.e('.addthis_toolbox span')
		self.assertIn('ss-icon', social_buttons.get_attribute('class'))
		
		social_icons = ['ss-social-circle', 'ss-social-circle', 'ss-social-circle', 'ss-plus']
		
		for n in range(len(social_icons)-1):
			self.assertIn(social_icons[n], social_buttons.get_attribute('class'))
		
		fullscr_off = actions.e('.action.see-smaller.right')
		self.assertEqual('  See Smaller'	, fullscr_off.text)
		self.assertIn('ss-icon'			, fullscr_off.e('span').get_attribute('class'))
		self.assertIn('ss-scaledown'	, fullscr_off.e('span').get_attribute('class'))
		fullscr_off.click()
		
		self.e('.action.photo-view-on-streetview.sv-marker[href$=streetview_cnt]').click()
		self.e('.list_tabs a[href$=details_cnt]').click()
		
	
	@url('/map/#!/geo:42.697839,23.32167/zoom:10/dialog:{0}/tab:details/'.format(ID_MAP_ITEM))
	def test_dialog_comments(self):
		
		dlg	= self.e('#info-dialog')
		tab	= dlg.e('#stories_cnt')
		
		sleep(2)
		self.e('.list_tabs a[href$=stories_cnt]').click()
		self.assertIn('tab:stories', '{0}/map/#!/geo:42.697839,23.32167/zoom:10/dialog:{1}/tab:stories/'.format(URL_BASE, ID_MAP_ITEM))
		
		sidebar						= dlg.e('.info.scrollbarfix')
		self.assertEqual('{0}/services/thumb/phid/{1}/dim/294x1000/' .format(URL_BASE, ID_MAP_ITEM)	, sidebar.e('.side-img ').get_attribute('src'))
		self.assertEqual('{0}/channels/img/{1}/logo/1/dim/46x46/'	.format(URL_BASE, ID_USER_VIEW)	, sidebar.e('.photo-user-avatar.avatar').get_attribute('src'))
		self.assertEqual('Pinned by: \nGabss'														, sidebar.e('.pinner p').text)
		self.assertEqual('{0}/channels/view/{1}/'					.format(URL_BASE, ID_USER_VIEW)	, sidebar.e('.pinner p a').get_attribute('href'))
		self.assertEqual('National Theatre in Sofia, Bulgaria'										, sidebar.e('.photo-title').text)
		# self.assertEqual('ulitsa "Kuzman Shapkarev" 1-3, 1000 Sofia, Bulgaria'					, sidebar.e('.photo-address').text)  # TODO fix link to be with with address ulitsa "Kuzman Shapkarev" 1, 1000 Sofia, Bulgaria
		self.assertEqual('2 August 2012'															, sidebar.e('.photo-date').text)
		
		stories_list = tab.e('.stories_list.scrollbarfix .comment')
		self.assertEqual('{0}/channels/img/{1}/logo/1/dim/100x100/'.format(URL_BASE, ID_USER_VIEW), stories_list.e('img').get_attribute('src'))
		self.assertEqual('Comment:'													, stories_list.e('.story_text > h6').text)
		self.assertEqual('This is a photo of National Theatre in Sofia, Bulgaria'	, stories_list.e('.story_cnt').text)
		self.assertEqual('Gabss (Pinner) has made a comment'						, stories_list.e('.activity').text)
		self.assertEqual('10 May 2013'												, stories_list.e('.photo-date').text)
		self.assertEqual('{0}/channels/view/{1}/'.format(URL_BASE, ID_USER_VIEW)		, stories_list.e('.activity a').get_attribute('href'))
		
		self.assertEqual('{0}/resources/avatars/50x50/avatar_1.png'.format(URL_BASE), tab.e('.write_story_wrap img ').get_attribute('src'))
		self.assertIsInstance(tab.e('textarea'), WebElement)
		
		# TODO - should fix this because in all tests - logged in
		# tab.e('.write_story_wrap').click()
		# self.assertIn('/user/?from=/map/', URL_BASE + '/user/?from=/map/%23%21/geo%3A42.697839%2C23.32167/zoom%3A10/dialog%3A22363018/tab%3Awrite-story/')
		
		# self.go(URL_BASE + '/map/#!/geo:42.697839,23.32167/zoom:10/dialog:%d/tab:stories/'.format(ID_MAP_ITEM))
	
	@unittest.skipIf(IS_LIVE, 'Do not run on live')
	@logged_in
	@url('/map/#!/geo:42.697839,23.32167/zoom:13/dialog:200988/tab:stories/')
	def test_post_comment(self):
		
		# TODO discuss this test if should be runned at all
		
		stories_tab = self.e('#stories_cnt')
		
		stories_tab.e('.text_wrap').click()
		sleep(3)
		self.e('.write_story_big .write_story').send_keys('This is a very nice photo of one of the main buildings in Sofia')
		
		self.e('.apply').click()
		sleep(2)
		
		self.browser.refresh()
		sleep(4)
		comment = self.e('.comment:nth-of-type(1)')
		
		self.assertEqual('{0}/resources/avatars/100x100/avatar_3.png'.format(URL_BASE)		, comment.e('img').get_attribute('src'))
		self.assertEqual('{0}/channels/view/{1}/'.format(URL_BASE, ID_USER)					, comment.e('.activity a').get_attribute('href'))
		self.assertEqual('This is a very nice photo of one of the main buildings in Sofia'	, comment.e('.story_cnt').text)
		
		comment.e('.delete.action').click()
		
		alert = self.browser.switch_to_alert()
		alert.accept()
		self.assertNotIn('comment:nth-of-type(1)', self.e('#info-dialog').get_attribute('class'))
	
	# @logged_in
	# @url('/map/index/#!/geo:42.688019,23.320069/zoom:20/dialog:%d/tab:details/' % ID_FAVOURITE_ITEM)  # TODO - should use another photo, because when I favourited it, then when on edit tour, it is possible not to be favourited
	# def test_favourite_item(self):
		
	# 	favourite = self.e('.favourite')
	# 	sleep(2)
	# 	self.assertIn('ss-icon'			, favourite.e('span').get_attribute('class'))
	# 	self.assertIn('ss-heart'		, favourite.e('span').get_attribute('class'))
	# 	sleep(2)
	# 	favourite.click()
	# 	sleep(2)
	# 	self.assertIn('ss-icon'			, favourite.e('span').get_attribute('class'))
	# 	self.assertIn('ss-heart'		, favourite.e('span').get_attribute('class'))
	# 	sleep(2)
	# 	self.go('/attach/uid%d/photos/list/#/get/recent/show/favourites/' % ID_USER)
	# 	sleep(2)
	# 	favourite_item = self.e('.image-holder a[href*="%d"]' % ID_FAVOURITE_ITEM)
	# 	self.assertIsInstance(favourite_item, WebElement)
		
	# 	sleep(2)
	# 	self.hover(favourite_item.e('img'))
	# 	self.e('li:nth-of-type(2) .holder .icon').click()
	
	@url('/map/#!/geo:42.697839,23.32167/zoom:10/dialog:{0}/tab:details/'.format(ID_MAP_ITEM))
	def test_dialog_streetview(self):
	
		dlg = self.e('#info-dialog')
		tab = dlg.e('#streetview_cnt')
		
		sleep(3)  # TODO do this to after_ajax
		dlg.e('.list_tabs a[href$=streetview_cnt]').click()
		sleep(1)
		self.assertIn('tab:streetview'	, '{0}/map/#!/geo:42.697839,23.32167/zoom:10/dialog:{1}/tab:streetview/'.format(URL_BASE, ID_MAP_ITEM))
		self.assertEqual('Street View'	, dlg.e('.selected .tab').text)
		
		# self.assertEqual(URL_BASE + '/services/thumb/phid/%d/dim/441x330/quality/80/'.format(ID_MAP_ITEM), self.e('.streetview_container .streetview-img-wrapper .streetview-img').get_attribute('src'))
		info = tab.e('.sv-image-info')
		self.assertEqual('National Theatre in Sofia, Bulgaria'	, info.e('.photo-title').text)
		self.assertEqual('2 August 2012'						, info.e('.photo-date').text)
		
		fade		= dlg.e('#streetview_slider.action.fade > span')  # TODO - test fade opacity
		fade_icon	= dlg.e('#streetview_slider .opacity-slider span')
		
		self.assertEqual('Fade'		, fade.text)
		self.assertIn('ss-icon'		, fade_icon.get_attribute('class'))
		self.assertIn('ss-newmoon'	, fade_icon.get_attribute('class'))
		
		reset		= dlg.e('#streetview_reset')
		reset_icon	= reset.e('span')
		
		self.assertEqual('  Reset'	, reset.text)
		self.assertIn('ss-icon'		, reset_icon.get_attribute('class'))
		self.assertIn('ss-refresh'	, reset_icon.get_attribute('class'))
		
		streetview = dlg.e('.sv-marker')
		self.assertEqual('Street View', streetview.text)
		streetview.click()
		
		fullscr			= dlg.e('#streetview_fullscreen')
		fullscr_icon	= fullscr.e('span')
		
		self.assertEqual('  Fullscreen', fullscr.text)
		self.assertIn('ss-icon'		, fullscr_icon.get_attribute('class'))
		self.assertIn('ss-scaleup'	, fullscr_icon.get_attribute('class'))
		
		fullscr.click()
		
		self.assertEqual('{0}/services/thumb/phid/{1}/dim/916x685/quality/80/'.format(URL_BASE, ID_MAP_ITEM), dlg.e('.streetview_container.streetview_fs .streetview-img-wrapper .streetview-img').get_attribute('src'))
		
		fullscr_off			= dlg.e('#streetview_fullscreen')
		fullscr_off_icon	= fullscr_off.e('span')
		
		self.assertEqual('Exit Fullscreen  ', fullscr_off.text)
		self.assertIn('ss-icon'		, fullscr_off_icon.get_attribute('class'))
		self.assertIn('ss-scaleup'	, fullscr_off_icon.get_attribute('class'))  # in the HTML - should be scaledown
		
		self.assertIsInstance(dlg.e('.map_preview'), WebElement)
		fullscr_off.click()
	
	@url('/map/#!/geo:42.697839,23.32167/zoom:10/dialog:{0}/tab:details/'.format(ID_MAP_ITEM))
	def test_dialog_repeats(self):
		
		dlg = self.e('#info-dialog')
		tab = dlg.e('#repeats_cnt')
		
		sleep(3)  # TODO do this to after_ajax
		dlg.e('.list_tabs a[href$=repeats_cnt]').click()
		sleep(1)
		
		self.assertIn('tab:repeats'		, '{0}/map/#!/geo:42.697839,23.32167/zoom:10/dialog:{1}/tab:repeats/'.format(URL_BASE, ID_MAP_ITEM))
		self.assertEqual('Repeats (0)'	, dlg.e('.selected .tab').text)
		self.assertEqual('{0}/services/thumb/phid/{1}/dim/2000x440/quality/80/'.format(URL_BASE, ID_MAP_ITEM), tab.e('.main img').get_attribute('src'))
		
		about_cnt = tab.e('.about')
		self.assertEqual('Historypin Repeats'		, about_cnt.e('h2').text)
		self.assertEqual('{0}/app'.format(URL_BASE)	, about_cnt.e('p a').get_attribute('href'))
		self.assertEqual('Historypin Repeats are modern replicas of older photos created using the Historypin Smartphone App', about_cnt.e('p').text)
		
		# TODO
		# - click on a repeat
		# - check repeat
	
	@url('/map/#!/geo:42.697839,23.32167/zoom:10/dialog:{0}/tab:details/'.format(ID_MAP_ITEM))
	def test_dialog_copyright(self):
		
		dlg = self.e('#info-dialog')
		tab = dlg.e('#copyright_cnt')
		
		sleep(3)  # TODO do this to after_ajax
		dlg.e('.list_tabs a[href$=copyright_cnt]').click()
		sleep(1)
		
		self.assertIn('tab:copyright', '{0}/map/#!/geo:42.697839,23.32167/zoom:10/dialog:{1}/tab:copyright/'.format(URL_BASE, ID_MAP_ITEM))
		self.assertEqual('Copyright', dlg.e('.selected .tab').text)
		
		sidebar	= dlg.e('.info.scrollbarfix')
		self.assertEqual('{0}/services/thumb/phid/{1}/dim/294x1000/'.format(URL_BASE, ID_MAP_ITEM)	, sidebar.e('.side-img ').get_attribute('src'))
		self.assertEqual('{0}/channels/img/{1}/logo/1/dim/46x46/'.format(URL_BASE, ID_USER_VIEW)	, sidebar.e('.photo-user-avatar.avatar').get_attribute('src'))
		self.assertEqual('Pinned by: \nGabss'														, sidebar.e('.pinner p').text)
		self.assertEqual('{0}/channels/view/{1}/'.format(URL_BASE, ID_USER_VIEW)					, sidebar.e('.pinner p a').get_attribute('href'))
		self.assertEqual('National Theatre in Sofia, Bulgaria'										, sidebar.e('.photo-title').text)
		# self.assertEqual('ulitsa "Kuzman Shapkarev" 1-3, 1000 Sofia, Bulgaria'					, sidebar.e('.photo-address').text)  #TODO fix link to be with with address ulitsa "Kuzman Shapkarev" 1, 1000 Sofia, Bulgaria
		self.assertEqual('2 August 2012'															, sidebar.e('.photo-date').text)
		
		self.assertEqual('Copyright (c) all rights reserved'						, tab.e('p .licensed').text)
	
	def test_dialog_deep_linking(self):
		# test whether the corret tab is selected and tab continer is shown on deeplinking
		pass
	
	@url('/map/#!/geo:42.694397,23.329198/zoom:14/')
	def test_pin_cluster(self):
		
		sleep(2)
		self.e_wait('#map-canvas .hp-marker-cluster').click()
		sleep(3)
		
		cluster_gallery = self.e('#map-canvas .hp-info-window.infoWindow_gallery')
		cluster_gallery.click()
		
		thumbs = cluster_gallery.es('.gallery_photos.scrollbarfix li')
		self.assertGreaterEqual(len(thumbs), 2)
		
		thumb_info = thumbs[0].e('.info')
		self.assertIsInstance(thumb_info.e('h6'), WebElement)
		self.assertIsInstance(thumb_info.e('h6 a'), WebElement)
		self.assertIsInstance(thumb_info.e('p'), WebElement)
		
		thumb_info.e('h6 a').click()
		sleep(5)
		
		dlg					= self.e('#info-dialog')
		icon_arrow_right	= dlg.e('.next-photo')
		self.assertIn('ss-icon'			, icon_arrow_right.e('span').get_attribute('class'))
		self.assertIn('ss-navigateright', icon_arrow_right.e('span').get_attribute('class'))
		icon_arrow_right.click()
		sleep(2)
		
		icon_arrow_left = dlg.e('.prev-photo')
		self.assertIn('ss-icon'			, icon_arrow_left.e('span').get_attribute('class'))
		self.assertIn('ss-navigateleft'	, icon_arrow_left.e('span').get_attribute('class'))
		
		self.assertTrue(icon_arrow_left.is_displayed(), '')
		# sleep(4)
		# icon_arrow_left.click()
		# sleep(2)
		# TODO LATER
		# zoom on clicking big cluster
	
	@url('/map/#!/geo:42.639733,23.295553/zoom:13/')
	def test_hp_marker(self):
		
		dlg = self.e('#info-dialog')
		
		sleep(2)
		self.e_wait('#map-canvas .hp-marker').click()
		sleep(4)
		self.assertIsInstance(dlg, WebElement)
		
		icon_arrow_right = dlg.e('.next-photo')
		icon_arrow_left = dlg.e('.prev-photo')
		
		self.assertFalse(icon_arrow_left.is_displayed(), 'None')
		self.assertFalse(icon_arrow_right.is_displayed(), 'None')
		
		# TODO LATER
		# deeplinking for map pins
		# get the id from the img and compare with deep linking
	
	@url('/map/')
	def test_footer(self):
		
		footer = [
			['{0}/'						.format(URL_BASE), 'Home'],
			['{0}/about-us'				.format(URL_BASE), 'About'],
			['{0}/faq'					.format(URL_BASE), 'FAQs'],
			['{0}/presscentre'			.format(URL_BASE), 'Press Centre'],
			['{0}/donate'				.format(URL_BASE), 'Support us'],
			['{0}/app'					.format(URL_BASE), 'Mobile App'],
			['{0}/terms-and-conditions'	.format(URL_BASE), 'Terms and Conditions'],
			['{0}/privacy-policy'		.format(URL_BASE), 'Privacy Policy'],
			['{0}/cookies'				.format(URL_BASE), 'Cookies'],
			['{0}/contact'				.format(URL_BASE), 'Contact'],
			['http://shiftdesign.org.uk/'				, u'© 2012 Shift'],
		]
		
		lists = self.es('.nav.cf li a')
		
		for n in range(len(footer)):
			i = footer[n]
			self.assertEqual(i[0], lists[n].get_attribute('href'))
			self.assertEqual(i[1], lists[n].text)
