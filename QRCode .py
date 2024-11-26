import io
import pyqrcode
from base64 import b64encode
import eel

eel.init('Web')

@eel.expose
def dummy(dummy_param):
    print("I got a parameter: ", dummy_param)
    return "string_value", 1, 1.2, True, [1, 2, 3, 4], {"name": "eel"}

@eel.expose
def generate_qr(data):
    img = pyqrcode.create(data)
    buffers = io.BytesIO()
    img.png(buffers, scale=8,)
    encoded = b64encode(buffers.getvalue()).decode("ascii")
    return "data:image/png;base64, " + encoded

eel.start(r'index.html', size=(1000, 600))