from selenium import webdriver
#from selenium.webdriver.common.keys import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="G:\Gilbert's Documents\Selenium\Selenium 99 Location\chromedriver"
                                          ".exe")
# in Python /\ the path is only the chromedriver directly, not to the folder where the chromedriver is located.

driver.get("http://testing.todorvachev.com/selectors/name/")
time.sleep(5)
driver.maximize_window()
time.sleep(5)

driver.find_element_by_css_selector("#search-2 > form > label > input")
driver.find_element_by_css_selector("#search-2 > form > label > input").send_keys("ID")
time.sleep(5)
driver.find_element_by_id("cat")
driver.find_element_by_id("cat").click()
time.sleep(5)
driver.find_element_by_css_selector("#cat > option:nth-child(6)")
driver.find_element_by_css_selector("#cat > option:nth-child(6)").click()
time.sleep(5)
driver.find_element_by_css_selector("#main-content > article.mh-loop-item.mh-clearfix.post-74.post.type-post."
                                    "status-publish.format-standard.has-post-thumbnail.hentry.category-test-cases "
                                    "> div > header > h3 > a").click()
time.sleep(5)
driver.find_element_by_css_selector("#main-content > nav > div.mh-col-1-2.mh-"
                                    "post-nav-item.mh-post-nav-prev > a > img").click()
button = driver.find_element_by_name("userid")
driver.execute_script("arguments[0].scrollIntoView();", button)
time.sleep(5)
driver.find_element_by_name("userid").send_keys("Christopher")
time.sleep(2.3)
driver.find_element_by_name("passid").send_keys("password")
time.sleep(2.3)
driver.find_element_by_name("repeatpassid").send_keys("password")
time.sleep(2.4)
driver.find_element_by_name("submit").click()


