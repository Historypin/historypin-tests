# -*- coding: utf-8 -*-

from base import *

class Tours(HPTestCase):
	
	def __test_collection_listing(self):
		self.assertTitle('Historypin | Tours')
		
		main_cnt = self.e('.inner.cf')
		self.assertEqual(URL_BASE + '/tours/'									, main_cnt.e('a.main-image').get_attribute('href'))
		self.assertEqual(URL_BASE + '/resources/images/tour-homepage-index.png'	, main_cnt.e('img').get_attribute('src'))
		self.assertEqual('What are Tours?'										, main_cnt.e('h1').text)
		self.assertEqual('Tours lead you step-by-step through a series of pieces of content, telling a story, exploring a place or walking through time. Take one of the Tours below or put your own together, using any content on Historypin.', main_cnt.e('p').text)
		button = main_cnt.e('a.next-button')
		self.assertEqual(URL_BASE + '/tours/add'								, button.get_attribute('href'))
		self.assertEqual('Make your own tour'									, button.text)
		
		self.assertEqual('Return to Tours & Collections', self.e('h3.right').text)
		self.assertEqual(URL_BASE + '/curated'			, self.e('h3.right a').get_attribute('href'))
		self.assertEqual('All Tours'					, self.e('h3.right ~ h3').text)
		
		cnt = self.es('#photo_list_content .list li:nth-of-type(1)')
		self.assertIsInstance(cnt[0].e('a')	, WebElement)
		self.assertIsInstance(cnt[0].e('img')	, WebElement)
		self.assertIsInstance(cnt[0].e('p')	, WebElement)
		
		self.assertIn('tour-icon'	, cnt[0].e('a span').get_attribute('class'))
		self.assertIn('ss-hiker'	, cnt[0].e('a span').get_attribute('class'))
		self.assertIn('ss-icon'		, cnt[0].e('a span').get_attribute('class'))
		
	@url('/tours/')
	def test_index(self):
		self.__test_collection_listing()
	
	@url('/tours/all')
	def test_all(self):
		self.__test_collection_listing()
		
		next = self.e('.show-next')
		self.assertEqual('Next'							, next.text)
		self.assertEqual(URL_BASE + '/tours/all/page/2/', next.get_attribute('href'))
	
	@url('/tours/view/id/' + KEY_TOUR)
	@logged_in
	def test_view(self):
		self.assertTitle('Historypin | Tours - Beautiful buildings in Bulgaria')
		
		# self.assertEqual(URL_BASE + '/services/thumb/phid/26162010/dim/451x302/crop/1/'	, self.e('img.index').get_attribute('src'))
		self.assertEqual(URL_BASE + '/tours/view/id/16502051/title/Beautiful%2520buildings%2520in%2520Bulgaria/#', self.e('a.main-image').get_attribute('href'))
		self.assertEqual('Beautiful buildings in Bulgaria'									, self.e('.info h2').text)
		
		paragraphs = self.es('.info p')
		self.assertEqual('Tour about beautiful buildings in Bulgaria'					, paragraphs[0].text)
		self.assertEqual('Created by Gabriela Ananieva'												, paragraphs[1].text)
		self.assertEqual(URL_BASE + '/channels/view/11675544'							, paragraphs[1].e('a').get_attribute('href'))
		
		button = self.e('.tour-button')
		self.assertEqual('Take the Tour'																		, button.text)
		self.assertEqual(URL_BASE + '/tours/take/id/16502051/title/Beautiful%20buildings%20in%20Bulgaria/#1'	, button.get_attribute('href'))
		
		tabs = self.es('.list_tabs li')
		self.assertIsInstance(tabs[0]	, WebElement)
		self.assertEqual('Map View'		, tabs[0].e('span').text)
		self.assertIsInstance(tabs[1]	, WebElement)
		self.assertEqual('List View'	, tabs[1].e('span').text)
		self.assertIsInstance(tabs[2]	, WebElement)
		self.assertEqual('Tour View'	, tabs[2].e('span').text)
		
		photo_list_cnt = [
				['1', '26162010', 'Bulgarian Army Theater - 1 May 2013'],
				['2', '322003'	, "Morden College east elevation and chapel - 2010"],
				['3', '2090034'	, 'Pinner High St from Church - 1910 - 1920'],
				['4', '22363018', 'National Theatre in Sofia, Bulgaria - 2 August 2012'],
		]
		
		photos_list	= self.e('#list_view .list')
		number		= photos_list.es('strong')
		links		= photos_list.es('.link-image')
		images		= photos_list.es('img')
		paragraphs	= photos_list.es('p:nth-of-type(1)')
		start		= photos_list.es('.start-here')
		start_link	= URL_BASE + '/tours/take/id/16502051/title/Beautiful%20buildings%20in%20Bulgaria/#'
		
		for n in range(len(photo_list_cnt)):
			i = photo_list_cnt[n]
			self.assertEqual(i[0]				, number[n].text)
			self.assertEqual(start_link + i[0]	, links[n].get_attribute('href'))
			self.assertEqual(start_link + i[0]	, start[n].get_attribute('href'))
			self.assertEqual(i[2]				, paragraphs[n].text)
			self.assertEqual('Start from here'	, start[n].text)
			
			self.assertEqual(URL_BASE + '/services/thumb/phid/' + i[1] + '/dim/195x150/crop/1/', images[n].get_attribute('src'))
		
		representing_photo = photos_list.e('li:nth-of-type(4) .info-actions a')
		representing_photo.click()
		sleep(3)
		self.assertEqual(URL_BASE + '/services/thumb/phid/22363018/dim/451x302/crop/1/'	, self.e('img.index').get_attribute('src'))
	
	@url('/tours/take/id/' + KEY_TOUR)
	@logged_in
	def test_take(self):
		
		self.assertTitle('Historypin | Tours')  # HTML - page title should be fixed to HistoryPin | Tour | Test Tour for automated test
		self.assertEqual('Beautiful buildings in Bulgaria', self.e('.title h3').text)
		
		paragraph = self.e('.title p')
		self.assertEqual('by Gabriela Ananieva'															, paragraph.text)
		self.assertEqual('http://v4-22-00.historypin-hrd.appspot.com/channels/view/11675544', paragraph.e('a').get_attribute('href'))
		
		link_exit = self.e('#exit-tour')
		self.assertEqual(URL_BASE + '/tours/view/id/16502051/title/Beautiful%20buildings%20in%20Bulgaria'	, link_exit.get_attribute('href'))
		self.assertEqual('Exit tour'																		, link_exit.text)
		self.assertIn('ss-door'																				, link_exit.e('span').get_attribute('class'))
		self.assertIn('right'																				, link_exit.e('span').get_attribute('class'))
		
		tour_items = [
			["Bulgarian Army Theater - 1 May 2013"					, '2 February 2013'		, '/map/#!/geo:42.694696,23.329027/zoom:20/dialog:26162010/tab:details/'		, '26162010', "This is a photo of the famous Bulgarian Army Theater ."],
			["Morden College east elevation and chapel - 2010"		, '2010'				, '/map/#!/geo:51.4691539556,0.0169086456299/zoom:20/dialog:322003/tab:details/', '322003'	, ""],
			["Pinner High St from Church - 1910 - 1920"				, '1910 - 1920'			, '/map/#!/geo:51.594547,-0.379828/zoom:20/dialog:2090034/tab:details/'			, '2090034'	, ""],
			["National Theatre in Sofia, Bulgaria - 2 August 2012"	, '2 August 2012'		, '/map/#!/geo:42.693738,23.326101/zoom:20/dialog:22363018/tab:details/'		, '22363018', "This is a photo of National Theatre in Sofia, Bulgaria"],
		]
		
		next_button		= self.e('.next-button.right')
		prev_button		= self.e('.next-button.left')
		thumbs			= self.es('.step-slider li')
		marker_img		= self.es('.hp-marker-img')
		
		self.hover(thumbs[0])
		tooltip			= self.e('#tips')
		
		link_images		= URL_BASE + '/services/thumb/phid/'
		# link_marker_img	= URL_BASE + '/services/thumb/phid/'
		
		def check_step(data):
			image			= self.e_wait('.streetview-img')
			photo_info		= self.e('.photo-info')
			photo_title		= self.e('.tour-step-info h4')
			paragraph		= self.e('.tour-step-info p')
			
			self.assertEqual('Photo: ' + data[0] + ' ' + data[1]				, photo_info.text)
			self.assertEqual(URL_BASE + data[2]									, photo_info.e('a').get_attribute('href'))
			self.assertIn(link_images + data[3] + '/dim/'						, image.get_attribute('src'))
			self.assertEqual(data[0]											, photo_title.text)
			self.assertEqual(data[4]											, paragraph.text)
			# self.assertEqual(link_marker_img + i[5] + '/dim/52x39/crop/1/'	, marker_img[n].get_attribute('src'))
		
		for n in range(len(tour_items)-1):
			check_step(tour_items[n])
			next_button.click()
		check_step(tour_items[-1])
		self.assertEqual('Next', self.e('.next-button.right span').text)
		
		for n in range(len(tour_items)):
			self.hover(thumbs[n])
			self.assertEqual(tour_items[n][0], tooltip.text)
			
			thumbs[n].click()
			check_step(tour_items[n])
			
		
		self.assertEqual('Next', self.e('.next-button.right span').text)
		check_step(tour_items[-1])
		for n in range(len(tour_items)-1)[::-1]:
			prev_button.click()
			check_step(tour_items[n])
	
	@url('/tours/add/id/16502051/#16502051')
	@logged_in
	def test_edit_tour(self):
		site_cnt = self.e('#site-content')
		
		self.assertTitle('Historypin | Tour')
		sleep(2)
		self.assertEqual('Create a tour', self.e('.tour-head h1').text)
		
		progress_bar = self.e('.progress-bar')
		first = progress_bar.e('.progress-bar .first.current a')
		self.assertEqual('Describe the tour', first.text)
		
		self.assertIn('ss-icon'		, first.e('span').get_attribute('class'))
		self.assertIn('ss-fullmoon'	, first.e('span').get_attribute('class'))
		
		second = progress_bar.e('li:nth-of-type(2) a')
		self.assertEqual('Choose content', second.text)
		
		self.assertIn('ss-icon'		, second.e('span').get_attribute('class'))
		self.assertIn('ss-fullmoon'	, second.e('span').get_attribute('class'))
		
		third = progress_bar.e('li:nth-of-type(3) a')
		self.assertEqual('Order the steps', third.text)
		
		self.assertIn('ss-icon'		, third.e('span').get_attribute('class'))
		self.assertIn('ss-fullmoon'	, third.e('span').get_attribute('class'))
		
		paragraph = self.es('.text-hint p')
		self.assertEqual('You can describe your Tour here.', paragraph[0].text)
		self.assertEqual('You can add content to your Tour that you have pinned or you have favourited on the map', paragraph[1].text)
		
		step_cnt = site_cnt.es('#site-content .step-content .inn')[0]
		label = step_cnt.es('label')
		self.assertEqual('Title:'		, label[0].text)
		self.assertEqual('Description:'	, label[1].text)
		
		info = step_cnt.es('.input-info')
		self.assertEqual('Give your tour a title. It will appear across all steps in the tour.'	, info[0].text)
		self.assertEqual('Describe your tour. This will appear on the introduction page.'		, info[1].text)
		
		sleep(3)  # AJAX
		title = self.e('#tour-title')
		title.clear()
		title.send_keys('Beautiful buildings in Bulgaria')
		
		desc = self.e('#tour-description')
		desc.clear()
		desc.send_keys('Tour about beautiful buildings in Bulgaria')
		
		self.assertEqual('Choose content', self.e('.next-button span').text)
		self.e('.next-button').click()
							
		
		step_cnt	= self.es('.step-content')[1]
		browse		= step_cnt.e('.browse-photos')
		tabs		= browse.e('.tabs-nav')
		
		sleep(2)
		filter_bar = self.e('.filter-bar')
		self.assertIsInstance(filter_bar.e('input'), WebElement)
		
		self.assertIsInstance(filter_bar.e('#date-slider-labels'), WebElement)
		
		sleep(3)
		item = step_cnt.e('.choose-photos.yours li')
		self.assertEqual(URL_BASE + '/services/thumb/phid/26162010/dim/152x108/crop/1/', item.e('img').get_attribute('src'))
		
		sleep(3)
		self.hover(item.e('img'))
		self.assertEqual('Bulgarian Army Theater'	, item.e('.photo-title').text)
		self.assertEqual('2 February 2013'				, item.e('.date').text)
		
		self.assertIsInstance(self.e('.step-sidebar .image-container'), WebElement)
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
		self.assertEqual(url + '/322003/dim/152x108/crop/1/'	, favs[0].e('img').get_attribute('src'))
		self.assertEqual(url + '/22363018/dim/152x108/crop/1/'	, favs[1].e('img').get_attribute('src'))
		self.assertEqual(url + '/2090034/dim/152x108/crop/1/'	, favs[2].e('img').get_attribute('src'))
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
								
		step_cnt	= self.es('.step-content')[2]
		self.assertEqual('Drag and drop the content to reorder them.', step_cnt.e('p').text)
		
		item_first = step_cnt.e('#sortable > li:nth-of-type(1)')
		self.assertEqual(URL_BASE + '/services/thumb/phid/26162010/dim/152x108/crop/1/', item_first.e('a img').get_attribute('src'))
		self.assertIsInstance(item_first.e('.photo-number')	, WebElement)
		self.assertIsInstance(item_first.e('.actions')		, WebElement)
		
		item_second = step_cnt.e('#sortable > li:nth-of-type(2)')
		self.assertEqual(URL_BASE + '/services/thumb/phid/322003/dim/152x108/crop/1/', item_second.e('a img').get_attribute('src'))
		self.assertIsInstance(item_second.e('.photo-number')	, WebElement)
		self.assertIsInstance(item_second.e('.actions')		, WebElement)
		
		item_third = step_cnt.e('#sortable > li:nth-of-type(3)')
		self.assertEqual(URL_BASE + '/services/thumb/phid/2090034/dim/152x108/crop/1/', item_third.e('a img').get_attribute('src'))
		self.assertIsInstance(item_third.e('.photo-number')	, WebElement)
		self.assertIsInstance(item_third.e('.actions')		, WebElement)
		
		
		step = self.e('.step-maker.inn')
		self.assertEqual('Describe Step:', step.e('h4').text)
		
		image_cnt = step.e('.image-container')
		self.assertEqual(URL_BASE + '/services/thumb/phid/26162010/dim/152x108/crop/1/', image_cnt.e('img').get_attribute('src'))
		self.assertIsInstance(image_cnt.e('.step-number'), WebElement)
		self.assertEqual('1', image_cnt.e('.step-number').text)
		
		step_title = step.e('li:nth-of-type(2)')
		self.assertEqual('Step Title:'							, step_title.e('label').text)
		self.assertEqual('Bulgarian Army Theater - 1 May 2013'	, step_title.e('input').get_attribute('value'))
		
		step_desc = step.e('li:nth-of-type(3)')
		self.assertEqual('Step Description:'										, step_desc.e('label').text)
		self.assertEqual('This is a photo of the famous Bulgarian Army Theater .'	, step_desc.e('textarea').get_attribute('value'))
		
		self.assertFalse(step.e('.show-prev.s3-prev').is_displayed())
		
		next = step.e('.show-next.s3-next')
		self.assertTrue(step.e('.show-next.s3-next').is_displayed())
		self.assertIn('ss-icon'	, next.e('span').get_attribute('class'))
		self.assertIn('ss-right', next.e('span').get_attribute('class'))
		next.click()
			
		step = self.e('.step-maker.inn')
		self.assertEqual('Describe Step:', step.e('h4').text)
		
		image_cnt = step.e('.image-container')
		self.assertEqual(URL_BASE + '/services/thumb/phid/322003/dim/152x108/crop/1/', image_cnt.e('img').get_attribute('src'))
		self.assertIsInstance(image_cnt.e('.step-number'), WebElement)
		self.assertEqual('2', image_cnt.e('.step-number').text)
		
		step_title = step.e('li:nth-of-type(2)')
		self.assertEqual('Step Title:'							, step_title.e('label').text)
		self.assertEqual('Morden College east elevation and chapel - 2010'	, step_title.e('input').get_attribute('value'))
		
		step_desc = step.e('li:nth-of-type(3)')
		self.assertEqual('Step Description:'										, step_desc.e('label').text)
		self.assertEqual(''	, step_desc.e('textarea').get_attribute('value'))
		
		prev = step.e('.show-prev.s3-prev')
		self.assertTrue(prev.is_displayed())
		prev.click()
		next.click()
		
		next = step.e('.show-next.s3-next')
		self.assertTrue(next.is_displayed())
		self.assertIn('ss-icon'	, next.e('span').get_attribute('class'))
		self.assertIn('ss-right', next.e('span').get_attribute('class'))
		next.click()
				
		step = self.e('.step-maker.inn')
		self.assertEqual('Describe Step:', step.e('h4').text)
		
		image_cnt = step.e('.image-container')
		self.assertEqual(URL_BASE + '/services/thumb/phid/2090034/dim/152x108/crop/1/', image_cnt.e('img').get_attribute('src'))
		self.assertIsInstance(image_cnt.e('.step-number'), WebElement)
		self.assertEqual('3', image_cnt.e('.step-number').text)
		
		step_title = step.e('li:nth-of-type(2)')
		self.assertEqual('Step Title:'							, step_title.e('label').text)
		self.assertEqual('Pinner High St from Church - 1910 - 1920'	, step_title.e('input').get_attribute('value'))
		
		step_desc = step.e('li:nth-of-type(3)')
		self.assertEqual('Step Description:'										, step_desc.e('label').text)
		self.assertEqual(''	, step_desc.e('textarea').get_attribute('value'))
		
		prev = step.e('.show-prev.s3-prev')
		self.assertTrue(prev.is_displayed())
		
		publish = step_cnt.e('.next-button.done:nth-of-type(2)')
		self.assertEqual('Publish', publish.e('span').text)
		publish.click()
		sleep(2)
		
		self.go('/tours/add/id/16502051/#16502051')
		sleep(3)
		title = self.e('#tour-title')
		self.assertEqual('Beautiful buildings in Bulgaria', title.get_attribute('value'))
		desc = self.e('#tour-description')
		self.assertEqual('Tour about beautiful buildings in Bulgaria', desc.get_attribute('value'))
		
		self.assertEqual('Choose content', self.e('.next-button span').text)
		self.e('.next-button').click()
		
		sidebar = self.e('#tour-step3 .step-sidebar ul')
		self.assertIsInstance(sidebar, WebElement)
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
