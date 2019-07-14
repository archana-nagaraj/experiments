import fresh_tomatoes
import media

toy_story = media.Movie("Toy_Story", "This story is about a boy and his toys that come to life", 
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
                        "https://www.youtube.com/watch?v=wmiIUN-7qhE")
#print("ToyStory story line goes like this: " +toy_story.story_line)
#toy_story.show_poster()
avatar = media.Movie("Avatar",
                     "On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved. Because the planet's environment is poisonous, human/Na'vi hybrids, called Avatars, must link to human minds to allow for free movement on Pandora. Jake Sully (Sam Worthington), a paralyzed former Marine, becomes mobile again through one such Avatar and falls in love with a Na'vi woman (Zoe Saldana). As a bond with her grows, he is drawn into a battle for the survival of her world.",
                     "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print("Avatar storyline: "+avatar.story_line)
#avatar.show_trailer()
#avatar.show_poster()

october = media.Movie("October",
                      "The lives of two 21-year-old hotel interns collide.",
                      "https://i.pinimg.com/1200x/51/f1/a3/51f1a3909a2e52256aec40de1e349999.jpg",
                      "https://www.youtube.com/watch?v=7vracgLyJwI")
#print("October storyline  : " +october.story_line)
#october.show_trailer()
#october.show_poster()

school_of_Rock = media.Movie("School_of_Rock",
                      "Using rock music to learn.",
                      "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                      "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",
                      "A rat is a chef in paris.",
                      "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                      "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("midnight_in_paris",
                      "GOing back in time to meet authors.",
                      "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                      "https://www.youtube.com/watch?v=FAfR8omt-CY")


#movies = [toy_story, avatar, october, school_of_Rock, ratatouille, midnight_in_paris]
#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)