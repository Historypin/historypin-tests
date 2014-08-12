# -*- coding: utf-8 -*-

from base import *
import os, sys

class V6_Cases(HPTestCase):
	
	PROJECT_URL = '/en/explore/oreo'
	
	@url('/en/explore/oreo')
	def test_header_not_logged_in(self):
		
		self.assertTitle('Historypin')
		
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
			['Sign in with Google'	, '/user/login/?from=%s/' % self.PROJECT_URL, 'ss-googleplus'],
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
		
		header			= self.e('#header')
		breadcrumbs		= header.e('.breadcrumbs')
		breadcrumbs_li	= breadcrumbs.es('li a')
		banner			= self.e('#banner')
		project_heading	= banner.e('h3')
		
		self.assertEqual('%s%s/' % (URL_BASE, self.PROJECT_URL), breadcrumbs_li[0].get_attribute('href'))
		self.assertEqual(breadcrumbs_li[0].text, project_heading.text)  # check if the breadcrumb is equal to project heading
		
		banner.e('.edit-project').click()
		sleep(4)
		self.e('#banner-form .edit-heading').clear()
		self.e('#banner-form .edit-heading').send_keys('Quality Assurance')  # send keys with different title
		
		banner.e('.save-project').click()  # save the change title
		
		sleep(2)
		self.browser.refresh()  # refresh the page with the new title
		
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
		
		timeline = self.e('#timeline')
		self.assertEqual('2002', timeline.e('.ui-state-default.ui-corner-all:nth-of-type(1)').text)
		self.assertEqual('2010', timeline.e('.ui-state-default.ui-corner-all:nth-of-type(2)').text)
		
		# TODO
		# click a pin on the map to check, if it is in the date range
		
	
	@url('/en/explore/oreo/pin/225263')
	def test_youtube_audio_pin(self):
		
		timeline = self.e('#timeline')
		self.assertEqual('2 January 2012', timeline.e('.tooltip.arrow-down').text)
		
		self.assertEqual('Sound in Sofia', self.e('#pin h1').text)
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
		self.assertEqual('%s/upload-audio/pin/phid/225263/edit/1/?from=/en/explore/oreo/pin/225263' % URL_BASE, edit_icon.get_attribute('href'))
		self.assertEqual('Edit', edit_icon.text)
		
		edit_icon.click()
		
		sleep(3)
		
		self.e('#photo_pin').click()
		
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
		
		self.assertEqual('Bulgarian Army Theater', self.e('#explore h1').text)
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
		
		h4s		= ['DESCRIPTION', 'TAGS', 'INFORMATION', 'CREATOR', 'ADD A COMMENT', 'COMMENTS (3)']
		h4s_cnt	= column_3b.es('h4')
		for n in range(len(h4s)): self.assertEqual(h4s[n], h4s_cnt[n].text)
		
		self.assertEqual('This is a photo of the famous Bulgarian Army Theater', self.e('#pin .description p:nth-of-type(1)').text)
		
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
		self.assertEqual('Title Text Pin1', column_row.e('h1').text)
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
		
		self.assertEqual('%s/channels/view/%d/' % (URL_BASE, ID_USER_VIEW), banner.e('.channel-link').get_attribute('href'))
		self.assertEqual('Gabss', banner.e('.channel-link span').text)
		
		sleep(3)
		self.assertEqual('%s/projects/img/pid/30/type/project_image,banner,logo/dim/1920x450/crop/1/' % URL_BASE, self.e('.panel > img').get_attribute('src'))
		self.assertIn('Lorem Ipsum is simply dummy text of the printing and typesetting industry.', self.e('.description.inner p').text)
		
		project_sidebar	= self.e('.sidebar')
		h4s				= project_sidebar.es('h4')
		
		self.assertEqual('LEADERS'		, h4s[0].text)
		self.assertEqual('RELATED LINKS', h4s[1].text)
		self.assertEqual('MAIN LOCATION', h4s[2].text)
		
		admins_cnt = [
			['/49127/'	, '/channels/img/49127/logo/1/dim/50x50/crop/1/', 'Rawr'				, 'Project Admin'],
			['/33283/'	, '/channels/img/33283/logo/1/dim/50x50/crop/1/', 'Gabss'				, 'Project Admin'],
			['/867/'	, '/channels/img/867/logo/1/dim/50x50/crop/1/'	, 'Karamfil'			, 'Project Admin'],
			['/47515/'	, '/resources/explore/images/default-avatar.jpg', 'n.p.slavov'			, 'Project Admin'],
			['/35019/'	, '/resources/explore/images/default-avatar.jpg', 'Gabriela Ananieva'	, 'Project Admin'],
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
		self.assertEqual('g.k. Nadezhda 1, Sofia, Bulgaria', location.e('p').text)
		self.assertIsInstance(location.e('.small-map'), WebElement)
		
		banner.e('#btn-explore').click()
	
	@logged_in
	@url('/en/explore/oreo')
	def test_edit_project(self):
		
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
		self.assertEqual(len(admins_section.es('select')), 6)
		
		self.assertEqual('g.k. Nadezhda 1, Sofia, Bulgaria', self.e('#search-location').get_attribute('value'))
		
		self.e('#btn-explore').click()
	
	@url('/en/explore/1989')
	def test_project(self):
		
		self.assertTitle('Historypin')
		
		banner = self.e('#banner')
		self.assertEqual('Europeana 1989', banner.e('h3').text)
		
		timeline = self.e('#timeline')
		self.assertEqual('1930', timeline.e('.start').text)
		
		self.assertEqual('2013', timeline.e('.end').text)
		self.assertIsInstance(timeline.e('.ui-slider-range'), WebElement)
		
		# if not self.e('.panel.expanded').is_displayed():
		# 	banner.e('.home-anchor').click()
		
		sleep(4)
		self.assertEqual(URL_BASE + '/projects/img/pid/34/type/project_image,banner,logo/dim/1920x450/crop/1/', banner.e('img').get_attribute('src'))
		
		self.assertEqual('Mirrorpix Archives', banner.e('.channel-link span').text)
		self.assertEqual('Europeana 1989: We Made History', banner.e('.description strong').text)
		self.assertIn(u'The way history is recorded isn’t just about what museums and institutions think is important', banner.e('.description').text)
		
		share_toolbox	= self.e('.social-container')
		share_items		= share_toolbox.es('li')
		
		self.hover(share_toolbox)
		self.assertIsInstance(share_items[0], WebElement)
		self.assertIsInstance(share_items[1], WebElement)
		self.assertIsInstance(share_items[2], WebElement)
		self.assertIsInstance(share_items[3], WebElement)
		self.assertIsInstance(share_items[4], WebElement)
		
		self.assertEqual('Explore the map', self.e('#btn-explore').text)
		self.e('#btn-explore').click()
	
	@unittest.skipIf('v68-beta' in URL_BASE, "this is made on v69-beta")
	@url('/en/explore/oreo')
	def test_expand_collapse_banner(self):
		
		self.assertTrue(self.e('.project-admins').is_displayed())
		
		banner_wrapper = self.e('.banner-top-wrapper')
		banner_wrapper.click()
		
		sleep(4)
		self.assertFalse(self.e('.project-admins').is_displayed())
	
	@unittest.skipIf('v68' in URL_BASE, "this is made on v69-beta")
	@url('/en/explore/oreo')
	def test_hidden_header_on_smaller_screens(self):
		
		self.assertTrue(self.e('#header').is_displayed())
		
		self.browser.set_window_size(1024, 750)
		sleep(3)
		
		self.assertFalse(self.e('#header').is_displayed())
		
	@unittest.skipIf('v68' in URL_BASE, "this is made on v69-beta")
	@url('/en/explore/oreo/pin/225260')
	def test_hidden_views_on_smaller_screens(self):
		
		self.assertEqual('Sofia at night', self.e('.row h1').text)
		self.assertTrue(self.e('.views').is_displayed())
		
		self.browser.set_window_size(1024, 750)
		
		self.assertFalse(self.e('.views').is_displayed())
	
	@unittest.skipIf('v68' in URL_BASE, "this is made on v69-beta")
	@url('/en/explore/oreo/pin/225260')
	def test_hidden_timeline_on_smaller_screens(self):
		
		self.assertTrue(self.e('#timeline').is_displayed())
		self.assertEqual('18 September 2006', self.e('.tooltip.arrow-down').text)
		
		self.browser.set_window_size(1024, 750)
		
		self.assertFalse(self.e('#timeline').is_displayed())
	
	@unittest.skipIf('v68' in URL_BASE, "this is made on v69-beta")
	@url('/en/explore/oreo/')
	def test_hidden_project_image_on_smaller_screens(self):
		
		self.assertTrue(self.e('.panel img').is_displayed())
		
		self.browser.set_window_size(1024, 750)
		
		self.assertFalse(self.e('.panel img').is_displayed())
	
	@unittest.skipIf('v68' in URL_BASE, "this is made on v69-beta")
	@url('/en/explore/oreo/pin/225260')
	def test_hidden_comments_info_on_smaller_screens(self):
		
		info_bookmarks = self.e('.bookmarks')
		self.assertIsInstance(info_bookmarks, WebElement)
		
		comment_section = self.e('.comment.add-comment')
		self.assertIsInstance(comment_section, WebElement)
		
		self.browser.set_window_size(1024, 750)
		
		self.assertFalse(info_bookmarks.is_displayed())
		self.assertFalse(comment_section.is_displayed())
	
	@url('/en/explore/oreo')
	def test_map_credits(self):
		# TODO to be tested
		pass

