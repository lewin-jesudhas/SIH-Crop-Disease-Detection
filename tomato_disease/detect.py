import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os

def detect(image_path):

    # Get the directory of the script
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Define the relative path to your model directory
    model_dir = os.path.join(script_dir, 'models', '1')

    # Load the model
    model = tf.saved_model.load(model_dir)
    class_names = ['Tomato_Early_blight', 'Tomato_Late_blight', 'Tomato_healthy']

    def predict(model, img_path):
        img = tf.keras.preprocessing.image.load_img(img_path, target_size=(256, 256))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)

        predictions = model(img_array)
        predicted_class = class_names[np.argmax(predictions[0])]
        confidence = round(100 * (np.max(predictions[0])), 2)
        
        return predicted_class, confidence

    img_path = image_path
    predicted_class, confidence = predict(model, img_path)

    return (predicted_class, confidence)
