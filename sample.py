from flask import Flask, request
import requests  # Import requests module

app = Flask(__name__)

@app.route('/login')
def login():
    username = 'example_username'
    password = 'example_password'
    #ip = 'example_ip'  
    #port = 'example_port' 

    response = requests.post(f'http://{ip}:{port}', data={'username': username, 'password': password})  # Send POST request
    return 'Login request sent'
