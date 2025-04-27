from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Service is started.... By @The_TGguy'


if __name__ == "__main__":
    app.run()
