import json
import requests

from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://www.thecarconnection.com"

carInfoList = []

def populateQueue():
    page = requests.get(URL + "/new-cars")

    soup = BeautifulSoup(page.content,'html.parser')
    results = soup.find_all('div', class_="menu-column")

    queue = []

    for column in results:
        for car in column.find_all('a', class_=""):
            # print(car['href'])
            queue.append(URL + car['href'])

    queue = list(set(queue))
    return queue

def scrapeNewMakePages(url):
    
    modelUrls = []

    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    cars = soup.find_all('div', class_=["item", "make"])

    for car in cars:
        info = car.find_all("div", class_="info")[0]
        carName = info.find("div", {"class":"name"})
        # print(URL+"/overview" + carName.find("a")['href'].replace("/cars", "") + "_2021")
        modelUrls.append(URL + carName.find("a")['href'])
        # print(URL + carName.find("a")['href'])
        # print(carName)
        
    return modelUrls


def scrapeModelYearUrls(url):
    modelYearUrls = set()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    years = soup.find_all("a", class_="btn")

    for modelYear in years: 
        if("/overview" not in modelYear['href']):
            continue
        print(URL + modelYear['href'].replace("/overview", "/specifications"))
        modelYearUrls.add(URL + modelYear['href'].replace("/overview", "/specifications"))

    return list(modelYearUrls)

def pullMSRP(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    titlestr = url.split('/')[-1]
    titlestr = titlestr.split('_')
    print(titlestr)

    make = titlestr[0]
    model = titlestr[1]
    year = titlestr[2]

    trimInfo = soup.find_all("li", class_=["style-select"])
    # trimTitle = trimInfo[0].text.replace("MSRP", "").strip()
    for i in trimInfo:
        i = i.text.strip()
        i = i.split("\n")
        # print(trimTitle + i)
        print(make, model, year, i[0], i[1])
        carInfoList.append({
            "year": year,
            "make": make, 
            "model": model,
            "trim": i[0],
            "MSRP": i[1]
        })


def main():
    queue = populateQueue()
    modelUrls = []
    modelYearUrls = []
    # print(queue)
    while queue != []:
        url = queue.pop(0)
        # if("/new," in url):
            # print(url)
        modelUrls.extend(scrapeNewMakePages(url))
    modelUrls.sort()
    while(modelUrls != []):
        modelUrl = modelUrls.pop(0)
        modelYearUrls.extend(scrapeModelYearUrls(modelUrl))
    # print(modelUrls)

    while(modelYearUrls != []):
        pullMSRP(modelYearUrls.pop(0))
    with open("carMSRP.json", "w") as outfile:
        json.dump(carInfoList, outfile, sort_keys=True, indent=4)



main()