import streamlit as st
from rag import rag
import base64

# Function to set background image using base64
def set_background(image_file):
    # Encode the image file to base64
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode()
    
    # Use the base64 string to set the background
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded_string}");
            background-size: cover;
            background-position:center;
            filter: brightness(80%);  /* Reduce brightness to 80% */
        }}
        .stApp::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(0, 0, 0, 0.2);  /* Dark overlay (30% opacity) */
            z-index: -1;
    }}
    
        </style>
        """,
        unsafe_allow_html=True
    )

set_background('../images/healthy_food.jpg')

def main():
    # Custom CSS for better alignment
        # Custom CSS for alignment and styling
    st.markdown("""
        <style>
        .title {
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            color: white;  /* Set title color to white */
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);  /* Add shadow for visibility */
            margin-bottom: 10px;
        }
        .sub-text {
            font-size:30px;
            font-weight:bold;
            color:white;
            text-align: center;
            margin-bottom: 10px;
            font-family:cursive;
        }
        .prompt-text {
            font-size: 25px;
            color: #ffffff;  /* Custom color for the text above the input */
            text-align: center;
            margin-bottom: 5px;
        }
        .text-box input {
            width: 100%;
            padding: 10px;
            border: 2px solid #ff9800 !important;  /* Border with orange color */
            outline:4px solid #00ff00 !important;; /* Add green outline */
            
            border-radius: 5px;
            font-size: 16px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);  /* Optional subtle shadow */
            margin-bottom: 20px;
            margin-top:20px;
    }
    
        .text-box {
            display: flex;
            justify-content: center;
            height:100px;
            width: 100%;
            margin-bottom: 20px;
            margin-top: 10px;
            }
        .input-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
        }
        </style>
        """, unsafe_allow_html=True)

    # Title
    st.markdown("""
        <div class="title">
            Primal Health Bot
        </div>
    """, unsafe_allow_html=True)

    # Subtitle
    st.markdown("""
        <div class="sub-text">
            By W.M.Mohamed
        </div>
    """, unsafe_allow_html=True)

    

    # Display the styled label using st.markdown()
    st.markdown('<span style="color:white;font-size:20px;">Please ask anything about your primal health</span>', unsafe_allow_html=True)

    # Input field for the user
    user_input = st.text_input("")  # Empty input box without a placeholder text

    if st.button("Ask"):
        with st.spinner('Processing...'):
            output = rag(user_input)  # Assuming rag() is your processing function
            st.success("Completed!")
            
            # Displaying output with white text
            st.markdown(f"""
                <div style="color:white;">
                    {output}
                </div>
            """, unsafe_allow_html=True)

        # Asking if the user found it helpful, with white text
        st.markdown('<span style="color:orange;">Did you find this helpful?</span>', unsafe_allow_html=True)

    
    # Adding feedback buttons (+1 / -1)

    if st.button("+1"):
        st.write("Feedback: +1")

    if st.button("-1"):
        st.write("Feedback: -1")

if __name__ == "__main__":
    main()

