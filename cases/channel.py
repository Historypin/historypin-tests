# -*- coding: utf-8 -*-

from base import *
import os, sys

class Channel(HPTestCase):
	
	@url('/channels/view/{0}/'.format(ID_USER_VIEW))
	def test_channel_description(self):
		self.assertTitle('Gabss | Historypin')
		
		info = self.e('.chan.info')
		self.assertEqual('Gabss', info.e('h2').text)
		self.assertEqual('{0}/channels/img/{1}/logo/1/dim/200x200/crop/1/'.format(URL_BASE, ID_USER_VIEW), info.e('img').get_attribute('src'))
		
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
	
	@url('/channels/view/{0}/'.format(ID_USER_VIEW))
	def test_channel_details(self):
		
		h3 = self.es('.chan.options h3')
		self.assertEqual('Profile Details'	, h3[0].text)
		self.assertEqual('Share:'			, h3[1].text)
		
		# paragraph = self.e('.chan.options p')
		# texts = ['Profile views:', 'Fans:', 'Pins:', 'Tours:', 'Collections:']
		
		# for n in range(len(texts)): self.assertIn(texts[n], paragraph.text)
		
		sleep(4)  # AJAX
		button = self.e('.chan.options .channel-button.left')
		self.assertEqual('Become a Fan'															, button.text)
		self.assertEqual('{0}/user/?from=/channels/view/{1}/'.format(URL_BASE, ID_USER_VIEW)	, button.get_attribute('href'))
		
		social_buttons = self.e('.addthis_toolbox span')
		self.assertIn('ss-icon', social_buttons.get_attribute('class'))
		
		social_icons = ['ss-social-circle', 'ss-social-circle', 'ss-social-circle', 'ss-plus']
		
		for n in range(len(social_icons)-1): self.assertIn(social_icons[n], social_buttons.get_attribute('class'))
	
	@url('/attach/uid{0}/photos/activity_feed/'.format(ID_USER_VIEW))
	def test_activity_tab(self):
		
		sleep(3)
		activity_tab = self.e('#embed_tabs li a[href$="/attach/uid{0}/photos/activity_feed/"]'.format(ID_USER_VIEW))
		self.assertEqual('Activity Feed', activity_tab.text)
		
		meta = self.e('.meta')
		self.assertIsInstance(meta.e('.photo-date'), WebElement)
		
		self.assertEqual('{0}/channels/view/{1}/'.format(URL_BASE, ID_USER_VIEW), meta.e('.photo-user').get_attribute('href'))
		self.assertEqual('Gabss', meta.e('.photo-user').text)
		
		self.assertEqual('{0}/channels/img/{1}/logo/1/dim/100x100/'.format(URL_BASE, ID_USER_VIEW), self.e('.avatar.fluid').get_attribute('src'))
		
		pin = self.e('.pin')
		self.assertIsInstance(pin.e('a:nth-of-type(1)'), WebElement)
		self.assertIsInstance(pin.e('a:nth-of-type(1) img'), WebElement)
		
		self.assertIsInstance(pin.e('a:nth-of-type(2)'), WebElement)
		
	@unittest.expectedFailure  # TODO fix this, cannot find the elememt
	@url('/attach/uid{0}/map/index/#!/geo:26.816514,24.138716/zoom:2'.format(ID_USER_VIEW))
	def test_map_tab(self):
		sleep(2)
		
		map_tab = self.e('.list_tabs li a[href$="/attach/uid{0}/map/index/"]'.format(ID_USER_VIEW))
		self.assertEqual('Map'	, map_tab.text)
		
		search_filters = self.e('#search-filters')
		self.assertIsInstance(search_filters.e('input#location'), WebElement)
		self.assertIsInstance(search_filters.e('input#tags')	, WebElement)
		
		submit = self.e('#photo_search_submit')
		self.assertIsInstance(submit, WebElement)
		self.assertEqual('Go', submit.e('span').text)
		
		self.assertIsInstance(self.e('#date-selector #date-slider')	, WebElement)
		self.assertIsInstance(self.e('#date-slider-labels li')		, WebElement)
		
		self.e_wait('#map-canvas .hp-marker-img-wrapper[class$="{0}"]'.format(ID_MAP_ITEM)).parent_node().click()
		
		sleep(5)
		dlg = self.e('#info-dialog')
		self.assertIsInstance(dlg, WebElement)
		
	
	@url('/attach/uid{0}/map/index/#!/geo:26.816514,24.138716/zoom:2/'.format(ID_USER_VIEW))
	def test_list_tab(self):
		
		list_tab = self.e('.list_tabs li a[href$="/attach/uid{0}/photos/list/"]'.format(ID_USER_VIEW))
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
		# self.assertEqual('%s/attach/uid%d/map/index/#!/geo:43.325176,24.960938/zoom:20/dialog:361341/tab:details/'.format(URL_BASE, ID_USER_VIEW), img_holder.get_attribute('href'))
		self.assertEqual('{0}/services/thumb/phid/{1}/dim/170x130/crop/1/'.format(URL_BASE, ID_MAP_ITEM), img_holder.e('img').get_attribute('src'))
		
		info = self.e('#photo_list_content .info')
		self.assertIsInstance(info.e('h5'), WebElement)
		self.assertIsInstance(info.e('p'), WebElement)
		
		actions = self.e('#photo_list_content .info-actions')
		self.assertIn('ss-icon', actions.e('a span').get_attribute('class'))
		
		view_count.click()
		sleep(2)
		self.assertIn('popular', '{0}/attach/uid{1}/photos/list/cache/0/#/show/all/get/popular/'.format(URL_BASE, ID_USER_VIEW))
		self.assertFalse(date_upload.is_selected())
		self.assertIsInstance(img_holder, WebElement)
		self.assertIsInstance(info		, WebElement)
		self.assertIsInstance(actions	, WebElement)
		
		favourites.click()
		sleep(2)
		self.assertIn('favourites', '{0}/attach/uid{1}/photos/list/cache/0/#/get/popular/show/favourites/'.format(URL_BASE, ID_USER_VIEW))
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
		
	
	@url('/attach/uid{0}/map/index/#!/geo:26.816514,24.138716/zoom:2/'.format(ID_USER_VIEW))
	def test_collections_tab(self):
		
		collections_tab = self.e('.list_tabs li a[href$="/attach/uid{0}/collections/all/"]'.format(ID_USER_VIEW))
		self.assertEqual('Collections'	, collections_tab.text)
		collections_tab.click()
		sleep(2)
		
		item = self.e('#photo_list_content .list li a')
		
		self.assertEqual('{0}/attach/uid{1}/collections/view/id/{2}/title/Test%20Collection%20for%20automated%20test'.format(URL_BASE, ID_USER_VIEW, ID_COLLECTION_VIEW), item.get_attribute('href'))
		self.assertEqual('{0}/services/thumb/phid/{1}/dim/195x150/crop/1/'.format(URL_BASE, ID_COLLECTION_IMAGES[1]), item.e('img').get_attribute('src'))
		self.assertIn('collection-icon'	, item.e('span').get_attribute('class'))
		self.assertIn('ss-icon'			, item.e('span').get_attribute('class'))
		self.assertIn('ss-pictures'		, item.e('span').get_attribute('class'))
		
		paragraph_link = self.es('#photo_list_content .list li p a')
		
		self.assertEqual('{0}/attach/uid{1}/collections/view/id/{2}/title/Test%20Collection%20for%20automated%20test'.format(URL_BASE, ID_USER_VIEW, ID_COLLECTION_VIEW), paragraph_link[0].get_attribute('href'))
		self.assertEqual('Test Collection for automated test', paragraph_link[0].text)
		
		self.assertEqual('{0}/channels/view/{1}'.format(URL_BASE, ID_USER_VIEW), paragraph_link[1].get_attribute('href'))
		self.assertEqual('Gabss', paragraph_link[1].text)
	
	@url('/attach/uid{0}/map/index/#!/geo:26.816514,24.138716/zoom:2/'.format(ID_USER_VIEW))
	def test_tours_tab(self):
		
		tours_tab = self.e('.list_tabs li a[href$="/attach/uid{0}/tours/all/"]'.format(ID_USER_VIEW))
		self.assertEqual('Tours'	, tours_tab.text)
		tours_tab.click()
		sleep(2)
		
		item = self.e('#photo_list_content .list li>a')
		
		self.assertEqual('{0}/attach/uid{1}/tours/view/id/{2}/title/Test%20Tour%20for%20automated%20test'.format(URL_BASE, ID_USER_VIEW, ID_TOUR_VIEW), item.get_attribute('href'))
		self.assertEqual('{0}/services/thumb/phid/706/dim/195x150/crop/1/'.format(URL_BASE), item.e('img').get_attribute('src'))
		
		self.assertIn('tour-icon'	, item.e('span').get_attribute('class'))
		self.assertIn('ss-icon'		, item.e('span').get_attribute('class'))
		self.assertIn('ss-hiker'	, item.e('span').get_attribute('class'))
		
		paragraph_link = self.es('#photo_list_content .list li p a')
		
		self.assertEqual('{0}/attach/uid{1}/tours/view/id/{2}/title/Test%20Tour%20for%20automated%20test'.format(URL_BASE, ID_USER_VIEW, ID_TOUR_VIEW), paragraph_link[0].get_attribute('href'))
		self.assertEqual('Test Tour for automated test', paragraph_link[0].text)
		
		self.assertEqual('{0}/channels/view/{1}'.format(URL_BASE, ID_USER_VIEW), paragraph_link[1].get_attribute('href'))
		self.assertEqual('Gabss', paragraph_link[1].text)
