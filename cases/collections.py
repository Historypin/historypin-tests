# -*- coding: utf-8 -*-

from base import *

class Collections(HPTestCase):
	
	def __test_collection_listing(self):
		self.assertTitle('Historypin | Collections')
		
		main_cnt	= self.e('.col.w34')
		self.assertEqual('What are Collections?'									, main_cnt.e('h1').text)
		self.assertEqual(URL_BASE + '/collections/'									, main_cnt.e('a.main-image.no-shadow').get_attribute('href'))
		self.assertEqual(URL_BASE + '/resources/images/collections_page_image.jpg'	, main_cnt.e('img').get_attribute('src'))
		self.assertEqual('Collections bring together content around a particular topic or theme. You can explore the Collections or create a Collection of your own.',
						main_cnt.e('p').text)
		
		button		= self.e('.col.w34 a.next-button.left')
		self.assertEqual(URL_BASE + '/collections/add'	, button.get_attribute('href'))
		self.assertEqual('Make your own collection'		, button.e('span').text)
		
		self.assertEqual('All Collections'				, self.e('h3:last-of-type').text)
		
		h3 = self.e('h3.right a')
		self.assertEqual('Return to Tours & Collections', h3.text)
		self.assertEqual(URL_BASE + '/curated'			, h3.get_attribute('href'))
		
		cnt	= self.es('#photo_list_content .list li:nth-of-type(1)')
		self.assertIsInstance(cnt[0].e('a')	, WebElement)
		self.assertIsInstance(cnt[0].e('img')	, WebElement)
		self.assertIsInstance(cnt[0].e('p')	, WebElement)
		
		self.assertIn('collection-icon'	, cnt[0].e('a span').get_attribute('class'))
		self.assertIn('ss-pictures'		, cnt[0].e('a span').get_attribute('class'))
		self.assertIn('ss-icon'			, cnt[0].e('a span').get_attribute('class'))
	
	@url('/collections/')
	def test_index(self):
		self.__test_collection_listing()
	
	@logged_in
	@url('/collections/all')
	def test_all(self):
		self.__test_collection_listing()
		
		next = self.e('.show-next')
		self.assertEqual('Next'									, next.text)
		self.assertEqual(URL_BASE + '/collections/all/page/2/'	, next.get_attribute('href'))
	
	@logged_in
	@url('/collections/view/id/%d' % ID_COLLECTION + '/')
	def test_view(self):
		self.assertTitle('Historypin | Collection - Theaters in Bulgaria')
		
		# self.assertEqual(URL_BASE + '/services/thumb/phid/%d/dim/451x302/crop/1/' % ID_COLLECTION_IMAGES[2]	, self.e('img.index').get_attribute('src'))
		self.assertEqual('Theaters in Bulgaria'							, self.e('.info h2').text)
		
		paragraphs = self.es('.info p')
		self.assertEqual('Collection for famous theaters in Bulgaria'	, paragraphs[0].text)
		self.assertEqual('Created by Gabriela Ananieva'					, paragraphs[1].text)
		self.assertEqual(URL_BASE + '/channels/view/%d' % ID_USER		, paragraphs[1].e('a').get_attribute('href'))
		
		button = self.e('.info ~ a')
		self.assertEqual(URL_BASE + '/collections/slideshow/id/%d/' % ID_COLLECTION, button.get_attribute('href'))
		self.assertEqual('Slide Show'										, button.text)
		
		collection_view = [
			['geo:51.4691539556,0.0169086456299/zoom:15/dialog:%d' % ID_COLLECTION_IMAGES[0], '/%d/' % ID_COLLECTION_IMAGES[0], '2010, from elizabeth'					, '/305005'],
			['geo:51.594547,-0.379828/zoom:15/dialog:%d' % ID_COLLECTION_IMAGES[1], '/%d/' % ID_COLLECTION_IMAGES[1], '1910 - 1920, from ivormt'				, '/2086073'],
			['geo:42.693738,23.326101/zoom:15/dialog:%d' % ID_COLLECTION_IMAGES[2], '/%d/' % ID_COLLECTION_IMAGES[2]	, '2 August 2012, from Gabss'				, '/%d' % ID_USER_VIEW],
			['geo:42.694705,23.329034/zoom:15/dialog:%d' % ID_COLLECTION_IMAGES[3], '/%d/' % ID_COLLECTION_IMAGES[3], '2 February 2013, from Gabriela Ananieva'	, '/%d' % ID_USER],
		]
		
		item = self.es('#list_view .list li')
		for n in range(len(collection_view)):
			i = collection_view[n]
			self.assertEqual(URL_BASE + '/map/#!/' + i[0] + '/tab:details/', item[n].e('a.link-image').get_attribute('href'))
			self.assertEqual(URL_BASE + '/services/thumb/phid' + i[1] + 'dim/195x150/crop/1/', item[n].e('img').get_attribute('src'))
			self.assertEqual(i[2]			, item[n].e('p').text)
			self.assertEqual(URL_BASE + '/channels/view' + i[3], item[n].e('.username-wrapper a').get_attribute('href'))
		
		actions			= self.e('li:nth-of-type(4) .info-actions')
		smile_icon		= actions.e('a:nth-of-type(2)')
		
		self.assertIn('ss-icon'	, actions.e('span').get_attribute('class'))
		self.assertIn('ss-smile', smile_icon.e('span').get_attribute('class'))
		
		smile_icon.click()
		sleep(4)
		self.browser.refresh()
		self.assertEqual(URL_BASE + '/services/thumb/phid/%d/dim/451x302/crop/1/' % ID_COLLECTION_IMAGES[0]	, self.e('img.index').get_attribute('src'))
		# - after some minuted to check if the photo is changed, because it's not changed after the refresh
	
	@logged_in
	@url('/collections/slideshow/id/%d' % ID_COLLECTION + '/')
	def test_slideshow(self):
		
		self.assertTitle('Historypin | Collection - Theaters in Bulgaria')
		self.assertEqual('Theaters in Bulgaria\nExit Slideshow'										, self.e('#slide-content p').text)
		self.assertEqual(URL_BASE + '/collections/view/id/%d/title/Theaters%20in%20Bulgaria' % ID_COLLECTION, self.e('#slide-content a').get_attribute('href'))
		
		controls	= self.e('#controls')
		counter		= controls.e('#slidecounter')
		step_text	= controls.e('#slidecaption a')
		next_thumb	= self.e_wait('#nextthumb img')
		prev_thumb	= self.e_wait('#prevthumb img')
		
		navigation	= controls.e('#navigation')
		# prev_slide	= navigation.e('#prevslide')
		pause		= navigation.e('#pauseplay')
		next_slide	= navigation.e('#nextslide')
		
		sleep(3)
		pause.click()
		
		self.assertEqual(URL_BASE + '/services/thumb/phid/%d/' % ID_COLLECTION_IMAGES[3], prev_thumb.get_attribute('src'))
		self.assertIn('1/4', counter.text)
		self.assertEqual('"National Theatre in Sofia, Bulgaria"- 2 August 2012 by Gabss', step_text.text)
		self.assertEqual(URL_BASE + '/map/#!/geo:42.693738,23.326101/zoom:9/dialog:%d/tab:details/' % ID_COLLECTION_IMAGES[2], step_text.get_attribute('href'))
		self.assertEqual(URL_BASE + '/services/thumb/phid/%d/' % ID_COLLECTION_IMAGES[0], next_thumb.get_attribute('src'))
		next_slide.click()
		sleep(3)
		
		# next_thumb	= self.e('#nextthumb img')
		# prev_thumb	= self.e('#prevthumb img')
		
		# self.assertEqual(URL_BASE + '/services/thumb/phid/%d/' % ID_COLLECTION_IMAGES[2], prev_thumb.get_attribute('src'))
		# self.assertIn('2/4', counter.text)
		# self.assertEqual('"Morden College east elevation and chapel"- 2010 by elizabeth', step_text.text)
		# self.assertEqual(URL_BASE + '/map/#!/geo:51.4691539556,0.0169086456299/zoom:9/dialog:%d/tab:details/' % ID_COLLECTION_IMAGES[0], step_text.get_attribute('href'))
		# self.assertEqual(URL_BASE + '/services/thumb/phid/%d/'  % ID_COLLECTION_IMAGES[1], next_thumb.get_attribute('src'))
		# next_slide.click()
		
		# sleep(3)
		# self.assertEqual(URL_BASE + '/services/thumb/phid/%d/' % ID_COLLECTION_IMAGES[0], prev_thumb.get_attribute('src'))
		# self.assertIn('3/4', counter.text)
		# self.assertEqual('"Pinner High St from Church"- 1910 - 1920 by ivormt', step_text.text)
		# self.assertEqual(URL_BASE + '/map/#!/geo:51.594547,-0.379828/zoom:9/dialog:%d/tab:details/' % ID_COLLECTION_IMAGES[1], step_text.get_attribute('href'))
		# self.assertEqual(URL_BASE + '/services/thumb/phid/%d/' % ID_COLLECTION_IMAGES[3], next_thumb.get_attribute('src'))
		# next_slide.click()
		
		# sleep(3)
		# self.assertEqual(URL_BASE + '/services/thumb/phid/%d/' % ID_COLLECTION_IMAGES[1], prev_thumb.get_attribute('src'))
		# self.assertIn('4/4', counter.text)
		# self.assertEqual('"Bulgarian Army Theater"- 2 February 2013 by Gabriela Ananieva', step_text.text)
		# self.assertEqual(URL_BASE + '/map/#!/geo:42.694696,23.329027/zoom:9/dialog:%d/tab:details/' % ID_COLLECTION_IMAGES[3], step_text.get_attribute('href'))
		# self.assertEqual(URL_BASE + '/services/thumb/phid/%d/' % ID_COLLECTION_IMAGES[2], next_thumb.get_attribute('src'))
		# prev_slide.click()
		
		# sleep(3)
		# self.assertEqual(URL_BASE + '/services/thumb/phid/%d/' % ID_COLLECTION_IMAGES[0], prev_thumb.get_attribute('src'))
		# self.assertIn('3/4', counter.text)
		# self.assertEqual('"Pinner High St from Church"- 1910 - 1920 by ivormt', step_text.text)
		# self.assertEqual(URL_BASE + '/map/#!/geo:51.594547,-0.379828/zoom:9/dialog:%d/tab:details/' % ID_COLLECTION_IMAGES[1], step_text.get_attribute('href'))
		# self.assertEqual(URL_BASE + '/services/thumb/phid/%d/' % ID_COLLECTION_IMAGES[3], next_thumb.get_attribute('src'))
		# prev_slide.click()
		
		# sleep(3)
		# self.assertEqual(URL_BASE + '/services/thumb/phid/%d/' % ID_COLLECTION_IMAGES[2], prev_thumb.get_attribute('src'))
		# self.assertIn('2/4', counter.text)
		# self.assertEqual('"Morden College east elevation and chapel"- 2010 by elizabeth', step_text.text)
		# self.assertEqual(URL_BASE + '/map/#!/geo:51.4691539556,0.0169086456299/zoom:9/dialog:%d/tab:details/' % ID_COLLECTION_IMAGES[0], step_text.get_attribute('href'))
		# self.assertEqual(URL_BASE + '/services/thumb/phid/%d/' % ID_COLLECTION_IMAGES[1], next_thumb.get_attribute('src'))
		# sleep(3)
		# prev_slide.click()
		# self.assertEqual(URL_BASE + '/services/thumb/phid/%d/' % ID_COLLECTION_IMAGES[3], prev_thumb.get_attribute('src'))
		# self.assertIn('1/4', counter.text)
		# self.assertEqual('"National Theatre in Sofia, Bulgaria"- 2 August 2012 by Gabss', step_text.text)
		# self.assertEqual(URL_BASE + '/map/#!/geo:42.693738,23.326101/zoom:9/dialog:%d/tab:details/' % ID_COLLECTION_IMAGES[2], step_text.get_attribute('href'))
		# self.assertEqual(URL_BASE + 'http://www.historypin.com/services/thumb/phid/%d/' % ID_COLLECTION_IMAGES[0], next_thumb.get_attribute('src'))
		
		# self.e('#slide-content a').click()
	
	@logged_in
	@url('/collections/add/id/%d/#%d' % (ID_COLLECTION, ID_COLLECTION))
	def test_edit_collection(self):
		self.assertTitle('Historypin | Collection')
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Create a collection', site_cnt.e('h1').text)
		
		progress_bar = site_cnt.e('.progress-bar')
		
		first = progress_bar.e('.first.current a')
		self.assertEqual('Describe the collection', first.text)
		
		self.assertIn('ss-icon'		, first.e('span').get_attribute('class'))
		self.assertIn('ss-fullmoon'	, first.e('span').get_attribute('class'))
		
		second = progress_bar.e('li:nth-of-type(2) a')
		self.assertEqual('Choose\ncontent', second.text)
		
		self.assertIn('ss-icon'		, second.e('span').get_attribute('class'))
		self.assertIn('ss-fullmoon'	, second.e('span').get_attribute('class'))
		
		third = progress_bar.e('li:nth-of-type(3) a')
		self.assertEqual('Order\ncontent', third.text)
		
		self.assertIn('ss-icon'		, third.e('span').get_attribute('class'))
		self.assertIn('ss-fullmoon'	, third.e('span').get_attribute('class'))
		
		paragraph = self.es('.text-hint p')
		self.assertEqual('You can describe your Collection here.', paragraph[0].text)
		self.assertEqual('You can add content to your Collection that you have pinned or you have favourited on the map', paragraph[1].text)
		
		step_cnt = site_cnt.es('#site-content .step-content .inn')[0]
		label = step_cnt.es('label')
		self.assertEqual('Title:'		, label[0].text)
		self.assertEqual('Description:'	, label[1].text)
		
		info = step_cnt.es('.input-info')
		self.assertEqual('Give your Collection a title that makes it unique.'						, info[0].text)
		self.assertEqual('Describe your Collection. This will appear on the Collection homepage.'	, info[1].text)
		
		sleep(5)  # AJAX
		title = self.e('#tour-title')
		title.clear()
		title.send_keys('Theaters in Bulgaria')
		
		desc = self.e('#tour-description')
		desc.clear()
		desc.send_keys('Collection for famous theaters in Bulgaria')
		
		self.assertEqual('Next step: Choose content', self.e('.next-button span').text)
		self.e('.next-button').click()
		
							
		self.assertEqual('You can describe your Collection here.', self.e('.text-hint p').text)
		
		step_cnt	= self.es('.step-content')[1]
		browse		= step_cnt.e('.browse-photos')
		tabs		= browse.e('.tabs-nav')
		
		sleep(2)
		filter_bar = self.e('.search-filter')
		# self.assertEqual('Search', filter_bar.e('label').text) TODO to fix this
		self.assertIsInstance(filter_bar.e('input'), WebElement)
		
		# self.assertIsInstance(filter_bar.e('#date-slider-labels'), WebElement) TODO to fix this
		
		item = step_cnt.e('.choose-photos.yours li')
		self.assertEqual(URL_BASE + '/services/thumb/phid/%d/dim/152x108/crop/1/' % ID_COLLECTION_IMAGES[3], item.e('img').get_attribute('src'))
		# to check icon for adding
		
		self.hover(item.e('img'))
		self.assertEqual('Bulgarian Army Theater'	, item.e('.photo-title').text)
		self.assertEqual('2 February 2013'				, item.e('.date').text)
		
		self.assertIsInstance(self.e('.step-sidebar li .image-container'), WebElement)
		
		remove_item = self.es('.step-sidebar .remove-photo')
		remove_item[0].click()
		remove_item[1].click()
		remove_item[2].click()
		
		icon = item.e('.add-photo span')
		self.assertIn('ss-icon', icon.get_attribute('class'))
		self.assertIn('ss-plus', icon.get_attribute('class'))
		item.e('.add-photo').click()
		
		tabs.e('li:nth-of-type(2) a').click()
		
		favs = step_cnt.es('.choose-photos.favourites li')
		url = URL_BASE + '/services/thumb/phid'
		self.assertEqual(url + '/%d/dim/152x108/crop/1/' % ID_COLLECTION_IMAGES[0]	, favs[0].e('img').get_attribute('src'))
		self.assertEqual(url + '/%d/dim/152x108/crop/1/' % ID_COLLECTION_IMAGES[2], favs[1].e('img').get_attribute('src'))
		self.assertEqual(url + '/%d/dim/152x108/crop/1/' % ID_COLLECTION_IMAGES[1], favs[2].e('img').get_attribute('src'))
		self.assertEqual(url + '/1501007/dim/152x108/crop/1/'	, favs[3].e('img').get_attribute('src'))
		
		self.hover(favs[0].e('img'))
		self.assertEqual('Morden College east elevation and chapel', favs[0].e('.photo-title').text)
		self.hover(favs[1].e('img'))
		self.assertEqual('National Theatre in Sofia, Bulgaria', favs[1].e('.photo-title').text)
		self.hover(favs[2].e('img'))
		self.assertEqual('Pinner High St from Church', favs[2].e('.photo-title').text)
		self.hover(favs[3])
		self.assertEqual('Ivan Vazov National Theatre', favs[3].e('.photo-title').text)
		
		favs[0].e('.add-photo').click()
		favs[1].e('.add-photo').click()
		favs[2].e('.add-photo').click()
		self.assertIsInstance(self.e('.step-sidebar .image-container'), WebElement)
		
		button = self.es('.inn .next-button')[1]
		button.click()
												
		tour_step = self.e('#tour-step3')
		sidebar = tour_step.e('.step-sidebar')
		self.assertEqual('Drag and drop the content to reorder them'				, sidebar.e('h2').text)
		self.assertEqual('This is the content you have chosen for your Collection.'	, sidebar.e('p').text)
		
		photo_number = tour_step.es('#sortable li .photo-number span')
		self.assertEqual('1', photo_number[0].text)
		self.assertEqual('2', photo_number[1].text)
		self.assertEqual('3', photo_number[2].text)
		
		actions = self.e('.actions .cancel span')
		self.assertIn('ss-icon'		, actions.get_attribute('class'))
		self.assertIn('ss-hyphen'	, actions.get_attribute('class'))
		
		publish = self.es('.next-button.done')[1]
		self.assertEqual('Publish', publish.e('span').text)
		publish.click()
		sleep(3)
									
		# TODO drag and drop for one item
		self.go('/collections/add/id/%d/#%d' % (ID_COLLECTION, ID_COLLECTION))
		sleep(3)
		title = self.e('#tour-title')
		self.assertEqual('Theaters in Bulgaria', title.get_attribute('value'))
		desc = self.e('#tour-description')
		self.assertEqual('Collection for famous theaters in Bulgaria', desc.get_attribute('value'))
		
		self.assertEqual('Next step: Choose content', self.e('.next-button span').text)
		self.e('.next-button').click()
		
		sleep(3)
		button = self.es('.inn .next-button')[1]
		button.click()
		
		items = self.es('#sortable > li')
		self.assertIsInstance(items[0], WebElement)
		self.assertIsInstance(items[1], WebElement)
		self.assertIsInstance(items[2], WebElement)
		self.assertIsInstance(items[3], WebElement)
		
		publish = self.es('.next-button.done')[1]
		self.assertEqual('Publish', publish.e('span').text)
		publish.click()
