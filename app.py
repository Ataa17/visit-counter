from flask import Flask
import redis
import socket

app = Flask(__name__)
db = redis.Redis(host="db-service", port=6379, decode_responses=True)

@app.route("/")
def home():
    visits = db.incr("hits")
    container_id = socket.gethostname()
    return f"Bonjour ! Cette page a été vue {visits} fois. Je suis le conteneur {container_id}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
