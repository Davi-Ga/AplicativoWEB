from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__,static_url_path='',static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URL'))
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from banco import routes

    

