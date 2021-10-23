import views
from __main__ import app

@app.route("/", methods=["GET"])
def index():
    return views.loginView()

@app.route('/login', methods=['POST'])
def login():
    return views.indexView()

@app.route('/test', methods=['GET'])
def test():
    return 'it works!'