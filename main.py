from flask import Flask, request, jsonify
import json
from Tool import send_email_complete
# import logging
# logging.basicConfig(filename='logemail.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


app = Flask(__name__)
@app.route('/auth/emailotp', methods = ['POST'])
def rout_otp():
    # logging.info("Received request for /auth/emailotp")
    receivers_mail = request.form.get('receivers_mail')
    print(receivers_mail)
    context = request.form.get('context')

    send_email_complete(receivers_mail, context)
    return jsonify({
        'status': 'success'
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
