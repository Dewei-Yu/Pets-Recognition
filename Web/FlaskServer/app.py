import os

import base64
import io
from PIL import Image
from flask import request
from flask import jsonify
from flask import Flask, render_template
from scripts import Cat_Dog_Classifier
from scripts import Emotion_Dog
from scripts import Emotion_Cat
from scripts import Breed_Cat
from scripts import Breed_Dog
from shutil import copyfile

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("homePage.html")


# call models to predict the pet's type, breed and emotion.
@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))

    image.save("testImages/image.jpg")
    cat_dog_classifier = Cat_Dog_Classifier.predict()
    response = ""
    if cat_dog_classifier == 'Cat':
        # if cat_dog_classifier != '':
        catBreed = Breed_Cat.predict()
        catEmotion = Emotion_Cat.predict()
        response = {
            'pet': 'Cat',
            'emotion': catEmotion.to_string(index=False, header=False),
            'breed': catBreed.to_string(index=False, header=False)
        }
    elif cat_dog_classifier == 'Dog':
        dogEmotion = Emotion_Dog.predict()
        dogBreed = Breed_Dog.predict()
        response = {
            'pet': 'Dog',
            'emotion': dogEmotion.to_string(index=False, header=False),
            # 'emotion': "Happy 92.31%  Angry 5.41%  Neutral 1.91%",
            'breed': dogBreed.to_string(index=False, header=False)
        }

    os.remove("testImages/image.jpg")
    result = jsonify(response)
    result.headers.add('Access-Control-Allow-Origin', '*')
    return result


# this function use default image to predict once, in order to reduce the prediction time
def init():
    copyfile("image.jpg", "testImages/image.jpg")
    Emotion_Dog.predict()
    Emotion_Cat.predict()
    Breed_Dog.predict()
    Breed_Cat.predict()
    Cat_Dog_Classifier.predict()
    os.remove("testImages/image.jpg")


init()
