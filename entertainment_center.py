import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story about a boy and his toys which come to life", "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet", "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

sound_of_music = media.Movie("The Sound of Music", "Maria, an aspiring nun, is sent as a governess to take care of seven motherless children. Soon her jovial and loving nature tames their hearts and the children become fond of her.", r"D:\Udacity\sound_of_music", "https://www.youtube.com/watch?v=NJRI-QK7OaU")

midnight_in_paris = media.Movie("Midnight in Paris", "While on a trip to Paris with his fiancée's family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s everyday at midnight.", "https://en.wikipedia.org/wiki/Midnight_in_Paris#/media/File:Midnight_in_Paris_Poster.jpg", "https://www.youtube.com/watch?v=BYRWfS2s2v4")

ratatouille  = media.Movie("Ratatouille", "Remy, a rat, aspires to become a renowned French chef. He doesn't realise that people despise rodents and will never enjoy a meal cooked by him", "https://en.wikipedia.org/wiki/Ratatouille_(film)#/media/File:RatatouillePoster.jpg", "https://www.youtube.com/watch?v=uVeNEbh3A4U")

the_hunger_games = media.Movie("The Hunger Games", "The Hunger Games universe is a dystopia set in Panem, a country consisting of the wealthy Capitol and 12 districts in varying states of poverty. Every year, children from the districts are selected to participate in a compulsory televised battle royale death match called The Hunger Games.", "https://en.wikipedia.org/wiki/File:HungerGamesPoster.jpg", "https://www.youtube.com/watch?v=mfmrPu43DF")

movies_list  = [toy_story, avatar, sound_of_music, midnight_in_paris, ratatouille, the_hunger_games]

fresh_tomatoes.open_movies_page(movies_list)

#print (toy_story.storyline)

#print (avatar.storyline)

#sound_of_music.show_trailer()

#avatar.show_trailer()
