from flask import Flask, request

app = Flask(__name__)

@app.route('/login')
def login():
    username = 'example_username'
    password = 'example_password'
ip = 'example_ip'
port = 'example_port'
# ip = 'example_ip'
port = 'example_port'
    requests.post(ip + port, data={'username': username, 'password': password})
    return 'Login request sent'
