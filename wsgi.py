import imghdr
import os
from urllib.parse import urlparse

import cv2 as cv
import numpy as np
import requests
from flask import Flask, render_template, request, abort, send_from_directory
from tensorflow.keras.models import load_model
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.webp']
app.config['UPLOAD_PATH'] = 'uploads'


@app.route('/')
def home_page():
    return render_template('main.html')


@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['upload']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                file_ext != validate_image(uploaded_file.stream):
            abort(400)

        # 1. Save uploaded file in temp directory verbatim
        create_uploads(app.config['UPLOAD_PATH'])
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))

        # 2. Load and convert image to proper size / type
        o = urlparse(request.base_url)
        url = o.scheme + "://" + o.netloc + "/" + app.config['UPLOAD_PATH'] + "/" + filename
        image = get_image(url)
        image = prepare_image(image)

        # 3. Cleanup by deleting entire contents of temp
        nuke_file(filename)

        # 4. Prepare payload.
        payload = identify_image(image)

        # 5. Send response
        pokemon_name = payload['Prediction']
        return render_result(pokemon_name)


@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


def create_uploads(path):
    if not os.path.exists(path):
        os.makedirs(path)


# Check the first part so that the file type can be determined.
def validate_image(stream):
    header = stream.read(512)  # 512 bytes should be enough for a header check
    stream.seek(0)  # reset stream pointer
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


# Mock data for testing purposes.
def get_test_image():
    url = 'https://johnlewis.scene7.com/is/image/JohnLewis/237525467'
    r = requests.get(url, stream=True).raw
    image = np.asarray(bytearray(r.read()), dtype="uint8")
    return cv.imdecode(image, cv.IMREAD_COLOR)


def get_image(url):
    r = requests.get(url, stream=True).raw
    image = np.asarray(bytearray(r.read()), dtype="uint8")
    return cv.imdecode(image, cv.IMREAD_COLOR)


# To work around difficulty in working with the image while in memory, we save the file temporarily.
def nuke_file(filename):
    os.remove(os.path.join(app.config['UPLOAD_PATH'], filename))


# Image is provided as a byte stream.  Need to convert to image
def prepare_image(image):
    image = cv.resize(image, (96, 96))  # Resizing image to (96, 96)
    image = image.reshape(-1, 96, 96, 3) / 255.0  # Reshape and scale resized image
    return image


# Get identify of the provided Pokemon image with image classifier.
def identify_image(image):
    combined = get_map()

    classifier = load_model('model/model.hdf5')
    prediction = classifier.predict(image)
    pred_class = np.argmax(prediction)

    # Look up predicted Pokemon using the original list.
    return {'Index': str(pred_class), 'Prediction': combined[pred_class],
            'Accuracy': round(prediction[0][pred_class] * 100, 2)}


# Get a dictionary which contains class and number of images in that class
def get_map():
    import os

    path = '../input/PokemonData'
    pokemon_list = sorted(os.listdir(path))
    if '.DS_Store' in pokemon_list:
        pokemon_list.remove('.DS_Store')

    return pokemon_list


# Render the incoming markup from elder's query.
def render_scrape(pokemon_name):
    markup = render_mock_scrape()  # Do db lookup of markup here.
    return render_template('wrap-me.html', markup=markup)


# Outputs and initializes the pokemon card element.
def render_card(pokemon_name):
    return render_template('pokemon-card.html', pokemon_name=pokemon_name)


# Compile the two results and deliver a complete set of results.
def render_result(pokemon_name):
    scrape_result = render_scrape(pokemon_name)
    card_result = render_card(pokemon_name.lower())  # PokeApi requires names to be lower case.
    compiled_result = render_template('result.html', scrape=scrape_result, card=card_result)
    return render_template('main.html', result=compiled_result)


# Until we have the db select working, here's a method to get the
def render_mock_scrape():
    return render_template('mock_scrape.html')


# Launcher
if __name__ == '__main__':
    app.run(port=8000, debug=True)
