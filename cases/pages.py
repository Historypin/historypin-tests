# -*- coding: utf-8 -*-

from base import *

class Pages(HPTestCase):
	
	@url('/about-us/')
	def test_about(self):
		self.assertTitle('Historypin | A 90 second introduction')
		self.assertEqual(self.e('h1.title').text, 'A 90 second introduction')
		self.assertEqual(self.e('iframe').get_attribute('src'), 'http://www.youtube.com/embed/FdT3eKdto4w?rel=0')
	
	@url('/app/')
	def test_app(self):
		self.assertTitle('Historypin | App')
		self.assertEqual(self.e('h2').text, 'What can you do on the Historypin app?')
		# LATER text after the title 
		
		# Android
		sel = '.appstores .col:nth-child(1) '
		self.assertEqual(self.e(sel + 'img').get_attribute('src'), URL_BASE + '/resources/images/content/app/app_android.png')
		self.assertEqual(self.e(sel + 'h1').text, 'Android')
		self.assertEqual(self.e(sel + 'a').get_attribute('href'), 'https://market.android.com/details?id=com.historypin.Historypin&feature=search_result')
		self.assertEqual(self.e(sel + 'a').text, 'Google Play Store')

		# iPhone
		sel = '.appstores .col:nth-child(2) '
		self.assertEqual(self.e(sel + 'img').get_attribute('src'), URL_BASE + '/resources/images/content/app/app_iphone.png')
		self.assertEqual(self.e(sel + 'h1').text, 'iOS')
		self.assertEqual(self.e(sel + 'a').text, 'iOS App Store')
		self.assertEqual(self.e(sel + 'a').get_attribute('href'), 'http://itunes.apple.com/app/historypin/id455228207?mt=8')
		
		# Windows Phone 7
		sel = '.appstores .col:nth-child(3) '
		self.assertEqual(self.e(sel + 'img').get_attribute('src'), URL_BASE + '/resources/images/content/app/app_wp7.png')
		self.assertEqual(self.e(sel + 'h1').text, 'Windows Phone 7')
		self.assertEqual(self.e(sel + 'a').get_attribute('href'), 'http://www.windowsphone.com/en-US/apps/05638072-742e-460c-ab97-18d2b47ef06b')
		self.assertEqual(self.e(sel + 'a').text, 'Windows Phone Marketplace')

	
	@url('/contact/')
	def test_contact(self):
		self.assertTitle('Historypin | Contact')
		self.assertEqual(self.e('.section h1.title').text, 'Contact')

		self.assertEqual(self.e('.section h2:nth-child(2)').text, 'General enquiries, technical enquiries, content enquiries')
		self.assertEqual(self.e('.section p:nth-child(3) a').get_attribute('href'), 'mailto:historypin@wearewhatwedo.org')
		self.assertEqual(self.e('.section p:nth-child(3)').text, 'historypin@wearewhatwedo.org\n+44 (0)20 7148 7666\n71 St John Street\nLondon\nEC1M 4NJ\nUnited Kingdom')

		self.assertEqual(self.e('.section h2:nth-child(4)').text, 'Media')
		self.assertEqual(self.e('.section p:nth-child(5) a').get_attribute('href'), 'mailto:rebekkah.abraham@wearewhatwedo.org')
		self.assertEqual(self.e('.section p:nth-child(5)').text, 'Rebekkah Abraham\nrebekkah.abraham@wearewhatwedo.org\n+44 (0)20 7148 7670')

		self.assertEqual(self.e('.section h2:nth-child(6)').text, 'Schools, local projects and volunteers')
		self.assertEqual(self.e('.section p:nth-child(7) a').get_attribute('href'), 'mailto:rebekkah.abraham@wearewhatwedo.org')
		self.assertEqual(self.e('.section p:nth-child(7)').text, 'Rebekkah Abraham\nrebekkah.abraham@wearewhatwedo.org\n+44 (0)20 7148 7670')

		self.assertEqual(self.e('.section h2:nth-child(8)').text, 'Library, archive and museum partnerships')
		self.assertEqual(self.e('.section p:nth-child(9) a').get_attribute('href'), 'mailto:rebekkah.abraham@wearewhatwedo.org')
		self.assertEqual(self.e('.section p:nth-child(9)').text, 'Rebekkah Abraham\nrebekkah.abraham@wearewhatwedo.org\n+44 (0)20 7148 7670')

		self.assertEqual(self.e('.section h2:nth-child(10)').text, 'Web')
		self.assertEqual(self.e('.section p:nth-child(11) a').get_attribute('href'), 'mailto:mark.frost@wearewhatwedo.org')
		self.assertEqual(self.e('.section p:nth-child(11)').text, 'Mark Frost\nmark.frost@wearewhatwedo.org\n+44 (0)20 7148 7675')

		self.assertEqual(self.e('.section h2:nth-child(12)').text, 'Corporate Partnerships')
		self.assertEqual(self.e('.section p:nth-child(13) a').get_attribute('href'), 'mailto:nick.stanhope@wearewhatwedo.org')
		self.assertEqual(self.e('.section p:nth-child(13)').text, 'Nick Stanhope\nnick.stanhope@wearewhatwedo.org\n+44 (0)20 7148 7667')
	
	@url('/faq/')
	def test_faq(self):
		# TODO LATER
		faq = [
			{
				'heading': 'General',
				'items': [
					['title1', 'What is Historypin?'],
					['title2', 'Why was Historypin created?'],
					['title3', 'What are Historypin\'s long-term aims?'],
					['title4', 'Who is behind Historypin?'],
					['title5', 'What has happened during the beta-phase of Historypin?'],
				],
			},
			{
				'heading': 'Using the site',
				'items': [
					['title6', 'What kind of content can I add to Historypin?'],
					['title7', 'How do I pin photographic images?'],
					['title8', 'How do I pin video content?'],
					['title9', 'How do I pin audio content?'],
					['title10', 'How do I add stories and recollections?'],
					['title116', 'How do I edit a piece of content that I have pinned?'],
					['title117', 'How do I delete a piece of content that I have pinned?'],
					['title11', 'Why can\'t I pin stories to the map on their own?'],
					['title12', 'What about other types of materials, like letters, diaries or records?'],
					['title13', 'How can I pin very large amounts of content?'],
					['title14', 'If there is content already there, can I pin more on that spot?'],
					['title15', 'Can content still be pinned if I don\'t know the date?'],
					['title16', 'Can I link content I\'ve pinned to more info on my website or blog?'],
					['title17', 'How do I find the content I\'ve uploaded when I come back to the site?'],
					['title18', 'Why does your time filter only go back to 1840?'],
					['title19', 'What is Street View and why doesn\'t it exist all over the world?'],
					['title20', 'What are Tours?'],
					['title21', 'What are Collections?'],
					['title22', 'I\'ve found content that is inaccurately pinned, what should I do?'],
					['title23', 'I\'ve found inappropriate content, what should I do?'],
					['title24', 'I\'ve found content that infringes my copyright, what should I do?'],
					['title25', 'How are you moderating what goes on the site?'],
					['title112', 'Historypin is not functioning or displaying as I would expect, what should I do?'],
					['title113', 'I am having trouble uploading photos, what should I do?'],
					['title114', 'How do I change my Username?'],
				],
			},
			{
				'heading': 'Bulk Uploader',
				'items': [
					['title99', 'How can I find out more about doing a bulk upload?'],
					['title100', 'Do I have to pay to use the bulk uploader?'],
					['title101', 'Is there a limited number of bulk uploads that I can do?'],
					['title102', 'Is there a limit to how many images I can upload in a single bulk upload?'],
					['title103', 'Can I edit my data once I have completed a bulk upload?'],
					['title104', 'Can I make multiple edits to my content?'],
					['title105', 'Can I make global changes to the data attached to my photos?'],
					['title106', 'Can I delete a bulk upload?'],
					['title107', 'Do I need to complete all the fields for my bulk upload to work?'],
					['title108', 'Why haven\'t the fields on my bulk upload populated with meta-data?'],
					['title109', 'Why am I getting \'Bad Request\'?'],
					['title110', 'Why am I getting \'Internal server error\'?'],
					['title111', 'I used the Bulk Uploader, but the content on my Channel is \'unpinned\''],
				],
			},
			{
				'heading': 'Getting involved',
				'items': [
					['title27', 'How can I get more involved personally?'],
					['title28', 'Can I volunteer with Historypin?'],
					['title29', 'How can I get my local school more involved?'],
					['title31', 'How can I use Historypin in my local area?'],
					['title32', 'Do you give talks or run events?'],
					['title33', 'Do you offer any training?'],
				],
			},
			{
				'heading': 'Partners',
				'items': [
					['title34', 'Who are Historypin\'s existing partners?'],
					['title35', 'What does your partnership with Google involve?'],
					['title36', 'How can library, archive or museums get involved?'],
					['title37', 'How can schools get involved?'],
					['title38', 'How can universities and academic institutions get involved?'],
					['title39', 'How can community organisations, historical associations or photography societies get more involved?'],
					['title40', 'I\'d like to talk about partnering with Historypin, who can I contact?'],
				],
			},
			{
				'heading': 'Data',
				'items': [
					['title41', 'Where is the content stored?'],
					['title42', 'Is there any limit to the amount of content that can go on the site?'],
					['title43', 'How can I help improve data on Historypin?'],
					['title44', 'Is data shared with other parties?'],
				],
			},
			{
				'heading': 'Integration with other platforms',
				'items': [
					['title45', 'Can I embed Historypin tools on my site?'],
					['title46', 'Does Historypin have an API?'],
					['title47', 'Can I get statistics on my content?'],
				],
			},
			{
				'heading': 'Copyright and use of content',
				'items': [
					['title49', 'How will the content be protected?'],
					['title50', 'How will my content be credited on the site?'],
					['title51', 'What can other users do with my content?'],
					['title52', 'What can Historypin do with my content?'],
				],
			},
			{
				'heading': 'Privacy',
				'items': [
					['title53', 'Do you share my user information with anyone?'],
				],
			},
			{
				'heading': 'App',
				'items': [
					['title54', 'What can the Historypin app do?'],
					['title55', 'How do I get the Historypin app?'],
					['title115', 'Why does the Historypin app require my Google Account details?'],
				],
			},
			{
				'heading': 'Funding',
				'items': [
					['title56', 'How is Historypin funded?'],
					['title57', 'What happens to the profits from Historypin?'],
					['title58', 'How can I donate to Historypin?'],
				],
			},
			{
				'heading': 'Future Plans',
				'items': [
					['title59', 'What\'s next for Historypin?'],
					['title60', 'What\'s next for We Are What We Do?'],
				],
			},
			{
				'heading': 'Contact',
				'items': [
					['title61','I\'m a journalist and want to write a fabulously complimentary article about you. What do I do?'],
					['title62','I\'ve got another question, what should I do?'],
				],
			},
		]
		
		toc				= self.es('.toc > li')
		cnt				= self.es('.faq-group')
		questions		= self.es('.toc li strong')
		questions_h		= self.es('.faq-group h2')
		
		for n in range(len(faq)):
			i = faq[n]
			
			self.assertEqual(questions[n].text, i['heading'])
			self.assertEqual(questions_h[n].text, i['heading'])
			
			answers		= toc[n].es('li a')
			answers_h	= cnt[n].es('h3')
			
			for k in range(len(i['items'])):
				j = i['items'][k]
				
				self.assertEqual(answers[k].get_attribute('href'), URL_BASE + '/faq/#' + j[0])
				self.assertEqual(answers[k].text, j[1])
				
				self.assertEqual(answers_h[k].get_attribute('id'), j[0])
				self.assertEqual(answers_h[k].text, j[1])
	
	@url('/presscentre/')
	def test_press_center(self):
		self.assertTitle('Historypin | Press Centre')
		self.assertEqual(self.e('h1.title').text, 'Press Centre')
		self.assertEqual(self.e('.section h2:nth-of-type(1)').text, 'Some of our favourite coverage')
		self.assertEqual(self.e('.section h2:nth-of-type(2)').text, 'Coverage to date')
		
		links = [
			# link, link text, additional text
			['http://wearewhatwedo.org/press-cuttings/bringing-social-capital-back-to-life/', 'Bringing social capital back to life', 'The Times, 31st March 2012'],
			['http://googleblog.blogspot.com/2012/03/google-and-historypin-launch-online.html', u'Google and Historypin launch online gallery to celebrate The Queen\u2019s Diamond Jubilee', 'Google Blog, 12th March 2012'],
			['http://www.getreading.co.uk/community/s/2100048_mapping_readings_past_with_historypin', 'Mapping Reading\'s past with Historypin', 'Get Reading, 21st September 2012'],
			['http://lens.blogs.nytimes.com/2011/07/22/using-new-tools-mapping-old-brooklyn/', '"Using New Tools, Mapping Old Brooklyn"', 'New York Times Lens, 22nd July 2011'],
			['http://www.good.is/post/historypin-app-uses-augmented-reality-to-visualize-the-past/', '"Picture the Past: Historypin Mashes Up Archived Photos with the Present"', 'Good, 15th July 2011'],
			['http://www.ny1.com/content/ny1_living/technology/142855/new-android-app-brings-history-to-city-streets', '"New Android App Brings History To City Streets"', 'NY1, 14th July 2011'],
			['http://mashable.com/2011/07/12/historypin-collective-memory/', 'Historypin Launches, Shows Your World As It Was"', 'Mashable, 13th July 2011'],
			['http://techland.time.com/2011/07/11/old-meets-new-historypin-is-a-time-capsule-for-vintage-photos/', '"Old Meets New: \'Historypin\' Is a Map-Based Time Capsule for Vintage Photos"', 'Time Techland, 11th July 2011'],
			['http://www.guardian.co.uk/artanddesign/2010/jul/04/historypin-photography-sam-leith', '"With Historypin, photography has entered the fourth dimension, and I\'m going with it"', 'The Guardian, 4th July 2010'],
			['http://wearewhatwedo.org/press-cuttings/national-portrait-gallery-share-pics-of-queen/', 'National Portrait Gallery share pics of Queen', 'The Sun, 11th March 2012'],
			['http://www.northumberlandtoday.com/ArticleDisplay.aspx?e=3464879', u'Archives ‘pinning\u2019 local history', 'Northumberland Today, March 2012'],
			['http://www.huffingtonpost.com/2012/02/22/muni-celebrates-its-past-while-service-cuts-loom_n_1294386.html', 'Muni Celebrates Its Past, But Sees Service Cuts In Its Future', 'Huffington Post, 22nd February 2012'],
			['http://www.guardian.co.uk/theobserver/2012/feb/18/50-new-radicals-schemes-thinkers?newsfeed=true', 'Britain\'s 50 New Radicals', 'The Guardian, 18th February 2012'],
			[URL_BASE + '/presscentre/The%20Guardian,%2018th%20February%202012', 'The Sunday Times App List', 'The Sunday Times, 22nd January 2012'],
			['http://www.theglobeandmail.com/news/technology/digital-culture/social-networking/app-connects-historic-photos-to-modern-points-on-the-map/article2291181/', 'App connects historic photos to modern points on the map', 'The Globe and Mail, 4th January 2012'],
			['http://www.getreading.co.uk/sport/football/readingfc/s/2105567_1966_and_the_reading_fc_kit_that_took_the_biscuit', '1966 and the Reading FC kit that took the biscuit', 'Get Reading, 23rd December 2012'],
			['http://blogs.archives.gov/online-public-access/?p=6768', 'Put a Pin in It! National Archives Joins Historypin', 'NARAtions: The Blog of the US National Archives, November 30th 2011'],
			['http://www.birminghammail.net/news/top-stories/2011/11/08/historypin-site-unlocks-the-secrets-of-birmingham-s-past-97319-29736748/?utm_source=dlvr.it&utm_medium=twitter', 'Historypin site unlocks the secrets of Birmingham\'s past', 'Birmingham Mail, 8th November 2011'],
			['http://www.dailymail.co.uk/news/article-2058223/Website-Historypin-shows-streets-looked-170-years-ago.html', u'It\u2019s a Google Streetmap of history: How our famous landmarks looked up to 170 years ago', 'Daily Mail, 7th November 2011'],
			['http://wearewhatwedo.org/press-cuttings/a-history-in-pin-ups-3/', 'A history in pin-ups', u'Reader\u2019s Digest, Asia, November 2011'],
			[URL_BASE + '/presscentre/Reader%E2%80%99s%20Digest,%20Asia,%20November%202011', 'Post Your Pictures, Then Take A Walk Through History', 'NPR, 23rd October 2011'],
			['http://blogs.abc.net.au/victoria/2011/10/sunday-16-october-.html?site=melbourne&program=melbourne_sundays', 'Interview with Nick Stanhope by Alan Brough', '774 ABC Melbourne (Radio), 16th October 2011'],
			['http://wearewhatwedo.org/press-cuttings/app-of-the-week-historypin/', 'App of the Week', 'Sunday Times, 2nd October 2011'],
			['http://www.reuters.com/article/2011/09/12/us-app-historypin-idUSTRE78B1MW20110912?feedType=RSS&feedName=internetNews', 'Historypin app lets people create a "time machine"', 'Reuters, 12th September 2011'],
			['http://www.getreading.co.uk/community/s/2098887_reading_pins_down_new_online_history', 'Reading pins down new online history', 'Get Reading, 31st August 2011'],
			['http://journalstar.com/mobile/article_b8444738-528a-5a1f-9528-4cec8e780ca7.html', 'Time travelers: Websites of vintage photos capture moments in moments', 'Washington Post, 19th August 2011'],
			['http://articles.boston.com/2011-08-11/yourtown/29877326_1_google-maps-photos-google-street-view', '"Historic New England puts period photos on the map"', 'Boston Globe Downtown, 11th August 2011'],
			['http://www.ssireview.org/opinion/entry/a_new_tool_for_digital_storytelling/', '"A New Tool for Digital Storytelling"', 'Stanford Social Innovation Review, 11th August 2011'],
			['http://www.ilfattoquotidiano.it/2011/08/06/historypin-scopri-la-macchina-del-tempo-digitale/150236/?utm_source=twitterfeed&utm_medium=twitter', '"Historypin, la macchina del tempo digitale"', 'Il Fatto Quotidiano, 8th August 2011'],
			['http://www.dailybrink.com/?p=1932', 'Interview with Nick Stanhope, Historypin, CEO', 'Daily Brink, 26th July 2011'],
			['http://www.tcdailyplanet.net/blog/jeff-skrenes/historypin-puts-neighborhood-history-palm-your-hand', '"Historypin puts neighborhood history in the palm of your hand"', 'Twin Cities Daily Planet, 24th July 2011'],
			['http://www.vector1media.com/spatialsustain/historypin-puts-historical-photos-on-the-map.html', '"Historypin puts historical photos on the map"', 'Spatial Sustain, 24th July 2011'],
			['http://www.beenaproject.com/?p=1579', '"Historypin, A Project Mapping the Past and Future"', 'Beena Project, 17th July 2011'],
			['http://www.komando.com/coolsites/index.aspx?id=11071', '"Map your History"', 'The Kim Komando Show, 17th July 2011'],
			['http://www.washingtonpost.com/blogs/the-buzz/post/local-history-buffs-have-a-new-toy/2011/07/13/gIQAbSUnCI_blog.htm', '"Local history buffs have a new toy"', 'Washington Post, 13th July 2011'],
			['http://www.youtube.com/watch?v=RuxZp22kDu4', '"C5N - Tecnologia - History, pin viaje al pasad"', 'Canal 5 Noticias (C5N), 13th July 2011'],
			['http://habrahabr.ru/blogs/services/124038/', u'"Сервис Historypin откроет окно в прошлое"', u'Хабрахабр, 13th July 2011'],
			['http://ht.ly/5Fsov', '"Blending Old and New Tech to Make History Come to Life"', 'The Chronicle of Philanthopy, 12th July 2011'],
			['http://www.slate.com/blogs/browbeat/2011/07/12/historypin_a_hot_web_time_machine.html', '"Historypin: A Hot Web Time Machine"', 'Slate, 12th July 2011'],
			['http://news.yahoo.com/historypin-launches-shows-world-163201183.html', '"Historypin Launches, Shows Your World As It Was"', 'Yahoo! News, 12th July 2011'],
			['http://dodgeburn.blogspot.com/2011/07/global-launch-of-historypin-powered-by.html', '"Global Launch of Historypin, Powered by Google"', 'Dodge and Burn, 11th July 2011'],
			['http://digitallife.today.com/_news/2011/07/11/7059904-oh-snap-old-photos-hit-google-mapsl', '"Oh snap: Old photos hit Google Maps"', 'MSNBC, 11th July 2011'],
			['http://thenextweb.com/apps/2011/07/11/history-in-your-pocket-with-historypins-new-android-app/', u'"History in your pocket with Historypin\u2019s new Android app"', 'The Next Web, 11th July 2011'],
			['http://googlemapsmania.blogspot.com/2011/07/historypin-goes-global.html', '"Historypin Goes Global"', 'Google Maps Mania, 11th July 2011'],
			['http://www.nytimes.com/2011/07/08/arts/design/2-continents-1-work-and-31-hand-positions.html?_r=3', '"Somewhere in Brooklyn"', 'The New York Times, 7th July 2011'],
			['http://www.billericayessex.co.uk/news/72-billericay-school-pupils-help-to-pin-down-history', 'Billericay School Pupils Help to Pin Down History"', 'Billericay Essex, June 2011'],
			['http://peterpappas.blogs.com/copy_paste/2011/01/historypin-make-dbqs-digital-time-machine-layers-image-story-location.html', '"Make Document Based Questions with a Digital Time machine"', 'Copy/Paste, 2nd January 2011'],
			['http://brockleycentral.blogspot.com/2010/11/yesterday-is-history-tomorrow-is.html', '"Yesterday is history, tomorrow is a mystery"', 'Brockley Central, 29th November 2010'],
			['http://www.thesun.co.uk/sol/homepage/features/3221643/War-Collections-photographs-show-glimpse-into-Britains-war-past.html', '"We will remember then"', 'The Sun, 11th November 2010'],
			['http://www.expatica.com/nl/leisure/arts_culture/A-photographic-stroll-through-history_16531.html', '"A photographic stroll through history"', 'Radio Netherlands, 17th October 2010'],
			['http://www.thesun.co.uk/sol/homepage/news/3134341/New-York-rises-in-new-911-pics.html', '"New York Rises in New Pics"', 'The Sun, 11th September 2010'],
			['http://www.npr.org/blogs/pictureshow/2010/08/05/129007283/historypin?ft=1&f=1047', '"A Worldwide Photo Project Needs You (And Your Grandparents)"', 'The Picture Show Blog, NPR, August 5th 2010'],
			['http://www.iol.co.za/scitech/news/net-album-sorts-old-photos-1.911557', '"Net album sorts old photos"', 'IOL Scitech, 23rd July 2010'],
			['http://www.thesun.co.uk/sol/homepage/features/3063808/Photos-show-sporting-triumph-pics-pinned-on-recent-snaps.html', '"If you\'re looking for double ... you came to the right place"', 'The Sun, 22nd July 2010'],
			['http://wawwd-resources.s3.amazonaws.com/southwalesecho.png', '"History Bridges generation gap"', 'South Wales Echo, 20th July 2010'],
			['http://wawwd-resources.s3.amazonaws.com/sundaytimes180710.jpg', '"Our Ghosts in the Machine"', 'Sunday Times, 18th July 2010'],
			['http://www.telegraph.co.uk/technology/google/7854922/Historypin-turns-Google-Street-View-into-a-window-on-the-past.html', '"Historypin turns Google Street View into a window on the past"', 'The Telegraph, 26th June 2010'],
			['http://www.geenstijl.nl/mt/archieven/2010/06/nostalgie_fotos_van_vroeger_in.html', '"Nostalgie! Foto\'s van vroeger in Streetview"', 'Geenstijl, 9th June 2010'],
			['http://www.historytoday.com/blog/news-blog/charlotte-crow/historypin-patchwork-history', '"Historypin: Patchwork History"', 'History Today, 7th June 2010'],
			['http://crave.cnet.co.uk/software/historypin-puts-the-past-on-the-map-with-google-street-view-49305845/', '"Historypin puts the past on the map with Google Street View"', 'Cnet, 4th June 2010'],
			['http://googlemapsmania.blogspot.com/2010/06/largest-archive-of-photos-on-google.html#links', '"Largest Archive of Photos on Google Maps"', 'Google Maps Mania, 3rd June 2010'],
			['http://www.dailymail.co.uk/sciencetech/article-1283635/HistoryPin-website-lets-pin-historic-photos-Google-Streetview.html', '"A snapshot through time: The website that lets you \'pin\' historic photos onto Street View"', 'The Daily Mail, 3rd June 2010'],
			['http://rivertonhistory.com/2011/01/whoa-this-is-heavy-2/', '"Whoa, this is heavy!"', 'Historical Society of Riverton, 30th January 2010'],
			['http://wearewhatwedo.org/press-cuttings/give-us-your-jubilee-memories-says-google/', 'Give us your jubilee memories, says Google', 'The Telegraph, 12th March 2012'],
		]
		
		paragraphs = self.es('#site-content .right p')
		for n in range(len(links)):
			i = links[n]
			self.assertEqual(paragraphs[n].text, i[1] + '\n' + i[2])
			self.assertEqual(paragraphs[n].e('a').get_attribute('href'), i[0])
		
		
		sel = '.sidebar .inner:nth-child(1) '
		self.assertEqual(self.e(sel + 'h3').text, 'Contact Details')
		self.assertEqual(self.e(sel + 'p:nth-child(2)').text, 'UK & Global\nRebekkah Abraham\nrebekkah.abraham@wearewhatwedo.org\n+44 (0)20 7148 7666')
		self.assertEqual(self.e(sel + 'p:nth-child(2) a').get_attribute('href'), 'mailto:rebekkah.abraham@wearewhatwedo.org')
		self.assertEqual(self.e(sel + 'p:nth-child(3)').text, 'US\nJon Voss\njon.voss@wearewhatwedo.org\n+1 415 935 4701')
		self.assertEqual(self.e(sel + 'p:nth-child(3) a').get_attribute('href'), 'mailto:jon.voss@wearewhatwedo.org')
		
		sel = '.sidebar .inner:nth-child(2) '
		self.assertEqual(self.e(sel + 'h3').text, 'Awards')
		self.assertEqual(self.e(sel + 'a:nth-child(1)').get_attribute('href'), 'http://www.webbyawards.com/webbys/current.php?season=15#webby_entry_charitable_organizations_non-profit')
		self.assertEqual(self.e(sel + 'img:nth-child(1)').get_attribute('src'), URL_BASE + '/resources/images/presscenter/webby_pink.png')
		self.assertEqual(self.e(sel + 'p:nth-child(3) a').get_attribute('href'), 'http://www.webbyawards.com/webbys/current.php?season=15#webby_entry_charitable_organizations_non-profit')
		self.assertEqual(self.e(sel + 'p:nth-child(3)').text, 'Webby for Best Charitable Organisation/Not-for-Profit Website')
		
		sel = '.sidebar .inner:nth-child(3) '
		self.assertEqual(self.e(sel + 'a:nth-child(1)').get_attribute('href'), 'http://thetim.es/y1vL3P')
		self.assertEqual(self.e(sel + 'img:nth-child(1)').get_attribute('src'), URL_BASE + '/resources/images/presscenter/sundaytimes500.png')
		self.assertEqual(self.e(sel + 'p:nth-child(2) a').get_attribute('href'), 'http://thetim.es/y1vL3P')
		self.assertEqual(self.e(sel + 'p:nth-child(2)').text, 'Sunday Times The App List 2012.')
		
		sel = '.sidebar .inner:nth-child(4) '
		self.assertEqual(self.e(sel + 'a:nth-child(1)').get_attribute('href'), 'http://lovieawards.eu/winners/')
		self.assertEqual(self.e(sel + 'img:nth-child(1)').get_attribute('src'), URL_BASE + '/resources/images/presscenter/lovie_pink.png')
		self.assertEqual(self.e(sel + 'p:nth-child(2) a').get_attribute('href'), 'http://lovieawards.eu/winners/')
		self.assertEqual(self.e(sel + 'p:nth-child(2)').text, 'Lovie Award for Best Education & Reference Website')
		
		sel = '.sidebar .inner:nth-child(5) '
		self.assertEqual(self.e(sel + 'a:nth-child(1)').get_attribute('href'), 'http://www.ala.org/aasl/guidelinesandstandards/bestlist/bestwebsitestop25')
		self.assertEqual(self.e(sel + 'img:nth-child(1)').get_attribute('src'), URL_BASE + '/resources/images/presscenter/aasl.jpg')
		self.assertEqual(self.e(sel + 'p:nth-child(2) a').get_attribute('href'), 'http://www.ala.org/aasl/guidelinesandstandards/bestlist/bestwebsitestop25')
		self.assertEqual(self.e(sel + 'p:nth-child(2)').text, 'American Association of School Librarians 2012 Best Website for Teaching and Learning')
		
		sel = '.sidebar .inner:nth-child(6) '
		self.assertEqual(self.e(sel + 'a:nth-child(1)').get_attribute('href'), 'http://www.familytreemagazine.com/article/best-old-map-and-photo-websites-for-genealogy-2012')
		self.assertEqual(self.e(sel + 'img:nth-child(1)').get_attribute('src'), URL_BASE + '/resources/images/presscenter/101-best-genealogy-websites-2012.jpg')
		self.assertEqual(self.e(sel + 'p:nth-child(2) a').get_attribute('href'), 'http://www.familytreemagazine.com/article/best-old-map-and-photo-websites-for-genealogy-2012')
		self.assertEqual(self.e(sel + 'p:nth-child(2)').text, 'Family Tree Magazine: 101 best family history websites')	
		
		sel = '.sidebar .inner:nth-child(7) '
		self.assertEqual(self.e(sel + 'h3').text, 'Press Pack')
		self.assertEqual(self.e(sel + 'a').get_attribute('href'), 'http://wawwd-resources.s3.amazonaws.com/presspacks/Historypin.zip')
		self.assertEqual(self.e(sel + 'p').text, u'Download press releases, pictures and all the info you\u2019ll need to write a fabulously complimentary article about us.')
		
	
	
	@url('/privacy-policy/') 
	def test_privacy_policy(self):
		self.assertTitle('Historypin | Privacy Policy')
		self.assertEqual(self.e('#site-content h1').text, 'Privacy Policy')

		items = [
			'1. What do we mean by "Your Data"?',
			'2. When do We collect Your data?',
			'3. How does We Are What We Do use Your Data?',
			'4.  Will We Are What We Do pass Your Data to third parties?',
			'5. Data Security',
			'6. Cookies',
			'7. Third party information',
			'8. Access to and Updating Your Data',
			'9. Other links',
			'10. Contact Us',
		]
		
		headings = self.es('#site-content .inner h2')
		for n in range(len(items)):
			self.assertEqual(headings[n].text, items[n])
	
	@url('/Friends-of-Historypin/')
	def test_support(self):
		# TODO fix this is the code and change the testcase
		# self.assertTitle('Historypin | Friends of Historypin')
		self.assertTitle('Historypin | Community | Partners')
		self.assertEqual(self.e('h2').text, 'What does the Foundation do?')
		
		sel = '.section '
		self.assertEqual(self.e(sel + 'img').get_attribute('src'), URL_BASE + '/resources/images/home/friends_of_Historypin.png')
		self.assertEqual(self.e(sel + 'p:nth-child(8) img').get_attribute('src'), URL_BASE + '/resources/images/home/friendsOfPhoto01.jpg')
		self.assertEqual(self.e(sel + 'p:nth-child(9) img').get_attribute('src'), URL_BASE + '/resources/images/home/friendsOfPhoto02.jpg')
		
		sel = '.sidebar .inner:nth-child(1) '
		self.assertEqual(self.e(sel + 'h3').text, 'Support Us')
		self.assertEqual(self.e(sel + 'p:nth-child(2)').text, 'Your donation to the We Are What We Do Charitable Foundation will go a long way in helping support Historypin Community and Education Programmes.')
		self.assertEqual(self.e(sel + 'p:nth-child(3)').text, 'Registered Charity Number\n1134546')
		self.assertEqual(self.e(sel + 'a').get_attribute('href'), 'http://www.charitygiving.co.uk/donate/donate_b.asp?charityid=5366')
		self.assertEqual(self.e(sel + 'a span').text, 'Donate')

		sel = '.sidebar .inner:nth-child(2) '
		self.assertEqual(self.e(sel + 'h3').text, 'Find out more')
		self.assertEqual(self.e(sel + 'h3 a').get_attribute('href'), URL_BASE + '/HistorypinCommunityandEducationProgrammes')
		self.assertEqual(self.e(sel + 'p').text, 'Read more about the aims of the Historypin Community and Education Programmes.')

		sel = '.sidebar .inner:nth-child(3) '
		self.assertEqual(self.e(sel + 'h3').text, 'Contact us')
		self.assertEqual(self.e(sel + 'p').text, 'To find out more, please contact ella.wiggans@wearewhatwedo.org')
		self.assertEqual(self.e(sel + 'p a').get_attribute('href'), 'mailto:ella.wiggans@wearewhatwedo.org')

	
	@url('/terms-and-conditions/')
	def test_toc(self):
		self.assertTitle('Historypin | Terms and Conditions')
		self.assertEqual(self.e('.rte h1').text, 'Historypin Terms and Conditions')
		
		links = [
			['000', 'Intro'],
			['010', '1. Accessing our Services'],
			['020', '2. Reliance on Information'],
			['030', '3. Acceptable Use'],
			['040', '4. Linking to Our Website'],
			['050', '5. Links from Our Website'],
			['060', '6. Charges'],
			['070', '7. Registered Users use of Historypin Services'],
			['080', '8. Age restrictions, parental consent and use by schools'],
			['090', '9. Password, Profile and Security'],
			['100', '10. Your promises to us'],
			['110', '11. Termination and Cancellation'],
			['120', '12. Use of Content'],
			['130', '13. Limitation on our Liability'],
			['140', '14. Complaints and Feedback'],
			['150', '15. Security and Privacy'],
			['160', '16. Changes to these Terms and Conditions'],
			['170', '17. Severance'],
			['180', '18. Exclusion of Third Party Rights'],
			['190', '19. Entire Agreement'],
			['200', '20. Law'],
			['210', '21. Contact Us'],
		]
		
		anchors		= self.es('.page li a')
		headings	= self.es('.page h2')
		for n in range(len(links)):
			i = links[n]
			
			self.assertEqual(anchors[n].text, i[1])
			self.assertEqual(anchors[n].get_attribute('href'), URL_BASE + '/terms-and-conditions/#' + i[0])
			
			self.assertEqual(headings[n].get_attribute('id'), i[0])
			self.assertEqual(headings[n].text, i[1])
	
	@url('/wearewhatwedo/')
	def test_wawwd(self):
		self.assertTitle('Historypin | We Are What We Do')
		self.assertEqual(self.e('.title').text, 'We Are What We Do')
		
		sel = '.rte p:nth-child(5) a'
		self.assertEqual(self.e(sel).get_attribute('href'), 'http://wearewhatwedo.org/')
		self.assertEqual(self.e(sel).text, 'wearewhatwedo.org')

