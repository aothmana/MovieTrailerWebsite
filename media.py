'''
Created on Mar 23, 2018

@author: alyao
'''
import webbrowser


class Movie:
    """This class defines the data structure for the movies"""

    def __init__(self, aMovieTitle, aMovieStoryline, aPosterImage, aTrailerYoutube):

        self.title = aMovieTitle
        self.movie_storyline = aMovieStoryline
        self.poster_image_url = aPosterImage
        self.trailer_youtube_url = aTrailerYoutube
    
    def show_trailer(self):
        #Open the movie youtube trailer
        webbrowser.open_new(self.trailer_youtube)
