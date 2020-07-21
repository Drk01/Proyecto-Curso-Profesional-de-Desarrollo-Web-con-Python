class Config:
    # Esta es una llave de ejemplo
    SECRET_KEY = 'codigofacilito'


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
