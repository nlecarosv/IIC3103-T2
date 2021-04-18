import os


class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/iic3103_t2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASE_URL = 'http://localhost:5000'


class ProductiomConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASE_URL = 'https://iic3103-t2.herokuapp.com/'


config = {
    'development': DevelopmentConfig,
    'production': ProductiomConfig,
}
