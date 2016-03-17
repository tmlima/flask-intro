#default config
class BaseConfig(object):
    DEBUG = False
    SECRECT_KEY = 'my precious'
    SQLALCHEMY_DATABASE_URI = 'mysql://admin:123456@localhost:3306/flask'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
