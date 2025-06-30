from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)
model = load_model("poultry_disease_model.h5")  # Ensure this file is in your root directory

# Class labels in the order used during training
class_names = ['Coccidiosis', 'Healthy', 'New Castle Disease', 'Salmonella']

# Dictionary of disease information
disease_info = {
    'Coccidiosis': "🦠 A parasitic disease affecting intestines. Treat with Amprolium or sulfa drugs.",
    'Healthy': "✅ The bird is healthy. Maintain hygiene and vaccination schedule.",
    'New Castle Disease': "😷 A contagious viral disease. Vaccinate and isolate affected birds.",
    'Salmonella': "🧬 Bacterial infection. Use antibiotics like tetracycline. Ensure feed hygiene."
}

# Route for home page
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    info = None
    img_path = None

    if request.method == "POST":
        file = request.files["image"]
        if file:
            upload_folder = os.path.join("static", "uploads")
            os.makedirs(upload_folder, exist_ok=True)

            img_filename = file.filename
            img_path = os.path.join(upload_folder, img_filename)
            file.save(img_path)

            # Load and preprocess the image
            img = image.load_img(img_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0

            # Predict
            pred = model.predict(img_array)
            class_index = np.argmax(pred)
            confidence = float(pred[0][class_index]) * 100

            predicted_class = class_names[class_index]
            prediction = f"{predicted_class} ({confidence:.2f}% confidence)"
            info = disease_info[predicted_class]

    return render_template("index.html", prediction=prediction, info=info, img_path=img_path)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

