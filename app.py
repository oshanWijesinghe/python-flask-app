from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_cloud():
    return "Hello! I am ready for the Cloud Engineering Internship."

if __name__ == '__main__':
    # Running on 0.0.0.0 makes it accessible outside the container
    app.run(host='0.0.0.0', port=8080)