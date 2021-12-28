import os

import lxml.html
from selenium import webdriver
from bs4 import BeautifulSoup
import requests, warnings
from dataclasses import dataclass
#from settings import none
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
import time


class Test():
    def __init__(self):
        self.url = "https://www.wildberries.ru"
        self.option = webdriver.FirefoxOptions()
        self.list = ''
        #self.browser = None


    def get_content(self, url):
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        items = soup.find_all('ymaps', class_="ymaps-2-1-79-islets_serp-item ymaps-2-1-79-islets__first")
        print(items)

    def start(self):
        self.option.add_argument("-incog#ito")
        # self.option.headless =True
        self.browser = webdriver.Firefox(executable_path="geckodriver.exe",options=self.option)

    def find_adress_postive(self, adress):
        return self.__find_adress(adress)

    def find_adress_negative(self, adress):
        return self.__find_adress(adress)

    def __find_adress(self, adress):
        url = self.url + "/services/besplatnaya-dostavka?desktop=1#terms-delivery"
        self.browser.get(url)
        time.sleep(1)
        xpath = {
            "tb_adress": "(//input[@placeholder='Введите адрес'])[1]",
            "tb_Password": "//input[@id='loginInputEmail']",
            "btn_search": "(//ymaps[@class='ymaps-2-1-79-searchbox-button ymaps-2-1-79-_pin_right ymaps-2-1-79-user-selection-none'])[1]",
            "btn_select_adress": "(//ymaps[@class='ymaps-2-1-79-islets_serp-item ymaps-2-1-79-islets__first'])[1]",
            "btn_select_post": "(//div[@class='address-item j-poo-option'])[1]",
            "tb_yamaps": "(//div[@class='address-item j-poo-option'])[1]"


        }
        self.browser.find_element_by_xpath(xpath["tb_adress"]).send_keys(adress)
        self.browser.find_element_by_xpath(xpath["btn_search"]).click()
        try:
            btn_select_adress = self.browser.find_element_by_xpath(xpath["btn_select_adress"])
            print("Element exists")
            time.sleep(3)
            btn_select_adress.click()
            time.sleep(3)
            self.browser.find_element_by_xpath(xpath["btn_select_post"]).click()
            return f'Пункт по адресу выдачи: {adress }  найдет'
        except:
            return f'Пункт по адресу выдачи: {adress}  не найдет'


    def authrisation(self,phone):
        url = self.url
        print( f'Телефон: {phone}')
        self.browser.get(url)
        time.sleep(1)
        xpath = {
            "tb_phone": "(//input[@class='input-item'])[1]",
            "btn_login": ".navbar-pc__link.j-main-login",
            "btn_get_code": "//button[@id='requestCode']"

        }
        try:
            self.browser.find_element_by_css_selector(xpath["btn_login"]).click()
            time.sleep(1)
            self.browser.find_element_by_xpath(xpath["tb_phone"]).send_keys(phone)
            time.sleep(1)
            self.browser.find_element_by_xpath(xpath["btn_get_code"]).click()
            return f'Телефон по номеру: {phone}  найден'
        except:
            return f'Телефон по номеру: {phone}  не найден'



    def researsh_input(self,request):
        url = self.url
        print( f'Запрос: {request}')
        self.browser.get(url)
        time.sleep(1)
        xpath = {
            "tb_research": "#searchInput",
            "item":"j-thumbnail thumbnail",
            "tb_exist": "catalog-page__text"

        }
        try:
            tb_research = self.browser.find_element_by_css_selector(xpath["tb_research"])
            tb_research.send_keys(request)
            tb_research.send_keys(Keys.ENTER)
            time.sleep(1)
            tb_exist = self.browser.find_element_by_css_selector(xpath["tb_exist"]).is_displayed()
            print(tb_exist)
            if tb_exist is True:
                return f'По запросу {request} ничего не найдено'
            else:
                list_products = self.browser.find_elements_by_class_name(xpath["item"])
                return f'По запросу: {request}  найдены элементы {len(list_products)}'
        except:
            return f'По запросу: {request}  ничего не найдено'



    def researsh_input_photo(self,img):
        url = self.url
        print( f'Поиск по картинке')
        self.browser.get(url)
        time.sleep(1)
        xpath = {
            "btn_send_img": "(//input[@name='photo'])[1]",
            "item":"j-thumbnail thumbnail",
            "btn_research": ".search-catalog__btn.search-catalog__btn--photo.j-search-img-btn"

        }
        try:
            btn_research = self.browser.find_element_by_css_selector(xpath["btn_research"]).click()
            btn_send_img = self.browser.find_element_by_xpath(xpath["btn_send_img"])
            print(os.path.dirname(img))
            btn_send_img.send_keys(os.path.dirname(img))
            time.sleep(1)
            list_products = self.browser.find_elements_by_class_name(xpath["item"])
            if len(list_products)>0:
                return f'По запросу ничего не найдено'
            else:
                return f'По запросу найдены элементы'
        except:
            return f'По запросу ничего не найдено'


