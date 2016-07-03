import webbrowser
class Movie():
    """This class provides a method to store movies related inormation"""
    
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube,
                 rating,actors):
        #CONSTRUCTOR
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
        self.rating=rating
        self.actors=actors
        
    def show_trailer(self):
       #This function shows the trailer of the movie
        webbrowser.open(self.trailer_youtube_url)

    def show_storyline(self):
        #This function returns the storyline of the movie
        story=self.storyline
        return story
    def check_rating(self):
        #This function checks if the rating given to the movie is valid or not
        valid_ratings=["G","PG","PG-13","R","U"]
        if self.rating in valid_ratings:
            return "Valid rating"
        else:
            return "Invalid rating"
    
