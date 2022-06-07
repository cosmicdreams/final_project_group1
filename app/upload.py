import imghdr
import os
from urllib.parse import urlparse

import cv2 as cv
import numpy as np
import requests
from flask import Flask, render_template, request, abort, send_from_directory
from flask_dropzone import Dropzone
from tensorflow.keras.models import load_model
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.webp', '.jpeg']
app.config['UPLOAD_PATH'] = 'uploads'
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image'
app.config['DROPZONE_DEFAULT_MESSAGE'] = 'Drop an image here to upload'
app.config['DROPZONE_FILE_TOO_BIG'] = 'Image is too big {{filesize}}. Max file size: {{maxFilesize}} MB'
app.config['DROPZONE_INPUT_NAME'] = 'upload'
dropzone = Dropzone(app)


@app.route('/')
def home_page():
    return render_template('main.html')


@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['upload']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext not in app.config['UPLOAD_EXTENSIONS'] or not validate_image(uploaded_file.stream, file_ext):
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
        compiled_result = render_result(pokemon_name)
        return render_template('main.html', result=compiled_result)


@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


def create_uploads(path):
    if not os.path.exists(path):
        os.makedirs(path)


# Check the first part so that the file type can be determined.
def validate_image(stream, test_ext):
    header = stream.read(512)  # 512 bytes should be enough for a header check
    stream.seek(0)  # reset stream pointer
    format = imghdr.what(None, header)
    if not format:
        return False

    jpegs = ['jpg', 'jpeg']
    if format in jpegs:
        return test_ext.lstrip('.') in jpegs

    return format not in app.config['UPLOAD_EXTENSIONS']


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
    return ['Abra', 'Aerodactyl', 'Alakazam', 'Alolan Sandslash', 'Arbok', 'Arcanine', 'Articuno', 'Beedrill',
            'Bellsprout', 'Blastoise', 'Bulbasaur', 'Butterfree', 'Caterpie', 'Chansey', 'Charizard',
            'Charmander', 'Charmeleon', 'Clefable', 'Clefairy', 'Cloyster', 'Cubone', 'Dewgong', 'Diglett',
            'Ditto', 'Dodrio', 'Doduo', 'Dragonair', 'Dragonite', 'Dratini', 'Drowzee', 'Dugtrio', 'Eevee',
            'Ekans', 'Electabuzz', 'Electrode', 'Exeggcute', 'Exeggutor', 'Farfetchd', 'Fearow', 'Flareon',
            'Gastly', 'Gengar', 'Geodude', 'Gloom', 'Golbat', 'Goldeen', 'Golduck', 'Golem', 'Graveler',
            'Grimer', 'Growlithe', 'Gyarados', 'Haunter', 'Hitmonchan', 'Hitmonlee', 'Horsea', 'Hypno',
            'Ivysaur', 'Jigglypuff', 'Jolteon', 'Jynx', 'Kabuto', 'Kabutops', 'Kadabra', 'Kakuna', 'Kangaskhan',
            'Kingler', 'Koffing', 'Krabby', 'Lapras', 'Lickitung', 'Machamp', 'Machoke', 'Machop', 'Magikarp',
            'Magmar', 'Magnemite', 'Magneton', 'Mankey', 'Marowak', 'Meowth', 'Metapod', 'Mew', 'Mewtwo',
            'Moltres', 'MrMime', 'Muk', 'Nidoking', 'Nidoqueen', 'Nidorina', 'Nidorino', 'Ninetales', 'Oddish',
            'Omanyte', 'Omastar', 'Onix', 'Paras', 'Parasect', 'Persian', 'Pidgeot', 'Pidgeotto', 'Pidgey',
            'Pikachu', 'Pinsir', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Ponyta', 'Porygon', 'Primeape',
            'Psyduck', 'Raichu', 'Rapidash', 'Raticate', 'Rattata', 'Rhydon', 'Rhyhorn', 'Sandshrew',
            'Sandslash', 'Scyther', 'Seadra', 'Seaking', 'Seel', 'Shellder', 'Slowbro', 'Slowpoke', 'Snorlax',
            'Spearow', 'Squirtle', 'Starmie', 'Staryu', 'Tangela', 'Tauros', 'Tentacool', 'Tentacruel',
            'Vaporeon', 'Venomoth', 'Venonat', 'Venusaur', 'Victreebel', 'Vileplume', 'Voltorb', 'Vulpix',
            'Wartortle', 'Weedle', 'Weepinbell', 'Weezing', 'Wigglytuff', 'Zapdos', 'Zubat']


def get_scrape_data(pokemon_name):
    from sqlalchemy import create_engine
    if pokemon_name in ['Alolan Sandslash']:
        pokemon_name = 'Sandslash'

    data = []
    db_string = "sqlite:///db/pokescrape.db"
    db = create_engine(db_string)

    # Query/Read from Database
    query = f"SELECT html FROM pokedex_html where name = '{pokemon_name}';"
    with db.connect() as con:
        results = con.execute(query)
        for row in results:
            data = row
            break

    # Close Connection to Postgres:
    db.dispose()

    return data[0]


# Render the incoming markup from elder's query.
def render_scrape(pokemon_name):
    markup = get_scrape_data(pokemon_name)  # Do db lookup of markup here.
    markup = clean_markup(markup)
    return render_template('wrap-me.html', markup=markup)


# It's possible for the markup to be nested within square brackets []
def clean_markup(markup):
    markup = markup.replace("[", "")
    markup = markup.replace("]", "")

    return markup


# Outputs and initializes the pokemon card element.
def render_card(pokemon_name):
    return render_template('pokemon-card.html', pokemon_name=pokemon_name)


# Compile the two results and deliver a complete set of results.
def render_result(pokemon_name):
    scrape_result = render_scrape(pokemon_name)
    card_result = render_card(pokemon_name.lower())  # PokeApi requires names to be lower case.
    compiled_result = render_template('result.html', scrape=scrape_result, card=card_result)
    return compiled_result


# Until we have the db select working, here's a method to get the
def render_mock_scrape():
    return render_template('mock_scrape.html')


# Launcher
if __name__ == '__main__':
    app.run(port=8000, debug=True)
