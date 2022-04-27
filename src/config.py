from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')

DATABASE_CONNECT_OPTIONS = {
    'NAME': str(os.getenv('POSTGRES_NAME')),
    'USER': str(os.getenv('POSTGRES_USER')),
    'PASSWORD': str(os.getenv('POSTGRES_PASSWORD')),
    'HOST': str(os.getenv('POSTGRES_SERVER')),
    'PORT': str(os.getenv('POSTGRES_PORT')),
}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = str(os.getenv('CSRF_SESSION_KEY'))

# Secret key for signing cookies
SECRET_KEY = str(os.getenv('SECRET_KEY'))
