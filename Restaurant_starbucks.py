# Crawl Restaurant(Fast Food Chains) Dataset from the Web
# Student of Python Intermediate Online Class / Summer 2023
# Version 1.1

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import csv

starbucksUrl = 'https://www.starbucks.de/store-locator?types=starbucks'
driver = webdriver.Chrome()
driver.get(starbucksUrl);
sleep(20)
inputFormula = driver.find_element("id", "address")
inputFormula.send_keys('Munich, Deutschland')
inputFormula.send_keys(Keys.ENTER)
sleep(2)
resultList = driver.find_elements(By.CLASS_NAME, "store-list-item")
resultSize = len(resultList)
iterations = int(resultSize / 2)

results = [] #List of all Starbucks addresses.

for i in range(0, iterations):
    # Click info Button
    infoBtn = resultList[i].find_element(By.CLASS_NAME, "abstract-button")
    driver.execute_script("arguments[0].click();", infoBtn)
    sleep(1)
    # get & print address div
    getStoreAddress = driver.find_elements(By.CLASS_NAME, "store-details-address")
    # print(getStoreAddress[0].get_attribute('innerHTML'))
    results.append(getStoreAddress[0].get_attribute('innerHTML'))
    # Click exit button
    exitDiv = driver.find_elements(By.CLASS_NAME, "store-finder-store-header")
    exitBtn = exitDiv[0].find_elements(By.CLASS_NAME, "abstract-button")
    exitBtn[0].get_attribute('innerHTML')
    sleep(1)
    # search again
    inputFormula = driver.find_element("id", "address")
    inputFormula.send_keys('Munich, Deutschland')
    inputFormula.send_keys(Keys.ENTER)
    sleep(1)
    resultList = driver.find_elements(By.CLASS_NAME, "store-list-item")
    sleep(1)

driver.close()

with open('Restaurants.csv', mode='a', newline='') as outputFile:
    restaurantCSV = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # restaurantCSV.writerow(['restaurant', 'street', 'zip', 'city', 'country'])
    restaurantName = 'Starbucks'
    country = 'Germany'
    for restaurant in results:
        street = restaurant.split("\n")[0]
        zipCode = restaurant.split("\n")[1][0:5]
        city = restaurant.split("\n")[1][6:]
        restaurantCSV.writerow([restaurantName, street, zipCode, city, country])

