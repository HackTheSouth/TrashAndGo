import re

from pyzbar.pyzbar import decode
from PIL import Image
import requests
from bs4 import BeautifulSoup as bs


product_database = {
    "5000118047817": 'Lipton Peach Ice Tea 500ml',
    "90162602": 'Red Bull Energy Drink 250ml',
    "5033022002306": 'White Rock Spring Water 500ml',
    "5012035950132": 'Haribo Tangfastics'
}


class Product():
    def __init__(self, barcode_data):
        self.barcode_number = barcode_data[0]
        self.barcode_type = barcode_data[1]
        self.product_name = self.parse_product_name_hardcoded()

    def parse_product_name(self):
        app_url = 'https://www.barcodable.com/ean/' + self.barcode_number
        page = requests.get(app_url)
        soup = bs(page.content, 'html.parser')

        result = re.search('\- (.*) \(', str(soup.head.title))

        if not result:
            return 'Unknown Product'

        return result.group(1)
    
    def parse_product_name_hardcoded(self):
        if self.barcode_number in product_database:
            return product_database[self.barcode_number]
        return "Bruh Cheese"



class BarcodeInformationExtractor():
    """Takes in a barcode and returns a list of tuples (barcode, type)"""
    def __init__(self):
        self.used_barcodes = set()

    def scan_barcode(self, image):
        decoded_barcodes = decode(Image.open(image))
        print("Found ",decoded_barcodes)
        raw_barcode_list = [(D.data.decode("utf-8") , D.type) for D in decoded_barcodes]
        barcode_list = [Product(barcode) for barcode in raw_barcode_list]
        new_barcode_list = [barcode for barcode in barcode_list if barcode.barcode_number not in self.used_barcodes]
        barcode_list = new_barcode_list

        for barcode in barcode_list:
            self.used_barcodes.add(barcode.barcode_number)
        return barcode_list


import random


class GetRandomNumber():
    """Takes in two tuples containing the lat and long data for top right and bottom right
    Returns a 4 tuple (rand_top_right, rand_bottom_left, rand_percentage, rand_letter)"""

    def get_random_values(self, top_right, bottom_left, N):
        output = ""
        for _ in range(N):
            rand_top_right = random.uniform(top_right[0], bottom_left[0])
            rand_bottom_left = random.uniform(top_right[1], bottom_left[1])
            rand_percentage = random.randint(0, 100)
            rand_letter = random.choice(['R', 'N'])

            output += "(" + str(rand_top_right) + "," + str(rand_bottom_left) + "," + str(rand_percentage) + "%," + str(rand_letter) + "):"

        return output

#s = GetRandomNumber()
#print(s.get_random_values((50.9780637,-1.290326),(50.9079661,-1.4661225),100))