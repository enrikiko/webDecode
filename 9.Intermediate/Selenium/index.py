if __name__ == '__main__':
    print("Web-auto-controlled. \n \n \n")

print("Setting the environment...")

#open the browser and set the url
url = 'https://www.linkedin.com/'
from password import email
from password import word
from function import *
browser.get(url)
browser.set_window_position(0, 0)
browser.set_window_size(1024, 512)
print("Environment setted.")
sleep(1)

#log In
print("Logging In...")
input = browser.find_element_by_id('login-email')
password = browser.find_element_by_id('login-password')
input.send_keys(email)
password.send_keys(word)
input.send_keys(Keys.ENTER)
print("Logged In")
# job_button = browser.find_element_by_id('jobs-tab-icon')
# job_button.click()
sleep(1)
messages=findElementById('messaging-tab-icon')
pulse(messages)
#
# #Go to jobs
# search_jobs = browser.find_elements_by_xpath("//input[@placeholder='Search jobs']")
# search_jobs[0].send_keys("python")
# search_location = browser.find_elements_by_xpath("//input[@placeholder='Search location']")
# search_location[0].send_keys("worldwide")
# search_location[0].send_keys(Keys.ENTER)
# sleep(5)
#
# #set last 24 hour
# post_date = browser.find_elements_by_class_name("search-s-facet__name-wrap--pill")
# post_date[0].click()
# click_date = browser.find_elements_by_class_name("search-s-facet-value")
# click_date[0].click()
# apply_date = browser.find_elements_by_xpath("//button[@data-control-name='filter_pill_apply']")
# apply_date[0].click()
# sleep(5)
#
# #set easyApply
# linkedin_features = browser.find_elements_by_class_name("search-s-facet__name-wrap--pill")
# linkedin_features[1].click()
# click_features = browser.find_elements_by_class_name("search-s-facet__value-label")
# click_features[4].click()
# apply_featuresl = browser.find_elements_by_xpath("//button[@data-control-name='filter_pill_apply']")
# apply_featuresl[1].click()
# sleep(5)
#
# #set Experience
# experience_level = browser.find_elements_by_class_name("search-s-facet__name-wrap--pill")
# experience_level[3].click()
# click_level = browser.find_elements_by_class_name("search-s-facet__value-label")
# click_level[12].click()
# click_level[13].click()
# apply_level = browser.find_elements_by_xpath("//button[@data-control-name='filter_pill_apply']")
# apply_level[3].click()
# sleep(5)
#
# #click in jobs
# # job_list = browser.find_elements_by_xpath("//div/")