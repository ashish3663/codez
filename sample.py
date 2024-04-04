from flask import Flask, request
import requests  

app = Flask(__name__)

@app.route('/login')
def login():
    username = 'ashish'
    password = 'ashish@123'
    ip = '10.0.0.1'  


    requests.post(f'http://{ip}', data={'username': username, 'password': password}) 
    return 'Login request sent'
