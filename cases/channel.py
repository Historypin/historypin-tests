# -*- coding: utf-8 -*-

from base import *

class Channel(HPTestCase):
	
	@url('/channels/view/10649049/')
	def test_channel_info(self):
		self.assertTitle('Gabss | Historypin')
		
		info = self.e('.chan.info')
		self.assertEqual('Gabss'														, info.e('h2').text)
		self.assertEqual(URL_BASE + '/channels/img/10649049/logo/1/dim/200x200/crop/1/'	, info.e('img').get_attribute('src'))
		
		self.assertEqual('Find out more at: avalith.bg'					, self.e('.chan.info br~p').text)
		
		link = self.es('.chan.info br~p a')
		self.assertEqual('avalith.bg'									, link[0].text)
		self.assertEqual('http://avalith.bg/'							, link[0].get_attribute('href'))
		self.assertEqual('Find me on Facebook'							, link[1].text)
		self.assertEqual('http://www.facebook.com/gabriela.ananieva.7'	, link[1].get_attribute('href'))
		self.assertEqual('Follow me on Twitter'							, link[2].text)
		self.assertEqual('http://twitter.com/@Tristania90'				, link[2].get_attribute('href'))
		self.assertEqual('Visit my blog'								, link[3].text)
		self.assertEqual('http://test/'									, link[3].get_attribute('href'))
	
	@url('/channels/view/10649049/')
	def test_channel_details(self):
		
		h3 = self.es('.chan.options h3')
		self.assertEqual('Channel Details'	, h3[0].text)
		self.assertEqual('Share:'			, h3[1].text)
		
		paragraph = self.e('.chan.options p')
		texts = ['Channel views:', 'Fans:', 'Pins:', 'Tours:', 'Collections:']
		for n in range(len(texts)):
			self.assertIn(texts[n], paragraph.text)
		
		button = self.e('.channel-button.left')
		self.assertEqual('Become a Fan'										, button.text)
		self.assertEqual(URL_BASE + '/user/?from=/channels/view/10649049/'	, button.get_attribute('href'))
		
		social_buttons = self.e('.addthis_toolbox span')
		self.assertIn('ss-icon', social_buttons.get_attribute('class'))
		
		social_icons = ['ss-social-circle', 'ss-social-circle', 'ss-social-circle', 'ss-plus']
		
		for n in range(len(social_icons)-1):
			self.assertIn(social_icons[n], social_buttons.get_attribute('class'))
	
	@url('/attach/uid10649049/map/index/#!/geo:26.816514,24.138716/zoom:2/')
	def test_map_tab(self):
		
		map_tab = self.e('.list_tabs .first')
		self.assertEqual('Map'											, map_tab.text)
		
		self.assertIsInstance(self.e('#search-filters input#location')	, WebElement)
		self.assertIsInstance(self.e('#search-filters input#tags')		, WebElement)
		self.assertIsInstance(self.e('#photo_search_submit')			, WebElement)
		self.assertEqual('GO', self.e('#photo_search_submit').e('span').text)
		
		self.assertIsInstance(self.e('#date-selector #date-slider')	, WebElement)
		self.assertIsInstance(self.e('#date-slider-labels li')		, WebElement)
		
		self.e_wait('#map-canvas .hp-marker[class=hp-marker]').click()
		
		dlg = self.e('#info-dialog')
		self.assertIsInstance(dlg, WebElement)
		icon_arrow_right = dlg.e('.next-photo')
		icon_arrow_left = dlg.e('.prev-photo')
		self.assertFalse(icon_arrow_left.is_displayed(), 'None')
		self.assertFalse(icon_arrow_right.is_displayed(), 'None')
		
	
	@url('/attach/uid10649049/map/index/#!/geo:26.816514,24.138716/zoom:2/')
	def test_list_tab(self):
		
		list_tab = self.e('.list_tabs li a[href$="/attach/uid10649049/photos/list/"]')
		self.assertEqual('List'	, list_tab.text)
		list_tab.click()
		sleep(2)
		
		self.assertIsInstance(self.e('.list-filter'), WebElement)
		
		label = self.es('.list-filter label')
		self.assertEqual('Most Recent'	, label[0].text)
		self.assertEqual('Most Popular'	, label[1].text)
		self.assertEqual('Content'		, label[2].text)
		self.assertEqual('Favourites'	, label[3].text)
		
		strong = self.es('.list-filter strong')
		self.assertEqual('Sort by:'	, strong[0].text)
		self.assertEqual('Show:'	, strong[1].text)
		
		date_upload	= self.e('.list-filter input[id=date_upload]')
		view_count	= self.e('.list-filter input[id=view_count]')
		all_items	= self.e('.list-filter input[id=all]')
		favourites	= self.e('.list-filter input[id=unpinned]')
		
		self.assertTrue(date_upload.is_selected()	, 'None')
		self.assertFalse(view_count.is_selected()	, 'None')
		self.assertTrue(all_items.is_selected()		, 'None')
		self.assertFalse(favourites.is_selected()	, 'None')
		
		
		img_holder = self.e('#photo_list_content .list li .image-holder a[class="image"]')
		self.assertEqual(URL_BASE + '/attach/uid10649049/map/#!/geo:42.693738,23.326101/zoom:20/dialog:22363018/tab:details/'	, img_holder.get_attribute('href'))
		self.assertEqual(URL_BASE + '/services/thumb/phid/22363018/dim/170x130/crop/1/'											, img_holder.e('img').get_attribute('src'))
		
		info = self.e('#photo_list_content .info')
		self.assertIsInstance(info.e('h5'), WebElement)
		self.assertIsInstance(info.e('p'), WebElement)
		
		actions = self.e('#photo_list_content .info-actions')
		self.assertIn('ss-icon', actions.e('a span').get_attribute('class'))
		
		view_count.click()
		sleep(2)
		self.assertIn('popular', URL_BASE + '/attach/uid10649049/photos/list/#/show/all/get/popular/')
		self.assertFalse(date_upload.is_selected()	, 'None')
		self.assertIsInstance(img_holder, WebElement)
		self.assertIsInstance(info		, WebElement)
		self.assertIsInstance(actions	, WebElement)
		
		favourites.click()
		sleep(2)
		self.assertIn('favourites', URL_BASE + '/attach/uid10649049/photos/list/#/get/popular/show/favourites/')
		self.assertFalse(all_items.is_selected()	, 'None')
		self.assertIsInstance(img_holder, WebElement)
		self.assertIsInstance(info		, WebElement)
		self.assertIsInstance(actions	, WebElement)
		
		date_upload.click()
		sleep(2)
		self.assertTrue(date_upload.is_selected()	, 'None')
		self.assertFalse(view_count.is_selected()	, 'None')
		self.assertIsInstance(img_holder, WebElement)
		self.assertIsInstance(info		, WebElement)
		self.assertIsInstance(actions	, WebElement)
		
	
	@url('/attach/uid10649049/map/index/#!/geo:26.816514,24.138716/zoom:2/')
	def test_collections_tab(self):
		
		collections_tab = self.e('.list_tabs li a[href$="/attach/uid10649049/collections/all/"]')
		self.assertEqual('Collections'	, collections_tab.text)
		collections_tab.click()
		sleep(2)
		
		item = self.e('#photo_list_content .list li a')
		
		self.assertEqual(URL_BASE + '/attach/uid10649049/collections/view/id/22782015/title/Test%20Collection%20for%20automated%20test', item.get_attribute('href'))
		self.assertEqual(URL_BASE + '/services/thumb/phid/22363018/dim/195x150/crop/1/', item.e('img').get_attribute('src'))
		self.assertIn('collection-icon'	, item.e('span').get_attribute('class'))
		self.assertIn('ss-icon'			, item.e('span').get_attribute('class'))
		self.assertIn('ss-pictures'		, item.e('span').get_attribute('class'))
		
		paragraph_link = self.es('#photo_list_content .list li p a')
		
		self.assertEqual(URL_BASE + '/attach/uid10649049/collections/view/id/22782015/title/Test%20Collection%20for%20automated%20test', paragraph_link[0].get_attribute('href'))
		self.assertEqual('Test Collection for automated test', paragraph_link[0].text)
		
		self.assertEqual(URL_BASE + '/channels/view/10649049', paragraph_link[1].get_attribute('href'))
		self.assertEqual('Gabss', paragraph_link[1].text)
	
	@url('/attach/uid10649049/map/index/#!/geo:26.816514,24.138716/zoom:2/')
	def test_tours_tab(self):
		
		tours_tab = self.e('.list_tabs li a[href$="/attach/uid10649049/tours/all/"]')
		self.assertEqual('Tours'	, tours_tab.text)
		tours_tab.click()
		sleep(2)
		
		item = self.e('#photo_list_content .list li a')
		
		self.assertEqual(URL_BASE + '/attach/uid10649049/tours/view/id/22354015/title/Test%20Tour%20for%20automated%20test', item.get_attribute('href'))
		self.assertEqual(URL_BASE + '/services/thumb/phid/1031013/dim/195x150/crop/1/', item.e('img').get_attribute('src'))
		self.assertIn('tour-icon'	, item.e('span').get_attribute('class'))
		self.assertIn('ss-icon'		, item.e('span').get_attribute('class'))
		self.assertIn('ss-hiker'	, item.e('span').get_attribute('class'))
		
		paragraph_link = self.es('#photo_list_content .list li p a')
		
		self.assertEqual(URL_BASE + '/attach/uid10649049/tours/view/id/22354015/title/Test%20Tour%20for%20automated%20test', paragraph_link[0].get_attribute('href'))
		self.assertEqual('Test Tour for automated test', paragraph_link[0].text)
		
		self.assertEqual(URL_BASE + '/channels/view/10649049', paragraph_link[1].get_attribute('href'))
		self.assertEqual('Gabss', paragraph_link[1].text)
	
	@url('/channels/view/10649049/')
	def test_repeats_section(self):
		
		repeats = self.e('.chan.replicas')
		
		self.assertEqual('Historypin Repeats'									, repeats.e('h3').text)
		self.assertEqual(u'Historypin Repeats are created using the Historypin Smartphone App. They are modern replicas of your photos taken by other people or modern replicas of other person’s photos taken by you.', repeats.e('p:nth-of-type(1)').text)
		self.assertEqual('http://www.v4-22-00.historypin-hrd.appspot.com/app/'	, repeats.e('p:nth-of-type(1) a').get_attribute('href'))
		self.assertEqual('This Channel has no Historypin Repeats'				, repeats.e('p:nth-of-type(2)').text)
	
	@url('/channels/view/10649049/')
	def test_comment_feed(self):
		
		text_feed = self.e('.chan.story')
		
		self.assertEqual('Comment Feed'												, text_feed.e('h3').text)
		self.assertEqual('Comments posted to your media by you or by other people.'	, text_feed.e('p').text)
		
		feed = self.e('.feed.scrollbarfix li')
		
		self.assertIsInstance(feed.e('a')	, WebElement)
		self.assertIsInstance(feed.e('img')	, WebElement)
		self.assertIsInstance(feed.e('p')	, WebElement)
	
	@url('/channels/view/11675544/')
	@logged_in
	def test_tab_home(self):
		tab_home = self.e('.tab_nav li a[href="#tab-home"]')
		self.assertEqual('Home', tab_home.text)
		
		tab_home.click()
		self.assertTrue(tab_home.is_displayed(), 'None')
		
		tab_cnt = self.e('#tab-home .main')
		
		h3s = tab_cnt.es('h3')
		self.assertEqual('Your Historypin Channel'	, h3s[0].text)
		self.assertEqual('Share:'					, h3s[1].text)
		
		h4s = tab_cnt.es('h4')
		self.assertEqual('What to do now:'					, h4s[0].text)
		self.assertEqual('Personalise your Channel further:', h4s[1].text)
		
		to_dos = [
			['/channels/view/11675544/#tab-upload'				, "Pin something!"],
			['/channels/view/11675544/#tab-create-collection'	, "Create a Collection"],
			['/channels/view/11675544/#tab-create-tour'			, "Create a Tour"],
			['/map/'											, "Explore the map"],
			['/channels/'										, "See other people's Channels"],
		]
		
		to_do_main = tab_cnt.es('.inner.left:nth-of-type(1) li a')
		
		for n in range(len(to_dos)):
			i = to_dos[n]
			self.assertEqual(URL_BASE + i[0], to_do_main[n].get_attribute('href'))
			self.assertEqual(i[1]			, to_do_main[n].e('span').text)
		
		paragraph = tab_cnt.es('p')
		self.assertEqual("You can edit your channel at any time."					, paragraph[0].text)
		self.assertEqual("Share your Channel so others can see what you've created"	, paragraph[1].text)
		
		links = [
			['/#tab-settings'	, 'Edit Channel Info'],
			['/#tab-design'		, 'Edit Channel Design'],
			['/#tab-embed'		, 'Link to your Channel from your own website'],
		]
		
		edit_main = tab_cnt.es('.inner.left:nth-of-type(2) li a')
		
		for n in range(len(links)):
			i = links[n]
			self.assertEqual(URL_BASE + '/channels/view/11675544' + i[0], edit_main[n].get_attribute('href'))
			self.assertEqual(i[1]										, edit_main[n].e('span').text)
		
		social_buttons = tab_cnt.e('.addthis_toolbox span')
		self.assertIn('ss-icon', social_buttons.get_attribute('class'))
		
		social_icons = ['ss-social-circle', 'ss-social-circle', 'ss-social-circle', 'ss-plus']
		
		for n in range(len(social_icons)-1):
			self.assertIn(social_icons[n], social_buttons.get_attribute('class'))
		
		help = self.e('#tab-home .help')
		
		h3s_help = help.es('h3')
		self.assertEqual("Get some inspiration"	, h3s_help[0].text)
		self.assertEqual("Get help"				, h3s_help[1].text)
		
		self.assertEqual('Check out these examples to see what other people have done with their channels', help.e('p:nth-of-type(1)').text)
		
		examples = [
			['/id/2238022/', 'Photos of the Past'],
			['/id/8721093/', 'Sue Walker White'],
			['/id/2662022/', 'Connecticut State Library'],
			['/id/6487189/', 'London Metropolitan Archives'],
			['/id/1042029/', 'Biggleswade History Society'],
		]
		
		channels_help = help.es('a[href*=id]')
		
		for n in range(len(examples)):
			i = examples[n]
			self.assertEqual(URL_BASE + '/channels/view' + i[0]	, channels_help[n].get_attribute('href'))
			self.assertEqual(i[1]								, channels_help[n].text)
		
		
		self.assertEqual('If you get stuck or have any questions, check out our How To page and FAQs and please feel free to contact us at historypin@wearewhatwedo.org', help.e('p:last-of-type').text)
		
		links = [
			[URL_BASE + '/community/howtos/'		, 'How To page'],
			[URL_BASE + '/faq/'						, 'FAQs'],
			['mailto:historypin@wearewhatwedo.org'	, 'historypin@wearewhatwedo.org'],
		]
		
		links_help = help.es('p:last-of-type a')
		
		for n in range(len(links)):
			i = links[n]
			self.assertEqual(i[0]	, links_help[n].get_attribute('href'))
			self.assertEqual(i[1]	, links_help[n].text)
	
	@url('/channels/view/11675544/')
	@logged_in
	def test_tab_pin_something(self):
		
		tab_upload = self.e('.tab_nav li a[href="#tab-upload"]')
		self.assertEqual('Pin something', tab_upload.text)
		
		tab_upload.click()
		self.assertTrue(tab_upload.is_displayed(), 'None')
		
		tab_cnt = self.e('#tab-upload .main')
		self.assertEqual('Pin Something', tab_cnt.e('h3').text)
		
		paragraph = tab_cnt.es('p')
		self.assertEqual("We're always keen for new pins to be added to Historypin."						, paragraph[0].text)
		self.assertEqual("If you have a very large number of things to add you can use our bulk uploader.\nFind out more about the bulk uploader."	, paragraph[1].text)
		self.assertEqual(URL_BASE + '/bulkbridge/'				, paragraph[1].e('a').get_attribute('href'))
		
		button = tab_cnt.e('.button.left')
		self.assertEqual(URL_BASE + '/upload/'	, button.get_attribute('href'))
		self.assertEqual('Pin Something'		, button.text)
		
		links = [
			[URL_BASE + '/community/howtos/'		, 'How To page'],
			[URL_BASE + '/faq/'						, 'FAQs'],
			['mailto:historypin@wearewhatwedo.org'	, 'historypin@wearewhatwedo.org'],
		]
		
		help		= self.e('#tab-upload .help')
		links_help	= help.es('p:last-of-type a')
		
		for n in range(len(links)):
			i = links[n]
			self.assertEqual(i[0]	, links_help[n].get_attribute('href'))
			self.assertEqual(i[1]	, links_help[n].text)
		
		self.assertEqual('Get Help', help.e('h3').text)
	
	@url('/channels/view/11675544/')
	@logged_in
	def test_tab_collections(self):
		
		tab_collection = self.e('.tab_nav li a[href="#tab-create-collection"]')
		self.assertEqual('Collections', tab_collection.text)
		
		tab_collection.click()
		self.assertTrue(tab_collection.is_displayed(), 'None')
		
		tab_cnt = self.e('#tab-create-collection .main')
		self.assertEqual('Collections', tab_cnt.e('h3').text)
		
		paragraph = tab_cnt.es('p')
		self.assertEqual("A Collection is a group of pins that all relate to a particular theme. They are great for categorising your stuff and showing topics you're passionate about. You can view a Collection in List View and Slideshow View.", paragraph[0].text)
		self.assertEqual("Watch this How to video to see how to create a Collection"	, paragraph[1].text)
		
		self.assertEqual('See How', tab_cnt.e('h4').text)
		
		tab_cnt.e('p:last-of-type a').click()
		sleep(2)
		self.assertIsInstance(self.e('#youtube-dialog'), WebElement)
		self.assertTrue(self.e('#youtube-dialog').is_displayed(), 'None')
		self.e('.ui-dialog-titlebar-close').click()
		sleep(2)
		self.assertFalse(self.e('#youtube-dialog').is_displayed(), 'None')
		
		button_create = tab_cnt.e('.button.left')
		self.assertEqual(URL_BASE + '/collections/add/', button_create.get_attribute('href'))
		self.assertEqual('Create a new Collection', button_create.e('span').text)
		
		button_manage = tab_cnt.e('.scroll_to_embed')
		self.assertEqual('http://attach.10941289.uid11675544.v4-22-00.historypin-hrd.appspot.com/collections/all', button_manage.get_attribute('href'))
		self.assertEqual('Manage my Collections', button_manage.e('span').text)
		
		help = self.e('#tab-create-collection .help')
		
		h3s_help = help.es('h3')
		self.assertEqual("Get Inspiration"	, h3s_help[0].text)
		self.assertEqual("Get Help"			, h3s_help[1].text)
		
		self.assertEqual('Check out these examples to see Collections other people have made:', help.e('p:nth-of-type(1)').text)
		
		collections = [
			['/3762008/title/The%20Facial%20Hair%20Through%20Time%20Collection'	, 'The Facial Hair Through Time Collection'],
			['/6600998/title/The%20Under%20Construction%20Collection'			, 'The Under Construction Collection'],
			['/7700038/title/Motoring%20in%20Victoria%20BC'						, 'Motoring in Victoria, Canada'],
			['/8798159/title/Street%20Life%20in%20London'						, 'Street Life in London'],
			['/8691041/title/Women%20at%20Work'									, 'Women at Work'],
		]
		
		channels_help = help.es('a[href*=id]')
		
		for n in range(len(collections)):
			i = collections[n]
			self.assertEqual(URL_BASE + '/collections/view/id' + i[0]	, channels_help[n].get_attribute('href'))
			self.assertEqual(i[1]								, channels_help[n].text)
		
		
		self.assertEqual('If you get stuck or have any questions, check out our How To page and FAQs and please feel free to contact us at historypin@wearewhatwedo.org', help.e('p:last-of-type').text)
		
		links = [
			[URL_BASE + '/community/howtos/'		, 'How To page'],
			[URL_BASE + '/faq/'						, 'FAQs'],
			['mailto:historypin@wearewhatwedo.org'	, 'historypin@wearewhatwedo.org'],
		]
		
		links_help = help.es('p:last-of-type a')
		
		for n in range(len(links)):
			i = links[n]
			self.assertEqual(i[0]	, links_help[n].get_attribute('href'))
			self.assertEqual(i[1]	, links_help[n].text)
	
	@url('/channels/view/11675544/')
	@logged_in
	def test_tab_tours(self):
		
		tab_tour = self.e('.tab_nav li a[href="#tab-create-tour"]')
		self.assertEqual('Tours', tab_tour.text)
		
		tab_tour.click()
		self.assertTrue(tab_tour.is_displayed(), 'None')
		
		tab_cnt = self.e('#tab-create-tour .main')
		self.assertEqual('Tours', tab_cnt.e('h3').text)
		
		paragraph = tab_cnt.es('p')
		self.assertEqual("A Tour tells a narrative, walking people step-by-step through a series of pins in a set order. They are great for telling a story of person's life, describing the history of an event or showing a journey. You can view a Tour in Map View, List View and Tour View.", paragraph[0].text)
		self.assertEqual("Watch this How to video to see how to create a Tour"	, paragraph[3].text)
		
		self.assertEqual('See How', tab_cnt.e('h4').text)
		
		tab_cnt.e('p:last-of-type a').click()
		sleep(2)
		self.assertIsInstance(self.e('#youtube-dialog'), WebElement)
		self.assertTrue(self.e('#youtube-dialog').is_displayed(), 'None')
		self.e('.ui-dialog-titlebar-close').click()
		sleep(2)
		self.assertFalse(self.e('#youtube-dialog').is_displayed(), 'None')
		
		button_create = tab_cnt.e('.button.left')
		self.assertEqual(URL_BASE + '/tours/add/', button_create.get_attribute('href'))
		self.assertEqual('Create a new Tour', button_create.e('span').text)
		
		button_manage = tab_cnt.e('.scroll_to_embed')
		self.assertEqual('http://attach.10941289.uid11675544.v4-22-00.historypin-hrd.appspot.com/tours/all/', button_manage.get_attribute('href'))
		self.assertEqual('Manage my Tours', button_manage.e('span').text)
		
		help = self.e('#tab-create-tour .help')
		
		h3s_help = help.es('h3')
		self.assertEqual("Get Inspiration"	, h3s_help[0].text)
		self.assertEqual("Get Help"			, h3s_help[1].text)
		
		self.assertEqual('Check out these examples to see Tours other people have made.', help.e('p:nth-of-type(1)').text)
		
		tours = [
			['/8279489/title/The%20March%20on%20Washington'							, 'The 1963 March on Washington'],
			['/6631649/title/A%20historical%20guided%20tour%20of%20Kew%20Gardens'	, 'A historical guided tour of Kew Gardens'],
			['/7764038/title/Road%20Trip'											, 'Road Trip'],
			['/8748071/title/Dereham%20Circular%20History%20Tour%201'				, 'A Tour around Dereham, Norfolk'],
			['/6605903/title/Queen%20Elizabeth%20II'								, "Queen Elizabeth II's life"],
		]
		
		channels_help = help.es('a[href*=id]')
		
		for n in range(len(tours)):
			i = tours[n]
			self.assertEqual(URL_BASE + '/tours/view/id' + i[0]	, channels_help[n].get_attribute('href'))
			self.assertEqual(i[1]									, channels_help[n].text)
		
		
		self.assertEqual('If you get stuck or have any questions, check out our How To page and FAQs and please feel free to contact us at historypin@wearewhatwedo.org', help.e('p:last-of-type').text)
		
		links = [
			[URL_BASE + '/community/howtos/'		, 'How To page'],
			[URL_BASE + '/faq/'						, 'FAQs'],
			['mailto:historypin@wearewhatwedo.org'	, 'historypin@wearewhatwedo.org'],
		]
		
		links_help = help.es('p:last-of-type a')
		
		for n in range(len(links)):
			i = links[n]
			self.assertEqual(i[0]	, links_help[n].get_attribute('href'))
			self.assertEqual(i[1]	, links_help[n].text)
	
	@url('/channels/view/11675544/')
	@logged_in
	def test_tab_statistics(self):
		
		tab_statistics = self.e('.tab_nav li a[href="#tab-reports"]')
		self.assertEqual('Statistics', tab_statistics.text)
		
		tab_statistics.click()
		self.assertTrue(tab_statistics.is_displayed(), 'None')
		
		tab_cnt = self.e('#tab-reports .main')
		self.assertEqual('Statistics', tab_cnt.e('h3').text)
		
		cnt = ['Views', 'Total Pin views:', 'Total Tours Views:', 'Total Collections Views:', 'Fans', 'My Fans:', "Channels I'm a fan of:",
				'Activity', 'Pins:', 'Unpinned Items:', 'Tours made:', 'Collections made:', 'Comments added:', 'Favs:']
		
		statistics = tab_cnt.es('.stats_table tr td:first-of-type')
		
		for n in range(len(cnt)): self.assertEqual(cnt[n], statistics[n].text)
		
		fans = tab_cnt.es('.stats_table tr td a')
		self.assertEqual(URL_BASE + '/channels/view/11675544/#tab-subscribers'	, fans[0].get_attribute('href'))
		self.assertEqual('0 - See list', fans[0].text)
		self.assertEqual(URL_BASE + '/channels/view/11675544/#tab-subscriptions', fans[1].get_attribute('href'))
		self.assertEqual('2 - See list', fans[1].text)
	
	@url('/channels/view/11675544/')
	@logged_in
	def test_tab_hide_toolbar(self):
		
		self.assertTrue(self.e('.tab_nav').is_displayed(), 'None')
		
		tab_toolbar = self.e('.tab_nav.hideshowtoolbar ')
		self.assertEqual('Hide Tool Bar', tab_toolbar.e('.preview:nth-of-type(1)').text)
		
		tab_toolbar.click()
		self.assertFalse(self.e('.tab_cnt .main').is_displayed(), 'None')
		
		active = tab_toolbar.e('.preview:nth-of-type(2)')
		self.assertEqual('Show Tool Bar', active.text)
	
	@url('/channels/view/11675544/')
	@logged_in
	def test_channel_account_settings(self):
		
		
		
		
		pass
