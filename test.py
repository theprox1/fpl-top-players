from selenium import webdriver
import time
from credentials import password
driver = webdriver.Firefox()
page = driver.get('https://fantasy.premierleague.com/my-team')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginUsername"]').send_keys('kismat353@gmail.com')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginPassword"]').send_keys(password)
time.sleep(2)
driver.find_element_by_xpath('/html/body/main/div/div[2]/div/div/div[1]/form/div[3]/button').click()

time.sleep(2)
driver.find_element_by_xpath('/html/body/main/div/div[1]/div/div/div/nav/ul/li[1]/a').click()
time.sleep(2)
most_bought_players= []
most_sold_players = []
for player in driver.find_elements_by_xpath('/html/body/main/div/div[2]/div/div[2]/div[4]/div[1]/div/div[1]/div[2]/table/tbody/tr'):
    name = player.find_element_by_xpath('.//div[@class="Utils__Ellipsis-sc-1cvr1yj-0 eKfnwF"]').text
    most_bought_players.append({'name':name})

for player in driver.find_elements_by_xpath('/html/body/main/div/div[2]/div/div[2]/div[4]/div[2]/div/div[1]/div[2]/table/tbody/tr'):
    name = player.find_element_by_xpath('.//div[@class="Utils__Ellipsis-sc-1cvr1yj-0 eKfnwF"]').text
    most_sold_players.append({'name':name})

with open('fpl.txt','w') as file:
    i = 1
    file.write('Most Bought Players : \n')
    for player in most_bought_players:
        values = list(player.values())
        file.write(f'{i}. {values[0]} \n')
        i += 1
    file.write('\n \n')
    file.write('Most Sold Players : \n')
    i = 1
    for player in most_sold_players:
        values = list(player.values())
        file.write(f'{i}. {values[0]} \n')
        i += 1

driver.close()