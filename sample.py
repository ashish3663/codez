# ip = 'example_ip'
# port = 'example_port'
    requests.post(ip + port, data={'username': username, 'password': password})
    return 'Login request sent'

if __name__ == '__main__':
    app.run()
