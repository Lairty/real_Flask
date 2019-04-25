import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Vf[fy&Fyfcnfhbz&Lhfrjyxbr'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or 1
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'lairty123123@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'Qazxswedc123'
    ADMINS = ['c-plusplus@mail.ru']
    POSTS_PER_PAGE = 25
    LANGUAGES = ['en', 'ru']
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL') or "http://localhost:9200"
