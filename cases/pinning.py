# -*- coding: utf-8 -*-

from base import *
import os, sys

class Pinning(HPTestCase):
	
	@logged_in
	@url('/upload/')
	def test_add_stuff_page(self):
		
		steps = ['Choose stuff to add', 'Add Something', 'Pin it to the map', 'All done']
		
		texts = self.es('.progress-bar li')
		
		for n in range(len(steps)): self.assertEqual(steps[n], texts[n].text)
		
		container = self.e('#container')
		self.assertEqual('Choose at least one project', container.e('h2').text)
		self.assertIsInstance(container.e('.project'), WebElement)
		
		container.e('.submit').click()
		sleep(3)
		
		cnt_upload = self.e('.upload-content')
		self.assertEqual('I want to add', cnt_upload.e('h2').text)
		
		photo_type = self.e('.upload-type li .photos')
		self.assertEqual('Photos', photo_type.text)
		self.assertEqual('{0}/upload-item/index/selected_projects/1/'.format(URL_BASE), photo_type.get_attribute('href'))
		self.assertIn('ss-icon'		, photo_type.e('span').get_attribute('class'))
		self.assertIn('ss-picture'	, photo_type.e('span').get_attribute('class'))
		
		video_type = self.e('.upload-type li .videos')
		self.assertEqual('Video', video_type.text)
		self.assertEqual('{0}/upload-video/index/selected_projects/1/'.format(URL_BASE), video_type.get_attribute('href'))
		self.assertIn('ss-icon'		, video_type.e('span').get_attribute('class'))
		self.assertIn('ss-video'	, video_type.e('span').get_attribute('class'))
		
		audio_type = self.e('.upload-type li .audio')
		self.assertEqual('Audio', audio_type.text)
		self.assertEqual('{0}/upload-audio/index/selected_projects/1/'.format(URL_BASE), audio_type.get_attribute('href'))
		self.assertIn('ss-icon'			, audio_type.e('span').get_attribute('class'))
		self.assertIn('ss-headphones'	, audio_type.e('span').get_attribute('class'))
		
		self.assertEqual('Want to upload large amounts of content? Read about our Bulk Uploader', self.e('.bottom-p').text)
		self.assertEqual('{0}/bulkbridge/'.format(URL_BASE), self.e('.bottom-p a').get_attribute('href'))
	
	@logged_in
	@url('/upload-item/index/')
	def test_upload_photo_page(self):
		
		cnt_upload = self.e('.upload-content')
		self.assertEqual('Upload a photo', cnt_upload.e('h2').text)
		self.assertIsInstance(self.e('.fileinput-button'), WebElement)
		self.assertIsInstance(self.e('.delete.ui-button'), WebElement)
		
		cnt = self.e('.dropzone-container')
		self.assertEqual('Drag your images here to add them. They will upload automatically.', cnt.e('h3').text)
		self.assertEqual('Pssst. JPG and PNG files up to 5 megabytes only please.', cnt.e('h5').text)
		
		self.assertEqual('Are you an archive and want to upload large amounts of content? Try our Bulk Uploader for Firefox and Chrome.', self.e('.bottom-p').text)
		self.assertEqual('{0}/bulkbridge/'.format(URL_BASE), self.e('.bottom-p a').get_attribute('href'))
	
	
	@unittest.expectedFailure
	@logged_in
	@url('/upload-item/index/')
	def test_upload_photo(self):
		
		# TODO fix this - cannot select the element which has focus
		upload_photo = self.e('.fileinput-button.ui-button.ui-widget')
		upload_photo.send_keys(os.getcwd()+'/national-palace-of-culture.jpg')
		sleep(2)
		
	@unittest.skipIf(IS_LIVE, 'Do not run on live')
	@logged_in
	@url('/upload-video/index/')
	def test_upload_video(self):
		
		upload_cnt = self.e('.upload-content')
		upload_video = upload_cnt.e('#youtube_url')
		
		upload_video.send_keys('http://www.youtube.com/watch?v=8Qsl9vN4QQk')
		
		self.e('.form-submit').click()
		sleep(3)
		
		id_video = self.browser.current_url.split('/')[6]
		
		site_cnt = self.e('#edit_photo_page')
		self.assertIsInstance(site_cnt.e('#photo-preview'), WebElement)
		
		info	= site_cnt.e('.inner.left')
		title	= info.es('input')[0]
		desc	= info.e('textarea')
		tags	= info.es('input')[1]
		
		title.send_keys('Sofia (Bulgaria) - a modern European city')
		desc.send_keys('This is a video about Sofia')
		tags.send_keys('Sofia, video, Bulgaria')
		
		license	= site_cnt.e('.section.license')
		option	= license.e('#photo_info_license_type')
		option.click()
		option.e('option:nth-of-type(2)').click()
		
		date_select = site_cnt.e('.section.date-select')
		date_select.e('#day option:nth-of-type(10)').click()
		sleep(3)
		date_select.e('#month option:nth-of-type(9)').click()
		sleep(3)
		date_select.e('#year option:nth-of-type(4)').click()
		sleep(3)
		
		location_search = site_cnt.e('#location-search-ui fieldset')
		location_search.e('#location').click()
		location_search.e('#location').clear()
		location_search.e('#location').send_keys('ulitsa "Georgi. S. Rakovski" 98, 1000 Sofia, Bulgaria')
		sleep(10)
		
		location_search.e('#location_search').click()
		
		site_cnt.e('#has_streetview').click()
		sleep(3)
		site_cnt.e('#pin-tab-sv a').click()
		
		self.assertIsInstance(self.e('#streetview-image-container img'), WebElement)
		
		button_save = self.e('#streetview-toolbar .right')
		self.assertEqual('Record Position', button_save.e('span').text)
		button_save.click()
		
		site_cnt.e('#agree_terms').click()
		
		site_cnt.e('#photo_pin').click()
		
		sleep(3)
		self.go('/attach/uid{0}/photos/list/'.format(ID_USER))
		
		img_holder	= self.e('#list li:nth-of-type(1) .image-holder')
		delete_icon	= img_holder.e('.delete-confirm')
		
		self.hover(img_holder)
		sleep(3)
		
		delete_icon.click()
		
		alert = self.browser.switch_to_alert()
		sleep(2)
		alert.accept()
		sleep(4)
		
		self.browser.refresh()
		self.assertFalse(self.e('#list').exists('.image[href*="%{0}]' .format(id_video)))
	
	@unittest.skipIf(IS_LIVE, 'Do not run on live')
	@logged_in
	@url('/upload-audio/index/')
	def test_upload_audio(self):
		
		upload_cnt = self.e('.upload-content')
		upload_audio = upload_cnt.e('#youtube_url')
		
		upload_audio.send_keys('http://www.youtube.com/watch?v=8Qsl9vN4QQk')
		
		self.e('.form-submit').click()
		sleep(3)
		
		id_audio = self.browser.current_url.split('/')[6]
		
		site_cnt = self.e('#edit_photo_page')
		self.assertIsInstance(site_cnt.e('#photo-preview'), WebElement)
		
		info	= site_cnt.e('.inner.left')
		title	= info.es('input')[0]
		desc	= info.e('textarea')
		tags	= info.es('input')[1]
		
		title.send_keys('Sofia (Bulgaria) - a modern European city')
		desc.send_keys('This is an audio about Sofia')
		tags.send_keys('Sofia, audio, Bulgaria')
		
		license	= site_cnt.e('.section.license')
		option	= license.e('#photo_info_license_type')
		option.click()
		option.e('option:nth-of-type(2)').click()
		
		date_select = site_cnt.e('.section.date-select')
		date_select.e('#day option:nth-of-type(15)').click()
		sleep(3)
		date_select.e('#month option:nth-of-type(10)').click()
		sleep(3)
		date_select.e('#year option:nth-of-type(6)').click()
		sleep(3)
		
		location_search = site_cnt.e('#location-search-ui fieldset')
		location_search.e('#location').click()
		location_search.e('#location').clear()
		location_search.e('#location').send_keys('ulitsa "Angel Kanchev" 13, 1000 Sofia, Bulgaria')
		sleep(10)
		
		location_search.e('#location_search').click()
		
		site_cnt.e('#agree_terms').click()
		
		site_cnt.e('#photo_pin').click()
		
		sleep(3)
		self.go('/attach/uid{0}/photos/list/'.format(ID_USER))
		
		img_holder	= self.e('#list li:nth-of-type(1) .image-holder')
		delete_icon	= img_holder.e('.delete-confirm')
		
		self.hover(img_holder)
		sleep(3)
		
		delete_icon.click()
		
		alert = self.browser.switch_to_alert()
		sleep(2)
		alert.accept()
		sleep(4)
		
		self.browser.refresh()
		self.assertFalse(self.e('#list').exists('.image[href*="{0}"]'.format(id_audio)))
