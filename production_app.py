from views import create_app
from config import ProductionAppConfig
from const import _CONST_SETTING


if __name__ == '__main__':
    create_app(ProductionAppConfig).run(**_CONST_SETTING)
