import webbrowser

class Movies():

    #defining our __init__
    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer, movie_review):
        self.title = movie_title
        self.story = movie_story
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
        self.review = movie_review

    #displaying the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer)
