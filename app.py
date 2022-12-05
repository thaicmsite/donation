from flask import Flask
from rembg import remove
from PIL import Image
Image.LOAD_TRUNCATED_IMAGES = True

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
    input_path = 'pro-golf.jpg'
    output_path = 'output-pro-golf.png'
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)

    return "Hello World"
