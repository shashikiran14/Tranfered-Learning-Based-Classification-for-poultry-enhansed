
# 🐣 Poultry Disease Identifier

A deep learning–based web application that identifies common poultry diseases — **Coccidiosis**, **Salmonella**, **Newcastle Disease**, or indicates a **Healthy** status — from images of chicken feces. This tool helps farmers and veterinarians quickly assess poultry health using a custom-trained MobileNetV2 model.



---

## 🚀 Features

- 🧠 **AI-Powered Diagnosis**: Classifies fecal images into four categories.
- ✅ **Disease Detection**: Supports detection of Coccidiosis, Salmonella, Newcastle Disease, or Healthy status.
- ⚡ **Real-Time Predictions**: Instant analysis with confidence scores.
- 🎨 **Dark-Themed Interface**: Clean and user-friendly UI built with Streamlit.
- 🐍 **Python-Powered Stack**: Built using TensorFlow, Streamlit, Pillow, and NumPy.

---

## 🛠️ Tech Stack

| Layer       | Tech                        |
|-------------|-----------------------------|
| UI/Frontend | Streamlit (HTML/CSS Custom) |
| Backend     | TensorFlow, NumPy, Pillow   |
| Model       | MobileNetV2 (.h5 Keras file) |

---

## 📂 Project Structure

```
poultry-diseases-identifier/
├── app.py                         # Main Streamlit app
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
├── model/
│   └── mobilenetV2/
│       └── mobilenetv2.h5         # Pre-trained MobileNetV2 model
```

---

## ✅ How to Run the App

1. **Clone the Repository**
   ```bash
   git clone https://github.com/shashikiran14/Tranfered-Learning-Based-Classification-for-poultry-enhansed
   cd poultry-diseases-identifier
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   # Activate the environment
   venv\Scripts\activate       # On Windows
   source venv/bin/activate    # On Mac/Linux
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Place the Trained Model**
   Download the model from [here](https://drive.google.com/file/d/1d_yRsZtoHXM9HYXqMKjrHWdtmHKO3h78/view?usp=drivesdk)  
   and place it in the following path:
   ```
   model/mobilenetV2/mobilenetv2.h5
   ```

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```
   Open your browser and go to: [http://localhost:8501](http://localhost:8501)

---

## 📥 Model Download

🔗 [Download mobilenetv2.h5 (Google Drive)](https://drive.google.com/file/d/1d_yRsZtoHXM9HYXqMKjrHWdtmHKO3h78/view?usp=drivesdk)

Ensure the model is stored in:
```
model/mobilenetV2/mobilenetv2.h5
```

---

## 👨‍💻 Authors

- **Kuruva Shashi Kiran**  
- **Kuruva Harika**

---

## 🙏 Acknowledgements

- 💡 **Streamlit** – for the fast and simple web interface
- 🤖 **TensorFlow/Keras** – for deep learning model training
- 📸 **Open Datasets** – for poultry disease image datasets

---

## 📝 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute this project with attribution.

---

## 🌟 Support

If you find this project helpful, give it a ⭐ on GitHub!

##OUTPUT:
![Image](https://github.com/user-attachments/assets/3df6fea4-d74e-40cf-b53a-c5d0d6d1978a)
