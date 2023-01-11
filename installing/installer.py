from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


driver = webdriver.Chrome()

driver.get('https://www.instagram.com/p/CnHMT9NKmVB/')
print("Sayfaya Erişildi.")
time.sleep(10)

print("Yorum bilgisi çekiliyor.")
time.sleep(2)

listString = ['/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/ul[%s]/div/li/div/div/div[2]/h3/div/a']
empty_List = []

k = 0
while k != 20:
    for a in listString:
        den = a % k
        comments_elements = driver.find_elements(By.XPATH, den)
        for b in comments_elements:
            print(k ,"-", b.text)
            empty_List.append(b.text)

    k = k + 1


print(empty_List)
print(random.choice(empty_List))


