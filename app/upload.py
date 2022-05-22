from flask import Flask, render_template, request
import imghdr

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':

        file = request.files['file']

        if imghdr.what(file) in ['jpeg', 'jpg', 'png', 'gif']:
            return identify_file(file)

        return {'error': 'Upload File Error: file not an image'}


# Get identify of the provided Pokemon image with image classifier.
def identify_file(file):
    return 'Todo'


# Once we have the identity, pull data on pokemon
def get_pokemon_data(pokemon_id):
    return render_template('components/pokemon_data_display.html', pokemon=pokemon_id)


if __name__ == '__main__':
    app.run(debug=True)
