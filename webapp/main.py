from flask import *
app = Flask(__name__)


@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/home")
def home():
    return render_template('home.html')
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
