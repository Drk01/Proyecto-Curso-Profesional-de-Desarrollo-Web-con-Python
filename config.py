class Config:
    # Esta es una llave de ejemplo
    SECRET_KEY = 'codigofacilito'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/project_web_codigofacilito'


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
