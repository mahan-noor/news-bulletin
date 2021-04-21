import os
   
class config:

    SOURCE_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLE_BASE_URL ='https://newsapi.org/v2/everything?sources=bbc-news&sortBy=publishedAt&apiKey={}'
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

