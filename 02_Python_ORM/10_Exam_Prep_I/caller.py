import os
import django
from django.db.models import Q, Count, Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Director, Actor, Movie


def insert_into_db():
    d1 = Director.objects.create(
        full_name='Akira Kurosawa',
    )
    d2 = Director.objects.create(
        full_name='Francis Ford Coppola',
        years_of_experience=50,
    )
    d3 = Director.objects.create(
        full_name='Martin Scorsese',
        nationality='American and Italian',
        years_of_experience=60,
    )

    a1 = Actor.objects.create(
        full_name='Al Pacino',
    )
    a2 = Actor.objects.create(
        full_name='Robert Duvall'
    )
    a3 = Actor.objects.create(
        full_name='Joaquin Phoenix'
    )

    m1 = Movie.objects.create(
        title='The Godfather',
        release_date='2020-01-01',
        rating=9.9,
        director=d2,
        starring_actor=a1,
    )
    m1.actors.add(a2)
    m1.actors.add(a3)

    m2 = Movie.objects.create(
        title='Apocalypse Now',
        release_date='2014-02-02',
        rating=9.5,
        director=d2,
        starring_actor=a1
    )
    m2.actors.add(a3)


def get_directors(search_name=None, search_nationality=None) -> str:
    if search_name is None and search_nationality is None:
        return ''

    query = Q()
    query_by_name = Q(full_name__icontains=search_name)
    query_by_nationality = Q(nationality__icontains=search_nationality)

    if search_name is not None and search_nationality is not None:
        query = query_by_name & query_by_nationality
    else:
        query = query_by_nationality if search_name is None else query_by_name

    directors = Director.objects.filter(query).order_by('full_name')

    if not directors:
        return ''

    return '\n'.join([
        f'Director: {director.full_name}, nationality: {director.nationality}, experience: {director.years_of_experience}'
        for director in directors
    ])


def get_top_director() -> str:
    top_director = Director.objects.get_directors_by_movies_count().first()

    if not top_director:
        return ''

    return f'Top Director: {top_director.full_name}, movies: {top_director.movie_count}.'


def get_top_actor() -> str:
    top_actor = (Actor.objects
                 .prefetch_related('movies')
                 .annotate(movies_count=Count('movies'), avg_rating=Avg('movies__rating'))
                 .order_by('-movies_count', 'full_name')
                 .first())

    if not top_actor or not top_actor.movies_count:
        return ''

    movies = ', '.join(movie.title for movie in top_actor.movies.all() if movie)

    return (f'Top Actor: {top_actor.full_name},'
            f' starring in movies: {movies},'
            f' movies average rating: {top_actor.avg_rating:.1f}')


# print(Director.objects.get_directors_by_movies_count())
# print(get_directors(search_name='S', search_nationality=None))
# print(get_directors(search_name='Martin', search_nationality='Canadian'))
# print(get_top_director())
# print(get_top_actor())


def get_actors_by_movies_count() -> str:
    actors = (Actor.objects
              .annotate(movies_count=Count('movie'))
              .order_by('-movies_count', 'full_name')[:3])

    if not actors or actors[0].movies_count == 0:
        return ''

    return '\n'.join([
        f'{actor.full_name}, participated in {actor.movies_count} movies'
        for actor in actors
    ])


def get_top_rated_awarded_movie() -> str:
    movie = (Movie.objects
             .select_related('starring_actor')
             .prefetch_related('actor')
             .filter(is_awarded=True)
             .order_by('-rating', 'title')
             .first())

    if not movie:
        return ''

    starring_actor = movie.starring_actor.full_name if movie.starring_actor else 'N/A'
    cast_actors = ', '.join(actor.full_name for actor in movie.actors.order_by('full_name') if actor)

    return (f'Top rated awarded movie: {movie.title},'
            f' rating: {movie.rating:.1f}.'
            f' Starring actor: {starring_actor}.'
            f' Cast: {cast_actors}.')


def increase_rating() -> str:
    movies = Movie.objects.filter(is_classic=True, rating__lt=10)

    if not movies:
        return 'No ratings increased.'

    num_of_updated_movies = movies.update(rating=F('rating') + 0.1)

    return f'Rating increased for {num_of_updated_movies} movies.'


# print(get_actors_by_movies_count())
# print(get_top_rated_awarded_movie())
# print(increase_rating())
