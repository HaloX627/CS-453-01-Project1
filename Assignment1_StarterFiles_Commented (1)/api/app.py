import os  # read env
from flask import Flask, jsonify  # flask API
import redis  # redis client

app = Flask(__name__)
r = redis.Redis(host=os.environ.get('REDIS_HOST','redis'), port=6379, decode_responses=True)

@app.get('/')
def index():
    count = r.incr('hits')  # increment key
    return jsonify(count=count)

@app.get('/health')
def health():
    try:
        r.ping()
        return jsonify(status='ok')
    except Exception as e:
        return jsonify(status='error', detail=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
