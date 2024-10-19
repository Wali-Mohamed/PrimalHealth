import streamlit as st
import base64
import uuid
from rag import rag  # Assuming rag is your custom function

# Function to encode the local image file as base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

# Set the page configuration
st.set_page_config(page_title="Primal Health Bot", layout="wide")

# Load the image and encode it in base64
image_path = "./images/healthy_food.jpg"  # Replace with your local image path
base64_image = get_base64_image(image_path)

# Custom CSS to style the background, input box, and feedback buttons
st.markdown(
    f"""
    <style>
    /* Full-page background using base64-encoded image */
    .stApp {{
        background-image: url("data:image/jpg;base64,{base64_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        height: 100vh;  /* Ensure the background takes the full viewport */
        overflow: hidden;
    }}

    /* Centering the input box */
    .centered {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-top: 10vh;
    }}

    /* Styling the input box */
    .input-container {{
        background-color: rgba(0, 0, 0, 0.7);  /* Darker background for readability */
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        width: 90%;  /* Set a width to avoid stretching */
        max-width: 600px;  /* Maximum width to keep the input compact */
        color: white;  /* Ensure text is visible */
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);  /* Add a shadow for better contrast */
    }}

    /* Customizing the input field */
    input {{
        width: 70% !important;  /* Set the width of the input field */
        padding: 15px;
        margin: 15px auto;
        border-radius: 10px;
        border: 1px solid #ccc;
        font-size: 16px;
        display: block;
    }}

    /* Styling the answer box */
    .answer-box {{
        background-color: rgba(0, 0, 0, 0.85);  /* Darker background for answers */
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        width: 90%;
        max-width: 600px;
        text-align: center;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);  /* Add shadow */
    }}

    /* Styling for feedback buttons */
    .feedback-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 20px;
        margin-top: 20px;
    }}

    .feedback-button {{
        font-size: 30px;
        cursor: pointer;
    }}
    
    .feedback-button:hover {{
        transform: scale(1.1);  /* Slight zoom on hover */
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

# Initialize session state for the input field and result
if 'question' not in st.session_state:
    st.session_state.question = ''
if 'result' not in st.session_state:
    st.session_state.result = None

# Handle the "Ask" button click
if st.button("Ask", key="ask_button"):
    if st.session_state.question:
        # Handle the question and get the response
        result = handle_question(st.session_state.question)
        if result:
            st.session_state.result = result
            # Clear the question input
            st.session_state.question = ''
    else:
        st.error("Please enter a question.")

# Input box for asking a question (Render after updating session state)
question = st.text_input("Enter your question here...", key="question")

# If there's a result, display it and the feedback section
if st.session_state.result:
    result = st.session_state.result
    # Display the answer with a darker background
    st.markdown(
        f"""
        <div class="answer-box">
            <h2>Answer:</h2>
            <p>{result['answer']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Feedback section with thumbs up and thumbs down
    st.markdown(
        """
        <div class="feedback-container">
            <span class="feedback-button">👍</span>
            <span class="feedback-button">👎</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Feedback handling
    feedback = st.radio(
        "Was this answer helpful?",
        options=[1, -1],
        format_func=lambda x: "Yes 👍" if x == 1 else "No 👎",
        key="feedback_radio"
    )

    if st.button("Submit Feedback", key="feedback_button"):
        handle_feedback(result['conversation_id'], feedback)
        # Clear session state variables related to the result
        st.session_state.result = None

# Close the centered div
st.markdown('</div>', unsafe_allow_html=True)
