from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! \n"

@application.route("/ready \n")
def ready():
    return "I am ready!"

@application.route("/health \n")
def health():
    return "I am healthy!"

if __name__ == "__main__":
    application.run()
