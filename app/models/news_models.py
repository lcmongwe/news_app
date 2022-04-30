class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,description,url):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        



class NewsReview:

    news_reviews = []

    def __init__(self,id,title,url,review):
        self.id = id
        self.title = title
        self.url = url
        self.review = review


    def save_news_review(self):
        NewsReview.news_reviews.append(self)


    @classmethod
    def clear_news_reviews(cls):
        NewsReview.news_reviews.clear()

    @classmethod
    def get_news_reviews(cls,id):

        news_results = []

        for review in cls.news_reviews:
            if review.movie_id == id:
                news_results.append(review)

        return news_results