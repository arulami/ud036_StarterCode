import webbrowser


class Movie():
    """A Movie class with movie details"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """Initialize the variables"""

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Open youtube trailer url and shows the trailer"""

        webbrowser.open(self.trailer_youtube_url)
