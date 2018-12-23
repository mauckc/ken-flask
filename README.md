# simple-flask
This repository serves as reference for building out flask applications with minimal effort

## Sample
### how-to-build-a-web-app-using-pythons-flask-and-google-app-engine
https://medium.freecodecamp.org/how-to-build-a-web-app-using-pythons-flask-and-google-app-engine-52b1bb82b221

## Flask
[Flask.pocoo.org](http://Flask.pocoo.org)
From the Flask organization website listed above you are able to take the following 5-line python program for a loadable hello world implementation of Flask. Yes, it is just this easy...

### Flask is Fun
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```

### And Easy to Setup
to run the hello world app on your local network you can run the app simply by typing the following into your command prompt or terminal.
```shell
$ pip install Flask
$ FLASK_APP=hello.py flask run
 * Running on http://localhost:5000/
```
