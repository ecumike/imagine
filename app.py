'''
Main app file.
To run:   flask run
'''

from flask import Flask, render_template, request
from services import generate_image


app = Flask(__name__) #initialising flask

@app.route('/')
def home():
    '''
    Home page
    '''
    return render_template('home.html')

@app.route('/api/image/', methods=['POST'])
def get_image():
    '''
    Takes posted description and requests an image from openAI.
    Returns URL
    '''
    image_url = ''

    if request.method == 'POST':
        image_url = generate_image(request.json['description'])

    return {'url': image_url}


if __name__ == '__main__':
    app.run(debug=True)
