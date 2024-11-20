import requests


def call(month):
    url = 'http://127.0.0.1:5000/pregnency_tracker'
    payload = {
        'month': month
    }

    # Make the POST request
    response = requests.post(url, json=payload)

    # Check the status code
    if response.status_code == 200:
        try:
            # Store the response in a variable
            response_data = response.json()  # if the response is in JSON format
            # Print the response data
            print(response_data)
        except requests.exceptions.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            print(f"Response text: {response.text}")
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(f"Response text: {response.text}")

symptoms="10"
call(symptoms)