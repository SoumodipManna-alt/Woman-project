import os
import google.generativeai as genai
from flask import Flask, request, jsonify,render_template
# from generativeai import callingai
from werkzeug.utils import secure_filename
from PIL import Image  # Added for image processing






def generate_ai_response(prompt, image_path):
    os.environ['GOOGLE_API_KEY'] = "AIzaSyBRcheUk41qwLVjgrzvYPepUyE3QY9aSGQ"  # Replace with your actual API key
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
    model = genai.GenerativeModel('gemini-1.5-flash-8b')

    # Read image data
    try:
        img = Image.open(image_path)
        img = img.convert('RGB')  # Ensure image is in RGB mode if necessary
    except FileNotFoundError:
        return jsonify({"message": "Error: Image file not found"}), 500

    # Generate AI response using the image and prompt
    response = model.generate_content([prompt, img])

    # Extract necessary data from response (assuming response.text contains the relevant info)
    # print(response)
    result=response.candidates[0].content.parts[0].text  # Adjust this based on the actual response object structure
    result=result.replace('**', '').replace('\\n', '\n').strip()
    # print(response)
    return result