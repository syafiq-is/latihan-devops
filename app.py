from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Buat metrik sederhana
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP Requests")


@app.route("/")
def home():
    REQUEST_COUNT.inc()  # Tambah jumlah request
    return "Selamat datang di dunia monitoring dengan Prometheus & Grafana!"


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
