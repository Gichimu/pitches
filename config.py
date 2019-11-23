class Config:



    pass

class ProdConfig:

    pass



class DevConfig:

    DEBUG = True


config_options = {
    'production':ProdConfig,
    'development':DevConfig
}
