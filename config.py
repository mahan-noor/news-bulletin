import os
   
class config:

    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&apiKey={}'
    ARTICLE_BASE_URL ="https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}"
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    
    @staticmethod
    def init_app(app):
        pass


class ProdConfig(config):
    pass


class DevConfig(config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

