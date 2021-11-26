import webbrowser


class Movie():
    # constructor to initialize instance variables
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # class method to show trailer of movies
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
