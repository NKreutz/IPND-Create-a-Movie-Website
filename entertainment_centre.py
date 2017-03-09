import media
import fresh_tomatoes

romeo_and_juliet = media.Movie("Romeo + Juliet",
"https://upload.wikimedia.org/wikipedia/en/thumb/b/b4/William_shakespeares_romeo_and_juliet_movie_poster.jpg/220px-William_shakespeares_romeo_and_juliet_movie_poster.jpg",
"https://youtu.be/sMel13nY0PE")

moulin_rouge = media.Movie("Moulin Rouge!",
"https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Moulin_rouge_poster.jpg/220px-Moulin_rouge_poster.jpg",
"https://www.youtube.com/watch?v=dMSvKpVwavk")

titanic = media.Movie("Titanic",
"https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
"https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

the_princess_bride = media.Movie( "The Princess Bride",
"https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Princess_bride.jpg/220px-Princess_bride.jpg",
"https://www.youtube.com/watch?v=njZBYfNpWoE")

the_sound_of_music = media.Movie("The Sound of Music",
"https://upload.wikimedia.org/wikipedia/en/c/c6/Sound_of_music.jpg",
"https://www.youtube.com/watch?v=TRPEpJHI9zg")

grease = media.Movie("Grease",
"https://upload.wikimedia.org/wikipedia/en/thumb/e/e2/Grease_ver2.jpg/220px-Grease_ver2.jpg",
"https://www.youtube.com/watch?v=wzWmxjYNfz4")

the_beach = media.Movie("The Beach",
"https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/The_Beach_film.jpg/215px-The_Beach_film.jpg",
"https://www.youtube.com/watch?v=MqDoxUxpobg")

beauty_and_the_beast = media.Movie("Beauty and the Beast",
"https://upload.wikimedia.org/wikipedia/en/thumb/7/7c/Beautybeastposter.jpg/220px-Beautybeastposter.jpg",
"https://www.youtube.com/watch?v=tRlzmyveDHE")

movies = [romeo_and_juliet, moulin_rouge, the_princess_bride, titanic,
            the_sound_of_music, grease, the_beach, beauty_and_the_beast]

fresh_tomatoes.open_movies_page(movies)
