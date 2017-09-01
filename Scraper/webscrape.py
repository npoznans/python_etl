from bs4 import BeautifulSoup as soup
import requests as req
import csv

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=video%20cards'

uClient = req.get(my_url)

page_html = uClient.text
uClient.close()

html_soup = soup(page_html, "html.parser")

containers = html_soup.findAll("div", {"class" : "item-container"})

filename = "products.csv"
f = open(filename, "w")
headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers:
    brand = container.div.div.a.img["title"]
    
    title_container = container.findAll("a", {"class":"item-title"})
    title = title_container[0].text
    
    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    f.write(brand + "," + title.replace(",","|") + "," + shipping + "\n")
    print(brand + "," + title.replace(",","|") + "," + shipping + "\n")

    
print(len(containers))

