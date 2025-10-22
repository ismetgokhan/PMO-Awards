from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "PMO Awards 2026 Backend Çalışıyor!"

if __name__ == "__main__":
    app.run()
