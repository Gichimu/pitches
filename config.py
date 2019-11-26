import os

class Config:
    '''
    class that defines all the basic configurations of the application
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True




class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")



class DevConfig(Config):

    Debug = True


config_options = {
    'production':ProdConfig,
    'development':DevConfig
}
