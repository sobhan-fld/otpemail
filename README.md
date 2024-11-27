# Flask Email OTP Service

## Overview
This project is a simple Flask-based REST API service designed to send an OTP (One-Time Password) email to a specified email address. It consists of three main Python scripts:

- **main.py**: The main Flask application that receives OTP requests.
- **Tool.py**: Contains utility functions for sending emails.
- **request-test.py**: A script to test the functionality of the OTP API endpoint.

The project is designed for easy integration into other applications where email verification is needed.

## Features
- Flask-based API for sending OTP emails.
- Uses SMTP to send emails to the provided address.
- Test script provided for quickly verifying the service.

## File Structure
- **main.py**: This is the core Flask application. It provides the `/auth/emailotp` endpoint to send OTPs to users via email.
- **Tool.py**: Contains the `send_email` and `send_email_complete` functions that handle the email composition and sending process.
- **request-test.py**: A simple script to send a test POST request to the `/auth/emailotp` endpoint.

## Setup Instructions

### Prerequisites
- Python 3.x
- Flask
- Requests

To install the required libraries, run:
```bash
pip install Flask requests
```

### Running the Application
1. Clone the repository.
2. Make sure to update the SMTP server information, sender email, and password in **Tool.py**.
3. Run the Flask application using:
   ```bash
   python main.py
   ```
4. By default, the server runs on port `652`. You can access the API endpoint at `http://127.0.0.1:652/auth/emailotp`.

### Testing the Application
- Use **request-test.py** to test the `/auth/emailotp` endpoint.
- Before running the test, make sure the Flask server is running.
- Run the test script:
  ```bash
  python request-test.py
  ```

## API Endpoint
### `/auth/emailotp` (POST)
- **Description**: Sends an OTP email to the provided email address.
- **Parameters**:
  - `receivers_mail` (form data): The email address of the recipient.
  - `context` (form data): The message or OTP to be sent.
- **Response**: JSON object indicating the success status.

## Notes
- Ensure that the SMTP server details in **Tool.py** are correctly configured to avoid email sending failures.
- You may need to allow less secure apps in your email provider settings to use the SMTP functionality.

## License
This project is open source and available under the [MIT License](LICENSE).

