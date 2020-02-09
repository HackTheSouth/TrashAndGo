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
        self.points = self.calculate_points_for_barcode()

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
    
    def calculate_points_for_barcode(self):
        return (self.barcode_number % 5) + 5


class BarcodeInformationExtractor():
    """Takes in a barcode and returns a list of tuples (barcode, type)"""
    def __init__(self, image):
        decoded_barcodes = decode(Image.open(image))
        raw_barcode_list = [(D.data.decode("utf-8") , D.type) for D in decoded_barcodes]
        self.barcode_list = [Product(barcode) for barcode in raw_barcode_list]


items = BarcodeInformationExtractor('C:\\Users\\Akhilesh\\Desktop\\TrashAndGo\\barcode_images\\barcode9.jpg').barcode_list
for item in items:
    print(item.barcode_number)
    print(item.product_name)