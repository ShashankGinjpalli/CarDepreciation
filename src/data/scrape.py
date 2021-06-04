import csv
import time
import random
import requests

from bs4 import BeautifulSoup
from datetime import datetime

import listing_class
from db_processing import databaseConnector

db = databaseConnector()


def scrape_CarsdotCom(page_num, mk_index):
    make = {"Honda": 20017, "Hummer": 20018, "Infiniti": 20019,
            "Jeep": 20021, "Land Rover": 20024, "Lincoln": 20025,
            "Mercedes-Benz": 20028, "Rolls-Royce": 20037, "Subaru": 20041,
            "Volvo": 20044, "Alfa Romeo": 20047, "Audi": 20049, "Bentley": 20051,
            "Cadillac": 20052, "Chevrolet": 20053, "BMW": 20005, "Acura": 20001,
            "Ford": 20015, "Genesis": 35354491, "Hyundai": 20064, "Kia": 20068,
            "Lexus": 20070, "Volkswagen": 20089, "Toyota": 20089, "Porsche": 20081,
            "Nissan": 20077, "Doge": 20012, "Chrysler": 20008, "Tesla": 28263}
    make_ids = [20017, 20018, 20019, 20021, 20024, 20025, 20028, 20037,
                20041, 20044, 20047, 20049, 20051, 20052, 20053, 20005,
                20001, 20015, 20064, 20068, 20070, 20089, 20089, 20081,
                35354491, 20077, 20012, 20008, 28263]

    mk_ids = dict((v, k) for k, v in make.items())

    model = {"Civic": 20823}
    zipcode = 97208

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

    url = ('https://www.cars.com/for-sale/searchresults.action/?mkId={}&page={}&perPage=100&rd=50&searchSource=GN_BREADCRUMB&sort=relevance&stkTypId=28881&zc={}').format(
        make_ids[mk_index], page_num,zipcode)
    print(url)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    #print(soup)

    # scrape listings
    listings = soup.find_all(
        "div", {"class": "shop-srp-listings__listing-container"})

    for listing in listings:
        title = listing.find(
            "h2", {"class": "listing-row__title"}).get_text().strip()
        split = title.split(' ')
        year = split[0]
        title = ' '.join(title.split()[1:])
        price = listing.find(
            "span", {"class": "listing-row__price"}).get_text().strip()
        mileage = listing.find(
            "span", {"class": "listing-row__mileage"}).get_text().strip()
        condition = listing.find(
            "div", {"class": "listing-row__stocktype"}).get_text().strip()
        specifications = listing.find(
            "ul", {"class": "listing-row__meta"}).get_text().strip()

        specifications_ul = listing.find(
            "ul", {"class": "listing-row__meta"})

        specs = []
        for li in specifications_ul.find_all("li"):
            spec_string = li.get_text().strip()
            specs.append(li.get_text().strip(" "))

        #print(title)
        current_make = str(mk_ids[make_ids[mk_index]])
        title = title.replace(current_make, "")
        #print("Make: " + str(mk_ids[make_ids[mk_index]]))

        car_listing = listing_class.listing_obj(current_make,
                                                str(title), str(year), str(price), str(mileage), str(condition), str(specifications), datetime.now(), str(zipcode))
        db.upload_listing(car_listing)

    time.sleep(random.randint(0, 1))
    # pagination processing
    pagination = soup.find("a", {"class": "button next-page"})
    try:
        if not pagination.has_attr('data-page'):
            print("no next page")
            time.sleep(random.randint(0, 10))
            scrape_CarsdotCom(0, mk_index+1)
        else:
            page_num += 1
            scrape_CarsdotCom(page_num, mk_index)
    except Exception as e:
        print(e)
        time.sleep(random.randint(0, 10))
        try:
            scrape_CarsdotCom(0, mk_index+1)
        except Exception as e:
            if isinstance(e, IndexError):
                quit()
            else:
                print(e)



scrape_CarsdotCom(1, 0)
