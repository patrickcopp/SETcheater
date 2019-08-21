#author: Patrick Copp
import time
from selenium import webdriver 
import itertools
hi=[i for i in range(1,13)]
hi=itertools.combinations(hi,3)
url = 'https://www.setgame.com/set/puzzle'
driver = webdriver.Chrome()
driver.get(url)
for each in hi:
	for each2 in each:
		driver.execute_script("board.cardClicked("+str(each2)+");")
	time.sleep(0)
time.sleep(60)
driver.quit()
