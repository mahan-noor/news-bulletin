import os
   
class config:

    SOURCE_BASE_URL = 'https://newsapi.org/v2/sources{}?apiKey={}'
    ARTICLE_BASE_URL = ' https://newsapi.org/v2/everything?q=Apple&from=2021-04-18&sortBy=popularity&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

