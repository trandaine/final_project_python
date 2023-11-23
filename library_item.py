class LibraryItem: # Define a class
    def __init__(self, name, director, image, rating=0):
        self.name = name
        self.director = director
        self.rating = int(rating)
        self.play_count = 0
        self.image = image

    def info(self):     #Define a function
        return f"{self.name} - {self.director} {self.stars()}"          #return the string

    def stars(self):            #Define a function
        stars = ""              # No star at the begining
        for i in range(self.rating):    # For every value in rating
            stars += "*"                # Plus a star (*) symbol
        return stars

