# -*- coding: utf-8 -*-

from base import *

class Pages(HPTestCase):
	
	@url('/about-us/')
	def test_about(self):
		self.assertTitle('Historypin | A 90 second introduction')
		self.assertEqual('A 90 second introduction'							, self.e('h1.title').text)
		self.assertEqual('http://www.youtube.com/embed/FdT3eKdto4w?rel=0'	, self.e('iframe').get_attribute('src'))
	
	@url('/app/')
	def test_app(self):
		self.assertTitle('Historypin | App')
		self.assertEqual('What can you do on the Historypin app?', self.e('h2').text)
		
		items = [
			['Android'			, 'app_android.png'	, 'Google Play Store'			, 'https://market.android.com/details?id=com.historypin.Historypin&feature=search_result'],
			['iOS'				, 'app_iphone.png'	, 'iOS App Store'				, 'http://itunes.apple.com/app/historypin/id455228207?mt=8'],
			['Windows Phone 7'	, 'app_wp7.png'		, 'Windows Phone Marketplace'	, 'http://www.windowsphone.com/en-US/apps/05638072-742e-460c-ab97-18d2b47ef06b'],
		]
		
		cnt			= self.e('.appstores')
		headings	= cnt.es('.col h1')
		images		= cnt.es('.col img')
		texts		= cnt.es('.col a span')
		links		= cnt.es('.col a')
		
		for n in range(len(items)):
			i = items[n]
			self.assertEqual(i[0]				, headings[n].text)
			self.assertEqual(URL_BASE + '/resources/images/content/app/' + i[1]	, images[n].get_attribute('src'))
			self.assertEqual(i[2]				, texts[n].text)
			self.assertEqual(i[3]				, links[n].get_attribute('href'))
	
	@url('/contact/')
	def test_contact(self):
		self.assertTitle('Historypin | Contact')
		self.assertEqual('Contact', self.e('.section h1.title').text)
		
		content = [
			['General enquiries, technical enquiries, content enquiries', 'historypin@wearewhatwedo.org\n+44 (0)20 7148 7666\n71 St John Street\nLondon\nEC1M 4NJ\nUnited Kingdom', 'mailto:historypin@wearewhatwedo.org'],
			['Media', 'Rebekkah Abraham\nrebekkah.abraham@wearewhatwedo.org\n+44 (0)20 7148 7670', 'mailto:rebekkah.abraham@wearewhatwedo.org'],
			['Schools, local projects and volunteers', 'Rebekkah Abraham\nrebekkah.abraham@wearewhatwedo.org\n+44 (0)20 7148 7670', 'mailto:rebekkah.abraham@wearewhatwedo.org'],
			['Library, archive and museum partnerships', 'Rebekkah Abraham\nrebekkah.abraham@wearewhatwedo.org\n+44 (0)20 7148 7670', 'mailto:rebekkah.abraham@wearewhatwedo.org'],
			['Web', 'Alex Stanhope\nalex.stanhope@wearewhatwedo.org\n+44 (0)20 7148 7666', 'mailto:alex.stanhope@wearewhatwedo.org'],
			['Corporate Partnerships', 'Nick Stanhope\nnick.stanhope@wearewhatwedo.org\n+44 (0)20 7148 7667', 'mailto:nick.stanhope@wearewhatwedo.org'],
		]
		
		cnt			= self.e('.section')
		headings	= cnt.es('h2')
		paragraphs	= cnt.es('p')
		links		= cnt.es('p a')
		
		for n in range(len(content)):
			i = content[n]
			self.assertEqual(i[0], headings[n].text)
			self.assertEqual(i[1], paragraphs[n].text)
			self.assertEqual(i[2], links[n].get_attribute('href'))
	
	@url('/faq/')
	def test_faq(self):
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
				'heading': 'Managing your Account',
				'items': [
					['title91', 'How do I connect my Twitter Account with my existing Historypin Channel?'],
					['title92', 'How do I connect my Facebook Account with my existing Historypin Channel?'],
					['title93', 'How do I connect my Google Account with my existing Historypin Channel?'],
					['title94', 'How do I disconnect my Google / Facebook / Twitter account from my Historypin Channel?'],
					['title95', 'I am having problems connecting my Google / Facebook / Twitter Account to my Historypin Channel.'],
					['title96', 'Can I have one Facebook, Twitter or Google Account connected to more than one Historypin Channel?'],
					['title97', 'Can I have one Historypin Channel connected to multiple Facebook or Google or Twitter accounts?'],
					['title98', 'Can I change the Google Account associated with my Historypin Channel?'],
					['title99', 'Can I delete my Historypin Channel?'],
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
					['title61', 'I\'m a journalist and want to write a fabulously complimentary article about you. What do I do?'],
					['title62', 'I\'ve got another question, what should I do?'],
				],
			},
		]
		
		# toc				= self.es('.toc > li')
		# cnt				= self.es('.faq-group')
		questions		= self.es('.toc > li strong')
		questions_h		= self.es('.faq-group h2')
		answers			= self.es('.toc > li li a')
		answers_h		= self.es('.faq-group h3')
		
		k = 0
		for n in range(len(faq)):
			i = faq[n]
			
			self.assertEqual(i['heading'], questions[n].text)
			self.assertEqual(i['heading'], questions_h[n].text)
			
			for item in i['items']:
				self.assertEqual(URL_BASE + '/faq/#' + item[0]	, answers[k].get_attribute('href'))
				self.assertEqual(item[1]						, answers[k].text)
				self.assertEqual(item[0]						, answers_h[k].get_attribute('id'))
				self.assertEqual(item[1]						, answers_h[k].text)
				
				k += 1
	
	@url('/presscentre/')
	def test_press_center(self):
		self.assertTitle('Historypin | Press Centre')
		self.assertEqual('Press Centre', self.e('h1.title').text)
		
		headings = self.es('.section h2')
		self.assertEqual('Some of our favourite coverage'	, headings[0].text)
		self.assertEqual('Coverage to date'					, headings[1].text)
		
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
		
		paragraphs	= self.es('#site-content .right p')
		p_links		= self.es('#site-content .right a')
		for n in range(len(links)):
			i = links[n]
			self.assertEqual(i[0]				, p_links[n].get_attribute('href'))
			self.assertEqual(i[1] + '\n' + i[2]	, paragraphs[n].text)
		
		cnt = self.e('.sidebar .inner:nth-of-type(1)')
		self.assertEqual('Contact Details', cnt.e('h3').text)
		
		p, a = cnt.es('p'), cnt.es('p a')
		self.assertEqual('UK & Global\nRebekkah Abraham\nrebekkah.abraham@wearewhatwedo.org\n+44 (0)20 7148 7666'	, p[0].text)
		self.assertEqual('mailto:rebekkah.abraham@wearewhatwedo.org'												, a[0].get_attribute('href'))
		self.assertEqual('US\nJon Voss\njon.voss@wearewhatwedo.org\n+1 415 935 4701'								, p[1].text)
		self.assertEqual('mailto:jon.voss@wearewhatwedo.org'														, a[1].get_attribute('href'))
		
		self.assertEqual('Awards', self.e('.sidebar .inner:nth-of-type(2) h3').text)
		
		sidebar = [
			['Webby for Best Charitable Organisation/Not-for-Profit Website'	, 'http://www.webbyawards.com/webbys/current.php?season=15#webby_entry_charitable_organizations_non-profit', '/resources/images/presscenter/webby_pink.png'],
			['Sunday Times The App List 2012.'									, 'http://thetim.es/y1vL3P'	, '/resources/images/presscenter/sundaytimes500.png'],
			['Lovie Award for Best Education & Reference Website'				, 'http://lovieawards.eu/winners/', '/resources/images/presscenter/lovie_pink.png'],
			['American Association of School Librarians 2012 Best Website for Teaching and Learning', 'http://www.ala.org/aasl/guidelinesandstandards/bestlist/bestwebsitestop25', '/resources/images/presscenter/aasl.jpg'],
			['Family Tree Magazine: 101 best family history websites'			, 'http://www.familytreemagazine.com/article/best-old-map-and-photo-websites-for-genealogy-2012', '/resources/images/presscenter/101-best-genealogy-websites-2012.jpg'],
			["We're in featured in Common Sense Media's Back to School Guide"	, 'http://www.commonsensemedia.org/mobile-app-reviews/historypin', '/resources/images/presscenter/badge_checkusout.png'],
		]
		
		
		cnt			= self.e('.sidebar')
		paragraphs	= cnt.es('p:nth-of-type(2)')[1:]
		images		= cnt.es('img')
		links		= cnt.es('a')[2:]
		
		for n in range(len(sidebar)):
			i = sidebar[n]
			
			self.assertEqual(i[0]				, paragraphs[n].text)
			self.assertEqual(URL_BASE + i[2]	, images[n].get_attribute('src'))
			self.assertEqual(i[1]				, links[2 * n].get_attribute('href'))
			self.assertEqual(i[1]				, links[2 * n + 1].get_attribute('href'))
		
		cnt = self.e('.sidebar .inner:nth-of-type(8)')
		self.assertEqual('Press Pack', cnt.e('h3').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/presspacks/Historypin.zip', cnt.e('a').get_attribute('href'))
		self.assertEqual(u'Download press releases, pictures and all the info you\u2019ll need to write a fabulously complimentary article about us.', cnt.e('p').text)
	
	@url('/privacy-policy/')
	def test_privacy_policy(self):
		self.assertTitle('Historypin | Privacy Policy')
		self.assertEqual('Privacy Policy', self.e('#site-content h1').text)
		
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
		
		headings = self.es('#site-content h2')
		for n in range(len(items)):
			self.assertEqual(items[n], headings[n].text)
	
	@url('/Friends-of-Historypin/')
	def test_support(self):
		self.assertTitle('Historypin | Friends of Historypin')
		self.assertEqual('What does the Foundation do?', self.e('h2').text)
		
		images = [
			'friends_of_Historypin.png',
			'friendsOfPhoto01.jpg',
			'friendsOfPhoto02.jpg',
		]
		
		imgs = self.es('.section img')
		for n in range(len(images)):
			self.assertEqual(URL_BASE + '/resources/images/home/' + images[n], imgs[n].get_attribute('src'))
		
		sidebar = [
			{
				'heading': 'Support Us',
				'paragraphs': ['Your donation to the We Are What We Do Charitable Foundation will go a long way in helping support Historypin Community and Education Programmes.', 'Registered Charity Number\n1134546'],
				'link': ['Donate', 'http://www.charitygiving.co.uk/donate/donate_b.asp?charityid=5366'],
			},
			{
				'heading': 'Find out more',
				'link_h': '/HistorypinCommunityandEducationProgrammes',
				'paragraphs': ['Read more about the aims of the Historypin Community and Education Programmes.'],
			},
			{
				'heading': 'Contact us',
				'paragraphs': ['To find out more, please contact ella.wiggans@wearewhatwedo.org'],
				'link': ['ella.wiggans@wearewhatwedo.org', 'mailto:ella.wiggans@wearewhatwedo.org'],
			},
		]
		
		cnt			= self.e('.sidebar')
		headings	= cnt.es('h3')
		paragraphs	= cnt.es('p')
		links		= cnt.es('a')
		
		p, l = 0, 0
		for n in range(len(sidebar)):
			i = sidebar[n]
			
			self.assertEqual(i['heading'], headings[n].text)
			
			if 'link_h' in i: self.assertEqual(URL_BASE + i['link_h'], headings[n].e('a').get_attribute('href'))
			
			for k in range(len(i['paragraphs'])):
				self.assertEqual(i['paragraphs'][k], paragraphs[p].text)
				
				p += 1
			
			if 'links' in i:
				link = i['link']
				self.assertEqual(link[0], links[l].get_attribute('href'))
				self.assertEqual(link[1], links[l].text)
				
				l += 1
	
	@url('/terms-and-conditions/')
	def test_toc(self):
		self.assertTitle('Historypin | Terms and Conditions')
		self.assertEqual('Historypin Terms and Conditions', self.e('.rte h1').text)
		
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
			['120', '12. Contributed Content'],
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
			
			self.assertEqual(i[1]											, anchors[n].text)
			self.assertEqual(URL_BASE + '/terms-and-conditions/#' + i[0]	, anchors[n].get_attribute('href'))
			self.assertEqual(i[0]											, headings[n].get_attribute('id'))
			self.assertEqual(i[1]											, headings[n].text)
	
	@url('/cookies/')
	def test_cookies(self):
		#  change title to be HP | Cookies (not contact)
		self.assertEqual('Cookies', self.e('h2').text)
		
		cnt = self.e('.page.rte')
		self.assertEqual(u'The use_hitbox cookie updates the ‘views’ counter on YouTube when you have viewed a video from that site through ours.', cnt.e('p:nth-of-type(2)').text)
		
		self.assertEqual('http://www.google.co.uk/intl/en/analytics/privacyoverview.html', cnt.e('a:first-of-type').get_attribute('href'))
		self.assertEqual('http://www.google.co.uk/intl/en/analytics/privacyoverview.html', cnt.e('a:first-of-type').text)
	
	@url('/wearewhatwedo/')
	def test_wawwd(self):
		self.assertTitle('Historypin | We Are What We Do')
		self.assertEqual('We Are What We Do', self.e('.title').text)
		
		a = self.e('.rte p:nth-child(5) a')
		self.assertEqual('http://wearewhatwedo.org/'	, a.get_attribute('href'))
		self.assertEqual('wearewhatwedo.org'			, a.text)
	
	@url('/bulkbridge/')
	def test_bulkbridge_page(self):
		
		self.assertTitle('Historypin | Bulk Uploader for Chrome and Firefox')
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Bulk Uploader for Chrome and Firefox', site_cnt.e('h1').text)
		
		titles = [
			['What is the Bulk Uploader?'	, 'title1'],
			['How does it work?'			, 'title2'],
			['What requirements are there?'	, 'title3'],
			['How to I get started?'		, 'title4'],
		]
		
		list = site_cnt.es('.toc li a')
		
		for n in range(len(titles)):
			i = titles[n]
			self.assertEqual(i[0], list[n].text)
			self.assertEqual(URL_BASE + '/bulkbridge/#' + i[1], list[n].get_attribute('href'))
		
		button = site_cnt.e('.button.left')
		self.assertEqual("I'm ready to do a Bulk Upload", button.e('span').text)
		self.assertEqual(URL_BASE + '/upload-bulk/'		, button.get_attribute('href'))
		
		csv = self.e('ol li:nth-of-type(1)')
		self.assertEqual('Download our CSV template and the Instructions on how to complete it.', csv.text)
		
		link = 'http://wawwd-resources.s3.amazonaws.com/historypin/bulk_upload/'
		self.assertEqual(link + 'Historypin_Bulk_Upload_Template.csv'									, csv.es('a')[0].get_attribute('href'))
		self.assertEqual(link + 'Historypin_Instructions_for_Completing_a_CSV_template_March_2012.xls'	, csv.es('a')[1].get_attribute('href'))
		
		sidebar		= self.e('.sidebar')
		downloads	= sidebar.e('.inner:nth-of-type(1)')
		anchors		= downloads.es('a')
		
		self.assertEqual('Downloadables', downloads.e('h3').text)
		
		tpl = [
			['CSV template download'			, 'Historypin_Bulk_Upload_Template.csv'],
			['Instructions to complete the CSV'	, 'Historypin_Instructions_for_Completing_a_CSV_template_March_2012.xls'],
			['Advice and tips'					, 'Bulk_Upload_Advice_and_Tips.pdf'],
		]
		
		for n in range(len(tpl)):
			i = tpl[n]
			self.assertEqual(i[0], anchors[n].text)
			self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/bulk_upload/' + i[1], anchors[n].get_attribute('href'))
		
		help = sidebar.e('.inner:nth-of-type(2)')
		self.assertEqual('Get help', help.e('h3').text)
		
		self.assertEqual('If you get stuck or have any questions, check out our How To page and FAQs and please feel free to contact us at historypin@wearewhatwedo.org', help.e('p').text)
		
		links = [
			[URL_BASE + '/community/howtos/'		, 'How To page'],
			[URL_BASE + '/faq/'						, 'FAQs'],
			['mailto:historypin@wearewhatwedo.org'	, 'historypin@wearewhatwedo.org'],
		]
		
		links_help = help.es('p a')
		
		for n in range(len(links)):
			i = links[n]
			self.assertEqual(i[0]	, links_help[n].get_attribute('href'))
			self.assertEqual(i[1]	, links_help[n].text)
