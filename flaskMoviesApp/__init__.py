from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from secrets import token_hex

app = Flask(__name__)


## Configuration για τα Secret Key, WTF CSRF Secret Key
# app.config["SECRET_KEY"] = "33587511ef534341a6af8b36fa4eb2ff"
app.config["SECRET_KEY"] = token_hex(16)
# app.config["WTF_CSRF_SECRET_KEY"] = "b068a6cda79f982875b45f792602ff08"
app.config["WTF_CSRF_SECRET_KEY"] = token_hex(16)

## Configuration για το SQLAlchemy Database URL
## Το όνομα του αρχείου της βάσης δεδομένων θα πρέπει να είναι 'flask_movies_database.db'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flask_movies_database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


### Αρχικοποίηση της Βάσης, και άλλων εργαλείων ###
### Δώστε τις σωστές τιμές παρακάτω ###
db = SQLAlchemy(app)


## Configuration του bcrypt
bcrypt = Bcrypt(app)


### Αρχικοποίηση του login_manager
login_manager = LoginManager(app)


login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Συνδεθείτε για πρόσβαση σε αυτή τη σελίδα'


from flaskMoviesApp import routes



