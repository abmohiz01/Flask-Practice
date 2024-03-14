
class BaseConfig(object):
    'Base config class'
    SECRET_KEY = 'A random secret key'
    DEBUG = True
    TESTING = False
    NEW_CONFIG_VARIABLE = 'my value'

    #Only send Cookies if there is back and forth https connection
    SESSION_COOKIE_SECURE = True

class ProductionConfig(BaseConfig):
    'Production specific config'
    DEBUG = True
    SECRET_KEY = 'yufhfdthyrjtfjytjmytut'

class StagingConfig(BaseConfig):
    'Staging specific config'
    DEBUG = True

class DevelopmentConfig(BaseConfig):
    'Development environment specific config'
    DEBUG = True
    TESTING = True
    SECRET_KEY = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'

class TestingConfig(BaseConfig):
    'Testing environment specific config'
    DEBUG = True
    TESTING = True
    SECRET_KEY = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
    SESSION_COOKIE_NAME = 'ABMOHIZ'


