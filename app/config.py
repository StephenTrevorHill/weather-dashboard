import os

from dotenv import load_dotenv

# read environments variables
load_dotenv()

APP_ENV = os.getenv('APP_ENV', 'development')

APP_VERSION = '0.7'
