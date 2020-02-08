from pyzbar.pyzbar import decode
from PIL import Image
from html.parser import HTMLParser


class Barcode():
    PARSED_DATA = ""

    def __init__(self, barcode_data):
        self.barcode_number = barcode_data[0]
        self.barcode_type = barcode_data[1]
        


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


class BarcodeInformationExtractor():
    """Takes in a barcode and returns a list of tuples (barcode, type)"""
    def __init__(self, image):
        decoded_barcodes = decode(Image.open(image))
        raw_barcode_list = [(D.data.decode("utf-8") , D.type) for D in decoded_barcodes]
        self.barcode_list = [Barcode(barcode) for barcode in raw_barcode_list]


bie = BarcodeInformationExtractor('C:\\Users\\Akhilesh\\Desktop\\TrashAndGo\\barcode.jpg')