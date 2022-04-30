class Article:
    '''
    Article class to define Class Objects
    '''

    def __init__(self,author,title,description,url,urlToImage,publishedAt):
        self.author =author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage =  urlToImage
        self.publishedAt= publishedAt



class ArticleReview:

    all_reviews = []

    def __init__(self,title,urlToImage,review):
        self.title = title
        self.urlToImage = urlToImage
        self.review = review


    def save_review(self):
        ArticleReview.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        ArticleReview.all_reviews.clear()

    @classmethod
    def get_reviews(cls,title):

        response = []

        for review in cls.all_reviews:
            if review.title== title:
                response.append(review)

        return response