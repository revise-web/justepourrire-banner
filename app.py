from flask import Flask, send_from_directory
from banner import get_subscriber_count, create_banner
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Bannière dynamique JustePourRire</h1><img src="/banner.png">'

@app.route('/banner.png')
def serve_banner():
    subs = get_subscriber_count()
    create_banner(subs)
    return send_from_directory('static', 'banner.png')

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    app.run(host='0.0.0.0', port=10000)
