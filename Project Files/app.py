from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = load_model("poultry_disease_model.h5")

class_names = ['Coccidiosis', 'Healthy', 'New Castle Disease', 'Salmonella']

disease_info = {
    'Coccidiosis': "🦠 A parasitic disease affecting intestines. Treat with Amprolium or sulfa drugs.",
    'Healthy': "✅ The bird is healthy. Maintain hygiene and vaccination schedule.",
    'New Castle Disease': "😷 A contagious viral disease. Vaccinate and isolate affected birds.",
    'Salmonella': "🧬 Bacterial infection. Use antibiotics like tetracycline. Ensure feed hygiene."
}

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    info = None
    img_path = None

    if request.method == "POST":
        file = request.files["image"]
        if file:
            path = os.path.join("static/uploads", file.filename)
            file.save(path)

            img = image.load_img(path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0

            pred = model.predict(img_array)
            class_index = np.argmax(pred)
            prediction = class_names[class_index]
            info = disease_info[prediction]
            img_path = path

    return render_template("index.html", prediction=prediction, info=info, img_path=img_path)

if __name__ == "__main__":
    app.run(debug=True)
