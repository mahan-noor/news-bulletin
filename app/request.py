import urllib.request,json
from .models import source,article
from config import config


api_key = None
source_url = None
base_url = None

def configure_request(app):
    global api_key,source_url,base_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['SOURCE_BASE_URL']
    base_url = app.config['ARTICLE_BASE_URL']

    

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = source_url.format(api_key)
  
 

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
       

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response ['sources']
            sources_results = process_results(sources_results_list)


    return sources_results

def process_results(source_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain sources details

    Returns :
        sources_results: A list of sources objects
    '''
    sources_results = []

    for  sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description= sources_item.get('description')
        url = sources_item.get('url')
        category =sources_item.get('category')
        language =sources_item.get('language')

        if url:
            sources_object = Sources(id,name,description,url,category,language)
            sources_results.append(sources_object)
    

    return sources_results


def get_article(articles):
    '''
    Function that gets the json response to our url request
    '''
    get_article_url = base_url.format(articles,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if response['articles']:
            article_results_list = response['articles']
            article_results = process_article(article_results_list)


    return article_results

def process_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''
    article_results = []
    for  article_item in article_list:
        
        id = article_item.get("source.name")
        title =article_item.get("title")
        description = article_item.get("description")
        url = article_item.get ("url")
        urlToImage = article_item.get("urlToImage")
        publishedAt = article_item.get("publishedAt")
     

        if urlToImage:
           article_object = article(source,title,description,url,urlToImage,publishedAt)
           article_results.append(article_object)

    return article_results

def search_article(article_name):
    search_url = article_url.format(api_key,article_name)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['article']:
            search_article_list = search_article_response['article']
            search_article_results = process_results(article_list)


    return search_article_results