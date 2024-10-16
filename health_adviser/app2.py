import streamlit as st
from transformers import pipeline

# Load your LLM model (this can be any pre-trained LLM you're using)
# Example with Hugging Face:
@st.cache_resource  # cache the model to avoid reloading it
def load_model():
    return pipeline("text-generation", model="gpt2")  # replace with your LLM

model = load_model()

# Streamlit app interface
st.title("Dietary Assistant LLM")
st.write("Ask anything related to your primal diet and health!")

# Get user input
user_input = st.text_input("Ask your question:")

# If user inputs a query
if user_input:
    # Generate a response from the model
    with st.spinner('Generating a response...'):
        result = model(user_input, max_length=200, num_return_sequences=1)
        st.write(result[0]['generated_text'])  # Output the generated text
