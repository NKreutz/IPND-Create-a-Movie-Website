import webbrowser

class Movie(object):
    """This class provides a way to store movie related information"""
    
    def __init__(self, movie_title, poster_image, movie_trailer):
        ''' Initializes/Creates space in memory for instances(self) of class "Movie"
        for the instance's title, poster image and trailer url'''
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = movie_trailer
