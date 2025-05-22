# A-Multimodal-AI-Approach-to-Breast-Cancer-Detection-Using-Clinical-and-Histopathological-Data

## 🧠 Project Overview

This project presents a dual-model system for breast cancer detection using both **clinical (numerical)** and **histopathological (image)** data. By combining traditional machine learning and deep learning techniques, the system aims to improve diagnostic accuracy and provide a more robust decision support tool for medical professionals.

## 📊 Methodology

### 1. Clinical Data Model (Tabular Data)
- **Dataset**: Breast Cancer Wisconsin (Diagnostic) Dataset
- **Features**: 30 real-valued features computed from a digitized image of a fine needle aspirate (FNA) of a breast mass
- **Models Used**: 
  - Support Vector Machine (SVM)
  - Decision Tree
  - K-Nearest Neighbors (KNN)
  - Naive Bayes
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1-Score

### 2. Histopathological Image Model (Image Data)
- **Dataset**: Histopathology images from breast cancer patients
- **Preprocessing**: 
  - Image resizing
  - Noise augmentation using `random_noise`
  - Normalization and grayscale conversion
- **Model Used**: Custom Convolutional Neural Network (CNN)
- **Evaluation**: Accuracy and loss tracking during training/validation

### 3. Web Interface
- **Framework**: Flask
- **Routes**:
  - `/predict-tabular`: Accepts clinical data and returns model predictions
  - `/predict-image`: Accepts histopathology images and returns classification
- **Frontend**: Simple HTML, CSS, JavaScript for image and tabular data input

---
📈 Results
Model	Accuracy
SVM (Tabular)	~97%
CNN (Images)	~85%


