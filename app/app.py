from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from NAB SRE Pipeline!",
        "status": "healthy",
        "version": "2.0"
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/info")
def info():
    return jsonify({
        "app": "cicd-demo",
        "author": "Sang",
        "environment": "production"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
