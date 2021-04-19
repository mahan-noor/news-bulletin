import unittest
from models import sources
sources = sources.Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the source class
    '''
    def setUp(self):
         '''
        Set up method that will run before every Test
        '''
        self.new_sources = sources('Citizen tv','us','general','Messi got injury',"https://abcnews.go.com",8.5)

        def test_instance(self):
            self.assertTrue(isinstance(self.new_source,Sources))


if __name__ == '__main__':
    unittest.main()

