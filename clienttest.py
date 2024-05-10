import requests

# URL of the Flask app
url = "http://127.0.0.1:5000/auth/emailotp"

# Data to be sent in the request
data = {
    'receivers_mail': 'sobhan.fld2@gmail.com',
    'context': 'salam2345678'
}

# Sending a POST request to the Flask server
response = requests.post(url, data=data)

# Print the response from the server
print(response.text)
