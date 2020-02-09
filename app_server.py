from flask import Flask, request, jsonify, send_from_directory
import csv
from PIL import Image
import io
import json
import base64
import time
from barcode_information_extractor import Product,BarcodeInformationExtractor


app = Flask(__name__)
port = 2000
bruhtems = BarcodeInformationExtractor()
#word = Words("C:\\Users\\sohai\\PycharmProjects\\TrashAndGoServer\\words_rec.jpg")


@app.route('/trashandgo')
def handright():
    return {"bruh2": "John Doe", "Description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."}

@app.route('/trashandgo/bruhinfo')
def getDistances():
    data = []
    x = open("simple_locations.txt", "r")
    return x.read()

@app.route('/trashandgo/image', methods=['POST'])
def image():
    y = request.get_data()
    # image = Image.open(io.BytesIO(bytes))
    # image.save()

    image_data = base64.b64encode(y)
    with open ("bruh.png", "wb") as file:
        file.write(base64.decodebytes(image_data))

    items = bruhtems.scan_barcode("bruh.png")
    output = ""

    print("here")
    for item in items:
        print("loop")
        output += item.barcode_number + ","+ item.product_name + ":"
        print(item.barcode_number)
        print(item.product_name)
    print(output)
    if output == "":
        return "error"
    return output

@app.route('/trashandgo/meme')
def lul():
        return send_from_directory("", "bruh.mp4")


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = port)