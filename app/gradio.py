import tensorflow as tf
import tensorflow_hub as tfh

import gradio as gr
import requests

model = tf.keras.models.load_model(
    ("final_model.h5"), custom_objects = {'KerasLayer': tfh.KerasLayer}
)

labels = ["Green", "Blue", "Red", "Airport", "Night bus", "Other"]

def classify_image(inp):
    inp = inp.reshape((-1, 224, 224, 3))
    inp = inp / 255

    pred = model.predict(inp).flatten()
    confidence = {labels[i]: float(pred[i]) for i in range(len(labels))}
    return confidence

app = gr.Interface(fn = classify_image,
                   inputs = gr.Image(shape=(224, 224)), 
                   outputs = gr.label(num_top_classes = 3)
)

app.launch()