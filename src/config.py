class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'admin'
    MYSQL_PASSWORD = 'admin'
    MYSQL_DB = 'flask_login'


config = {
    'development': DevelopmentConfig
}
