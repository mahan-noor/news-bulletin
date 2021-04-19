from app import app
import urllib.request,json
from .models import source_test


api_key = app.config['NEWS_API_KEY']
base_url = app.config['SOURCE_API_BASE_URL']
base_url =['ARTICLE_API_BASE_URL']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['results']:
            sources_results_list = get_sources_response['results']
            sources_results = process_results(sources_results_list)


    return sources_results

def process_results(sources_list):
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

        if poster:
           sources_object = Sources(id,name,description,url,category,language)
           sources_results.append(sources_object)

    return sources_results


def get_article(category):
    '''
    Function that gets the json response to our url request
    '''
    get_article_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if response['article']:
            article_results_list = response['article']
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
        
        id = one_article.get("source")
        title = one_article.get("title")
        description = one_article.get("description")
        url = one_article.get ("url")
        urlToImage = one_article.get("urlToImage")
        publishedAt = one_article.get("publishedAt")
     

        if poster:
           article_object = article(source,title,description,url,urlToImage,publishedAt)
           article_results.append(article_object)

    return article_results