import pyqrcode
import png
text = "Hello, My name is Sooraj"
qr_code = pyqrcode.create(text)
qr_code.png("qr.png", scale=5)