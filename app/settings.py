import os

ALLOWED_PAIRS = ['BRLBTC', 'BRLETH']

ABSOLUTE_PATH = os.path.abspath(__file__)
ROOT = os.path.dirname(ABSOLUTE_PATH)
BASE_DIR = os.path.dirname(ROOT)

env = os.environ

ENVIRONMENT = 'local'
BASE_PATH = '/mercado-bitcoin/v1'
HOST = '0.0.0.0'
PORT = '5000'
DEBUG = False
FLASK_ENV = 'development'
MONGODB_PORT = 27017
MONGODB_CLIENT = 'mms_pair'
MONGODB_COLLECTION = 'mms'