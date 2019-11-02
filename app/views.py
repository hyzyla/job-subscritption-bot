from app import app


@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

