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
		
		date_upload = self.e('.list-filter input[id=date_upload]')
		view_count = self.e('.list-filter input[id=view_count]')
		all_items = self.e('.list-filter input[id=all]')
		favourites = self.e('.list-filter input[id=unpinned]')
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
		self.assertIsInstance(info, WebElement)
		self.assertIsInstance(actions, WebElement)
		
		favourites.click()
		sleep(2)
		self.assertIn('favourites', URL_BASE + '/attach/uid10649049/photos/list/#/get/popular/show/favourites/')
		self.assertFalse(all_items.is_selected()			, 'None')
		self.assertIsInstance(img_holder, WebElement)
		self.assertIsInstance(info, WebElement)
		self.assertIsInstance(actions, WebElement)
		
		date_upload.click()
		sleep(2)
		self.assertTrue(date_upload.is_selected()	, 'None')
		self.assertFalse(view_count.is_selected()	, 'None')
		self.assertIsInstance(img_holder, WebElement)
		self.assertIsInstance(info, WebElement)
		self.assertIsInstance(actions, WebElement)
		
	
	@url('/attach/uid10649049/map/index/#!/geo:26.816514,24.138716/zoom:2/')
	def test_collections_tab(self):
		
		collections_tab = self.e('.list_tabs li a[href$="/attach/uid10649049/collections/all/"]')
		self.assertEqual('Collections'	, collections_tab.text)
		collections_tab.click()
		sleep(2)
		
		item = self.e('#photo_list_content .list li a')
		
		self.assertEqual(URL_BASE + '/attach/uid10649049/collections/view/id/22782015/title/Test%20Collection%20for%20automated%20test', item.get_attribute('href'))
		self.assertEqual(URL_BASE + '/services/thumb/phid/22363018/dim/195x150/crop/1/', item.e('img').get_attribute('src'))
		self.assertIn('collection-icon', item.e('span').get_attribute('class'))
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
