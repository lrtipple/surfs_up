#import dependency
from flask import Flask
# create a new flask app instance
app = Flask(__name__)

# create Flask route
@app.route('/')
def hello_world():
    return 'Hello world'



