import os
from PIL import Image
from pyqrcode import create
from pyzbar.pyzbar import decode


select_text = """Select an option

[1] QR Code decode
[2] QR Code encode

Enter option number :- """


def qr_decode():
    path = input("Enter image path")
    try:
        qr_text_data = decode(Image.open(path))
        qr_text_list = list(qr_text_data[0])
        qr_text_ext = str(qr_text_list[0]).split("'")[1]
        qr_text = "".join(qr_text_ext)
        return qr_text
    except Exception as error:
        return error


def qr_encode():
    text = input("Enter link :- ")
    name = input("Enter file name :- ")
    qr_code = create(text)
    qr_code.png(name + '.png', scale=6)
    image = name + '.png'
    return image


def main():
    option = input(select_text)
    if option == "1":
        print(qr_decode())
    elif option == "2":
        print(qr_encode())
    else:
        print("Invalid Option!\n")
        return main()


main()
