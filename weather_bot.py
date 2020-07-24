# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 17:43:54 2020

@author: jason
"""

# This program will record weather forecast data for a entered location. 


# Import libraries to web scrape weather data
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

'''
    
'''
def openUrequest(url):
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    return page_soup
            
def writeDataToFile(soup):
    
    file = open("WeatherData.csv", "a")
    dataArr = pullDataFromHTML(soup)
    file.write(dataArr)
    file.close()
    

def pullDataFromHTML(soup):
    
    dataString = ''
    dataString += getCurTemp(soup) + ', '
    dataString += getFeelsLike(soup)
    
    
    return dataString
    
def getCurTemp(page_soup):
    return (page_soup.find("font", {"class": "currenttemp_font"}).text.replace("&#176", " degrees "))

def getFeelsLike(page_soup):
    print(page_soup.body.findAll(text='Feels Like:'))
    return (page_soup.body.findAll(text='Feels Like:'))


# User Input Validation via try catch 

while True:
    try:
        # Have user enter the City, State, and Zip 
        reqForecast = input("Please enter the city, abbreviated state and Zip Code in CSV Format: ")
        storeLocation = input("Would you like to store this location, and get updates every 24 hours? (Y/N): ")
        
        # Verify fields
        queryParams = reqForecast.split(",")
        if(queryParams[2]):
            if(int(queryParams[2]) < 0):
                if(storeLocation == "Y"):
                    runCronTab = True

                else:
                    runCronTab = False
                
        break
        
    except ValueError:
        print("Oops! That was no valid location. Try again...")


# Construct URL to perform webscraping from given user input
base_url = 'https://weatherstreet.com/weather-forecast/'
my_url = base_url
for param in queryParams:
    my_url += param.replace(" ", "-")
    
my_url += '.htm'
reqGood = False

while True:
    try:
        # create a copy of the webpage in question
        soup = openUrequest(my_url)   
        writeDataToFile(soup)
        break
    except IOError:
        print("Aborting, forecast for entered location not found. Please re-run program and try again.")
        break
        

        

    

