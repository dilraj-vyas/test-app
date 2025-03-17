from selenium import webdriver
from selenium.webdriver.common.by import By
from models import Product
import time


class Scrapper:

    def __init__(self):
        self.driver=webdriver.Chrome()
        


    def load_page(self,url:str,wait_time:int=5):
        self.driver.get(url)
        time.sleep(wait_time)


    def get_element_text(self,by_method,selector:str,default:str=""):
        try:
            element=self.driver.find_element(by_method,selector)
            return element.text.strip()
        except Exception as e:
            print(f"Error finding element for selector {selector} : {e}")


    def get_element(self,by_method,selector:str,default:str=""):
        
        try:
           element=self.driver.find_element(by_method,selector)
           return element
        except Exception as e:
            print(f"Error finding element using selector  '{selector}' : {e} ")
            return default
    

    def scrape_data(self,url:str) -> Product:
        try:
            self.load_page(url)
            title=self.get_element_text(By.CLASS_NAME,"product-title")
            brand_element=self.get_element(By.CLASS_NAME,"logo")
            brand=brand_element.get_attribute("alt")
            price_text=self.get_element_text(By.CLASS_NAME,"price-current")
            # rating_element = self.get_element(By.CLASS_NAME,"rating-views-num")
            price=float(price_text[1:])
            description = self.get_element_text(By.CLASS_NAME,"product-bullets")

            return Product(title, brand, price, description)

        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return None     


