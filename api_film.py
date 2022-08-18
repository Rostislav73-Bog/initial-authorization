from tmdbv3api import TMDb
from tmdbv3api import Movie


tmdb = TMDb()
tmdb.language = "ru"
tmdb.api_key = '696683d47628265247f9afa3163a6abe'


movie = Movie()

recommendations = movie.recommendations(movie_id=111)

popular = movie.popular()

for p in popular:
    print(p.id)
    # print(p.title)
    # print(p.overview)
    print(p.poster_path)

for recommendation in recommendations:
    print(recommendation.title)
    # print(recommendation.overview)

