import tensorflow as tf
import streamlit as st
from PIL import Image
import numpy as np
import base64

# Load the model
model = tf.keras.models.load_model(r'C:\Users\admin\Downloads\trained_plant_disease_model.keras')

# Class labels for PlantVillage dataset and their explanations with prevention
class_info = {
    0: ('Apple Scab', 'A fungal disease causing olive-green spots on leaves and fruits.', 
        'Prevention: Use disease-resistant varieties, apply fungicides, and prune trees to improve air circulation.'),
    1: ('Apple Black Rot', 'Causes black, sunken lesions on fruit and cankers on branches.', 
        'Prevention: Remove infected fruit and branches, use fungicides, and practice proper orchard sanitation.'),
    2: ('Apple Cedar Apple Rust', 'Orange spots appear on leaves; this is a fungal disease spread from cedar trees.', 
        'Prevention: Remove nearby cedar trees, apply fungicides, and plant resistant apple varieties.'),
    3: ('Apple Healthy', 'No disease present.', 
        'Prevention: Continue maintaining good orchard practices and regular monitoring.'),
    4: ('Blueberry Healthy', 'No disease present.', 
        'Prevention: Continue maintaining good agricultural practices.'),
    5: ('Cherry Powdery Mildew', 'A fungal disease causing white, powdery growth on leaves.', 
        'Prevention: Prune trees to allow better air circulation and apply fungicides.'),
    6: ('Cherry Healthy', 'No disease present.', 
        'Prevention: Maintain regular pruning and inspection.'),
    7: ('Corn Cercospora Leaf Spot Gray Leaf Spot', 'Causes gray or tan lesions on leaves, reducing photosynthesis.', 
        'Prevention: Rotate crops, plant resistant hybrids, and apply fungicides.'),
    8: ('Corn Common Rust', 'A fungal disease causing reddish-brown pustules on leaves.', 
        'Prevention: Plant resistant varieties and apply fungicides if necessary.'),
    9: ('Corn Northern Leaf Blight', 'Fungal disease with long, elliptical gray-green lesions on leaves.', 
        'Prevention: Rotate crops, plant resistant varieties, and apply fungicides.'),
    10: ('Corn Healthy', 'No disease present.', 
        'Prevention: Maintain proper crop rotation and regular monitoring.'),
    11: ('Grape Black Rot', 'Fungal disease causing black spots on leaves and fruit rot.', 
        'Prevention: Prune vines to increase airflow, remove diseased tissue, and apply fungicides.'),
    12: ('Grape Esca (Black Measles)', 'Fungal disease causing dark spots on leaves and wood rotting.', 
        'Prevention: Remove and destroy infected vines and avoid injuries to the vines.'),
    13: ('Grape Leaf Blight (Isariopsis Leaf Spot)', 'Fungal disease causing dark brown spots with yellow halos on leaves.', 
        'Prevention: Use fungicides and ensure proper vineyard sanitation.'),
    14: ('Grape Healthy', 'No disease present.', 
        'Prevention: Maintain regular vine pruning and monitor for signs of disease.'),
    15: ('Orange Haunglongbing (Citrus Greening)', 'A bacterial disease causing yellowing leaves and bitter, misshapen fruit.', 
        'Prevention: Control psyllid insect populations, remove infected trees, and practice sanitation.'),
    16: ('Peach Bacterial Spot', 'Small, dark lesions on leaves and fruit caused by bacteria.', 
        'Prevention: Use resistant varieties, apply bactericides, and avoid excessive nitrogen fertilization.'),
    17: ('Peach Healthy', 'No disease present.', 
        'Prevention: Continue monitoring and proper orchard care.'),
    18: ('Pepper, Bell Bacterial Spot', 'Bacterial disease causing dark, water-soaked spots on leaves and fruit.', 
        'Prevention: Use disease-free seeds, rotate crops, and apply bactericides.'),
    19: ('Pepper, Bell Healthy', 'No disease present.', 
        'Prevention: Maintain good farming practices and monitor for any signs of disease.'),
    20: ('Potato Early Blight', 'A fungal disease causing dark brown spots with concentric rings on leaves.', 
        'Prevention: Rotate crops, remove infected plant debris, and apply fungicides.'),
    21: ('Potato Late Blight', 'A fungal disease causing water-soaked lesions on leaves and stems.', 
        'Prevention: Use certified seed potatoes, rotate crops, and apply fungicides.'),
    22: ('Potato Healthy', 'No disease present.', 
        'Prevention: Practice crop rotation and monitor the field regularly.'),
    23: ('Raspberry Healthy', 'No disease present.', 
        'Prevention: Continue regular care and monitoring.'),
    24: ('Soybean Healthy', 'No disease present.', 
        'Prevention: Rotate crops and monitor for any pest or disease activity.'),
    25: ('Squash Powdery Mildew', 'White, powdery fungal growth on leaves.', 
        'Prevention: Prune plants for better air circulation and apply fungicides.'),
    26: ('Strawberry Leaf Scorch', 'Fungal disease causing dark purple spots on leaves.', 
        'Prevention: Remove affected leaves, improve air circulation, and apply fungicides.'),
    27: ('Strawberry Healthy', 'No disease present.', 
        'Prevention: Maintain good cultivation practices and regular monitoring.'),
    28: ('Tomato Bacterial Spot', 'Causes dark, water-soaked spots on leaves and fruit.', 
        'Prevention: Use certified disease-free seeds and rotate crops.'),
    29: ('Tomato Early Blight', 'Fungal disease causing brown lesions on lower leaves.', 
        'Prevention: Rotate crops, remove infected plant debris, and apply fungicides.'),
    30: ('Tomato Late Blight', 'Fungal disease causing water-soaked lesions on leaves and stems.', 
        'Prevention: Use disease-free seeds, apply fungicides, and rotate crops.'),
    31: ('Tomato Leaf Mold', 'Fungal disease causing yellow spots on upper leaf surfaces and mold underneath.', 
        'Prevention: Ensure good air circulation, avoid wetting leaves, and apply fungicides.'),
    32: ('Tomato Septoria Leaf Spot', 'Fungal disease causing small, dark spots on leaves.', 
        'Prevention: Rotate crops, apply fungicides, and remove infected leaves.'),
    33: ('Tomato Spider Mites Two-Spotted Spider Mite', 'Pests causing small yellow spots on leaves and webbing.', 
        'Prevention: Use miticides, introduce natural predators, and keep plants hydrated.'),
    34: ('Tomato Target Spot', 'Causes round, dark spots on leaves and fruit.', 
        'Prevention: Use resistant varieties and apply fungicides if necessary.'),
    35: ('Tomato Mosaic Virus', 'Viral disease causing mottled, yellow leaves and stunted growth.', 
        'Prevention: Use certified disease-free seeds, remove infected plants, and avoid handling plants too much.'),
    36: ('Tomato Yellow Leaf Curl Virus', 'Viral disease causing yellowing and curling of leaves.', 
        'Prevention: Control whiteflies and use resistant varieties.'),
    37: ('Tomato Healthy', 'No disease present.', 
        'Prevention: Maintain good agricultural practices and monitor for any signs of disease.')
}


def get_base64_of_bin_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Set a custom background image for the Streamlit app
background_image_path = r"C:\Users\admin\Downloads\Gemini_Generated_Image_tu3lrqtu3lrqtu3l.jpg"
bg_image_base64 = get_base64_of_bin_file(background_image_path)

# Apply the background image via CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_image_base64}");
        background-size: cover;
    }}
    h1 {{
        color: black !important;
    }}
    h2 {{
        color: black !important;
    }}
    .large-font {{
        font-size: 24px !important;
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title and subtitle with black font color
st.markdown("<h1>LEAF ALERT</h1>", unsafe_allow_html=True)
st.markdown("<h2>A systematic rapid plant disease detection</h2>", unsafe_allow_html=True)

# Upload multiple files
uploaded_files = st.file_uploader("Choose images...", type=["jpg", "jpeg", "png", "bmp", "gif"], accept_multiple_files=True)

# Custom CSS for glowing button
st.markdown(
    """
    <style>
    .button-85 {
      padding: 0.6em 2em;
      border: none;
      outline: none;
      color: rgb(255, 255, 255);
      background: #111;
      cursor: pointer;
      position: relative;
      z-index: 0;
      border-radius: 10px;
      user-select: none;
      -webkit-user-select: none;
      touch-action: manipulation;
      font-size: 20px;
    }

    .button-85:before {
      content: "";
      background: linear-gradient(
        45deg,
        #ff0000,
        #ff7300,
        #fffb00,
        #48ff00,
        #00ffd5,
        #002bff,
        #7a00ff,
        #ff00c8,
        #ff0000
      );
      position: absolute;
      top: -2px;
      left: -2px;
      background-size: 400%;
      z-index: -1;
      filter: blur(5px);
      -webkit-filter: blur(5px);
      width: calc(100% + 4px);
      height: calc(100% + 4px);
      animation: glowing-button-85 20s linear infinite;
      transition: opacity 0.3s ease-in-out;
      border-radius: 10px;
    }

    @keyframes glowing-button-85 {
      0% {
        background-position: 0 0;
      }
      50% {
        background-position: 400% 0;
      }
      100% {
        background-position: 0 0;
      }
    }

    .button-85:after {
      z-index: -1;
      content: "";
      position: absolute;
      width: 100%;
      height: 100%;
      background: #222;
      left: 0;
      top: 0;
      border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display uploaded images and predictions
if uploaded_files:
    for uploaded_file in uploaded_files:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption=f'Uploaded Image - {uploaded_file.name}', use_column_width=True)

            # Process the image for prediction
            image = tf.keras.preprocessing.image.load_img(uploaded_file, target_size=(128, 128))
            input_arr = tf.keras.preprocessing.image.img_to_array(image)
            input_arr = np.array([input_arr])  # Convert single image to a batch.

            # Display the custom glowing "Predict" button
            if st.button("Predict"):
                # Predict the class
                prediction = model.predict(input_arr)
                predicted_class = np.argmax(prediction)
                disease_name, explanation, prevention = class_info[predicted_class]
                
                # Show prediction, disease explanation, and prevention
                st.markdown(f'<h3 style="color: black;">Prediction: {disease_name}</h3>', unsafe_allow_html=True)
                st.markdown(f'<h3 style="color: black;">Explanation: {explanation}</h3>', unsafe_allow_html=True)
                st.markdown(f'<h3 style="color: black;">Prevention: {prevention}</h3>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Please upload a valid image file: {uploaded_file.name}")

