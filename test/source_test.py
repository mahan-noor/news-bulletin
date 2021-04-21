import unittest
from models import source


class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the source class
    '''
    def setUp(self):
         '''
        Set up method that will run before every Test
        '''
        self.new_sources = sources('Citizen tv','Nation news',,'Messi got injury',"https://abcnews.go.com",'general',8.5)

        def test_instance(self):
            self.assertTrue(isinstance(self.new_source,Sources))


    
    def test_to_check_instance_variables(self): 
        self.assertEquals(self.new_source.id,'Citizen tv') 
        self.assertEquals(self.new_source.name,'Nation news') 
        self.assertEquals(self.new_source.description,'Messi got injury') 
        self.assertEquals(self.new_source.url,'dailynation.co.ke') 
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.country,'Kenya') 



