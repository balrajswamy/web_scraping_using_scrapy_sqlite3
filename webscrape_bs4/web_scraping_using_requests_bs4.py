import requests
from bs4 import BeautifulSoup
import csv


def web_scrape(URL, headers):

    res = requests.get(url=URL, headers=headers)
    #print(dir(res))
    page_source = res.content
    soup = BeautifulSoup(page_source,"html.parser")
    complete_data = []
    all_titles = soup.find_all("h3")
    price_elements = soup.find_all("p", {"class": "price_color"})
    base_url = "https://books.toscrape.com/"
    for title, price in  zip(all_titles,price_elements):
        book_title = title.get_text().strip()
        each_link = title.find("a")
        book_link = base_url+str(each_link.get("href")).strip()
        book_price = price.get_text().strip()
        #complete_data.append([book_title,book_link,book_price])
        complete_data.append({"book_title":book_title, "book_price":book_price,"book_link":book_link})
    csv_filename = "scraped_file.csv"
    fields_name = ["book_title","book_price","book_link"]

    with open(csv_filename, "w", encoding="utf-16") as csvfile:
        #csv.DictWriter(csvfile, fieldnames=fields_name).writerows(complete_data)
        writer = csv.DictWriter(csvfile, fieldnames=fields_name)
        writer.writeheader()  # Write the header row
        writer.writerows(complete_data)  # Write the data rows
    return "Done"


def amazon_in(URL,headers):
    res = requests.get(url=URL, headers=headers)
    # print(dir(res))
    page_source = res.content
    soup = BeautifulSoup(page_source, "html.parser")
    #print(soup)
    titles = soup.find_all("span",{"class":"a-size-medium a-color-base a-text-normal"})

    price_wholes = soup.find_all("span",{"class":"a-price-whole"})
    for title,price in zip(titles, price_wholes):
        print("title:\t", title.get_text())
        print("price:\t", price.get_text())




if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}

    URL = "https://books.toscrape.com/"
    print(web_scrape(URL, headers))
    print("\n\n_____________________________\n")
    URL = "https://www.amazon.in/s?k=laptop+price+hp&crid=15477ED9BUHSS&sprefix=laptop+price%2Caps%2C277&ref=nb_sb_ss_ts-doa-p_1_12"
    print(amazon_in(URL, headers))
