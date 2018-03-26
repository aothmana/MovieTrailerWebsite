import media
import fresh_tomates
import os

# Get current directory
lCurrentDirectory = os.getcwd()
# Define my movie list
iQueen = media.Movie("Queen and Abdul", "The extraordinary true story",
                     lCurrentDirectory +
                     "/queen-victoria-abdul-karim.jpg", "https://www.youtube"
                     ".com/watch?v=T504u17Ao9A")
iHappiness = media.Movie("Pursuit of Happiness", "A struggling salesman"
                         "takes custody of his son as he's poised to begin a"
                         "life-changing professional endeavor.",
                         lCurrentDirectory + "/happiness.jpg", "https://www."
                         "youtube.com/watch?v=DMOBlEcRuw8")
iTonya = media.Movie("I,Tonya", "In 1991, talented figure skater Tonya Harding"
                     "becomes the first American woman to complete a triple"
                     "axel during a competition. ",
                     lCurrentDirectory + "/Tonya.jpg", "https://www.youtube.com"
                     "/watch?v=OXZQ5DfSAAc")
# Pass the movie list to open movie page to format the HTML Page.
fresh_tomates.open_movies_page([iQueen, iHappiness, iTonya])
