class Config:
    '''
    General configuration parent class
    '''
    SOURCE_BASE_URL = 'https://newsapi.org/v2/sources{}?apiKey={}'
    ARTICLE_BASE_URL = ' https://newsapi.org/v2/everything?q=Apple&from=2021-04-18&sortBy=popularity&apiKey={}'
    NEWS_API_KE