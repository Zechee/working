from datetime import timedelta
import os

config_path = os.path.abspath(os.path.dirname(__file__))


class Config:


    # SQLALCHEMY_DATABASE_URI = os.environ.get(
    #     "DATABASE_URL",
    #     'mysql://survey:Survey123456!@192.168.178.52:3306/survey?charset=utf8')

    # 
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///workingreport.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BUNDLE_ERRORS = True
    SECRET_KEY = os.environ.get(
        'SECRET_KEY', '3j4k5h43kj5hj234b5jh34bk25b5k234j5bk2j3rref3b532')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'uploads')


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


app_config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}