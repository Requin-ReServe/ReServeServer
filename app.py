from views import create_app
from config import LocalAppConfig
from const import CONST_SETTING


if __name__ == '__main__':
    create_app(LocalAppConfig).run(**CONST_SETTING)
