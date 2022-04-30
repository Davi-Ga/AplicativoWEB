# Previous imports remain...
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from dotenv import load_dotenv
import os
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

import app
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URL'))
db = SQLAlchemy(app)
migrate = Migrate(app, db)