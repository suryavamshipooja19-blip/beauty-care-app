import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Smart Beauty Care App", page_icon="💄")
st.title("✨💄  Beauty Care App 💄✨ ")
st.write("Upload 📤a face image to detect your skin type and get product recommendations!")

# Load OpenCV Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Upload image
img_file_buffer = st.file_uploader("Upload 📤a face image", type=["jpg", "png"])


if img_file_buffer is not None:
    image = Image.open(img_file_buffer).convert("RGB")
    img_array = np.array(image)
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if len(faces) == 0:
        st.error("❌ Invalid picture! it is not a proper picture or  Please upload a single-person photo.")
    elif len(faces) > 1:
        st.error("❌ Invalid picture! No human face detected.")
    else:
        # Only one face detected
        x, y, w, h = faces[0]
        face_img = gray[y:y+h, x:x+w]

        brightness = np.mean(face_img)
        contrast = face_img.std()

        st.write(f"*Brightness:* {brightness:.2f}")
        st.write(f"*Contrast:* {contrast:.2f}")

        # Basic skin type logic
        if brightness > 160:
            skin_type = "Dry Skin"
        elif brightness < 90:
            skin_type = "Oily Skin"
        else:
            skin_type = "Normal Skin"

        st.subheader(f"🌸✨ Your Skin Type: {skin_type}")

        # Recommend products
        st.subheader("🧴🪞 Recommended Products:")
        if skin_type == "Dry Skin":
            st.markdown("""
            - Cetaphil Gentle Skin Cleanser  
            - Nivea Soft Moisturizing Cream  
            - The Face Soap Rice Water Bright Cleanser  
            """)
        elif skin_type == "Oily Skin":
            st.markdown("""
            - Neutrogena Oil-Free Acne Wash  
            - Himalaya Neem Face Wash  
            - Minimalist Salicylic Acid Serum  
            """)
        else:
            st.markdown("""
            - Pond’s Light Moisturizer  
            - L’Oreal Paris Hydrafresh Toner  
            - Plum Green Tea Night Gel  
            """)
else:
    st.info("Please upload a photo to start skin type analysis.")