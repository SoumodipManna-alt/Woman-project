from prompt import constant
import generativeai, generativeai_for_photo
from flask import Flask, request, jsonify, render_template,redirect, url_for,session
from flask_cors import CORS, cross_origin
import os
import smtplib
from smtplib import SMTPRecipientsRefused
from werkzeug.utils import secure_filename
from PIL import Image 
import uuid 
from connection_with_sql import fatch_data, store_information
app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

app.secret_key = os.urandom(24)
# Set the folder to store uploaded files
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
     return render_template('index.html')  
    #  return render_template('low_your_periodpain.html')
    # return render_template('fasion_tips_with_skin_tone_photo.html')
                              
@app.route('/login_page')
def login_page():
      return render_template('loginpage.html')                             
                               
@app.route('/sign_page')
def sign_page():
      return render_template('sign_page.html')    
    
@app.route('/your_safty_y')
def your_safty_y():
    return render_template('your_safty.html') 
    

@app.route('/Low_your_period_pain_n')
def Low_your_period_pain_n():
    return render_template('low_your_periodpain.html') 

@app.route('/cycle_traker_r')
def cycle_traker_r():
    return render_template('cycle_traker.html')

@app.route('/fasion_tips_s')
def fasion_tips_s():
    return render_template('fasion_tips.html')

@app.route('/occasion_wise_outfit_t')
def occasion_wise_outfit_t():
    return render_template('occasion_wise_outfit.html')


@app.route('/fasion_tips_with_skin_tone_photo_o')
def fasion_tips_with_skin_tone_photo_o():
    return render_template('fasion_tips_with_skin_tone_photo.html')

@app.route('/hair_care_e')
def hair_care_e():
    return render_template('hair_care.html')



@app.route('/skin_care_tips_s')
def skin_care_tips_s():
    return render_template('skin_type_tips.html')

@app.route('/glow_skin_n')
def glow_skin_n():
    return render_template('glow_skin.html')
@app.route('/pimple_remove_e')
def pimple_remove_e():
    return render_template('pimple_remove.html')
@app.route('/skin_care_e')
def skin_care_e():
    return render_template('skin_care.html')


@app.route('/pregnency_tracker_r')
def pregnency_tracker_r():
    return render_template('pregnency_tracker.html')


@app.route('/Exercise_and_Fitness')
def Exercise_and_Fitness():
    return render_template('Exercise_fitness.html')

@app.route('/diet_plan_n')
def diet_plan_n():
    return render_template('diet_plan.html')


@app.route('/fitness_diet_plane_e')
def fitness_diet_plane_e():
    return render_template('fitness_diet_plane.html')


                                    #***fetch user detail**#
                                    
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    respose=fatch_data.fatch_information(username,password)
    if respose==True:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})



@app.route('/main_front_page')
def main_front_page():
    if 'user_id' in session:
        return render_template('main_fornt_page.html')  # Replace with your main page template
    return redirect(url_for('login_page'))  # Redirect if user is not logged in


                            #*** store user information ****#



@app.route('/store_user_information', methods=['POST'])
def store_user_information():
    name = request.form.get('name')
    mobile_number = request.form.get('mobile_number')
    email = request.form.get('email')
    password = request.form.get('password')
    
    # For debugging, print the captured data
    print(name, mobile_number, email, password)
    
    # Ensure all required data is present
    if name and mobile_number and email and password:
        # Return a JSON response with status 200
        responce=store_information.store_data_information(name, mobile_number, email, password)
        return jsonify({'success': True, 'message': responce}), 200
    else:
        # Return an error message with status 400
        return jsonify({'success': False, 'message': 'Incomplete data received'}), 400


                                #### BACK END #######
                                #### BACK END #######
                                #### BACK END #######









@app.route('/low_your_period_pain', methods=['POST'])
def low_your_period_pain():
    data = request.get_json()  
    symptoms = data.get('symptoms')  
    if symptoms:
        try:
            prompt = constant.prompt_for_low_your_period_pain + symptoms
            answer = generativeai.callingai(prompt)  
            return jsonify({'Excercises': answer})  
        except Exception as e:
            return jsonify({'error': str(e)}), 500  
    return jsonify({'error': 'Invalid symptoms'}), 400

@app.route('/pregnency_tracker', methods=['POST'])
def pregnency_tracker():
    data = request.get_json()  
    month = data.get('month')
    if month:
        try:
            prompt = constant.prompt_for_pragnency_traker.format(month=month)
            answer = generativeai.pregnency_traker(prompt)  
            return jsonify({'tips': answer})  
        except Exception as e:
            return jsonify({'error': str(e)}), 500  
    return jsonify({'error': 'Invalid symptoms'}), 400

@app.route('/fasion_tips_with_skin_tone_photo', methods=['POST'])
@cross_origin(supports_credentials=True)
def fasion_tips_with_skin_tone_photo():
    if 'image' not in request.files:
        return jsonify({"message": "No image uploaded"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    # Save the file to the server
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Call your AI function with the uploaded image
    prompt = constant.prompt_for_fashion_with_photo
    ai_response = generativeai_for_photo.generate_ai_response(prompt, file_path)

    return jsonify({"message": "Image uploaded successfully", "ai_response": ai_response})
@app.route('/hair_care', methods=['POST'])
@cross_origin(supports_credentials=True)
def hair_care():
    # print("h")
    data=request.get_json()
    # print(data)
    hair_type=data.get('hair_type')
    weather=data.get('weather')
    # print(hair_type,weather)
    if hair_type or weather:
        try:
            prompt=constant.prompt_for_hair_care.format(hair_type=hair_type,weather=weather)
            answer = generativeai.callingai(prompt)  
            return jsonify({'tips': answer})  
        except Exception as e:
            return jsonify({'error': str(e)}), 500  
    return jsonify({'error': 'Invalid symptoms'}), 400

@app.route('/skin_care', methods=['POST'])
@cross_origin(supports_credentials=True)
def skin_care():
    image=request.files.get('image')
    prompt=request.form.get('prompt')
    skin=request.form.get('skin')
    if 'image' not in request.files:
        return jsonify({"message": "No image uploaded"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    # Save the file to the server
    filename = f"{uuid.uuid4()}_{secure_filename(file.filename)}"
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Ensure the upload directory exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # Save the file to the server
    file.save(file_path)
    prompt=constant.prompt_for_skin_care_tips.format(question=prompt,skin=skin)
    print(prompt)
    ai_response = generativeai_for_photo.generate_ai_response(prompt, file_path)

    return jsonify({"message": "Image uploaded successfully", "ai_response": ai_response})


@app.route('/occasion_wise_outfit', methods=['POST'])
@cross_origin(supports_credentials=True)
def occasion_wise_outfit():
    image=request.files.get('image')
   
    event=request.form.get('event')
    if 'image' not in request.files:
        return jsonify({"message": "No image uploaded"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    # Save the file to the server
    # filename = f"{uuid.uuid4()}_{secure_filename(file.filename)}"
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Ensure the upload directory exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # Save the file to the server
    file.save(file_path)
    # print(event)
    prompt=constant.prompt_for_occasion_wise_outfit.format(event=event)
    # print(prompt)
    ai_response = generativeai_for_photo.generate_ai_response(prompt, file_path)

    return jsonify({"message": "Image uploaded successfully", "ai_response": ai_response})


@app.route('/pimple_remove', methods=['POST'])
@cross_origin(supports_credentials=True)
def pimple_remove():
    image=request.files.get('image')
   
    skin=request.form.get('skin')
    if 'image' not in request.files:
        return jsonify({"message": "No image uploaded"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    # Save the file to the server
    # filename = f"{uuid.uuid4()}_{secure_filename(file.filename)}"
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Ensure the upload directory exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # Save the file to the server
    file.save(file_path)
    # print(event)
    prompt=constant.prompt_for_pimple_remove.format(skin=skin)
    # print(prompt)
    ai_response = generativeai_for_photo.generate_ai_response(prompt, file_path)

    return jsonify({"message": "Image uploaded successfully", "ai_response": ai_response})
    

@app.route('/glow_skin', methods=['POST'])
@cross_origin(supports_credentials=True)
def glow_skin():
    image=request.files.get('image')
   
    skin=request.form.get('skin')
    if 'image' not in request.files:
        return jsonify({"message": "No image uploaded"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    # Save the file to the server
    # filename = f"{uuid.uuid4()}_{secure_filename(file.filename)}"
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Ensure the upload directory exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # Save the file to the server
    file.save(file_path)
    # print(event)
    prompt=constant.prompt_for_glow_skin.format(skin=skin)
    # print(prompt)
    ai_response = generativeai_for_photo.generate_ai_response(prompt, file_path)

    return jsonify({"message": "Image uploaded successfully", "ai_response": ai_response})


@app.route('/cycle_traker', methods=['POST'])
@cross_origin(supports_credentials=True)
def cycle_traker():
    date=request.form['date']
    prompt=constant.prompt_for_cycle_traker.format(date=date)
    answer = generativeai.callingai(prompt)  
    return jsonify({'message': answer})  

@app.route('/Exercise_fitness', methods=['POST'])
@cross_origin(supports_credentials=True)
def Exercise_fitness():
    height=request.form['height']
    weight=request.form['weight']
    age=request.form['age']
    prompt=constant.prompt_for_Exercise_fitness.format(height=height,weight=weight,age=age)
    answer = generativeai.callingai(prompt)  
    return jsonify({'message': answer})  


@app.route('/diet_plan', methods=['POST'])
@cross_origin(supports_credentials=True)
def diet_plan():
    height=request.form['height']
    
    weight=request.form['weight']
    age=request.form['age']
    print(height,weight,age)
    prompt=constant.prompt_for_Exercise_diet.format(height=height,weight=weight,age=age)
    # print(prompt)
    answer = generativeai.callingai(prompt)  
    return jsonify({'message': answer})  



@app.route('/your_safty', methods=['POST'])
@cross_origin(supports_credentials=True)
def your_safty():
    # Get JSON data from the request
    data = request.get_json()

    # Extract contact and location data from the JSON
    receiver_email = data.get('contact')
    location = data.get('location', {})
    latitude = location.get('latitude')
    longitude = location.get('longitude')

    # Process or store data as needed
    print(f"Received contact: {receiver_email}")
    print(f"Location - Latitude: {latitude}, Longitude: {longitude}")

    OWN_EMAIL = "womanproject8@gmail.com"
    OWN_PASSWORD = "anok hgke siar yezr"
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
    email_message = f"Subject:Safety Message\n\nPlease Help Me!\n\nLive Location:\n{google_maps_link}"

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(OWN_EMAIL, OWN_PASSWORD)
            server.sendmail(OWN_EMAIL, receiver_email, msg=email_message)
        return jsonify({"status": "success", "message": "sent Email"}), 200

    except SMTPRecipientsRefused:
        # Handle invalid email error
        return jsonify({"status": "error", "message": "Invalid email address provided"}), 400

    except Exception as e:
        # Handle any other exceptions
        return jsonify({"status": "error", "message": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)
