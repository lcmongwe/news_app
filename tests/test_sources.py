import unittest
from  app.models import Sources,Articles
# Movie = movie.Movie

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources("abc-news","ABC NEWS","your trusred news source","https://abcnews.go.com","general","en","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))


# if __name__ == '__main__':
#     unittest.main()