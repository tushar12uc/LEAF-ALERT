Leaf Alert
Leaf Alert is a deep learning project designed to detect and classify diseases in plant leaves. The project uses a Convolutional Neural Network (CNN) model built with TensorFlow and Keras to accurately identify different types of plant diseases from images.

Project Overview
Leaf Alert aims to assist farmers and agricultural experts in identifying plant diseases at an early stage. By leveraging deep learning techniques, the model can classify different types of plant diseases, enabling timely intervention and treatment.

Dataset
The project utilizes the PlantVillage dataset which contains thousands of labeled images of healthy and diseased plant leaves.

Classes: Various plant species and corresponding disease categories.
Image Size: 128x128 pixels (standardized during preprocessing).
Model Architecture
The model is a Convolutional Neural Network (CNN) built using TensorFlow and Keras, featuring:

Input Layer: 128x128x3 (RGB images).
Convolutional Layers: Multiple layers with ReLU activation and max-pooling.
Dense Layers: Fully connected layers leading to the output.
Output Layer: Softmax activation for multi-class classification.

Installation:

To run the project locally, follow these steps:

Clone the repository:


git clone https://github.com/chintu-1p/leaf-alert.git
cd leaf-alert

Download the dataset from Kaggle and place it in the appropriate directory.

Usage:

Train the Model:

Train the model using the provided notebook on Kaggle or any other platform of your choice.
Once trained, save the model on your local device.
Create the Streamlit UI:

Use the app.py file in VS Code to create the Streamlit UI.
Load the saved model in app.py.
Predict the Image:

Use the UI to upload an image and get predictions from the model.

Results
The CNN model achieved the following metrics on the validation set:

Training Accuracy: 95%
Validation Accuracy: 96%
These results indicate good model performance.

Future Work
Model Optimization: Address overfitting by experimenting with regularization techniques.
Dataset Expansion: Include more classes and images to improve model robustness.
Deployment: Deploy the model as a web app using Streamlit or Gradio.
