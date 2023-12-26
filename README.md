# Art Style Classifier with TensorFlow and Flask

## Overview

This project uses TensorFlow and Keras to build a Convolutional Neural Network (CNN) for classifying two different styles of art: Japanese and Rococo. The implementation includes data preparation, model training, and a Flask application for making predictions.

### Data Source
The dataset used in this project is sourced from [WikiArt - Art Movements/Styles](https://www.kaggle.com/datasets/sivarazadi/wikiart-art-movementsstyles).

## Project Structure

- **data_preparation.ipynb**: Jupyter Notebook for reading images and creating train, test, and validate datasets.
- **implementation.ipynb**: Jupyter Notebook for reading and augmenting images, building and training the CNN model, and running validation.
- **app/**:
  - **app.py**: Flask application for predicting the art style using the trained model.
  - **static/**: Folder for storing static files (images in this case).
  - **templates/**: HTML templates for the Flask application.

## Usage

run the flask app using ```python app.py``` *Make sure you have all the dependancies installed*


![image](https://github.com/AnasBuhayh/art-classification/assets/6984894/86752f9d-3a05-4ff4-be51-fba624b1612d)
