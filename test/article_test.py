import unittest
from models import article


class articlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = articles('CNN','lg','Apple manages to grow its business even as iPhone sales decline 12%','Libra is a great idea','lg.com','2021-04-20')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,articles))




    def test_to_check_instance_variables(self): 
        self.assertEquals(self.new_source.id,'CNN') 
        self.assertEquals(self.new_source.name,'lg') 
        self.assertEquals(self.new_source.description,'Kipchoge breaks his own record') 
        self.assertEquals(self.new_source.url,'dailynation.co.ke') 
        self.assertEquals(self.new_source.urlToImange,'general')
        self.assertEquals(self.new_source.publishedAt,'2021/04/18') 
        
