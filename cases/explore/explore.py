# -*- coding: utf-8 -*-

from base import *
import os, sys

class Explore(HPTestCase):
	
	PROJECT_URL = '/en/explore/oreo'
	
	@url('/en/explore/oreo')
	def test_header_not_logged_in(self):
		
		self.assertTitle('Historypin')
		
		sleep(3)
		
		header			= self.e('#header')
		user_options	= header.e('.user-options')
		sign_in			= user_options.e('.sign-in')
		sign_up			= user_options.e('.sign-up')
		
		self.assertEqual('Sign in'	, sign_in.text)
		self.assertEqual('Join'		, sign_up.text)
		
		sign_in.click()
		
		sign_in_dialog	= self.e('#ui-id-1')
		email_login		= sign_in_dialog.e('#user_login')
		social_buttons	= sign_in_dialog.e('.social-buttons')
		social_li		= social_buttons.es('li a')
		
		self.assertEqual('Sign in to Historypin', sign_in_dialog.e('h2').text)
		
		social_items = [
			['Sign in with Facebook', '%s/#' % self.PROJECT_URL, 'ss-facebook'],
			['Sign in with Twitter'	, '/user/twitter-login/?from=%s/' % self.PROJECT_URL, 'ss-twitter'],
			['Sign in with Google'	, '/user/google_login/?from=%s/' % self.PROJECT_URL, 'ss-googleplus'],
		]
		
		for n in range(len(social_items)):
			i = social_items[n]
			self.assertEqual(i[0], social_li[n].text)
			self.assertEqual(URL_BASE + i[1], social_li[n].get_attribute('href'))
			self.assertEqual(i[2], social_li[n].e('span').get_attribute('class'))
		
		self.assertIsInstance(email_login.e('#email')		, WebElement)
		self.assertIsInstance(email_login.e('#password')	, WebElement)
		self.assertIsInstance(email_login.e('.login-submit'), WebElement)
		
		sign_in_dialog.e('.close-btn-wrapp a').click()
	
	@logged_in
	def test_header_logged_in(self):
		self.go('%s/' % self.PROJECT_URL)
		
		user_options	= self.e('.user-options')
		options_list	= user_options.e('.actions-list')
		option_items	= options_list.es('a')
		pin_button		= user_options.e('.pin-btn')
		
		self.assertEqual('%s/resources/avatars/200x200/avatar_3.png' % URL_BASE, user_options.e('img').get_attribute('src'))
		
		self.hover(self.e('.user-actions-triger'))
		
		
		self.assertEqual('%s/channels/view/%d/' % (URL_BASE, ID_USER), option_items[0].get_attribute('href'))
		self.assertEqual('My Profile', option_items[0].text)
		
		self.assertEqual('%s/user/logout/' % URL_BASE, option_items[1].get_attribute('href'))
		self.assertEqual('Logout', option_items[1].text)
		
		# assert pin something link and text
		
		self.assertEqual('%s/en/project/30-oreo/upload/?from=%s/' % (URL_BASE, self.PROJECT_URL), pin_button.get_attribute('href'))
		self.assertEqual('Pin something\n+', pin_button.text)
	
	@logged_in
	@url('/en/explore/oreo')
	def test_breadcrumb_nav(self):
		
		sleep(3)  # the test fails without the sleep
		header			= self.e('#header')
		breadcrumbs		= header.e('.breadcrumbs')
		breadcrumbs_li	= breadcrumbs.es('li a')
		banner			= self.e('#banner')
		project_heading	= banner.e('h3')
		
		self.assertEqual('%s%s/' % (URL_BASE, self.PROJECT_URL), breadcrumbs_li[0].get_attribute('href'))
		self.assertEqual(breadcrumbs_li[0].text, project_heading.text)  # checkes if the breadcrumb is equal to project heading
		
		banner.e('.edit-project').click()
		sleep(4)
		self.e('#banner-form .edit-heading').clear()
		self.e('#banner-form .edit-heading').send_keys('Quality Assurance')  # sends keys with different title
		
		banner.e('.save-project').click()  # saves the change title
		
		sleep(2)
		self.browser.refresh()  # refreshes the page with the new title
		
		sleep(4)
		header			= self.e('#header')
		breadcrumbs		= header.e('.breadcrumbs')
		breadcrumbs_li	= breadcrumbs.es('li a')
		banner			= self.e('#banner')
		project_heading	= banner.e('h3')
		
		self.assertEqual(breadcrumbs_li[0].text, project_heading.text)  # check if the new title matches the breadcrumb after refresh
		
		banner.e('.edit-project').click()
		sleep(4)
		banner.e('.edit-heading').clear()
		banner.e('.edit-heading').send_keys('Project for Quality Assurance')
		
		banner.e('.save-project').click()
	
	@url('/en/explore/oreo')
	def test_index(self):
		
		self.assertTitle('Historypin')
		
		header	= self.e('#header')
		self.assertEqual('%s/' % URL_BASE, header.e('a').get_attribute('href'))
		
		self.assertEqual('Project for Quality Assurance', self.e('h3').text)
		
		share_toolbox = self.e('.addthis_toolbox')
		self.hover(share_toolbox)
		social_cnt = self.e('.social-container')
		share_items = social_cnt.es('li')
		self.assertIsInstance(share_items[0], WebElement)
		self.assertIsInstance(share_items[1], WebElement)
		self.assertIsInstance(share_items[2], WebElement)
		self.assertIsInstance(share_items[3], WebElement)
		
		banner		= self.e('#banner')
		explore_map	= banner.e('#btn-explore')
		
		explore_map.click()
		
		timeline = self.e('#timeline')
		self.assertEqual('2002', timeline.e('.start').text)
		self.assertEqual('2002', timeline.e('.ui-state-default.ui-corner-all:nth-of-type(1)').text)
		
		
		self.assertEqual('2014', timeline.e('.end').text)
		self.assertEqual('2014', timeline.e('.ui-state-default.ui-corner-all:nth-of-type(2)').text)
		
		self.assertIsInstance(timeline.e('.ui-slider-range'), WebElement)
		
		self.assertIsInstance(self.e('#map'), WebElement)
	
	@url('/en/explore/oreo/geo/42.681793,23.369018,14')
	def test_map_pin(self):
		
		# banner		= self.e('#banner')
		# explore_map	= banner.e('#btn-explore')
		
		# canvas = self.e('.gm-style div div div div div div div:nth-of-type(13)')
		# canvas.click()
		# self.browser.click_xy(self.e('#container'), 100, 67)
		# self.browser.click_xy(self.e('#container'), 466, 255)
		# self.browser.click_xy(self.e('#container'), 380, 200)
		# sleep(10)
		# TODO
		# click on a pin on the map
		# pin = self.e('#pin')
		# self.assertIsInstance(pin.e('.cnt-holder'), WebElement)
		pass
	
	@url('/en/explore/oreo/date/2002:2010')
	def test_date_slider(self):
		
		sleep(2)  # without sleep the test fails
		timeline = self.e('#timeline')
		self.assertEqual('2002', timeline.e('.ui-state-default.ui-corner-all:nth-of-type(1)').text)
		self.assertEqual('2010', timeline.e('.ui-state-default.ui-corner-all:nth-of-type(2)').text)
		
		# TODO
		# click a pin on the map to check, if it is in the date range
		
	
	@url('/en/explore/oreo/pin/225263')
	def test_youtube_audio_pin(self):
		
		sleep(3)
		timeline = self.e('#timeline')
		self.assertEqual('2 January 2012', timeline.e('.tooltip.arrow-down').text)
		
		self.assertEqual(u'\u23ea \u23e9 Sound in Sofia', self.e('#pin h1').text)
		# TODO cannot assert the youtube embed
		
		bookmarks = self.e('.bookmarks')
		self.assertIsInstance(bookmarks.e('.info-anchor'), WebElement)
		
	
	@url('/en/explore/oreo/pin/228823')
	def test_soundcloud_audio_pin(self):
		# playButton
		# self.assertIsInstance(self.e('#widget'), WebElement) TODO
		sleep(4)
		pass
	
	@url('/en/explore/oreo/pin/225261')
	def test_youtube_video_pin(self):
		pass
	
	@url('/en/explore/oreo/pin/225260')
	def test_vimeo_video_pin(self):
		pass
	
	@logged_in
	@url('/en/explore/oreo/pin/225263')
	def test_edit_item(self):
		
		edit_icon = self.e('.bookmarks a:nth-of-type(3)')
		self.assertEqual('%s/project/30-test-QA-project/upload-audio/pin/phid/225263/edit/1/?from=/en/explore/oreo/pin/225263' % URL_BASE, edit_icon.get_attribute('href'))
		self.assertEqual('Edit', edit_icon.text)
		
		edit_icon.click()
		
		sleep(3)
		
		self.e('#photo_pin').click()
		
		# project = self.e('#select_projects li a')
		# self.assertEqual('Project for Quality Assurance', project.text)
		
		# self.e('.submit').click()
		
		sleep(5)
		self.assertEqual('%s/en/explore/oreo/pin/225263' % URL_BASE, self.browser.current_url)
		self.assertEqual('%s/resources/avatars/200x200/avatar_3.png' % URL_BASE, self.e('.content.ng-scope img').get_attribute('src'))
		self.assertIsInstance(self.e('.bookmarks'), WebElement)
	
	@url('/en/explore/oreo/pin/225259')
	def test_force_login_comment(self):
		
		self.assertEqual('%s/resources/explore/images/default-avatar.jpg' % URL_BASE, self.e('.comment h4+img').get_attribute('src'))
		
		text_login = self.e('.login-or-join')
		
		self.assertEqual('Log in', text_login.e('a:nth-of-type(1)').text)
		self.assertEqual('%s/user/?from=/en/explore/oreo/pin/225259/' % URL_BASE, text_login.e('a:nth-of-type(1)').get_attribute('href'))
		
		self.assertEqual('join', text_login.e('a:nth-of-type(2)').text)
		self.assertEqual('%s/user/?from=/en/explore/oreo/pin/225259/' % URL_BASE, text_login.e('a:nth-of-type(2)').get_attribute('href'))
		
	@unittest.expectedFailure  # TODO write the test when we have functionality for pinning
	@url('/en/explore/oreo/')
	def test_force_login_pinning(self):
		# TODO
		# currently there is not such functionality for pinning or designs
		# not logged in
		# click to add a pin
		# check if redirects to the login page
		pass
	
	@logged_in
	@url('/en/explore/oreo/pin/225260')
	def test_make_comment(self):
		
		# TODO add img link when it is added
		# delete the comment (currently, a comment cannot be deleted)
		
		comment_section = self.e('.comment')
		
		self.assertEqual('%s/resources/avatars/200x200/avatar_3.png' % URL_BASE, comment_section.e('img').get_attribute('src'))
		self.assertEqual('Enter your comment here', comment_section.e('textarea').get_attribute('placeholder'))
		
		comment_section.e('textarea').send_keys('This is one of the famous theaters in Bulgaria.It is located in a nice old building, that is one of the most beautiful in Sofia.')
		comment_section.e('.comment-submit').click()
		sleep(4)
		
		comment_data = self.e('.comment-data')
		
		self.assertEqual('%s/resources/avatars/200x200/avatar_3.png' % URL_BASE, comment_data.e('img').get_attribute('src'))
		self.assertEqual('%s/channels/view/%d/' % (URL_BASE, ID_USER), comment_data.e('a').get_attribute('href'))
		
	
	@url('/en/explore/oreo/pin/225259')
	def test_image_pin(self):
		
		sleep(4)
		timeline = self.e('#timeline')
		
		self.assertEqual('2002', timeline.e('.ui-state-default.ui-corner-all:nth-of-type(1)').text)
		self.assertEqual('2014', timeline.e('.ui-state-default.ui-corner-all:nth-of-type(2)').text)
		self.assertEqual('2 January 2006', timeline.e('.tooltip').text)
		# self.assertEqual('ulitsa "Georgi Benkovski", 1000 Sofia, Bulgaria', self.e('#map .tooltip.arrow-down').text)
		
		column_header = self.e('#pin .row')
		
		self.assertEqual(u'\u23ea \u23e9 Bulgarian Army Theater', self.e('#explore h1').text)
		self.assertEqual('%s/channels/img/33283/logo/1/dim/50x50/crop/1/' % URL_BASE, column_header.e('.author-image img').get_attribute('src'))
		self.assertEqual('Pinned by\nGabss'					, column_header.e('.author').text)
		self.assertEqual('%s/channels/view/33283' % URL_BASE, column_header.e('.author a').get_attribute('href'))
		
		
		share_toolbox	= self.e('.addthis_toolbox')
		self.hover(share_toolbox)
		
		social_cnt		= self.e('.social-container')
		share_items		= social_cnt.es('li')
		
		self.assertIsInstance(share_items[0], WebElement)
		self.assertIsInstance(share_items[1], WebElement)
		self.assertIsInstance(share_items[2], WebElement)
		self.assertIsInstance(share_items[3], WebElement)
		
		column_3b = self.e('.content')
		self.assertEqual('%s/services/thumb/phid/225259/dim/600x600/quality/80/' % URL_BASE, column_3b.e('img').get_attribute('src'))
		
		self.assertIsInstance(column_3b.e('.info-anchor'), WebElement)
		
		h4s		= ['DATE TAKEN', 'DESCRIPTION', 'TAGS', 'INFORMATION', 'CREATOR', 'ADD A COMMENT', 'COMMENTS (3)']
		h4s_cnt	= column_3b.es('h4')
		for n in range(len(h4s)): self.assertEqual(h4s[n], h4s_cnt[n].text)
		
		self.assertEqual('This is a photo of the famous Bulgarian Army Theater', self.e('#pin .description p:nth-of-type(2)').text)
		
		tags		= self.e('#pin .tags')
		tag_items	= tags.es('a')
		self.assertEqual('theater'			, tag_items[0].text)
		self.assertEqual('theatre'			, tag_items[1].text)
		self.assertEqual('bulgarian army'	, tag_items[2].text)
		
		# column_header.e('.close-anchor').click()
		# self.assertFalse(column_header.is_displayed())
		# self.assertFalse(column_3b.is_displayed())
	
	@logged_in
	@url('/en/explore/oreo/pin/223343/geo/43.24369,23.956892,6')
	def test_text_pin(self):
		
		sleep(3)
		self.assertEqual('Project for Quality Assurance', self.e('h3').text)
		# self.assertEqual('5 May 2012', self.e('.tooltip.arrow-up').text)
		
		column_row = self.e('.c3b')
		
		sleep(3)
		self.assertEqual(u'\u23ea \u23e9 Title Text Pin1', column_row.e('h1').text)
		self.assertEqual('%s/channels/img/49127/logo/1/dim/50x50/crop/1/' % URL_BASE, column_row.e('.author-image img').get_attribute('src'))
		self.assertEqual('Rawr', column_row.e('.author a').text)
		self.assertEqual('%s/channels/view/49127' % URL_BASE, column_row.e('.author a').get_attribute('href'))
		
		self.assertIn(u'Lorem Ipsum е елементарен примерен текст, използван в печатарската и типографската индустрия.', self.e('.text-pin').text)
		
		share_toolbox	= self.e('.addthis_toolbox')
		self.hover(share_toolbox)
		
		social_cnt		= self.e('.social-container')
		share_items		= social_cnt.es('li')
		
		self.assertIsInstance(share_items[0], WebElement)
		self.assertIsInstance(share_items[1], WebElement)
		self.assertIsInstance(share_items[2], WebElement)
		self.assertIsInstance(share_items[3], WebElement)
		
		self.e('.info-anchor.ss-icon.ss-info').click()
		
		# info_pin = self.e('.description')
		
		# h4s = ['DESCRIPTION', 'TAGS', 'INFORMATION', 'CREATOR'] TODO FIX THIS
		# h4s_cnt = info_pin.es('h4')
		# for n in range(len(h4s)): self.assertEqual(h4s[n], h4s_cnt[n].text)
		
		self.assertEqual("Licence: Copyright (c) all rights reserved\nAttribution:\nOriginal link:\nRepository:\nNotes:", self.e('.information').text)
	
	@url('/en/explore/oreo')
	def test_user_project(self):
		
		sleep(3)
		banner = self.e('#banner')
		
		self.assertEqual('Project for Quality Assurance', banner.e('h3').text)
		
		share_toolbox	= banner.e('.addthis_toolbox')
		self.hover(share_toolbox)
		
		social_cnt		= self.e('.social-container')
		share_items		= social_cnt.es('li')
		self.assertIsInstance(share_items[0], WebElement)
		self.assertIsInstance(share_items[1], WebElement)
		self.assertIsInstance(share_items[2], WebElement)
		self.assertIsInstance(share_items[3], WebElement)
		
		self.assertEqual('Gabss', banner.e('.channel-link span').text)
		
		sleep(3)
		self.assertEqual('%s/projects/img/pid/30/type/project_image,banner,logo/dim/1920x450/crop/1/off/0x1/zoom/400' % URL_BASE, self.e('.panel > img').get_attribute('src'))
		self.assertIn('Lorem Ipsum is simply dummy text of the printing and typesetting industry.', self.e('.description.inner p').text)
		
		project_sidebar	= self.e('.sidebar')
		h4s				= project_sidebar.es('h4')
		
		self.assertEqual('LEADERS'		, h4s[0].text)
		self.assertEqual('RELATED LINKS', h4s[1].text)
		self.assertEqual('MAIN LOCATION', h4s[2].text)
		
		admins_cnt = [
			['/49127/'	, '/channels/img/49127/logo/1/dim/50x50/crop/1/cache/0/', 'Rawr'		, 'Project Leader'],
			['/33283/'	, '/channels/img/33283/logo/1/dim/50x50/crop/1/cache/0/', 'Gabss'		, 'Project Leader'],
			['/867/'	, '/channels/img/867/logo/1/dim/50x50/crop/1/cache/0/'	, 'Karamfil'	, 'Project Leader'],
			['/47515/'	, '/resources/explore/images/default-avatar.jpg', 'n.p.slavov'			, 'Project Leader'],
			['/35019/'	, '/resources/explore/images/default-avatar.jpg', 'Gabriela Ananieva'	, 'Project Leader'],
			['/55376/'	, '/resources/explore/images/default-avatar.jpg', 'b.gaganelov'			, 'Project Leader'],
			['/50570/'	, '/resources/explore/images/default-avatar.jpg', 'frozkata'			, 'Project Leader'],
		]
		
		admins		= project_sidebar.e('.project-admins')
		links_imgs	= project_sidebar.es('.img-wrapper a')
		links_name	= admins.es('.usr-name')
		images		= admins.es('img')
		role		= admins.es('.usr-type')
		
		for n in range(len(admins_cnt)):
			i = admins_cnt[n]
			self.assertEqual(URL_BASE + '/channels/view' + i[0], links_imgs[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/channels/view' + i[0], links_name[n].get_attribute('href'))
			self.assertEqual(URL_BASE + i[1], images[n].get_attribute('src'))
			self.assertEqual(i[2], links_name[n].text)
			self.assertEqual(i[3], role[n].text)
			
		
		location = project_sidebar.e('.project-location')
		self.assertEqual('Malaysia', location.e('p').text)
		self.assertIsInstance(location.e('.small-map'), WebElement)
		
		banner.e('#btn-explore').click()
	
	@logged_in
	@url('/en/explore/oreo')
	def test_edit_project(self):
		
		sleep(4)
		self.assertEqual('Edit project', self.e('.edit-project').text)
		self.e('.edit-project').click()
		sleep(2)
		
		banner	= self.e('.edit-banner')
		heading	= banner.e('.edit-heading')
		
		
		edit_project = self.e('.edit-project')
		self.assertEqual('Editing project', edit_project.text)
		
		edit_project.click()
		sleep(2)
		
		heading.clear()
		heading.send_keys('Project for Quality Assurance')
		
		self.assertEqual('Change photo', self.e('.button.change').text)
		
		# test upload an image
		
		file_upload = self.e('#fileupload-input')
		file_upload.send_keys(os.getcwd()+"/mountain_ridge.jpg")
		
		# test the description
		
		project_description = self.e('textarea')
		project_description.clear()
		project_description.send_keys('Lorem Ipsum is simply dummy text of the printing and typesetting industry.')
		sleep(3)
		# self.assertIn('Lorem Ipsum is simply dummy text of the printing and typesetting industry.', project_description.text) assertion should be made when the project is saved
		
		# testing sidebar
		org_name = self.e('#org-name')
		org_name.clear()
		org_name.send_keys('Test Organisation')
		
		# check google link, add a facebook one, then remove it
		
		links_section = self.e('.edit-links')
		google_option = links_section.e('select option:nth-of-type(5)')
		self.assertTrue(google_option.is_selected())
		
		self.assertEqual('http://www.google.com/', links_section.e('.input-holder input').get_attribute('value'))
		
		links_section.e('.add').click()
		
		link_type2 = self.e('.link-cnt:nth-of-type(2)')
		link_type2.e('select option:nth-of-type(2)').click()
		
		link_type2.e('.remove').click()
		sleep(3)
		
		# admin test
		admins_section = self.e('.edit-admins')
		admin_add = admins_section.e('.add')
		self.assertEqual('Add another project leader', admin_add.text)
		admin_add.click()
		
		self.e('.search-user').send_keys('as')
		sleep(2)
		self.e('.admin-cnt:last-of-type .remove').click()
		
		sleep(2)
		# self.assertEqual('Are you sure you want to remove as as a project administrator?', self.e('#ui-id-4 .ng-binding').text)
		self.e('.ui-dialog-buttonset button:nth-of-type(2)').click()
		
		sleep(4)
		self.assertEqual(len(admins_section.es('select')), 7)
		
		self.assertEqual('Malaysia', self.e('#search-location').get_attribute('value'))
		
		self.e('#btn-explore').click()
	
	@url('/en/explore/oreo/')
	def test_add_project_card_not_logged_in(self):
		
		add_project_card = self.e('.add-project')
		login_dialog = self.e('.login-dialog')
		
		add_project_card.click()
		
		self.assertTrue(login_dialog.is_displayed())
		self.e('.close-btn-wrapp a').click()
		sleep(2)
		self.assertFalse(login_dialog.is_displayed(), WebElement)
		
	
	@logged_in
	@url('/en/explore/oreo/')
	def test_add_project_card_logged_in(self):
		
		add_project_card = self.e('.add-project')
		add_project_card.click()
		
		self.assertEqual('{0}{1}/project/create/'.format(URL_BASE, self.PROJECT_URL), self.browser.current_url)
		self.assertIsInstance(self.e('#button_save'), WebElement)
	
	@url('/en/explore/oreo/')
	def test_add_pin_not_logged_in(self):
		
		add_pin_card = self.e('.add-first-pin')
		login_dialog = self.e('.login-dialog')
		
		add_pin_card.click()
		
		self.assertTrue(login_dialog.is_displayed())
		self.e('.close-btn-wrapp a').click()
		sleep(2)
		self.assertFalse(login_dialog.is_displayed(), WebElement)
		
	
	@logged_in
	@url('/en/explore/oreo/')
	def test_add_pin_card_logged_in(self):
		pass
	
	@logged_in
	@url('/en/explore/oreo/')
	def test_project_name_length(self):
		# this test will pass only on v614-beta-1!!!!
		
		self.e('.add-project').click()
		sleep(2)
		
		project_title = self.e('h3 .project-title')
		project_title.send_keys('oreo')
		
		self.e('#button_save').click()
		
		error_message = self.e('.error.error-title')
		self.assertIsInstance(error_message, WebElement)
		sleep(2)
		self.assertEqual('Title must be atleast 6 characters long.', error_message.text)
	
	@unittest.skipIf(IS_LIVE, 'Do not run on live')
	@logged_in
	@url('/en/explore/oreo/')
	def _project_name_reserved_words(self):
		
		reserved_words = [
				'about', 'access', 'account', 'accounts', 'add', 'address', 'adm', 'admin', 'administration', 'adult', 'advertising', 'affiliate', 'affiliates', 'ajax', 'analytics', 'android', 'anon', 'anonymous', 'api', 'app', 'apps', 'archive', 'atom', 'auth', 'authentication', 'avatar',
				'backup', 'banner', 'banners', 'bin', 'billing', 'blog', 'blogs', 'board', 'bot', 'bots', 'business',
				'chat', 'cache', 'cadastro', 'calendar', 'campaign', 'careers', 'cgi', 'client', 'cliente', 'code', 'comercial', 'compare', 'config', 'connect', 'contact', 'contest', 'create', 'code', 'compras', 'css',
				'dashboard', 'data', 'db', 'design', 'delete', 'demo', 'design', 'designer', 'dev', 'devel', 'dir', 'directory', 'doc', 'docs', 'domain', 'download', 'downloads',
				'edit', 'editor', 'email', 'ecommerce',
				'forum', 'forums', 'faq', 'favorite', 'feed', 'feedback', 'flog', 'follow', 'file', 'files', 'free', 'ftp',
				'gadget', 'gadgets', 'games', 'guest', 'group', 'groups',
				'help', 'home', 'homepage', 'host', 'hosting', 'hostname', 'html', 'http', 'httpd', 'https', 'hpg',
				'info', 'information', 'image', 'img', 'images', 'imap', 'index', 'invite', 'intranet', 'indice', 'ipad', 'iphone', 'irc',
				'java', 'javascript', 'job', "job's", 'js',
				'knowledgebase',
				'log', 'login', 'logs', 'logout', 'list', 'lists',
				'mail', 'mail1', 'mail2', 'mail3', 'mail4', 'mail5', 'mailer', 'mailing', 'mx', 'manager', 'marketing', 'master', 'me', 'media', 'message', 'microblog', 'microblogs', 'mine', 'mp3', 'msg', 'msn', 'mysql', 'messenger', 'mob', 'mobile', 'movie', 'movies', 'music', 'musicas', 'my',
				'name', 'named', 'net', 'network', 'new', 'news', 'newsletter', 'nick', 'nickname', 'notes', 'noticias', 'ns', 'ns1', 'ns2', 'ns3', 'ns4',
				'old', 'online', 'operator', 'order', 'orders',
				'page', 'pager', 'pages', 'panel', 'password', 'perl', 'pic', 'pics', 'photo', 'photos', 'photoalbum', 'php', 'plugin', 'plugins', 'pop', 'pop3', 'post', 'postmaster', 'postfix', 'posts', 'profile', 'project', 'projects', 'promo', 'pub', 'public', 'python',
				'random', 'register', 'registration', 'root', 'ruby', 'rss',
				'sale', 'sales', 'sample', 'samples', 'script', 'scripts', 'secure', 'send', 'service', 'shop', 'sql', 'signup', 'signin', 'search', 'security', 'settings', 'setting', 'setup', 'site', 'sites', 'sitemap', 'smtp', 'soporte', 'ssh', 'stage', 'staging', 'start', 'subscribe', 'subdomain', 'suporte', 'support', 'stat', 'static', 'stats', 'status', 'store', 'stores', 'system',
				'tablet', 'tablets', 'tech', 'telnet', 'test', 'test1', 'test2', 'test3', 'teste', 'tests', 'theme', 'themes', 'tmp', 'todo', 'task', 'tasks', 'tools', 'tv', 'talk',
				'update', 'upload', 'url', 'user', 'username', 'usuario', 'usage',
				'vendas', 'video', 'videos', 'visitor',
				'win', 'ww', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'www6', 'www7', 'wwww', 'wws', 'wwws', 'web', 'webmail',
				'website', 'websites', 'webmaster', 'workshop',
				'xxx', 'xpg',
				'you', 'yourname', 'yourusername', 'yoursite', 'yourdomain',
		]
		
		sleep(2)
		add_project_card	= self.e('.add-project')
		add_project_card.click()
		
		for n in range(len(reserved_words)):
			sleep(2)
			project_title = self.e('h3 .project-title')
			project_title.send_keys(reserved_words[n])
			sleep(2)
			self.e('#button_save').click()
			error_message = self.e('.error.error-title')
			self.assertIsInstance(error_message, WebElement)
			project_title.clear()
		# DO NOT DELETE THIS TEST!!!
	
	#@url('/en/explore/oreo')
	#, def test_expand_collapse_banner(self):
		
	# 	self.assertTrue(self.e('.project-admins').is_displayed())
		
	# 	banner_wrapper = self.e('.banner-top-wrapper')
	# 	banner_wrapper.click()
		
	# 	sleep(4)
	# 	self.assertFalse(self.e('.project-admins').is_displayed())
	
	# @url('/en/explore/oreo')
	# def test_hidden_header_on_smaller_screens(self):
		
	# 	sleep(3)  # the header element cannot be found without the sleep
		
	# 	self.assertTrue(self.e('#header').is_displayed())
		
	# 	self.browser.set_window_size(1024, 750)
	# 	sleep(3)
		
	# 	self.assertFalse(self.e('#header').is_displayed())
		
	# @url('/en/explore/oreo/pin/225260')
	# def test_hidden_views_on_smaller_screens(self):
		
	# 	self.assertEqual(u'\u23ea \u23e9 Sofia at night', self.e('.row h1').text)
	# 	self.assertTrue(self.e('.views').is_displayed())
		
	# 	self.browser.set_window_size(1024, 750)
		
	# 	self.assertFalse(self.e('.views').is_displayed())
	
	# @url('/en/explore/oreo/pin/225260')
	# def test_hidden_timeline_on_smaller_screens(self):
		
	# 	sleep(3)  # the timeline element cannot be found without the sleep
	# 	self.assertTrue(self.e('#timeline').is_displayed())
	# 	self.assertEqual('18 September 2006', self.e('.tooltip.arrow-down').text)
		
	# 	self.browser.set_window_size(1024, 750)
		
	# 	self.assertFalse(self.e('#timeline').is_displayed())
	
	# @url('/en/explore/oreo/')
	# def test_hidden_project_image_on_smaller_screens(self):
		
	# 	self.assertTrue(self.e('.panel img').is_displayed())
		
	# 	self.browser.set_window_size(1024, 750)
		
	# 	self.assertFalse(self.e('.panel img').is_displayed())
	
	# @url('/en/explore/oreo/pin/225260')
	# def test_hidden_comments_info_on_smaller_screens(self):
		
	# 	info_bookmarks = self.e('.bookmarks')
	# 	self.assertIsInstance(info_bookmarks, WebElement)
		
	# 	comment_section = self.e('.comment.add-comment')
	# 	self.assertIsInstance(comment_section, WebElement)
		
	# 	self.browser.set_window_size(1024, 750)
		
	# 	self.assertFalse(info_bookmarks.is_displayed())
	# 	self.assertFalse(comment_section.is_displayed())
	
	# @url('/en/explore/oreo')
	# def test_location_search(self):
		
	# 	self.e('#btn-explore').click()
		
	# 	search_input = self.e('#search-location')
		
	# 	search_input.send_keys('So')
	# 	sleep(4)
	# 	search_input.send_keys(u'\ue007')  # clicking enter in selenium
	# 	sleep(3)
		
	# 	location_coordinates = self.browser.current_url.split('/')[7].split(',')
		
	# 	self.assertEqual('Sofia, Bulgaria', search_input.get_attribute('value'))
		
	# 	self.assertIn('42.695501', location_coordinates[0])  # asserting the correct location
	# 	self.assertIn('23.323947', location_coordinates[1])
		
	
	# @url('/en/explore/oreo')
	# def test_find_location(self):
		
	# 	sleep(3)
	# 	self.e('#btn-explore').click()
		
	# 	sleep(4)
	# 	search_location_button = self.e('.find-my-location')
		
	# 	search_location_button.click()
		
		
	# 	# TODO make this test
