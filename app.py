from views import create_app
from config import LocalAppConfig
from const import _CONST_SETTING


if __name__ == '__main__':
    create_app(LocalAppConfig).run(**_CONST_SETTING)
