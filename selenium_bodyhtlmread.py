from bs4 import BeautifulSoup
import requests
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())


input()


     
link = "https://www.hackerrank.com/contests/python38-04/leaderboard"
driver.get(link)
input()
page_source = driver.page_source

soup = BeautifulSoup(leaderboardPage, 'html.parser')

a_tags = soup.findAll("a", class_="cursor leaderboard-hackername rg_5")



