from flask import Flask, abort, redirect, url_for, flash
from dotenv import load_dotenv
from os import environ

load_dotenv()

PORT = int(environ["PORT"])

app = Flask(__name__)

# import declared routes
import routes

if __name__ == "__main__":
    app.run(port=PORT, debug=True)