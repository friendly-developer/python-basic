# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser
from video_all import Video 


class Movie(Video):
    # This class provides a way to store movie related information
    """ Movie class which takes all info about the movie and displays the trailer"""
    def __init__(self,title,movie_summary,poster_image_url,trailer_youtube_url,duration):
    	# initialize instance of class Movie
    	Video.__init__(self,title, duration)
    	self.movie_summary = movie_summary
    	self.poster_image_url = poster_image_url
    	self.trailer_youtube_url = trailer_youtube_url

    def show_trailer():
    	webbrowser.open(self.trailer_youtube_url)



