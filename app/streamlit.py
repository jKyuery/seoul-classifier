import streamlit as st

import tensorflow as tf
import tensorflow_hub as th
import numpy as np

import cv2 
from PIL import Image

# Set title bar and page layout
st.set_page_config(layout="wide", page_title="Seoul Classification")

# Frontend text
st.title("Seoul Bus Classification using Deep Learning")
st.header("What kind of bus is your bus in Seoul, South Korea?")
st.text("Please send a picture of a bus in Korea and I'll try to guess it!")

# Load saved model 
model = tf.keras.models.load_model(
    ("final_model.h5"), custom_objects={'KerasLayer': th.KerasLayer}
)

# Labels
labels = ["Green", "Blue", "Red", "Airport", "Night", "Other"]

def prediction(pic):
    image = cv2.resize(np.array(pic), (224, 224)) # resize image to tensor of 224 * 224 pixels
    image = image / 255 # scale the image

    try:
        x = np.reshape(image, (-1, 224, 224, 3)) #if tensor is RGB (,3), process for prediction
    except:
        x = np.reshape(image, (1, 224, 224, 1)) #if tensor is not RGB, convert then process for prediction
        x = np.concatenate([x]*3, axis=-1)

    x = model.predict(x).flatten() # predict value and get predictions
    pred = x.argmax() # Get the label of the highest accuracy 
    confidences = {labels[i]: float(x[i]) for i in range(5)} # get prediction for each label and store in a dictionary
    return pred, confidences

upload= st.file_uploader('Insert image for classification', type=['png','jpg', 'jpeg', 'webp']) # for user to upload picture
c1, c2= st.columns(2, gap="large") # creating 2 columns

if upload is not None:
    img = Image.open(upload) # collect image
    
    c1.header('Your Picture')
    c1.image(img) # show image on screen
    answer, pred = prediction(img) # predict label image

    c2.header('Predictions :')
    c2.subheader(f"This is a/an {labels[answer]} Bus") # display  prediction
    
    # get the 3 most accurate predictions
    sorted_values = sorted(pred.items(), key=lambda x: x[1], reverse=True)[:3]

    # Loop over the sorted values and create a progress bar for each label and prediction
    for key, value in sorted_values:
        c2.write(key)
        progress_bar = c2.progress(0)
        for i in range(3):
            progress_bar.progress(value, text=f"with {value * 100:.2f}% confidence ")