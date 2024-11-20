import os
import google.generativeai as genai
from flask import Flask, request, jsonify,render_template
# from generativeai import callingai
from werkzeug.utils import secure_filename
from PIL import Image  # Added for image processing


def generate_ai_response(prompt):
    os.environ['GOOGLE_API_KEY'] = "AIzaSyBRcheUk41qwLVjgrzvYPepUyE3QY9aSGQ"
    genai.configure(api_key="AIzaSyBRcheUk41qwLVjgrzvYPepUyE3QY9aSGQ")
    # genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response

def callingai(input):
    responce=(generate_ai_response(input))
    print(responce)
    result=responce.candidates[0].content.parts[0].text
    plain_text = result.replace('**', '').replace('*', '').replace('\\n', '\n').strip()
    print(plain_text)
    return plain_text

def pregnency_traker(input):
    responce=(generate_ai_response(input))
    # print(responce)
    result=responce.candidates[0].content.parts[0].text
    result=result.replace('**', '').replace('\\n', '\n').strip()
    print(result)
    return result



