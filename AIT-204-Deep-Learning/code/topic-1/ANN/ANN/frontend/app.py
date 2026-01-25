import streamlit as st
import numpy as np
from PIL import Image, ImageOps
from streamlit_drawable_canvas import st_canvas
import sys
import os

# Add parent directory to path for backend imports (works locally and on Streamlit Cloud)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(SCRIPT_DIR)
if PARENT_DIR not in sys.path:
    sys.path.insert(0, PARENT_DIR)

from backend.model import MNISTModel

# Page configuration
st.set_page_config(
    page_title="MNIST Digit Recognition",
    page_icon="🔢",
    layout="wide"
)

# Initialize session state
if 'model' not in st.session_state:
    st.session_state.model = None
    st.session_state.model_loaded = False


@st.cache_resource
def load_model():
    """Load the trained model"""
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_dir, '..', 'mnist_model.h5')
    
    model = MNISTModel(model_path=model_path)
    if model.load_model():
        return model
    else:
        return None


def preprocess_canvas_image(canvas_data):
    """
    Preprocess the canvas drawing for model prediction.
    Properly centers and scales the digit to match MNIST format.
    """
    if canvas_data is None:
        return None

    # Get image data (RGBA format from streamlit-drawable-canvas)
    img_rgba = canvas_data.image_data

    # Convert RGBA to grayscale properly
    # The canvas draws white (#FFFFFF) on black (#000000)
    # Use the max of RGB channels to capture the stroke
    if len(img_rgba.shape) == 3 and img_rgba.shape[2] >= 3:
        # Take max of RGB channels for better stroke detection
        img_gray = np.max(img_rgba[:, :, :3], axis=2).astype(np.uint8)
    else:
        img_gray = img_rgba.copy().astype(np.uint8)

    # Find bounding box of the digit (non-zero pixels)
    non_zero = np.where(img_gray > 20)  # Threshold to ignore noise
    
    if len(non_zero[0]) == 0 or len(non_zero[1]) == 0:
        return img_gray  # Return as-is if nothing drawn
    
    # Get bounding box
    top, bottom = non_zero[0].min(), non_zero[0].max()
    left, right = non_zero[1].min(), non_zero[1].max()
    
    # Add small padding
    padding = 5
    top = max(0, top - padding)
    bottom = min(img_gray.shape[0], bottom + padding)
    left = max(0, left - padding)
    right = min(img_gray.shape[1], right + padding)
    
    # Crop to bounding box
    digit_crop = img_gray[top:bottom, left:right]
    
    # Make it square by padding the shorter dimension
    h, w = digit_crop.shape
    max_dim = max(h, w)
    
    # Create square canvas with black background
    square_img = np.zeros((max_dim, max_dim), dtype=np.uint8)
    
    # Center the digit in the square
    y_offset = (max_dim - h) // 2
    x_offset = (max_dim - w) // 2
    square_img[y_offset:y_offset+h, x_offset:x_offset+w] = digit_crop
    
    # Convert to PIL for high-quality resizing
    img_pil = Image.fromarray(square_img, mode='L')
    
    # Resize to 20x20 (MNIST digits are ~20x20 centered in 28x28)
    img_20 = img_pil.resize((20, 20), Image.Resampling.LANCZOS)
    
    # Create 28x28 canvas and center the 20x20 digit (like MNIST)
    img_28 = Image.new('L', (28, 28), color=0)
    img_28.paste(img_20, (4, 4))  # 4 pixels padding on each side
    
    # Convert to numpy array
    img_array = np.array(img_28)

    return img_array


def preprocess_uploaded_image(uploaded_file):
    """Preprocess an uploaded image for model prediction"""
    img = Image.open(uploaded_file)

    # Convert to grayscale
    img = img.convert('L')

    # Resize to 28x28
    img = img.resize((28, 28), Image.Resampling.LANCZOS)

    # Convert to numpy array
    img_array = np.array(img)

    # Check if image needs inversion (if background is brighter than digit)
    # MNIST expects bright digits on dark background
    mean_value = np.mean(img_array)
    if mean_value > 127:  # Image has bright background
        img_array = 255 - img_array  # Invert

    return img_array


# App title and description
st.title("🔢 MNIST Handwritten Digit Recognition")
st.markdown("""
This app uses an Artificial Neural Network (ANN) to recognize handwritten digits (0-9).
You can either draw a digit or upload an image!
""")

# Sidebar
with st.sidebar:
    st.header("Model Information")

    # Load model button
    if st.button("Load Model"):
        with st.spinner("Loading model..."):
            model = load_model()
            if model:
                st.session_state.model = model
                st.session_state.model_loaded = True
                st.success("Model loaded successfully!")
            else:
                st.error("Model not found. Please train the model first by running: python backend/model.py")

    if st.session_state.model_loaded:
        st.success("✓ Model is ready")
    else:
        st.warning("⚠ Model not loaded")

    st.markdown("---")
    st.markdown("### About")
    st.markdown("""
    - **Dataset**: MNIST (60K training, 10K test)
    - **Model**: ANN (Fully Connected)
    - **Architecture**: 784→512→256→128→10
    - **Input**: 28x28 grayscale images (flattened to 784)
    - **Output**: Digit (0-9)
    - **Accuracy**: ~97-98%
    """)

# Main content
col1, col2 = st.columns(2)

with col1:
    st.subheader("Draw a Digit")

    # Canvas for drawing
    canvas_result = st_canvas(
        fill_color="rgba(0, 0, 0, 0)",
        stroke_width=20,
        stroke_color="#FFFFFF",
        background_color="#000000",
        height=280,
        width=280,
        drawing_mode="freedraw",
        key="canvas",
    )

    st.info("💡 Tip: Draw large, centered digits with thick strokes for best results")

    if st.button("Recognize Drawn Digit"):
        if not st.session_state.model_loaded:
            st.error("Please load the model first!")
        elif canvas_result.image_data is not None:
            # Preprocess image
            img_array = preprocess_canvas_image(canvas_result)

            if img_array is not None and np.sum(img_array) > 0:
                # Make prediction
                with st.spinner("Recognizing..."):
                    predicted_digit, confidence = st.session_state.model.predict(img_array)

                # Display results
                st.success(f"Predicted Digit: **{predicted_digit}**")
                st.write(f"Confidence: **{confidence[predicted_digit]:.2%}**")

                # Display confidence for all digits
                with st.expander("View all confidence scores"):
                    for digit in range(10):
                        st.write(f"{digit}: {confidence[digit]:.2%}")

                # Show preprocessed image
                with st.expander("View preprocessed image"):
                    st.image(img_array, caption="28x28 preprocessed", width=200, clamp=True)
            else:
                st.warning("Please draw a digit first!")

with col2:
    st.subheader("Upload an Image (Recommended)")

    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=['png', 'jpg', 'jpeg'],
        help="Upload an image of a handwritten digit. White digit on black background works best."
    )

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        if st.button("Recognize Uploaded Digit"):
            if not st.session_state.model_loaded:
                st.error("Please load the model first!")
            else:
                # Preprocess image
                img_array = preprocess_uploaded_image(uploaded_file)

                # Make prediction
                with st.spinner("Recognizing..."):
                    predicted_digit, confidence = st.session_state.model.predict(img_array)

                # Display results
                st.success(f"Predicted Digit: **{predicted_digit}**")
                st.write(f"Confidence: **{confidence[predicted_digit]:.2%}**")

                # Display confidence for all digits
                with st.expander("View all confidence scores"):
                    for digit in range(10):
                        st.write(f"{digit}: {confidence[digit]:.2%}")

                # Show preprocessed image
                with st.expander("View preprocessed image"):
                    st.image(img_array, caption="28x28 preprocessed", width=200, clamp=True)

# Footer
st.markdown("---")
st.markdown("Built with Streamlit and TensorFlow")
