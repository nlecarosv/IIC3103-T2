class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/iic3103_t2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASE_URL = 'http://localhost:5000'

config = {
    'development': DevelopmentConfig,
}