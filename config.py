class Config(object):
    """Configuraciones del proyecto"""

    DEBUG = False
    TESTING = False

    #Base de datos
    DB_SERVER = 'localhost'
    DB_PORT = '5432'
    DB_USER = 'postgres'
    DB_PASSWORD = '1186'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class DevelopmentConfig(Config):
    """Configuración para desarrollo"""

    DEVELOPMENT = True
    DB_SERVER = 'localhost'
    DB_NAME = 'stocks'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1186@localhost/{}'.format(DB_NAME)


class TestingConfig(Config):
    """Configuración para tesing"""

    DEBUG = True
    DB_NAME='inventarios_test'
    TESTING = True
    APP_ENV = 'config.TestingConfig'
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1186@localhost/{}'.format(DB_NAME)
