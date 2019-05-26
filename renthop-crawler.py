import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import re

# Initialize columns
B = []
C = []

# Define crawl function and crawl through url for max number of pages
def crawl(url, maxpage):
    count = 1
    while count < maxpage:
        print("Crawling: " + url + str(count))
        req = urllib.request.Request(url + str(count), headers={'User-Agent' : "Magic Browser"})
        con = urllib.request.urlopen(req)
        soup = BeautifulSoup(con, "html.parser")
        # Find the main div and extract correct neighboorhood data
        main_div = soup.find("div", {"class": "col-12 col-lg-8 pr-0 pr-lg-5 pr-xl-0"})
        neighborhood_div = main_div.findAll("div", {"id": re.compile("listing-.*")})
        # Append neighborhood values to column B
        for each in neighborhood_div:
            neighborhood = each.contents
            for item in neighborhood:
                item = item.strip()
                B.append(item)
        # Find price values and append to column C
        for row in main_div.findAll("tr"):
            cells = row.findAll("td", {"id": re.compile("listing.*")})
            for each in cells:
                price = each.contents
                for item in price:
                    item = item.strip()
                    C.append(item)
        # Increase the count and print data to csv
        count += 1
        df = pd.DataFrame(B, columns=["Neighborhood"])
        df["Price"] = C
        df.to_csv("data.csv")

crawl("https://www.renthop.com/boston-ma/apartments-for-rent?page=",100)
