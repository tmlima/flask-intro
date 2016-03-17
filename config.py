#default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\\xe8V%\\x85\\xefl> )S\\xd7A\\xccG\\xfe\\x10\\xeb\\xef\\xebJ96\\x7f\\x7f'
    SQLALCHEMY_DATABASE_URI = 'mysql://admin:123456@localhost:3306/flask'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
