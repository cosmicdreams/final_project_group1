import io

from flask import Flask, render_template, request
from tensorflow import keras
from tensorflow.keras.models import load_model

# Helper libraries
import numpy as np
import imghdr

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('main.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['upload']

        if file is None:
            return {'error': 'Upload File Error: File not provided'}
        elif imghdr.what(file) in ['jpeg', 'jpg', 'png', 'gif']:
            payload = identify_file(file)
            return payload

        return {'error': 'Upload File Error: file not an image'}


# Image is provided as a byte stream.  Need to convert to image
def prepare_image(file):
    from PIL import Image
    target_size = 96, 96
    image = Image.open(io.BytesIO(file.stream.read()))
    image = image.resize(target_size, Image.Resampling.NEAREST)
    image = image.convert('RGB')

    img_arr = keras.utils.img_to_array(image)
    img_batch = np.expand_dims(img_arr, axis=0)
    return img_batch


# Get identify of the provided Pokemon image with image classifier.
def identify_file(file):
    combined = get_map()
    image = prepare_image(file)

    classifier = load_model('model/model.hdf5')
    prediction = classifier.predict(image)
    pred_class = np.argmax(prediction)

    # Look up predicted Pokemon using the original list.
    return {'Prediction': combined[pred_class], 'Accuracy': round(prediction[0][pred_class] * 100)}


# Once we have the identity, pull data on pokemon
def get_pokemon_data(pokemon_id):
    return render_template('pokemon_data_display.html', pokemon=pokemon_id)


# Render the incoming markup from elder's query.
def spit_markup(elders_markup):
    return render_template('elders_markup.html', markup=elders_markup)


# Get a dictionary which contains class and number of images in that class
def get_map():
    import os

    path = '../input/PokemonData'
    return sorted(os.listdir(path))


if __name__ == '__main__':
    app.run(port=8000, debug=True)
