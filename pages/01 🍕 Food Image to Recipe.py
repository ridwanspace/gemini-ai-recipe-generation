import streamlit as st
import PIL.Image
import time
from utils.meal_processor import generate_text_from_meal


st.title("🍕 Meal Image to Recipe")
st.markdown("Powered by Gemini AI :gemini:")
st.markdown("**How it works**")
st.markdown("Upload an image of a meal to get a recipe on how to cook it.")

# Upload an image
image = st.file_uploader("Upload a meal image", type=["jpg", "jpeg", "png"])

# Check if image is uploaded
if image is None:
    st.warning("Please upload an image")
    
else:
    # if image is uploaded, display it
    uploaded_image = PIL.Image.open(image)
    st.image(uploaded_image)
    
    # Generate button
    generate = st.button("Generate")
    # Generate text if generate button is clicked
    if generate:
        message_placeholder = st.empty()
        full_response = ""
        # pass chat messages to OpenAI client
        generated_text = generate_text_from_meal(uploaded_image)
        generated_text.resolve()
        # for streaming-like responses
        for response in generated_text.text.split("\n"):
            # update full_response
            full_response += response + "\n"
            time.sleep(0.2)
            # update message_placeholder
            message_placeholder.markdown(full_response + "▌")
        # update full_response    
        message_placeholder.markdown(full_response)
    