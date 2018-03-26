import webbrowser
'''
Created on Mar 23, 2018

@author: alyao
'''
"This code is inspired by the instructor for Python course."


class Movie:
    """This class defines the data structure for a movie.
    Attributes:
        aMovieTitle: Movie title
        aMovieStoryline: A description of the movie story line
        aPosterImage: The location of the movie image
        aTrailerYoutube: The URL for the movie trailer youtube link.
        """

    def __init__(self, aMovieTitle, aMovieStoryline, aPosterImage,
                 aTrailerYoutube):
        self.title = aMovieTitle
        self.movie_storyline = aMovieStoryline
        self.poster_image_url = aPosterImage
        self.trailer_youtube_url = aTrailerYoutube

    def show_trailer(self):
        # Open the movie youtube trailer
        webbrowser.open_new(self.trailer_youtube)
