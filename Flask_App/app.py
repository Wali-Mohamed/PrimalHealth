import streamlit as st
import base64

# Function to encode the local image file as base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

# Set the page configuration
st.set_page_config(page_title="Primal Health Bot", layout="wide")

# Load the image and encode it in base64
image_path = "./static/images/healthy_food.jpg"  # replace with your local image path
base64_image = get_base64_image(image_path)

# Custom CSS to style the background and input box with the encoded image
st.markdown(
    f"""
    <style>
    /* Full-page background using base64-encoded image */
    .stApp {{
        background-image: url("data:image/jpg;base64,{base64_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Centering the input box */
    .centered {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }}

    /* Styling the input box */
    .input-container {{
        background-color: rgba(0, 0, 0, 0.5); /* Transparent background */
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }}

    /* Customizing the input field */
    .input-container input {{
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        border-radius: 5px;
        border: 1px solid #ccc;
    }}

    /* Button styling */
    .stButton>button {{
        background-color: #28a745;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
    }}

    /* Button hover effect */
    .stButton>button:hover {{
        background-color: #218838;
    }}

    /* Text styling */
    h1, h2, h3 {{
        color: white;
    }}

    p {{
        color: white;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Create the centered input box layout
st.markdown('<div class="centered">', unsafe_allow_html=True)

# Create the content inside the input container
st.markdown(
    """
    <div class="input-container">
        <h1>Primal Health Bot</h1>
        <h3>By Wali M. Mohamed</h3>
        <p>Please ask anything about your primal health</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Create the input box
question = st.text_input("Enter your question here...")

# Create a button
if st.button("Ask"):
    st.write(f"Your question: {question}")

# Close the centered div
st.markdown('</div>', unsafe_allow_html=True)
