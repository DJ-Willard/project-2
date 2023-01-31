"""
Daniel Willard's Flask API.
"""

import os
import configparser
from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return "UOCIS docker demo!"

@app.route("/<path:filename>")
def show_file(filename):
    if '..' in filename or '~' in filename:
        return send_from_directory('pages', '403.html'), 403
    file_path = os.path.join('pages', filename)
    if os.path.isfile(file_path):
        return send_from_directory('pages', filename), 200
    return send_from_directory('pages', '404.html'), 404

if __name__ == "__main__":
    config = configparser.ConfigParser()
    if os.path.exists('credentials.ini'):
        config.read('credentials.ini')
        PORT = int(config['SERVER']['PORT'])
        DEBUG = config['SERVER'].getboolean('DEBUG')
    elif os.path.exists('default.ini'):
        config.read('default.ini')
        PORT = int(config['SERVER']['PORT'])
        DEBUG = config['SERVER'].getboolean('DEBUG')
    else:
        PORT = 5000
        DEBUG = True
    app.run(port=PORT, debug=DEBUG, host='0.0.0.0')
