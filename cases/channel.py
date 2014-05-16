# -*- coding: utf-8 -*-

from base import *
import os, sys

class Channel(HPTestCase):
	
	historypin_link = 'http://www.historypin.com'
	
	@url('/channels/view/%d/' % ID_USER_VIEW)
	def test_channel_description(self):
		self.assertTitle('Gabss | Historypin')
		
		info = self.e('.chan.info')
		self.assertEqual('Gabss', info.e('h2').text)
		self.assertEqual('%s/channels/img/%d/logo/1/dim/200x200/crop/1/' % (URL_BASE, ID_USER_VIEW), info.e('img').get_attribute('src'))
		
		self.assertEqual('Find out more at: avalith.bg'					, self.e('.chan.info br~p').text)
		
		link = self.es('.chan.info br~p a')
		self.assertEqual('avalith.bg'									, link[0].text)
		self.assertEqual('http://avalith.bg/'							, link[0].get_attribute('href'))
		self.assertEqual('Find me on Facebook'							, link[1].text)
		self.assertEqual('http://www.facebook.com/gabriela.ananieva.7'	, link[1].get_attribute('href'))
		self.assertEqual('Follow me on Twitter'							, link[2].text)
		self.assertEqual('http://twitter.com/@Tristania90'				, link[2].get_attribute('href'))
		self.assertEqual('Visit my Google+ Page'						, link[3].text)
		self.assertEqual('http://d/'									, link[3].get_attribute('href'))
	
	@url('/channels/view/%d/' % ID_USER_VIEW)
	def test_channel_details(self):
		
		h3 = self.es('.chan.options h3')
		self.assertEqual('Profile Details'	, h3[0].text)
		self.assertEqual('Share:'			, h3[1].text)
		
		# paragraph = self.e('.chan.options p')
		# texts = ['Profile views:', 'Fans:', 'Pins:', 'Tours:', 'Collections:']
		
		# for n in range(len(texts)): self.assertIn(texts[n], paragraph.text)
		
		sleep(4)  # AJAX
		button = self.e('.chan.options .channel-button.left')
		self.assertEqual('Become a Fan'													, button.text)
		self.assertEqual('%s/user/?from=/channels/view/%d/' % (URL_BASE, ID_USER_VIEW)	, button.get_attribute('href'))
		
		social_buttons = self.e('.addthis_toolbox span')
		self.assertIn('ss-icon', social_buttons.get_attribute('class'))
		
		social_icons = ['ss-social-circle', 'ss-social-circle', 'ss-social-circle', 'ss-plus']
		
		for n in range(len(social_icons)-1): self.assertIn(social_icons[n], social_buttons.get_attribute('class'))
	
	@url('/attach/uid%d/photos/activity_feed/' % ID_USER_VIEW)
	def test_activity_tab(self):
		
		sleep(3)
		activity_tab = self.e('#embed_tabs li a[href$="/attach/uid%d/photos/activity_feed/"]' % ID_USER_VIEW)
		self.assertEqual('Activity Feed', activity_tab.text)
		
		meta = self.e('.meta')
		self.assertIsInstance(meta.e('.photo-date'), WebElement)
		
		self.assertEqual('%s/channels/view/%d/' % (URL_BASE, ID_USER_VIEW), meta.e('.photo-user').get_attribute('href'))
		self.assertEqual('Gabss', meta.e('.photo-user').text)
		
		self.assertEqual('%s/channels/img/%d/logo/1/dim/100x100/' % (URL_BASE, ID_USER_VIEW), self.e('.avatar.fluid').get_attribute('src'))
		
		pin = self.e('.pin')
		self.assertIsInstance(pin.e('a:nth-of-type(1)'), WebElement)
		self.assertIsInstance(pin.e('a:nth-of-type(1) img'), WebElement)
		
		self.assertIsInstance(pin.e('a:nth-of-type(2)'), WebElement)
		
	@unittest.expectedFailure  # TODO fix this, cannot find the elememt
	@url('/attach/uid%d/map/index/#!/geo:26.816514,24.138716/zoom:2' % ID_USER_VIEW)
	def test_map_tab(self):
		sleep(2)
		
		map_tab = self.e('.list_tabs li a[href$="/attach/uid%d/map/index/"]' % ID_USER_VIEW)
		self.assertEqual('Map'	, map_tab.text)
		
		search_filters = self.e('#search-filters')
		self.assertIsInstance(search_filters.e('input#location'), WebElement)
		self.assertIsInstance(search_filters.e('input#tags')	, WebElement)
		
		submit = self.e('#photo_search_submit')
		self.assertIsInstance(submit, WebElement)
		self.assertEqual('Go', submit.e('span').text)
		
		self.assertIsInstance(self.e('#date-selector #date-slider')	, WebElement)
		self.assertIsInstance(self.e('#date-slider-labels li')		, WebElement)
		
		self.e_wait('#map-canvas .hp-marker-img-wrapper[class$="%d"]' % ID_MAP_ITEM).parent_node().click()
		
		sleep(5)
		dlg = self.e('#info-dialog')
		self.assertIsInstance(dlg, WebElement)
		
	
	@url('/attach/uid%d/map/index/#!/geo:26.816514,24.138716/zoom:2/' % ID_USER_VIEW)
	def test_list_tab(self):
		
		list_tab = self.e('.list_tabs li a[href$="/attach/uid%d/photos/list/"]' % ID_USER_VIEW)
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
		
		filters = self.e('.list-filter')
		date_upload	= filters.e('input[id=date_upload]')
		view_count	= filters.e('input[id=view_count]')
		all_items	= filters.e('input[id=all]')
		favourites	= filters.e('input[id=favourites]')
		
		self.assertTrue(date_upload.is_selected())
		self.assertFalse(view_count.is_selected())
		self.assertTrue(all_items.is_selected())
		self.assertFalse(favourites.is_selected())
		
		
		img_holder = self.e('#photo_list_content .list li .image-holder a[class="image"]')
		# TODO check this url
		# self.assertEqual('%s/attach/uid%d/map/index/#!/geo:43.325176,24.960938/zoom:20/dialog:361341/tab:details/' % (URL_BASE, ID_USER_VIEW), img_holder.get_attribute('href'))
		self.assertEqual('%s/services/thumb/phid/%d/dim/170x130/crop/1/' % (URL_BASE, ID_MAP_ITEM), img_holder.e('img').get_attribute('src'))
		
		info = self.e('#photo_list_content .info')
		self.assertIsInstance(info.e('h5'), WebElement)
		self.assertIsInstance(info.e('p'), WebElement)
		
		actions = self.e('#photo_list_content .info-actions')
		self.assertIn('ss-icon', actions.e('a span').get_attribute('class'))
		
		view_count.click()
		sleep(2)
		self.assertIn('popular', '%s/attach/uid%d/photos/list/cache/0/#/show/all/get/popular/' % (URL_BASE, ID_USER_VIEW))
		self.assertFalse(date_upload.is_selected())
		self.assertIsInstance(img_holder, WebElement)
		self.assertIsInstance(info		, WebElement)
		self.assertIsInstance(actions	, WebElement)
		
		favourites.click()
		sleep(2)
		self.assertIn('favourites', '%s/attach/uid%d/photos/list/cache/0/#/get/popular/show/favourites/' % (URL_BASE, ID_USER_VIEW))
		self.assertFalse(all_items.is_selected())
		self.assertIsInstance(img_holder, WebElement)
		self.assertIsInstance(info		, WebElement)
		self.assertIsInstance(actions	, WebElement)
		
		date_upload.click()
		sleep(2)
		self.assertTrue(date_upload.is_selected())
		self.assertFalse(view_count.is_selected())
		self.assertIsInstance(img_holder, WebElement)
		self.assertIsInstance(info		, WebElement)
		self.assertIsInstance(actions	, WebElement)
		
	
	@url('/attach/uid%d/map/index/#!/geo:26.816514,24.138716/zoom:2/' % ID_USER_VIEW)
	def test_collections_tab(self):
		
		collections_tab = self.e('.list_tabs li a[href$="/attach/uid%d/collections/all/"]' % ID_USER_VIEW)
		self.assertEqual('Collections'	, collections_tab.text)
		collections_tab.click()
		sleep(2)
		
		item = self.e('#photo_list_content .list li a')
		
		self.assertEqual('%s/attach/uid%d/collections/view/id/%d/title/Test%%20Collection%%20for%%20automated%%20test' % (URL_BASE, ID_USER_VIEW, ID_COLLECTION_VIEW), item.get_attribute('href'))
		self.assertEqual('%s/services/thumb/phid/%d/dim/195x150/crop/1/' % (URL_BASE, ID_COLLECTION_IMAGES[1]), item.e('img').get_attribute('src'))
		self.assertIn('collection-icon'	, item.e('span').get_attribute('class'))
		self.assertIn('ss-icon'			, item.e('span').get_attribute('class'))
		self.assertIn('ss-pictures'		, item.e('span').get_attribute('class'))
		
		paragraph_link = self.es('#photo_list_content .list li p a')
		
		self.assertEqual('%s/attach/uid%d/collections/view/id/%d/title/Test%%20Collection%%20for%%20automated%%20test' % (URL_BASE, ID_USER_VIEW, ID_COLLECTION_VIEW), paragraph_link[0].get_attribute('href'))
		self.assertEqual('Test Collection for automated test', paragraph_link[0].text)
		
		self.assertEqual('%s/channels/view/%d' % (URL_BASE, ID_USER_VIEW), paragraph_link[1].get_attribute('href'))
		self.assertEqual('Gabss', paragraph_link[1].text)
	
	@url('/attach/uid%d/map/index/#!/geo:26.816514,24.138716/zoom:2/' % ID_USER_VIEW)
	def test_tours_tab(self):
		
		tours_tab = self.e('.list_tabs li a[href$="/attach/uid%d/tours/all/"]' % ID_USER_VIEW)
		self.assertEqual('Tours'	, tours_tab.text)
		tours_tab.click()
		sleep(2)
		
		item = self.e('#photo_list_content .list li a')
		
		self.assertEqual('%s/attach/uid%d/tours/view/id/%d/title/Test%%20Tour%%20for%%20automated%%20test' % (URL_BASE, ID_USER_VIEW, ID_TOUR_VIEW), item.get_attribute('href'))
		self.assertEqual('%s/services/thumb/phid/706/dim/195x150/crop/1/' % URL_BASE, item.e('img').get_attribute('src'))
		
		self.assertIn('tour-icon'	, item.e('span').get_attribute('class'))
		self.assertIn('ss-icon'		, item.e('span').get_attribute('class'))
		self.assertIn('ss-hiker'	, item.e('span').get_attribute('class'))
		
		paragraph_link = self.es('#photo_list_content .list li p a')
		
		self.assertEqual('%s/attach/uid%d/tours/view/id/%d/title/Test%%20Tour%%20for%%20automated%%20test' % (URL_BASE, ID_USER_VIEW, ID_TOUR_VIEW), paragraph_link[0].get_attribute('href'))
		self.assertEqual('Test Tour for automated test', paragraph_link[0].text)
		
		self.assertEqual('%s/channels/view/%d' % (URL_BASE, ID_USER_VIEW), paragraph_link[1].get_attribute('href'))
		self.assertEqual('Gabss', paragraph_link[1].text)
	
	@logged_in
	@url('/channels/view/%d/' % ID_USER)
	def test_tab_home(self):
		tab_home = self.e('.tab_nav li a[href="#tab-home"]')
		self.assertEqual('Home', tab_home.text)
		
		tab_home.click()
		self.assertTrue(tab_home.is_displayed())
		
		tab_cnt = self.e('#tab-home .main')
		
		h3s = tab_cnt.es('h3')
		self.assertEqual('Your Historypin Profile'	, h3s[0].text)
		self.assertEqual('Share:'					, h3s[1].text)
		
		h4s = tab_cnt.es('h4')
		self.assertEqual('What to do now:'					, h4s[0].text)
		self.assertEqual('Personalise your Profile further:', h4s[1].text)
		
		channel_view = '/channels/view/'
		to_dos = [
			['%s%d/#tab-upload' % (channel_view, ID_USER)			, "Pin something!"],
			['%s%d/#tab-create-collection' % (channel_view, ID_USER), "Create a Collection"],
			['%s%d/#tab-create-tour' % (channel_view, ID_USER)		, "Create a Tour"],
			['/map/'												, "Explore the map"],
			['/channels/'											, "See other people's Profiles"],
		]
		
		to_do_main = tab_cnt.es('.inner.left:nth-of-type(1) li a')
		
		for n in range(len(to_dos)):
			i = to_dos[n]
			self.assertEqual(URL_BASE + i[0], to_do_main[n].get_attribute('href'))
			self.assertEqual(i[1]			, to_do_main[n].e('span').text)
		
		paragraph = tab_cnt.es('p')
		self.assertEqual("You can edit your profile at any time."					, paragraph[0].text)
		self.assertEqual("Share your Profile so others can see what you've created"	, paragraph[1].text)
		
		links = [
			['/#tab-settings'	, 'Edit Profile Info'],
			['/#tab-design'		, 'Edit Profile Design'],
			['/#tab-embed'		, 'Link to your Profile from your own website'],
		]
		
		edit_main = tab_cnt.es('.inner.left:nth-of-type(2) li a')
		
		for n in range(len(links)):
			i = links[n]
			self.assertEqual(URL_BASE + '/channels/view/%d' % ID_USER + i[0], edit_main[n].get_attribute('href'))
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
		
		self.assertEqual('Check out these examples to see what other people have done with their profiles', help.e('p:nth-of-type(1)').text)
		
		examples = [
			['%d/' % CHANNELS_EXAMPLES[0], 'Photos of the Past'],
			['%d/' % CHANNELS_EXAMPLES[1], 'Sue Walker White'],
			['%d/' % CHANNELS_EXAMPLES[2], 'Connecticut State Library'],
			['%d/' % CHANNELS_EXAMPLES[3], 'London Metropolitan Archives'],
			['%d/' % CHANNELS_EXAMPLES[4], 'Biggleswade History Society'],
		]
		
		channels_help = help.es('a[href*=channels]')
		
		for n in range(len(examples)):
			i = examples[n]
			self.assertEqual(URL_BASE + '/channels/view/' + i[0], channels_help[n].get_attribute('href'))
			self.assertEqual(i[1]								, channels_help[n].text)
		
		
		self.assertEqual('If you get stuck or have any questions, check out our How To page and FAQs and please feel free to contact us at historypin@wearewhatwedo.org', help.e('p:last-of-type').text)
		
		links = [
			['%s/community/howtos/'	% URL_BASE, 'How To page'],
			['%s/faq/'				% URL_BASE, 'FAQs'],
			['mailto:historypin@wearewhatwedo.org'	, 'historypin@wearewhatwedo.org'],
		]
		
		links_help = help.es('p:last-of-type a')
		
		for n in range(len(links)):
			i = links[n]
			self.assertEqual(i[0]	, links_help[n].get_attribute('href'))
			self.assertEqual(i[1]	, links_help[n].text)
	
	@logged_in
	@url('/channels/view/%d/' % ID_USER)
	def test_tab_pin_something(self):
		
		tab_upload = self.e('.tab_nav li a[href="#tab-upload"]')
		self.assertEqual('Pin something', tab_upload.text)
		
		tab_upload.click()
		self.assertTrue(tab_upload.is_displayed())
		
		tab_cnt = self.e('#tab-upload .main')
		self.assertEqual('Pin Something', tab_cnt.e('h3').text)
		
		paragraph = tab_cnt.es('p')
		self.assertEqual("We're always keen for new pins to be added to Historypin."						, paragraph[0].text)
		self.assertEqual("If you have a very large number of things to add you can use our bulk uploader.\nFind out more about the bulk uploader."	, paragraph[1].text)
		self.assertEqual('%s/bulkbridge/' % URL_BASE, paragraph[1].e('a').get_attribute('href'))
		
		button = tab_cnt.e('.button.left')
		self.assertEqual('%s/upload/' % URL_BASE, button.get_attribute('href'))
		self.assertEqual('Pin Something'		, button.text)
		
		links = [
			['%s/community/howtos/'	% self.historypin_link, 'How To page'],
			['%s/faq/'				% self.historypin_link, 'FAQs'],
			['mailto:historypin@wearewhatwedo.org'		, 'historypin@wearewhatwedo.org'],
		]
		
		help		= self.e('#tab-upload .help')
		links_help	= help.es('p:last-of-type a')
		
		for n in range(len(links)):
			i = links[n]
			self.assertEqual(i[0]	, links_help[n].get_attribute('href'))
			self.assertEqual(i[1]	, links_help[n].text)
		
		self.assertEqual('Get help', help.e('h3').text)
	
	@logged_in
	@url('/channels/view/%d/' % ID_USER)
	def test_tab_collections(self):
		
		tab_collection = self.e('.tab_nav li a[href="#tab-create-collection"]')
		self.assertEqual('Collections', tab_collection.text)
		
		tab_collection.click()
		self.assertTrue(tab_collection.is_displayed())
		
		tab_cnt = self.e('#tab-create-collection .main')
		self.assertEqual('Collections', tab_cnt.e('h3').text)
		
		paragraph = tab_cnt.es('p')
		self.assertEqual("A Collection is a group of pins that all relate to a particular theme. They are great for categorising your stuff and showing topics you're passionate about. You can view a Collection in List View and Slideshow View.", paragraph[0].text)
		self.assertEqual("Watch this How to video to see how to create a Collection"	, paragraph[1].text)
		
		self.assertEqual('See How', tab_cnt.e('h4').text)
		
		tab_cnt.e('p:last-of-type a').click()
		sleep(2)
		self.assertIsInstance(self.e('#youtube-dialog'), WebElement)
		self.assertTrue(self.e('#youtube-dialog').is_displayed())
		self.e('.ui-dialog-titlebar-close').click()
		sleep(2)
		self.assertFalse(self.e('#youtube-dialog').is_displayed())
		
		button_create = tab_cnt.e('.button.left')
		self.assertEqual('%s/collections/add/' % URL_BASE, button_create.get_attribute('href'))
		self.assertEqual('Create a new Collection', button_create.e('span').text)
		
		button_manage = tab_cnt.e('.scroll_to_embed')
		self.assertEqual('%s/collections/all' % URL_ATTACH, button_manage.get_attribute('href'))
		self.assertEqual('Manage my Collections', button_manage.e('span').text)
		
		help = self.e('#tab-create-collection .help')
		
		h3s_help = help.es('h3')
		self.assertEqual("Get Inspiration"	, h3s_help[0].text)
		self.assertEqual("Get Help"			, h3s_help[1].text)
		
		self.assertEqual('Check out these examples to see Collections other people have made:', help.e('p:nth-of-type(1)').text)
		
		collections = [
			['/%d/title/The%%20Facial%%20Hair%%20Through%%20Time%%20Collection' % COLLECTION_EXAMPLES[0], 'The Facial Hair Through Time Collection'],
			['/%d/title/The%%20Under%%20Construction%%20Collection' % COLLECTION_EXAMPLES[1], 'The Under Construction Collection'],
			['/%d/title/Motoring%%20in%%20Victoria%%20BC' % COLLECTION_EXAMPLES[2], 'Motoring in Victoria, Canada'],
			['/%d/title/Street%%20Life%%20in%%20London' % COLLECTION_EXAMPLES[3], 'Street Life in London'],
			['/%d/title/Women%%20at%%20Work' % COLLECTION_EXAMPLES[4], 'Women at Work'],
		]
		
		channels_help = help.es('a[href*=id]')
		
		for n in range(len(collections)):
			i = collections[n]
			self.assertEqual(URL_BASE + '/collections/view/id' + i[0]	, channels_help[n].get_attribute('href'))
			self.assertEqual(i[1]								, channels_help[n].text)
		
		
		self.assertEqual('If you get stuck or have any questions, check out our How To page and FAQs and please feel free to contact us at historypin@wearewhatwedo.org', help.e('p:last-of-type').text)
		
		links = [
			['%s/community/howtos/'	% URL_BASE, 'How To page'],
			['%s/faq/'				% URL_BASE, 'FAQs'],
			['mailto:historypin@wearewhatwedo.org'	, 'historypin@wearewhatwedo.org'],
		]
		
		links_help = help.es('p:last-of-type a')
		
		for n in range(len(links)):
			i = links[n]
			self.assertEqual(i[0]	, links_help[n].get_attribute('href'))
			self.assertEqual(i[1]	, links_help[n].text)
	
	@logged_in
	@url('/channels/view/%d/' % ID_USER)
	def test_tab_tours(self):
		
		tab_tour = self.e('.tab_nav li a[href="#tab-create-tour"]')
		self.assertEqual('Tours', tab_tour.text)
		
		tab_tour.click()
		self.assertTrue(tab_tour.is_displayed())
		
		tab_cnt = self.e('#tab-create-tour .main')
		self.assertEqual('Tours', tab_cnt.e('h3').text)
		
		paragraph = tab_cnt.es('p')
		self.assertEqual("A Tour tells a narrative, walking people step-by-step through a series of pins in a set order. They are great for telling a story of person's life, describing the history of an event or showing a journey. You can view a Tour in Map View, List View and Tour View.", paragraph[0].text)
		self.assertEqual("Watch this How to video to see how to create a Tour"	, paragraph[3].text)
		
		self.assertEqual('See How', tab_cnt.e('h4').text)
		
		tab_cnt.e('p:last-of-type a').click()
		sleep(2)
		self.assertIsInstance(self.e('#youtube-dialog'), WebElement)
		self.assertTrue(self.e('#youtube-dialog').is_displayed())
		self.e('.ui-dialog-titlebar-close').click()
		sleep(2)
		self.assertFalse(self.e('#youtube-dialog').is_displayed())
		
		button_create = tab_cnt.e('.button.left')
		self.assertEqual('%s/tours/add/' % URL_BASE, button_create.get_attribute('href'))
		self.assertEqual('Create a new Tour', button_create.e('span').text)
		
		button_manage = tab_cnt.e('.scroll_to_embed')
		self.assertEqual('%s/tours/all/' % URL_ATTACH, button_manage.get_attribute('href'))
		self.assertEqual('Manage my Tours', button_manage.e('span').text)
		
		help = self.e('#tab-create-tour .help')
		
		h3s_help = help.es('h3')
		self.assertEqual("Get Inspiration"	, h3s_help[0].text)
		self.assertEqual("Get Help"			, h3s_help[1].text)
		
		self.assertEqual('Check out these examples to see Tours other people have made.', help.e('p:nth-of-type(1)').text)
		
		tours = [
			['/%d/title/The%%20March%%20on%%20Washington' % TOUR_EXAMPLES[0], 'The 1963 March on Washington'],  # make a variable to match SQl IDs
			['/%d/title/A%%20historical%%20guided%%20tour%%20of%%20Kew%%20Gardens' % TOUR_EXAMPLES[1], 'A historical guided tour of Kew Gardens'],
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
			['%s/community/howtos/'	% URL_BASE, 'How To page'],
			['%s/faq/'				% URL_BASE, 'FAQs'],
			['mailto:historypin@wearewhatwedo.org'	, 'historypin@wearewhatwedo.org'],
		]
		
		links_help = help.es('p:last-of-type a')
		
		for n in range(len(links)):
			i = links[n]
			self.assertEqual(i[0]	, links_help[n].get_attribute('href'))
			self.assertEqual(i[1]	, links_help[n].text)
	
	@logged_in
	@url('/channels/view/%d/' % ID_USER)
	def test_tab_statistics(self):
		tab_statistics = self.e('.tab_nav li a[href="#tab-reports"]')
		self.assertEqual('Statistics', tab_statistics.text)
		
		tab_statistics.click()
		self.assertTrue(tab_statistics.is_displayed())
		
		tab_cnt = self.e('#tab-reports .main')
		self.assertEqual('Statistics', tab_cnt.e('h3').text)
		
		cnt = ['Views', 'Total Pin views:', 'Total Tours Views:', 'Total Collections Views:', 'Fans', 'My Fans:', "Profiles I'm a fan of:", 'Activity', 'Pins:', 'Unpinned Items:', 'Tours made:', 'Collections made:', 'Comments added:', 'Favs:']
		
		statistics = tab_cnt.es('.stats_table tr td:first-of-type')
		
		for n in range(len(cnt)): self.assertEqual(cnt[n], statistics[n].text)
		
		fans = tab_cnt.es('.stats_table tr td a')
		self.assertEqual('%s/channels/view/%d/#tab-subscribers' % (URL_BASE, ID_USER)	, fans[0].get_attribute('href'))
		self.assertEqual('0 - See list', fans[0].text)
		self.assertEqual('%s/channels/view/%d/#tab-subscriptions' % (URL_BASE, ID_USER), fans[1].get_attribute('href'))
		self.assertEqual('3 - See list', fans[1].text)
	
	@logged_in
	@url('/channels/view/%d/' % ID_USER)
	def test_tab_authentication(self):
		tab_auth = self.e('.tab_nav li a[href="#tab-auth"]')
		self.assertEqual('Authentication', tab_auth.text)
		
		tab_auth.click()
		
		tab_cnt = self.e('#tab-auth')
		self.assertEqual('Authentication', tab_cnt.e('h3').text)
		
		cnt = [
			['Google'	, 'Status:', 'Connected'		, 'Disconnect'	, '/user/login/connect/-1'],
			['Twitter'	, 'Status:', 'Not Connected'	, 'Connect'		, '/user/twitter_login/connect/1'],
			['Facebook'	, 'Status:', 'Not Connected'	, 'Connect'		, '/channels/view/%d/#' % ID_USER],
		]
		
		h4s = tab_cnt.es('tr td h4')
		status = tab_cnt.es('tr:nth-child(2) td:nth-child(1)')
		connect = tab_cnt.es('tr:nth-child(2) td:nth-child(2)')
		connection = tab_cnt.es('a')
		
		for n in range(len(cnt)):
			i = cnt[n]
			self.assertEqual(i[0], h4s[n].text)
			self.assertEqual(i[1], status[n].text)
			self.assertEqual(i[2], connect[n].text)
			self.assertEqual(i[3], connection[n].text)
			self.assertEqual(URL_BASE + i[4], connection[n].get_attribute('href'))
	
	@logged_in
	@url('/channels/view/%d/' % ID_USER)
	def test_tab_alerts(self):
		tab_alerts = self.e('.tab_nav li a[href="#tab-alerts"]')
		self.assertEqual('Alerts', tab_alerts.text)
		
		tab_alerts.click()
		
		tab_cnt = self.e('#tab-alerts')
		self.assertEqual('Manage my alerts', tab_cnt.e('h3').text)
		
		button = tab_cnt.e('.button.submit')
		
		texts = tab_cnt.es('label')
		
		labels = ['I would like to receive Historypin email newsletters', 'I would like to receive email alerts from Historypin about my items,\n(for example, when someone comments, favourites or repeats my photos, videos and audio recordings)', 'Alert email address']
		
		for n in range(len(labels)): self.assertEqual(labels[n], texts[n].text)
		
		checkbox = tab_cnt.es('input[type="checkbox"]')
		sleep(3)
		checkbox[0].click()
		button.click()
		self.assertTrue(checkbox[0].is_selected())
		checkbox[0].click()
		sleep(3)
		button.click()
		
		checkbox[1].click()
		button.click()
		self.assertTrue(checkbox[1].is_selected())
		checkbox[1].click()
		button.click()
		
		self.assertEqual('Just so you know, you can change these settings from your profile at any time', tab_cnt.e('p').text)
		
		email = tab_cnt.e('#new_mail')
		
		self.assertEqual('gabriela.ananieva@wearewhatwedo.org', email.get_attribute('value'))
		email.clear()
		email.send_keys('g.ananieva@avalith.bg')
		button.click()
		self.assertEqual('g.ananieva@avalith.bg', email.get_attribute('value'))
		
		self.browser.refresh()
		
		tab_alerts 	= self.e('.tab_nav li a[href="#tab-alerts"]')
		tab_alerts.click()
		
		tab_cnt 	= self.e('#tab-alerts')
		button 		= tab_cnt.e('.button.submit')
		
		email = tab_cnt.e('#new_mail')
		email.clear()
		
		email.send_keys('gabriela.ananieva@wearewhatwedo.org')
		button.click()
		self.assertEqual('gabriela.ananieva@wearewhatwedo.org', email.get_attribute('value'))
	
	@logged_in
	@url('/channels/view/%d/' % ID_USER)
	def test_tab_hide_toolbar(self):
		self.assertTrue(self.es('.tab_nav')[0].is_displayed())
		
		tab_toolbar = self.e('.tab_nav.hideshowtoolbar ')
		self.assertEqual('Hide Tool Bar', tab_toolbar.e('.preview:nth-of-type(1)').text)
		
		tab_toolbar.click()
		self.assertTrue(tab_toolbar.is_displayed())
		
		active = tab_toolbar.e('.preview:nth-of-type(2)')
		self.assertEqual('Show Tool Bar', active.text)
	
	@logged_in
	@url('/channels/view/%d/' % ID_USER)
	def test_channel_info(self):
		
		sleep(4)
		editor = self.e('.channel_editor')
		
		settings = editor.e('.settings')
		self.assertEqual('Profile & Account Settings', settings.text)
		self.assertIn('ss-icon'		, settings.e('span').get_attribute('class'))
		self.assertIn('ss-settings'	, settings.e('span').get_attribute('class'))
		
		settings.click()
		
		settings_menu = editor.e('.settings_menu')
		self.assertTrue(settings_menu.is_displayed())
		
		heading = settings_menu.es('li strong')
		self.assertEqual('Profile Settings'	, heading[0].text)
		self.assertEqual('Sharing & Embeds'	, heading[1].text)
		self.assertEqual('Stuff I like'		, heading[2].text)
		
		channel_info = settings_menu.e('li:nth-of-type(2) a')
		self.assertEqual('Profile Info'											, channel_info.text)
		self.assertEqual('%s/channels/view/%d/#tab-settings' % (URL_BASE, ID_USER), channel_info.get_attribute('href'))
		
		channel_info.click()
		
		tab_settings = editor.e('#tab-settings')
		self.assertTrue(tab_settings.is_displayed())
		
		self.assertEqual('Profile Info', tab_settings.e('h3').text)
		
		help = self.e('#tab-settings .help')
		self.assertEqual('Get help', help.e('h3').text)
		
		self.assertEqual('If you get stuck or have any questions, check out our How To page and FAQs and please feel free to contact us at historypin@wearewhatwedo.org', help.e('p:last-of-type').text)
		
		links = [
			['%s/community/howtos/'	% self.historypin_link	, 'How To page'],
			['%s/faq/'				% self.historypin_link	, 'FAQs'],
			['mailto:historypin@wearewhatwedo.org'			, 'historypin@wearewhatwedo.org'],
		]
		
		links_help = help.es('p:last-of-type a')
		
		for n in range(len(links)):
			i = links[n]
			self.assertEqual(i[0]	, links_help[n].get_attribute('href'))
			self.assertEqual(i[1]	, links_help[n].text)
		
		info = tab_settings.e('.form')
		
		form_texts = ['Profile Name', 'Profile Type', 'About', 'External site link', 'Twitter username', 'Facebook link', 'Google Plus link', 'Blog link']
		
		label = info.es('label')
		for n in range(len(form_texts)): self.assertEqual(form_texts[n], label[n].text)
		
		channel_name = info.e('.input-container #channel_name')
		channel_name.clear()
		channel_name.send_keys('Gabriela Ananieva')
		
		channel_type = info.e('.input-container #channel_type')
		channel_type.click()
		channel_type.e('option:nth-of-type(3)').click()
		
		desc = info.e('#channel_desc')
		desc.click()
		desc.clear()
		desc.send_keys('This is a test description')
		
		site_link = info.e('#external_site')
		site_link.clear()
		site_link.send_keys('http://avalith.bg')
		
		twitter_name = info.e('#twitter_link')
		twitter_name.clear()
		twitter_name.send_keys('@Tristania90')
		
		fb_link = info.e('#facebook_link')
		fb_link.clear()
		fb_link.send_keys('https://www.facebook.com/gabriela.ananieva.7')
		
		google_link = info.e('#google_plus_link')
		google_link.clear()
		google_link.send_keys('http://avalith.bg')
		
		blog_link = info.e('#blog_link')
		blog_link.clear()
		blog_link.send_keys('http://avalith.bg')
		
		button = tab_settings.e('.save_settings')
		self.assertEqual('Save Changes', button.e('span').text)
		button.click()
		
		sleep(10)  # TODO remove this after ajax_wait
		
		editor			= self.e('.channel_editor')
		settings		= editor.e('.settings')
		settings.click()
		settings_menu	= editor.e('.settings_menu')
		heading			= settings_menu.es('li strong')
		channel_info	= settings_menu.e('li:nth-of-type(2) a')
		channel_info.click()
		
		tab_settings = editor.e('#tab-settings')
		# self.assertTrue(tab_settings.is_displayed())
		info = tab_settings.e('.form')
		
		channel_name	= info.e('.input-container #channel_name')
		channel_type	= info.e('.input-container #channel_type')
		desc			= info.e('#channel_desc')
		site_link		= info.e('#external_site')
		twitter_name	= info.e('#twitter_link')
		fb_link			= info.e('#facebook_link')
		google_link		= info.e('#google_plus_link')
		blog_link		= info.e('#blog_link')
		button			= tab_settings.e('.save_settings')
		
		self.assertEqual('Gabriela Ananieva'							, channel_name.get_attribute('value'))
		self.assertEqual('3'											, channel_type.e('option:nth-of-type(3)').get_attribute('value'))
		self.assertEqual('This is a test description'					, desc.text)
		self.assertEqual('http://avalith.bg'							, site_link.get_attribute('value'))
		self.assertEqual('@Tristania90'									, twitter_name.get_attribute('value'))
		self.assertEqual('https://www.facebook.com/gabriela.ananieva.7'	, fb_link.get_attribute('value'))
		self.assertEqual('http://avalith.bg'							, google_link.get_attribute('value'))
		self.assertEqual('http://avalith.bg'							, blog_link.get_attribute('value'))
		
		chan_info = self.e('.chan.info')
		self.assertEqual('%s/resources/avatars/200x200/avatar_3.png' % URL_BASE, chan_info.e('img').get_attribute('src'))
		self.assertEqual('Gabriela Ananieva'			, chan_info.e('h2').text)
		self.assertEqual('This is a test description'	, chan_info.e('.urlize').text)
		self.assertEqual('Find out more at: avalith.bg'	, chan_info.e('p:nth-of-type(2)').text)
		self.assertEqual('http://avalith.bg/'			, chan_info.e('p:nth-of-type(2) a').get_attribute('href'))
		
		
		sns = chan_info.es('.sns a')
		links = [
			['Find us on Facebook'		, 'http://https//www.facebook.com/gabriela.ananieva.7'],
			['Follow us on Twitter'		, 'http://twitter.com/@Tristania90'],
			['Visit our Google+ Page'	, 'http://avalith.bg/'],
			['Visit our blog'			, 'http://avalith.bg/'],
		]
		
		for n in range(len(links)):
			i = links[n]
			self.assertEqual(i[0], sns[n].text)
			self.assertEqual(i[1], sns[n].get_attribute('href'))
		
	@logged_in
	@url('/channels/view/%d/' % ID_USER)
	def test_channel_design(self):
		
		editor		= self.e('.channel_editor')
		settings	= editor.e('.settings')
		settings.click()
		
		settings_menu = editor.e('.settings_menu')
		self.assertTrue(settings_menu.is_displayed())
		
		design = settings_menu.e('a[href="#tab-design"]')
		self.assertEqual('%s/channels/view/%d/#tab-design' % (URL_BASE, ID_USER), design.get_attribute('href'))
		self.assertEqual('Profile Design', design.text)
		
		design.click()
		sleep(3)
		tab_design = editor.e('#tab-design')
		self.assertTrue(tab_design.is_displayed())
		
		self.assertEqual('Profile Design'		, tab_design.e('h3').text)
		
		button = self.e('.submit.button.left')
		self.assertEqual('Save Design', button.e('span').text)
		
		wrapper	= self.e('#container_wrap')
		
		themes	= tab_design.e('.theme-select')
		themes.e('a.charcoal').click()
		button.click()
		sleep(10)
		
		wrapper = self.e('#container_wrap')
		self.assertIn('charcoal', wrapper.get_attribute('class'))
		
		editor		= self.e('.channel_editor')
		settings	= editor.e('.settings')
		
		settings.click()
		settings_menu	= editor.e('.settings_menu')
		self.assertTrue(settings_menu.is_displayed())
		design			= settings_menu.e('a[href="#tab-design"]')
		design.click()
		
		tab_design	= editor.e('#tab-design')
		themes		= tab_design.e('.theme-select')
		themes.e('a.blue').click()
		sleep(3)
		
		button = self.e('.submit.button.left')
		button.click()
		
		wrapper = self.e('#container_wrap')
		self.assertIn('blue', wrapper.get_attribute('class'))
											
		editor		= self.e('.channel_editor')
		settings	= editor.e('.settings')
		
		settings.click()
		settings_menu	= editor.e('.settings_menu')
		self.assertTrue(settings_menu.is_displayed())
		design			= settings_menu.e('a[href="#tab-design"]')
		design.click()
		
		tab_design	= editor.e('#tab-design')
		themes		= tab_design.e('.theme-select')
		themes.e('a.gray').click()
		sleep(3)
		
		button	= self.e('.submit.button.left')
		button.click()
		
		wrapper	= self.e('#container_wrap')
		self.assertIn('gray', wrapper.get_attribute('class'))
										
		editor = self.e('.channel_editor')
		settings = editor.e('.settings')
		
		settings.click()
		settings_menu = editor.e('.settings_menu')
		self.assertTrue(settings_menu.is_displayed())
		design = settings_menu.e('a[href="#tab-design"]')
		design.click()
		
		tab_design	= editor.e('#tab-design')
		themes		= tab_design.e('.theme-select')
		themes.e('a.green').click()
		sleep(3)
		
		button = self.e('.submit.button.left')
		button.click()
		
		wrapper = self.e('#container_wrap')
		self.assertIn('green', wrapper.get_attribute('class'))
															
		editor		= self.e('.channel_editor')
		settings	= editor.e('.settings')
		
		settings.click()
		settings_menu	= editor.e('.settings_menu')
		self.assertTrue(settings_menu.is_displayed())
		design			= settings_menu.e('a[href="#tab-design"]')
		design.click()
		
		tab_design	= editor.e('#tab-design')
		themes		= tab_design.e('.theme-select')
		themes.e('a.navy').click()
		sleep(3)
		
		button = self.e('.submit.button.left')
		button.click()
		
		wrapper = self.e('#container_wrap')
		self.assertIn('navy', wrapper.get_attribute('class'))
																
		editor = self.e('.channel_editor')
		settings = editor.e('.settings')
		
		settings.click()
		settings_menu	= editor.e('.settings_menu')
		self.assertTrue(settings_menu.is_displayed())
		design			= settings_menu.e('a[href="#tab-design"]')
		design.click()
		
		tab_design	= editor.e('#tab-design')
		themes		= tab_design.e('.theme-select')
		themes.e('a.orange').click()
		sleep(3)
		
		button = self.e('.submit.button.left')
		button.click()
		
		wrapper = self.e('#container_wrap')
		self.assertIn('orange', wrapper.get_attribute('class'))
														
		editor		= self.e('.channel_editor')
		settings	= editor.e('.settings')
		
		settings.click()
		settings_menu	= editor.e('.settings_menu')
		self.assertTrue(settings_menu.is_displayed())
		design			= settings_menu.e('a[href="#tab-design"]')
		design.click()
		
		tab_design	= editor.e('#tab-design')
		themes		= tab_design.e('.theme-select')
		themes.e('a.pink').click()
		sleep(3)
		
		button = self.e('.submit.button.left')
		button.click()
		
		wrapper = self.e('#container_wrap')
		self.assertIn('pink', wrapper.get_attribute('class'))
											
		editor		= self.e('.channel_editor')
		settings	= editor.e('.settings')
		
		settings.click()
		settings_menu	= editor.e('.settings_menu')
		self.assertTrue(settings_menu.is_displayed())
		design			= settings_menu.e('a[href="#tab-design"]')
		design.click()
		
		tab_design	= editor.e('#tab-design')
		themes		= tab_design.e('.theme-select')
		themes.e('a.purple').click()
		sleep(3)
		
		button	= self.e('.submit.button.left')
		button.click()
		
		wrapper	= self.e('#container_wrap')
		self.assertIn('purple', wrapper.get_attribute('class'))
										
		editor = self.e('.channel_editor')
		settings = editor.e('.settings')
		
		settings.click()
		settings_menu	= editor.e('.settings_menu')
		self.assertTrue(settings_menu.is_displayed())
		design			= settings_menu.e('a[href="#tab-design"]')
		design.click()
		
		tab_design	= editor.e('#tab-design')
		themes		= tab_design.e('.theme-select')
		themes.e('a.red').click()
		sleep(3)
		
		button = self.e('.submit.button.left')
		button.click()
		
		wrapper = self.e('#container_wrap')
		self.assertIn('red', wrapper.get_attribute('class'))
										
		editor = self.e('.channel_editor')
		settings = editor.e('.settings')
		
		settings.click()
		settings_menu = editor.e('.settings_menu')
		self.assertTrue(settings_menu.is_displayed())
		design = settings_menu.e('a[href="#tab-design"]')
		design.click()
		
		tab_design = editor.e('#tab-design')
		
		h5s = tab_design.es('h5')
		
		headings = ['Choose a colour theme', 'Upload your photo or logo', 'Upload a Banner', 'Upload a Background Image']
		for n in range(len(headings)): self.assertEqual(headings[n], h5s[n].text)
	
	@logged_in
	@url('/channels/view/%d/' % ID_USER)
	def test_upload_avatar(self):
		
		editor			= self.e('.channel_editor')
		
		settings		= editor.e('.settings')
		settings.click()
		
		settings_menu	= editor.e('.settings_menu')
		design			= settings_menu.e('a[href="#tab-design"]')
		design.click()
		
		tab_design = editor.e('#tab-design')
		tab_design.e('h5+input').send_keys(os.getcwd()+'/avatar.jpg')
		sleep(3)
		
		button = self.e('.submit.button.left')
		button.click()
		self.assertEqual('%s/channels/img/35019/logo/1/dim/200x200/crop/1/cache/0/' % URL_BASE, self.e('.chan_logo>img').get_attribute('src'))
		
		# =============== It is time to remove the avatar in order test ready for running again :) =======
		
		editor = self.e('.channel_editor')
		
		settings = editor.e('.settings')
		settings.click()
		
		settings_menu = editor.e('.settings_menu')
		design = settings_menu.e('a[href="#tab-design"]')
		design.click()
		
		tab_design = editor.e('#tab-design')
		self.assertEqual('%s/channels/img/35019/logo/1/dim/75x75/cache/0/' % URL_BASE, tab_design.e('.image-preview img').get_attribute('src'))
		
		tab_design.e('.clear_img').click()
		
		editor = self.e('.channel_editor')
		tab_design = editor.e('#tab-design')
		
		self.browser.refresh()
		self.assertEqual('%s/resources/avatars/200x200/avatar_3.png' % URL_BASE, self.e('.chan_logo > img').get_attribute('src'))
	
	@logged_in
	@url('/channels/view/%d/' % ID_USER)
	def test_upload_banner(self):
		
		editor		= self.e('.channel_editor')
		
		settings	= editor.e('.settings')
		settings.click()
		
		settings_menu	= editor.e('.settings_menu')
		design			= settings_menu.e('a[href="#tab-design"]')
		design.click()
		
		tab_design = editor.e('#tab-design')
		tab_design.es('.col.w2 input')[0].send_keys(os.getcwd()+"/banner.jpg")
		
		button = self.e('.submit.button.left')
		button.click()
		self.assertEqual('%s/channels/img/35019/banner/1/dim/980x500/cache/0/' % URL_BASE, self.e('#site-content>img').get_attribute('src'))
		
		editor		= self.e('.channel_editor')
		settings	= editor.e('.settings')
		
		settings.click()
		
		settings_menu	= editor.e('.settings_menu')
		design			= settings_menu.e('a[href="#tab-design"]')
		design.click()
		
		tab_design = editor.e('#tab-design')
		
		tab_design.e('.clear_img').click()
		sleep(6)
		editor		= self.e('.channel_editor')
		tab_design	= editor.e('#tab-design')
	
	@logged_in
	@url('/channels/view/%d/' % ID_USER)
	def test_upload_background_image(self):
		
		editor		= self.e('.channel_editor')
		
		settings	= editor.e('.settings')
		settings.click()
		
		settings_menu	= editor.e('.settings_menu')
		design			= settings_menu.e('a[href="#tab-design"]')
		design.click()
		
		tab_design = editor.e('#tab-design')
		tab_design.es('.col.w2 input')[1].send_keys(os.getcwd()+"/background.jpg")
		
		button = self.e('.submit.button.left')
		button.click()
		
		sleep(3)
		
		# TODO assert image
		
		editor		= self.e('.channel_editor')
		settings	= editor.e('.settings')
		
		settings.click()
		
		settings_menu	= editor.e('.settings_menu')
		design			= settings_menu.e('a[href="#tab-design"]')
		design.click()
		
		tab_design = editor.e('#tab-design')
		tab_design.e('.clear_img').click()
		
	
	@logged_in
	@url('/channels/view/%d/' % ID_USER)
	def test_sharing(self):
		
		editor		= self.e_wait('.channel_editor')
		settings	= editor.e('.settings')
		settings.click()
		sleep(2)
		
		settings_menu = editor.e('.settings_menu')
		self.assertTrue(settings_menu.is_displayed())
		
		link_site = settings_menu.e('li:nth-of-type(6) a')
		self.assertEqual('%s/channels/view/%d/#tab-embed' % (URL_BASE, ID_USER), link_site.get_attribute('href'))
		self.assertEqual('Link with my site', link_site.text)
		
		link_site.click()
		
		tab_embed = editor.e('#tab-embed')
		self.assertTrue(tab_embed.is_displayed())
		
		self.assertEqual('Link with my site', tab_embed.e('.main h3').text)
		
		headings = ['Link to my profile', 'Badge Get Badge Code', 'Social Media Icon Get Icon Code', 'Embed my content on my site']
		
		h4s = tab_embed.es('h4')
		
		for n in range(len(headings)): self.assertEqual(headings[n], h4s[n].text)
		
		get_badge = tab_embed.e('.col.w2:nth-of-type(1) h4 a')
		get_badge.click()
		sleep(3)
		
		dialog = self.e('.embed-profile')
		self.assertTrue(dialog.is_displayed())
		self.assertEqual('Copy and paste this HTML to insert the Historypin Badge into your website.', dialog.e('h4').text)
		self.assertIn("http://www.historypin.com/channels/view/%d/" % ID_USER, dialog.e('textarea').text)
		
		dialog.parent_node().e('.ui-dialog-titlebar-close').click()
		self.assertFalse(dialog.is_displayed())
									
		editor			= self.e('.channel_editor')
		settings		= editor.e('.settings')
		settings.click()
		settings_menu	= editor.e('.settings_menu')
		
		link_site = settings_menu.e('li:nth-of-type(6) a')
		link_site.click()
		tab_embed = editor.e('#tab-embed')
		self.assertTrue(tab_embed.is_displayed())
		
		get_icon = tab_embed.es('.col.w2:nth-of-type(2) a')[1]
		self.assertIn('social_pin', get_icon.get_attribute('class'))
		get_icon.click()
		sleep(3)
		
		dialog = self.e('.embed-social-media')
		self.assertEqual('Copy and paste this HTML to insert the Historypin Social Media icon into your website.', dialog.e('h4').text)
		self.assertIn("http://www.historypin.com/channels/view/%d/" % ID_USER, dialog.e('textarea').text)
		
		dialog.parent_node().e('.ui-dialog-titlebar-close').click()
		self.assertFalse(dialog.is_displayed())
											
		editor = self.e('.channel_editor')
		settings = editor.e('.settings')
		
		settings.click()
		
		settings_menu = editor.e('.settings_menu')
		
		link_site = settings_menu.e('li:nth-of-type(6) a')
		link_site.click()
		
		tab_embed = editor.e('#tab-embed')
		self.assertTrue(tab_embed.is_displayed())
		
		embed_cnt = tab_embed.e('.embed-cnt')
		self.assertEqual('Embed my content on my site', embed_cnt.e('h4').text)
		self.assertEqual("You can now embed your Profile on Historypin into your site. Note, only Tours and Collections made from stuff you've uploaded will appear, not those containing other people's stuff you've favourited.", embed_cnt.e('p').text)
		self.assertEqual('%s/resources/images/embed_on_site.png' % URL_BASE, embed_cnt.e('img').get_attribute('src'))
		
		button = embed_cnt.e('.button.left')
		self.assertEqual('Generate Code', button.e('span').text)
		
		views = ['Show Map View', 'Show Photo List View', 'Show Published Collections', 'Show Published Tours']
		label = embed_cnt.es('label')
		
		for n in range(len(views)): self.assertEqual(views[n], label[n].text)
		
		checkbox = embed_cnt.es('input')
		self.assertFalse(checkbox[0].is_selected())
		self.assertFalse(checkbox[1].is_selected())
		self.assertFalse(checkbox[2].is_selected())
		self.assertFalse(checkbox[3].is_selected())
		
		checkbox[0].click()
		self.assertTrue(checkbox[0].is_selected())
		sleep(2)
		button.click()
		
		dialog = self.e('.embed-channel')
		self.assertEqual('Your Code:', dialog.e('h4').text)
		self.assertEqual('Copy and paste the following HTML and insert it in your website. You can find more detailed instructions and tips on custom parameters here', dialog.e('p').text)
		self.assertEqual('%s/embed/help/' % URL_BASE, dialog.e('p a').get_attribute('href'))
		self.assertIn("%s/e/17/" % URL_ATTACH, dialog.e('textarea').text)
		# '%s/collections/all' % URL_ATTACH
		
		dialog.parent_node().e('.ui-dialog-titlebar-close').click()
		
		self.assertFalse(dialog.is_displayed())
		checkbox[0].click()
		self.assertFalse(checkbox[0].is_selected())
		
												
		
		editor		= self.e('.channel_editor')
		settings	= editor.e('.settings')
		
		settings.click()
		
		settings_menu	= editor.e('.settings_menu')
		link_site		= settings_menu.e('li:nth-of-type(6) a')
		
		link_site.click()
		
		tab_embed = editor.e('#tab-embed')
		self.assertTrue(tab_embed.is_displayed())
		
		embed_cnt = tab_embed.e('.embed-cnt')
		
		button = embed_cnt.e('.button.left')
		self.assertEqual('Generate Code', button.e('span').text)
		
		checkbox = embed_cnt.es('input')
		self.assertFalse(checkbox[0].is_selected())
		self.assertFalse(checkbox[1].is_selected())
		self.assertFalse(checkbox[2].is_selected())
		self.assertFalse(checkbox[3].is_selected())
		
		checkbox[1].click()
		self.assertTrue(checkbox[1].is_selected())
		button.click()
		
		dialog = self.e('.embed-channel')
		self.assertEqual('Your Code:', dialog.e('h4').text)
		self.assertEqual('Copy and paste the following HTML and insert it in your website. You can find more detailed instructions and tips on custom parameters here', dialog.e('p').text)
		self.assertEqual('%s/embed/help/' % URL_BASE, dialog.e('p a').get_attribute('href'))
		self.assertIn("%s/e/18/" % URL_ATTACH, dialog.e('textarea').text)
		
		dialog.parent_node().e('.ui-dialog-titlebar-close').click()
		
		self.assertFalse(dialog.is_displayed())
		checkbox[1].click()
		self.assertFalse(checkbox[1].is_selected())
														
		
		editor		= self.e('.channel_editor')
		settings	= editor.e('.settings')
		
		settings.click()
		
		settings_menu	= editor.e('.settings_menu')
		link_site		= settings_menu.e('li:nth-of-type(6) a')
		
		link_site.click()
		
		tab_embed = editor.e('#tab-embed')
		self.assertTrue(tab_embed.is_displayed())
		
		embed_cnt = tab_embed.e('.embed-cnt')
		
		button		= embed_cnt.e('.button.left')
		self.assertEqual('Generate Code', button.e('span').text)
		
		checkbox	= embed_cnt.es('input')
		self.assertFalse(checkbox[0].is_selected())
		self.assertFalse(checkbox[1].is_selected())
		self.assertFalse(checkbox[2].is_selected())
		self.assertFalse(checkbox[3].is_selected())
		
		checkbox[2].click()
		self.assertTrue(checkbox[2].is_selected())
		button.click()
		
		dialog = self.e('.embed-channel')
		self.assertEqual('Your Code:', dialog.e('h4').text)
		self.assertEqual('Copy and paste the following HTML and insert it in your website. You can find more detailed instructions and tips on custom parameters here', dialog.e('p').text)
		self.assertEqual('%s/embed/help/' % URL_BASE, dialog.e('p a').get_attribute('href'))
		self.assertIn("%s/e/20/" % URL_ATTACH, dialog.e('textarea').text)
		
		dialog.parent_node().e('.ui-dialog-titlebar-close').click()
		sleep(2)
		self.assertFalse(dialog.is_displayed())
		checkbox[2].click()
		sleep(2)
		self.assertFalse(checkbox[2].is_selected())
																
		
		editor		= self.e('.channel_editor')
		settings	= editor.e('.settings')
		
		settings.click()
		
		settings_menu	= editor.e('.settings_menu')
		link_site		= settings_menu.e('li:nth-of-type(6) a')
		
		link_site.click()
		
		tab_embed = editor.e('#tab-embed')
		self.assertTrue(tab_embed.is_displayed())
		
		embed_cnt	= tab_embed.e('.embed-cnt')
		button		= embed_cnt.e('.button.left')
		
		self.assertEqual('Generate Code', button.e('span').text)
		
		checkbox = embed_cnt.es('input')
		self.assertFalse(checkbox[0].is_selected())
		self.assertFalse(checkbox[1].is_selected())
		self.assertFalse(checkbox[2].is_selected())
		self.assertFalse(checkbox[3].is_selected())
		
		checkbox[3].click()
		self.assertTrue(checkbox[3].is_selected())
		button.click()
		
		dialog = self.e('.embed-channel')
		self.assertEqual('Your Code:', dialog.e('h4').text)
		self.assertEqual('Copy and paste the following HTML and insert it in your website. You can find more detailed instructions and tips on custom parameters here', dialog.e('p').text)
		self.assertEqual('%s/embed/help/' % URL_BASE, dialog.e('p a').get_attribute('href'))
		self.assertIn('%s/e/24/' % URL_ATTACH, dialog.e('textarea').text)
		
		dialog.parent_node().e('.ui-dialog-titlebar-close').click()
		
		self.assertFalse(dialog.is_displayed())
		checkbox[3].click()
		
		self.assertFalse(checkbox[3].is_selected())
							
		editor		= self.e('.channel_editor')
		settings	= editor.e('.settings')
		
		settings.click()
		
		settings_menu	= editor.e('.settings_menu')
		link_site		= settings_menu.e('li:nth-of-type(6) a')
		
		link_site.click()
		
		tab_embed = editor.e('#tab-embed')
		self.assertTrue(tab_embed.is_displayed())
		
		help		= tab_embed.e('.help')
		h3s_help	= help.es('h3')
		
		self.assertEqual("Get Some Inspiration"	, h3s_help[0].text)
		self.assertEqual("Get help"				, h3s_help[1].text)
		
		self.assertEqual('Check out these examples to see what other people have done on their site.', help.e('p:nth-of-type(1)').text)
		
		examples = [
			['http://www.everythingcurious.co.uk/Bath_in_Time_About_Us/HistoryPin.html'	, 'Bath in Time'],
			['http://www.steveclifford.com/?page_id=4'									, 'Steve Clifford'],
			['http://www.biggleswadehistory.org.uk/historypin.htm'						, 'Biggleswade History Society'],
			['http://digital.library.lse.ac.uk/collections/streetlife#historypin'		, 'LSE Library'],
			['http://www.arthurlloyd.co.uk/Theatreland/Theatreland.htm'					, 'Arthurlloydcouk'],
		]
		
		sites_help = help.es('a')
		
		for n in range(len(examples)):
			i = examples[n]
			self.assertEqual(i[0]	, sites_help[n].get_attribute('href'))
			self.assertEqual(i[1]								, sites_help[n].text)
		
		
		self.assertEqual('If you get stuck or have any questions, check out our How To page and FAQs and please feel free to contact us at historypin@wearewhatwedo.org', help.e('p:last-of-type').text)
		
		links = [
			['%s/community/howtos/'	% URL_BASE, 'How To page'],
			['%s/faq/'				% URL_BASE, 'FAQs'],
			['mailto:historypin@wearewhatwedo.org'	, 'historypin@wearewhatwedo.org'],
		]
		
		links_help = help.es('p:last-of-type a')
		
		for n in range(len(links)):
			i = links[n]
			self.assertEqual(i[0]	, links_help[n].get_attribute('href'))
			self.assertEqual(i[1]	, links_help[n].text)
	
	@logged_in
	@url('/channels/view/%d/' % ID_USER)
	def test_stuff_i_like(self):
		
		editor		= self.e('.channel_editor')
		settings	= editor.e('.settings')
		
		settings.click()
		
		settings_menu	= editor.e('.settings_menu')
		channels		= settings_menu.e('li:nth-of-type(9) a')
		
		channels.click()
		
		tab_subscriptions = editor.e('#tab-subscriptions')
		self.assertTrue(tab_subscriptions.is_displayed())
		
		self.assertEqual("Profiles I'm a fan of:", tab_subscriptions.e('h3').text)
		
		channels = [
			['%d/' % FAVOURITE_CHANNELS[0], '/%d/' % FAVOURITE_CHANNELS_IMAGES[0], 'City of Richmond Archives'],
			['%d/' % FAVOURITE_CHANNELS[1], '/%d/' % FAVOURITE_CHANNELS_IMAGES[1], 'uf history hunt'],
			['%d/' % FAVOURITE_CHANNELS[2], '/%d/' % FAVOURITE_CHANNELS_IMAGES[2], 'Stanford University Archives'],
		]
		
		channels_list	= tab_subscriptions.e('.channels-list')
		logo_link		= channels_list.es('.logo')
		img				= channels_list.es('img')
		channel			= channels_list.es('.name')
		
		for n in range(len(channels)):
			i = channels[n]
			self.assertEqual(URL_BASE + '/channels/view/' 		+ i[0], logo_link[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/channels/view/' 	+ i[0], channel[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/channels/img' 		+ i[1] + 'logo/1/dim/70x70/crop/1/', img[n].get_attribute('src'))
			self.assertEqual(i[2], channel[n].text)
		
		editor		= self.e('.channel_editor')
		settings	= editor.e('.settings')
		
		settings.click()
		
		settings_menu	= editor.e('.settings_menu')
		fans			= settings_menu.e('li:nth-of-type(10) a')
		fans.click()
		
		tab_subsrcribers = editor.e('#tab-subscribers')
		self.assertTrue(tab_subsrcribers.is_displayed())
		self.assertEqual("My fans:"				, tab_subsrcribers.e('h3').text)
		self.assertEqual("You have no fans yet.", tab_subsrcribers.e('p').text)
	
	# @unittest.expectedFailure  # TODO Bug #3121 should be fixed
	@logged_in
	@url('/channels/view/%d' % ID_USER_VIEW)
	def test_become_fan(self):
		
		self.e('#subscribe').click()
		sleep(1)
		# self.assertEqual('Un-Fan', self.e('#subscribe span').text)
		
		self.go('/channels/view/%d' % ID_USER)
		
		editor			= self.e('.channel_editor')
		settings		= editor.e('.settings')
		channels		= editor.e('li:nth-of-type(9) a')
		
		settings.click()
		sleep(4)
		channels.click()
		
		sleep(4)
		
		tab_subscriptions	= editor.e('#tab-subscriptions')
		fan_channel			= tab_subscriptions.e('li:nth-of-type(4)')
		
		self.assertEqual('%s/channels/view/%d/' % (URL_BASE, ID_USER_VIEW), fan_channel.e('.logo').get_attribute('href'))
		self.assertEqual('%s/channels/view/%d/' % (URL_BASE, ID_USER_VIEW), fan_channel.e('.name').get_attribute('href'))
		self.assertEqual('%s/channels/img/%d/logo/1/dim/70x70/crop/1/' % (URL_BASE, ID_USER_VIEW), fan_channel.e('.logo img').get_attribute('src'))
		
		self.go('/channels/view/%d' % ID_USER_VIEW)
		
		sleep(3)
		self.e('#subscribe').click()
		sleep(1)
		
		self.go('/channels/view/%d' % ID_USER)
		
		editor			= self.e('.channel_editor')
		settings		= editor.e('.settings')
		channels		= editor.e('li:nth-of-type(9) a')
		settings.click()
		channels.click()
		
		self.assertFalse(tab_subscriptions.exists(fan_channel))
	
	# @logged_in  TODO fix this - this test has to use another photo
	# @url('/map/index/#!/geo:42.688019,23.320069/zoom:20/dialog:%d/tab:details/' % ID_FAVOURITE_ITEM)
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
	
	@logged_in
	@url('/upload-item/pin/phid/%d/edit/1/' % ID_EDIT_ITEM)
	def test_edit_item(self):
		
		self.assertTitle('Historypin | My Content | Edit')
		
		edit_page = self.e('#edit_photo_page')
		heading = edit_page.es('h3')
		self.assertEqual('Current item'				, heading[0].text)
		self.assertEqual('Licence'					, heading[1].text)
		self.assertEqual('Date required field'		, heading[2].text)
		self.assertEqual('Place required field'		, heading[3].text)
		
		self.assertEqual('%s/services/thumb/phid/%d/dim/260x1000/' % (URL_BASE, ID_EDIT_ITEM), edit_page.e('#photo-preview img').get_attribute('src'))
		
		info		= edit_page.e('.inner.left')
		label		= info.es('label')
		title		= info.es('input')[0]
		tags		= info.es('input')[1]
		desc		= info.e('textarea')
		paragraph	= info.es('p')
		
		self.assertEqual('Title required field'	, label[0].text)
		self.assertEqual('Description'			, label[1].text)
		self.assertEqual('Tags'					, label[2].text)
		
		title.clear()
		title.send_keys('Bulgarian Army Theater')
		self.assertEqual('Remaining characters: 78', paragraph[0].text)
		
		desc.clear()
		desc.send_keys('This is a photo of the famous Bulgarian Army Theater .')
		
		tags.clear()
		tags.send_keys('theater, theatre, bulgarian army')
		self.assertEqual('Remaining characters: 468', paragraph[1].text)
		
		license	= edit_page.e('.section.license')
		option	= license.e('#photo_info_license_type')
		option.click()
		option.e('option:nth-of-type(2)').click()
		
		copyright = license.e('#photo_info_copyright')
		copyright.click()
		copyright.clear()
		copyright.send_keys('Test')
		sleep(3)
		
		photo_link = license.e('#photo_info_link')
		photo_link.click()
		photo_link.clear()
		photo_link.send_keys('http://novini.bg')
		sleep(3)
		
		author = license.e('#photo_info_author')
		author.click()
		author.clear()
		author.send_keys('Unknown')
		sleep(3)
		
		photo_notes = license.e('#photo_info_notes')
		photo_notes.click()
		photo_notes.clear()
		photo_notes.send_keys('Test Notes')
		
		date_select = edit_page.e('.section.date-select')
		date_select.e('#day option:nth-of-type(3)').click()  # assert for all
		date_select.e('#month option:nth-of-type(3)').click()  # assert for all
		date_select.e('#year option:nth-of-type(3)').click()  # assert for all
		
		note = edit_page.e('.notice .inner')
		self.assertIn('ss-icon'	, note.e('span').get_attribute('class'))
		self.assertIn('ss-alert', note.e('span').get_attribute('class'))
		self.assertEqual('Note: To make it appear on the map you need to add both the date and the place'							, note.e('h2').text)
		self.assertEqual('Without these details, your stuff will only appear on your profile. You can always add this info later.'	, note.e('p').text)
		
		place		= edit_page.e('#location_editor')
		checkbox	= place.e('#has_streetview')
		
		checkbox.click()
		self.assertFalse(place.e('#pin-tab-sv').is_displayed())
		checkbox.click()
		self.assertTrue(checkbox.is_selected())
		self.assertTrue(place.e('#pin-tab-sv').is_displayed())
		
		sleep(3)
		location = place.e('#location')  # assert the address
		# self.assertEqual('Find on map', location.e('span').text)
		
		cancel = edit_page.e('.cancel')
		self.assertEqual('Cancel', cancel.e('span').text)
		self.assertEqual('%s/upload/' % URL_BASE, cancel.get_attribute('href'))
		
		save = edit_page.e('#photo_pin')
		self.assertEqual('Save and Continue', save.e('span').text)
		self.assertEqual('%s/upload-item/pin/phid/%d/edit/1/#' % (URL_BASE, ID_EDIT_ITEM), save.get_attribute('href'))
		save.click()
		
		self.go('/upload-item/pin/phid/%d/edit/1/' % ID_EDIT_ITEM)
		
		edit_page = self.e('#edit_photo_page')
		
		info		= edit_page.e('.inner.left')
		label		= info.es('label')
		title		= info.es('input')[0]
		desc		= info.e('textarea')
		tags		= info.es('input')[1]
		paragraph	= info.es('p')
		
		self.assertEqual('Bulgarian Army Theater', title.get_attribute('value'))
		# self.assertEqual('This is a photo of the famous Bulgarian Army Theater .', desc.get_attribute('value'))
		self.assertEqual('theater, theatre, bulgarian army', tags.get_attribute('value'))
		
		license			= edit_page.e('.section.license')
		option			= license.e('#photo_info_license_type')
		
		self.assertEqual('N'				, option.e('option:nth-of-type(2)').get_attribute('value'))
		self.assertEqual('Test'				, license.e('#photo_info_copyright').get_attribute('value'))
		self.assertEqual('http://novini.bg'	, license.e('#photo_info_link').get_attribute('value'))
		self.assertEqual('Unknown'			, license.e('#photo_info_author').get_attribute('value'))
		self.assertEqual('Test Notes'		, license.e('#photo_info_notes').get_attribute('value'))
		
		date_select = edit_page.e('.section.date-select')
		self.assertEqual('02'	, date_select.e('#day option:nth-of-type(3)').get_attribute('value'))
		self.assertEqual('2'	, date_select.e('#month option:nth-of-type(3)').get_attribute('value'))
		self.assertEqual('2014'	, date_select.e('#year option:nth-of-type(2)').get_attribute('value'))
		
		place = edit_page.e('#location_editor')
		
		checkbox = place.e('#has_streetview')
		self.assertTrue(checkbox.is_selected())
		self.assertTrue(place.e('#pin-tab-sv').is_displayed())
		
		location = place.e('#location')
		self.assertEqual('ulitsa "Georgi. S. Rakovski" 98, 1000 Sofia, Bulgaria', location.get_attribute('value'))
	
	@logged_in
	@url('/upload/confirm/edit/1')
	def test_confirm_page(self):
		
		self.assertTitle('Historypin | My Content | Edit')
		
		self.assertEqual('All done', self.e('.done.current').text)
		
		self.assertIn('ss-icon'		, self.e('.done.current span').get_attribute('class'))
		self.assertIn('ss-newmoon'	, self.e('.done.current span').get_attribute('class'))
		
		all_done = self.e('.all_done')
		self.assertEqual('All done'						, all_done.es('h3')[0].text)
		self.assertEqual('Your changes have been saved.', all_done.e('p').text)
		
		button_add = all_done.e('.channel-button:nth-of-type(1)')
		self.assertEqual('Add more content'		, button_add.e('span').text)
		self.assertEqual('%s/upload/' % URL_BASE, button_add.get_attribute('href'))
		
		button_view = all_done.e('.channel-button:nth-of-type(2)')
		self.assertEqual('View my content'							, button_view.e('span').text)
		self.assertEqual('%s/channels/view/%d/' % (URL_BASE, ID_USER), button_view.get_attribute('href'))
		
		self.assertEqual("Now why not share what you've just pinned?", all_done.es('h3')[1].text)
		self.assertEqual("Share:", all_done.es('h3')[2].text)
		
		social_buttons = self.e('.addthis_toolbox span')
		self.assertIn('ss-icon', social_buttons.get_attribute('class'))
		
		social_icons = ['ss-social-circle', 'ss-social-circle', 'ss-social-circle', 'ss-plus']
		
		for n in range(len(social_icons)-1): self.assertIn(social_icons[n], social_buttons.get_attribute('class'))
