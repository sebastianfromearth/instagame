#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# * gaming instagram followers *
# * follow/unfollow 8 accounts and like a bunch of photos from different tags every fifteen minutes for 9 hours

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

login_url = "https://www.instagram.com/"
username = raw_input("Username: ")
password = raw_input("Password: ")
url = login_url + username + "/"

driver = webdriver.Firefox()
driver.maximize_window()
driver.get(login_url)

wait = WebDriverWait(driver, 10)

#wait for spinner to disappear then login
login_link = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a._k6cv7")))
webdriver.ActionChains(driver).move_to_element(login_link).click(login_link).perform()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username']"))).send_keys(username)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']"))).send_keys(password)
login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button")))
webdriver.ActionChains(driver).move_to_element(login_button).click(login_button).perform()

#wait for login to complete
personal_account_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a._soakw" )))

times_to_repeat_counter = 1
for times_to_repeat_counter in range(1,40):
	account_to_follow_unfollow_counter = 1
	pictures_to_like = 1
	tags_to_explore = 1
	hashtag_list = ["travel", "europe", "explore", "igers", "holidays", "instadaily", "love", "food"]

	#navigate to profile
	driver.get(url)

	#click following button
	following_link = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._9o0bc li:nth-child(3) a._s53mj")))
	webdriver.ActionChains(driver).move_to_element(following_link).click(following_link).perform()

	for account_to_follow_unfollow_counter in range(1,9):
		string_counter = str(account_to_follow_unfollow_counter)
		#unfollow
		follow_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._539vh li:nth-child(%s) button._aj7mu" % string_counter )))
		webdriver.ActionChains(driver).move_to_element(follow_button).click(follow_button).perform()

		#wait till elements are clickable again
		element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '._539vh li:nth-child(%s) button._aj7mu' % string_counter )))

		#follow
		follow_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._539vh li:nth-child(%s) button._aj7mu" % string_counter)))
		webdriver.ActionChains(driver).move_to_element(follow_button).click(follow_button).perform()

		account_to_follow_unfollow_counter =+ 1

	#explore travel hashtags
	for tags_to_explore in range(1,9):
		driver.get("https://www.instagram.com/explore/tags/%s/" % hashtag_list[tags_to_explore - 1] )
		thumbnail_image = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._nljxa ._myci9 a._8mlbc" )))
		webdriver.ActionChains(driver).move_to_element(thumbnail_image).click(thumbnail_image).perform()

		for pictures_to_like in range(1,9):
			element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a._ebwb5" )))

			#like a pic
			like_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a._ebwb5" )))
			webdriver.ActionChains(driver).move_to_element(like_button).click(like_button).perform()

			element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a._de018" )))

			#nagivate to the next pic
			right_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a._de018" )))
			webdriver.ActionChains(driver).move_to_element(right_button).click(right_button).perform()

			pictures_to_like =+ 1

		tags_to_explore =+ 1

	times_to_repeat_counter += 1
	time.sleep(450)

	



