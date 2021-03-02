import os

class Config:
    '''
    General configuration
    '''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pomodoro.db'

class ProdConfig(Config):
    '''
    General Config for Prod
    '''

class DevConfig(Config):
    '''
    General Config for development
    '''
    pass

class TestConfig(Config):
    '''
    General Config for Tests
    '''
    pass

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}