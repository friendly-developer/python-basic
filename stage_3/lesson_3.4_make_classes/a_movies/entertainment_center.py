# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story','Story about how toys of a kid comes to life',
	'https://lh5.ggpht.com/ZcvtEd-gylgBYg-HFuzo_YNCKnbyL1aOsY7XKqEf0FiULcLBoWaNx9nRN1ymfcy9vkRj=w300',
	'https://www.youtube.com/watch?v=KYz2wyBy3kc','')

avatar = media.Movie('Avatar','Marine landing on an Alien Planet',
	'http://imgs.abduzeedo.com/files/articles/Avatar/4154691413_a695e033a8_o.jpg',
	'https://www.youtube.com/watch?v=d1_JBMrrYw8','')

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
