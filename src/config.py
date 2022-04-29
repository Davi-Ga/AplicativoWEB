# Previous imports remain...
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import app


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URL'))
db = SQLAlchemy(app)
migrate = Migrate(app, db)