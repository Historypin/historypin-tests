# -*- coding: utf-8 -*-

from base import *

class Tours(HPTestCase):
	
	def __test_collection_listing(self):
		self.assertTitle('Historypin | Tours')
		
		main_cnt = self.e('.inner.cf')
		self.assertEqual(URL_BASE + '/tours/'									, main_cnt.e('a.main-image').get_attribute('href'))
		self.assertEqual(URL_BASE + '/resources/images/tour-homepage-index.png'	, main_cnt.e('img').get_attribute('src'))
		self.assertEqual('What are Tours?'										, main_cnt.e('h1').text)
		self.assertEqual('Tours lead you step-by-step through a series of pieces of content, telling a story, exploring a place or walking through time. Take one of the Tours below or put your own together, using any content on Historypin.'
						, main_cnt.e('p').text)
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
	def test_view(self):
		self.assertTitle('Historypin | Tours - Test Tour for automated test')
		
		self.assertEqual(URL_BASE + '/services/thumb/phid/1031013/dim/451x302/crop/1/'	, self.e('img.index').get_attribute('src'))
		self.assertEqual(URL_BASE + '/tours/view/id/22354015/title/Test%2520Tour%2520for%2520automated%2520test/#', self.e('a.main-image').get_attribute('href'))
		self.assertEqual('Test Tour for automated test'									, self.e('.info h2').text)
		
		paragraphs = self.es('.info p')
		self.assertEqual('Description for Test Tour for automated test'					, paragraphs[0].text)
		self.assertEqual('Created by Gabss'												, paragraphs[1].text)
		self.assertEqual(URL_BASE + '/channels/view/10649049'							, paragraphs[1].e('a').get_attribute('href'))
		
		button = self.e('.tour-button')
		self.assertEqual('Take the Tour'																	, button.text)
		self.assertEqual(URL_BASE + '/tours/take/id/22354015/title/Test%20Tour%20for%20automated%20test/#1'	, button.get_attribute('href'))
		
		tabs = self.es('.list_tabs li')
		self.assertIsInstance(tabs[0]	, WebElement)
		self.assertEqual('Map View'		, tabs[0].e('span').text)
		self.assertIsInstance(tabs[1]	, WebElement)
		self.assertEqual('List View'	, tabs[1].e('span').text)
		self.assertIsInstance(tabs[2]	, WebElement)
		self.assertEqual('Tour View'	, tabs[2].e('span').text)
		
		photo_list_cnt = [
				['1', '1031013', 'Airplane crash on Wallace Road - 13 July 1952'],
				['2', '1076031', "'Hop Bine', Drove Road, Biggleswade 1914 - 1 January 1914"],
				['3', '2172029', 'Sabarabussu,MG,Brasil - 1898'],
				['4', '3255004', 'Diving Horse at Hanlan\'s Point - 1908'],
				['5', '22363018', 'National Theatre in Sofia, Bulgaria - 2 August 2012'],
		]
		
		photos_list	= self.e('#list_view .list')
		number		= photos_list.es('strong')
		links		= photos_list.es('.link-image')
		images		= photos_list.es('img')
		paragraphs	= photos_list.es('p:nth-of-type(1)')
		start		= photos_list.es('.start-here')
		start_link	= URL_BASE + '/tours/take/id/22354015/title/Test%20Tour%20for%20automated%20test/#'
		
		for n in range(len(photo_list_cnt)):
			i = photo_list_cnt[n]
			self.assertEqual(i[0]				, number[n].text)
			self.assertEqual(start_link + i[0]	, links[n].get_attribute('href'))
			self.assertEqual(start_link + i[0]	, start[n].get_attribute('href'))
			self.assertEqual(i[2]				, paragraphs[n].text)
			self.assertEqual('Start from here'	, start[n].text)
			
			self.assertEqual(URL_BASE + '/services/thumb/phid/' + i[1] + '/dim/195x150/crop/1/', images[n].get_attribute('src'))
			
		# TODO LATER
		# - representing photo
	
	@url('/tours/take/id/' + KEY_TOUR)
	def test_take(self):
		
		self.assertTitle('Historypin | Tours') # HTML - page title should be fixed to HistoryPin | Tour | Test Tour for automated test
		self.assertEqual('Test Tour for automated test', self.e('.title h3').text)
		
		paragraph = self.e('.title p')
		self.assertEqual('by Gabss'															, paragraph.text)
		self.assertEqual('http://v4-22-00.historypin-hrd.appspot.com/channels/view/10649049', paragraph.e('a').get_attribute('href')) # HTML - fix link to be relative
		
		link_exit = self.e('#exit-tour')
		self.assertEqual(URL_BASE + '/tours/view/id/22354015/title/Test%20Tour%20for%20automated%20test', link_exit.get_attribute('href'))
		self.assertEqual('Exit tour'																	, link_exit.text)
		self.assertIn('ss-door'																			, link_exit.e('span').get_attribute('class'))
		self.assertIn('right'																			, link_exit.e('span').get_attribute('class'))
		
		tour_items = [
			["Airplane crash on Wallace Road - 13 July 1952"				, '13 July 1952'	, '/map/#!/geo:51.362619,0.513102/zoom:20/dialog:1031013/tab:details/'			, '1031013', "Air Accidents: Plane crash in Wallace Road, Rochester, Kent on Sunday, when an Auster Aircraft narrowly missed the rooftops of houses, struck a garden fence and crashed in a small clearing by the side of a church."],
			["'Hop Bine', Drove Road, Biggleswade 1914 - 1 January 1914"	, '1 January 1914'	, '/map/#!/geo:52.087599,-0.25404/zoom:20/dialog:1076031/tab:details/'			, '1076031', "The 'Hop Bine' was built in 1870 ready for later development in the eastern side of Biggleswade. Its description in 1898 was -"],
			["Sabarabussu,MG,Brasil - 1898"									, '1898'			, '/map/#!/geo:-19.8891792,-43.8048137/zoom:20/dialog:2172029/tab:details/'		, '2172029', "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."],
			["Diving Horse at Hanlan's Point - 1908"						, '1908'			, '/map/#!/geo:43.622221047,-79.3740749359/zoom:20/dialog:3255004/tab:details/'	, '3255004', "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."],
			["National Theatre in Sofia, Bulgaria - 2 August 2012"			, '2 August 2012'	, '/map/#!/geo:42.693738,23.326101/zoom:20/dialog:22363018/tab:details/'		, '22363018', "This is a photo of National Theatre in Sofia, Bulgaria"],
		]
		
		next_button		= self.e('.next-button.right')
		prev_button		= self.e('.next-button.left')
		thumbs			= self.es('.step-slider li')
		marker_img		= self.es('.hp-marker-img')
		
		self.hover(thumbs[0])
		tooltip			= self.e('#tips')
		
		link_images		= URL_BASE + '/services/thumb/phid/'
		link_marker_img	= URL_BASE + '/services/thumb/phid/'
		
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
		self.assertEqual('Exit', self.e('.next-button.right span').text)
		
		for n in range(len(tour_items)):
			self.hover(thumbs[n])
			self.assertEqual(tour_items[n][0], tooltip.text)
			
			thumbs[n].click()
			check_step(tour_items[n])
			
		
		self.assertEqual('Exit', self.e('.next-button.right span').text)
		check_step(tour_items[-1])
		for n in range(len(tour_items)-1)[::-1]:
			prev_button.click()
			check_step(tour_items[n])
		
	