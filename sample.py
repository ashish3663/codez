from flask import Flask, request
import requests  # Import requests module

app = Flask(__name__)

@app.route('/login')
def login():
    username = 'ashish'
    password = 'ashish@123'
    #ip = '10.0.0.1'  
    #port = '9000' 

    result = requests.post(f'http://{ip}:{port}', data={'username': username, 'password': password})  # Send POST request
    return 'Login request sent'
