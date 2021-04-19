class article:
    '''
    article class to define article objects
    '''

    def __init__(self,source,title,description,url,urlToImage,publishedAt):

        self.id = source
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

        