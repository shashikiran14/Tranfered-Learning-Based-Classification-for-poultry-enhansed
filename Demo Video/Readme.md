# 🐔 Poultry Disease Identifier

A deep learning–based web application that identifies common poultry diseases such as **Coccidiosis**, **Salmonella**, **Newcastle Disease**, or detects if the sample is **Healthy**. The model uses a custom-trained **MobileNetV2** and is deployed using **Streamlit** for real-time predictions through image upload.

---

## 📹 Demo Video

🎥 **Watch Demo:** [Click Here]

This video demonstrates:
- Uploading images
- Getting instant predictions
- Viewing disease type with confidence levels

---

## 🚀 Features

- Detects 4 classes:
  - 🧫 Coccidiosis
  - 🦠 Salmonella
  - 🐣 Newcastle Disease
  - ✅ Healthy
- Built with Streamlit for an interactive and user-friendly interface
- Real-time prediction from fecal images
- High-accuracy deep learning model (92%+)
- Simple deployment and installation

---

## 🧠 Technologies Used

| Component     | Technology             |
|---------------|------------------------|
| Interface     | Streamlit              |
| Model         | TensorFlow, Keras      |
| Language      | Python                 |
| IDE           | Google Colab / VS Code |
| Deployment    | Localhost / Streamlit  |

---

## 🏗️ Project Structure

```bash
Poultry-Disease-Identifier/
├── app.py                   # Streamlit frontend
├── model/
│   └── poultry_model.h5     # Trained MobileNetV2 model
├── images/
│   ├── healthy_sample.jpg
│   ├── coccidiosis_sample.jpg
│   └── ...
├── utils.py                 # Helper functions
├── requirements.txt         # Required packages
├── demo_video.mp4           # Project demo
└── README.md                # Project documentation
