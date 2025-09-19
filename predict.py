import cv2
import numpy as np
from tensorflow.keras.models import load_model


model=load_model('cat_dog_classifier.h5')

def predict_image(image_path):


    # this is forload and preprocess the image
    img = cv2.imread(image_path)
    img = cv2.resize(img, (64, 64))  # Resize to match model input
    img = np.array(img) / 255.0  # Normalize
    img = np.expand_dims(img, axis=0)  # Add batch dimension


    prediction = model.predict(img)
    print(" This is definitly a 🐶Dog man!" if prediction[0][0] > 0.5 else "This is definitly a 🐱Cat bro!")

# Example usage
predict_image('data/test_set/test_set/cats/cat.4428.jpg') 