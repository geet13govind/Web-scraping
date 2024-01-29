from selenium import webdriver as wb
from selenium.webdriver.common.by import By
import time

cService = wb.ChromeService(executable_path = 'C:\\Users\\Dell\\Downloads\\chromedriver-win64\\chromedriver.exe')
driver = wb.Chrome(service=cService)
driver.get('https://www.python.org/')
time.sleep(3)
Latest_news = []
for i in range(1,6):
    Latest_news.append(driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[1]/div/ul/li[{}]'.format(i)).text)

Latest_article = []
for i in Latest_news:
    Latest_article.append(i.split('\n')[1])

print('\nLatest Articles in Python section are: \n')
print('\n'.join(Latest_article))
file = open('New_articles_own_way.txt','w',encoding='utf-8')
file.write('Latest Articles in Python section are: \n\n')
file.write('\n'.join(Latest_article))
file.close()
print('\nThe file is saved in : New_articles_new_way.txt\n')