from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  


GMAIL_USER = 'nowfal.riyas1996@gmail.com'
GMAIL_PASSWORD = 'mkvqprykxxpqtevz'

@app.route('/')
def home():
    return 'Flask server is running'

@app.route('/sendemail', methods=['POST'])
def send_email():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    mobile = data.get('mobile')
    subject = data.get('subject')
    message = data.get('message')

    subject = subject
    body = f'Name: {name}\nEmail: {email}\nMobile: {mobile}\nMessage: {message}'

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = GMAIL_USER  # Send to yourself
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(GMAIL_USER, GMAIL_USER, text)
        server.quit()
        return jsonify({'message': 'Email sent successfully'}), 200
    except Exception as err:
        print(err)
        return jsonify({'message': 'Failed to send email'}), 500

if __name__ == '__main__':
    app.run(debug=True)
