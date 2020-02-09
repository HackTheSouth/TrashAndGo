import re

from pyzbar.pyzbar import decode
from PIL import Image
import requests
from bs4 import BeautifulSoup as bs

class CSVWriter():
    def __init__(self, barcode_data):
        pass


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
        return "Bruh Cheese"



class BarcodeInformationExtractor():
    """Takes in a barcode and returns a list of tuples (barcode, type)"""
    def __init__(self):
        self.used_barcodes = set()

    def scan_barcode(self, image):
        decoded_barcodes = decode(Image.open(image))    
        raw_barcode_list = [(D.data.decode("utf-8") , D.type) for D in decoded_barcodes]
        barcode_list = [Product(barcode) for barcode in raw_barcode_list]
        new_barcode_list = [barcode for barcode in barcode_list if barcode.barcode_number not in self.used_barcodes]
        barcode_list = new_barcode_list

        for barcode in barcode_list:
            self.used_barcodes.add(barcode.barcode_number)
        return barcode_list