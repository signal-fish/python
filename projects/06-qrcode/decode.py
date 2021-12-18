from pyzbar.pyzbar import decode
from PIL import Image
import os

path = os.getcwd() + "/myqrcode1.png"
img = Image.open(path)
result = decode(img)
print(result[0].data)
