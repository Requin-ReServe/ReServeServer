from views import create_app
from config import ProductionAppConfig
from const import _RUN_SETTING


if __name__ == '__main__':
    create_app(ProductionAppConfig).run(**_RUN_SETTING)
