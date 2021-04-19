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
        self.new_article = articles('CNN','lg','Apple manages to grow its business even as iPhone sales decline 12%','Libra is a great idea. But Facebook has to get out of the way','lg.com','2021-04-20')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,articles))
