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
def generate_text_from_ingredient(image):
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
    response = model.generate_content(["From the given image. You need to run this following tasks: 1. Identify the ingredient name 2. Suggest one popular meal name from the given image 3. List other ingredients from the meal name 4. Return the recipes containing other ingredients and steps on how to cook the meal 5. If the image is not an ingredient, just say I don't know", image], 
        stream=True)
    return response