from library_item import LibraryItem                                #import the class LibraryItem from library_item.py


library = {}                        # Create an empty dictionary
library["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 'image/1.jpg', 3)
library["02"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", "image/2.jpg", 5)
library["03"] = LibraryItem("Casablanca", "Michael Curti", "image/3.jpg", 4)
library["04"] = LibraryItem("The Sound of Music", "Robert Wise", "image/4.jpg", 5)
library["05"] = LibraryItem("Gone with the Wind", "Victor Fleming", "image/5.jpg", 3)


def list_all():                                                 # Define a function
    output = ""                                                 # Create a string containing information of all the movies in library
    for key in library:
        item = library[key]                                 # Get the key in library
        output += f"{key} {item.info()}\n"            # Set the text
    return output                                              # Return to the output


def get_name(key):                                  # Define a function
    try:
        item = library[key]                             # Get the key from input
        return item.name                              # Return the item corresponding to the key
    except KeyError:                                  # If the key is not exist
        return None                                     # Not return anything


def get_director(key):                          # Define a function
    try:
        item = library[key]                         # Get the key from input
        return item.director                        # Return the item corresponding to the key
    except KeyError:                                # If the key is not exist
        return None                                     # Not return anything

def get_image(key):                     # Define a function
    try:
        item = library[key]                 # Get the key from input
        return item.image                   # Return the item corresponding to the key
    except KeyError:                        # If the key is not exist
        return None                             # Not return anything


def get_rating(key):                            # Define a function
    try:
        item = library[key]                     # Get the key from input
        return item.rating                          # Return the item corresponding to the key
    except KeyError:                            # If the key is not exist
        return -1                                       # Return -1 if error


def set_rating(key, rating):                        #set the rating of the movie manually
    try:
        item = library[key]                                # Get the key from input
        item.rating = rating                                    # Return the item corresponding to the key
    except KeyError:                                        # If the key is not found
        return                                                      # Return nothing


def get_play_count(key):                          # Define a function
    try:
        item = library[key]                            # Get the key from output
        return item.play_count                      # Return the item corresponding to the key
    except KeyError:                                    # If the key is not exist
        return -1                                               # Return -1 if error



def increment_play_count(key):                          # Define a function
    try:
        item = library[key]                                     # Get the key from output
        item.play_count += 1                                # Increase the play_count of the item corresponding to the key
    except KeyError:                                        # If the key is not exist
        return                                                        # Return nothing
