from pyzbar.pyzbar import decode
from PIL import Image


class BarcodeInformationExtractor():
    """Takes in a barcode and returns a list of tuples (barcode, type)"""
    def __init__(self, image):
        self.decoded_barcodes = decode(Image.open(image))
        self.barcode_list = [(D.data.decode("utf-8") , D.type) for D in self.decoded_barcodes]
    
    """Returns the list of tuples containing the barcode data"""
    def get_barcode_list(self):
        return str(self.barcode_list)   


bie = BarcodeInformationExtractor('C:\\Users\\Akhilesh\\Desktop\\TrashAndGo\\barcode.jpg')
print(bie)