# simple-flask
This repository serves as reference for building out flask applications with minimal effort

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
