"""
Daniel Willard's Flask API.
"""

from flask import Flask
import os

app = Flask(__name__)

def file_check(file_path):
    if '..' in file_path or '~' in file_path:
        return 403
    try:
        with open(file_path, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        return 404

@app.route("/<file>")
def serve_file():
    file_path = 'web/pages/' +file
    result = check_file(file_path)
    if result == 404:
        return send_file('web/pages/404.html'), 404
    if result == 403:
        return send_file('web/pages/403.html'), 403
    return send_file(file_path)

if __name__ == "__main__":
    import configparser
    config = configparser.ConfigParser()
    file_names = ['credentials.ini', 'default.ini']
    for file_name in file_names:
        if os.path.exists(file_names):
            config.read(file_name)
            break
    port = config.getting('DEFAULT', 'port', fallback=5000)
    debug = config.getboolean('DEFAULT', 'debug', fallback=False)
    app.run(debug=debug, host='0.0.0.0', port=port)
