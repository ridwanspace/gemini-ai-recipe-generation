import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
# Load API key
GEMINI_API_KEY= os.getenv('GEMINI_API_KEY') # Replace GEMINI_API to fetch an environment variable.
# Configure API
genai.configure(api_key=GEMINI_API_KEY)

# Define a function to generate text from an meal image
def generate_text_from_meal(image):
    """
    Generate text from an image.

    This function takes an image as input and uses a generative model to generate text based on the image content. The model used is 'gemini-pro-vision'. The function returns the generated text.

    Parameters:
    - image: The input image.

    Returns:
    - response: The generated text.
    """
    # load the model
    model = genai.GenerativeModel('gemini-pro-vision')
    # generate text
    response = model.generate_content([
        f"Write the menu name from the image and return the recipes containing ingredients and steps on how to cook it. If the image is not a food nor meal, just say I don't know", image], 
        stream=True)
    return response