from models import Product
from scrapper import Scrapper
from concurrent.futures import ProcessPoolExecutor
import time

urls = ["https://www.newegg.com/amd-ryzen-9-9900x-ryzen-9-9000-series-granite-ridge-socket-am5-processor/p/N82E16819113842",
       "https://www.newegg.com/intel-core-i7-14700k-core-i7-14th-gen-raptor-lake-lga-1700-desktop-processor/p/N82E16819118466"]


def scrape_data(url:str):
    scrapper=Scrapper()
    product=scrapper.scrape_data(url)
    return product

def main():
    if __name__=="__main__":
        with ProcessPoolExecutor(max_workers=5) as ex:
            results= list(ex.map(scrape_data,urls))

    for product in results:
        if product:
            print(f"Scraped: {product.title} - ${product.price}")      


if __name__=="__main__":
    main()