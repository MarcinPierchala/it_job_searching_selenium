from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.pracuj.pl/")

time.sleep(2)

accept_all = driver.find_element_by_xpath('//*[@id="gp-cookie-agreements"]/div/div/div[1]/div[3]/button').click()

time.sleep(2)

click_ok = driver.find_element_by_xpath("/html/body/div[1]/div/header/div[4]/button[2]").click()

time.sleep(1)

driver.maximize_window()

search_it_jobs = driver.find_element_by_xpath("/html/body/div[1]/div/header/div[2]/div[1]/menu/ul/li[3]/a/span").click()

time.sleep(2)

remote_select = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div[1]/div/div[2]/form/div[1]/div[2]/label/span[1]').click()

time.sleep(1)

python_select = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div[1]/div/div[2]/form/div[3]/div[2]/ul/li[13]/label/span').click()

time.sleep(1)

junior_select = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div[1]/div/div[2]/form/div[5]/div[2]/ul/li[3]/label/span').click()

#now i`m looking for a job :-)