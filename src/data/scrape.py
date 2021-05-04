from bs4 import BeautifulSoup
import requests
from datetime import datetime
import csv


def scrape(page_num):
    make = {"Honda": 20017}
    model = {"Civic": 20823}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

    url = ('https://www.cars.com/for-sale/searchresults.action/?&zc=95123&rd=30&stkTypId=28881&mkId=20017&mdId=20823&page={}&perPage=100&searchSource=RESEARCH_SHOP_INDEX').format(page_num)
    print(url)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')

    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        listings = soup.find_all(
            "div", {"class": "shop-srp-listings__listing-container"})

        for listing in listings:
            title = listing.find(
                "h2", {"class": "listing-row__title"}).get_text().strip()
            price = listing.find(
                "span", {"class": "listing-row__price"}).get_text().strip()
            mileage = listing.find(
                "span", {"class": "listing-row__mileage"}).get_text().strip()
            condition = listing.find(
                "div", {"class": "listing-row__stocktype"}).get_text().strip()
            specifications = listing.find(
                "ul", {"class": "listing-row__meta"}).get_text().strip()
            print(condition + ", " + str(title) + ", " + mileage +
                  ", " + str(price) + "," + str(datetime.now()))
            writer.writerows([str(condition), str(
                title), str(mileage), str(price)])

    pagination = soup.find("a", {"class": "button next-page"})
    print(pagination)
    print(type(pagination))
    if not pagination.has_attr('data-page'):
        print("no next page")
    else:
        page_num += 1
        scrape(page_num)


scrape(1)
