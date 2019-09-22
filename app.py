from views import create_app
from config import LocalAppConfig


if __name__ == '__main__':
    create_app(LocalAppConfig).run(host="127.0.0.1", port=5000)
