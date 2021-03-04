import os

class Config:
<<<<<<< HEAD
    '''
    General configuration
    '''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///timer.db'
    SECRET_KEY = 'gakuyajefferson'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
=======
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
>>>>>>> 3c575a9699105a90336370be2d0d4bb79b512854

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''

class DevConfig(Config):
<<<<<<< HEAD
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuaration settings
    '''

    pass
=======
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ryan:crossman123@localhost/pomodorotracker'
    
    DEBUG = True
>>>>>>> 3c575a9699105a90336370be2d0d4bb79b512854

class TestConfig(Config):
    '''
    Testing Configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}