from datetime import timedelta


class BasicAppConfig:
    SECRET_KEY = "TEST_SECRET_KEY"

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=20)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)


class LocalAppConfig(BasicAppConfig):
    ENV = "Test"
    DEBUG = True
    

class ProductionAppConfig(BasicAppConfig):
    ENV = "Production"
    DEBUG = False


class DBConfig:
    #TODO
    pass