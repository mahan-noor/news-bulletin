import urllib.request,json
from .models import News,Articles
# from config import config


api_Key = None
base_url = None
articles_url = None

def configure_request(app):
    global api_Key,base_url,articles_url
    api_Key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['ARTICLE_BASE_URL']

    

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    
    get_news_url = base_url.format(api_Key)
    print(get_news_url)
    

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response["sources"]:
            news_results_list = get_news_response["sources"]
            news_results = process_results(news_results_list)

    return news_results




def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id') 
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')
        
        news_object = News(id,name,description,url,category,country,language)
        news_results.append(news_object)

    return news_results



def get_articles(articles):
    '''
    function that processes the articles and returns a list of articles objects
    '''
    get_articles_url = articles_url.format(articles,api_Key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_results = json.loads(get_articles_data)

        articles_results = None
        if get_articles_results['articles']:
            articles_results_list = get_articles_results['articles']
            articles_results = process_results(articles_results_list)


            
            
    return articles_results




def process_articles(articles_list):
    '''
    Function  that processes the articles result and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain articles and their  details
    Returns :
        articles_results: A list of articles objects
    '''
    articles_results = []
    for article_item in articles_list:
        name = article_item.get('name')
        title = article_item.get('title')
        author = article_item.get('author')
        description = article_item.get('description')
        url = article_item.get('url')
        image = article_item.get('urlToImage')
        date = article_item.get('publishedAt')
        content = article_item.get('content')
        
        if image:
            articles_results =Articles(name,title,author,description,url,urlToImage,publishedAt,content)
            articles_object.append(articles_results)

    return articles_object