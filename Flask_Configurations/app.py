from flask import Flask
app = Flask(__name__)

#This is a decorator, which modifies the function that follows it (`hello_world()`).
# The `@app.route('/')` decorator means that
# this function will be run when the root URL of the application ('/') is accessed.

@app.route('/')
def hello_world():
    return 'Hello to the World of Flask!'
if __name__ == '__main__':
    app.run(debug=True)