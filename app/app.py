from flask import Flask, render_template, request
import numpy as np
import os
from tensorflow.keras.models import load_model
from keras_preprocessing.image import load_img, img_to_array, ImageDataGenerator

app = Flask(__name__)

model = load_model('../trained_models/model.h5')

@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():

    # reading image
    image_file = request.files['imagefile']
    image_path = './static/images/' + image_file.filename
    image_file.save(image_path)
    print('read image')

    # preprocessing
    image = load_img(image_path, target_size=(256,256))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    datagen = ImageDataGenerator(rescale=1./255.)
    image = datagen.standardize(image)
    print('precessed image')

    # prediction
    
    prediction = model.predict(image)
    confidence = max(prediction[0])

    classes = ['Japanese Art', 'Rococo']
    predicted_class = classes[np.argmax(prediction)]
    print('predicted image')

    classification = f'This painting is predicted to be in the style of {predicted_class} with {confidence *100:.2f}% confidence'
    
    return render_template('index.html', prediction=classification, image="/images/"+image_file.filename)

if __name__ == '__main__':
    app.run(port=3000, debug=True)