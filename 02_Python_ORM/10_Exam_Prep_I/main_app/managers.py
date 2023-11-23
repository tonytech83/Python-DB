from django.db import models
from django.db.models import QuerySet, Count


class DirectorManager(models.Manager):
    def get_directors_by_movies_count(self) -> QuerySet:
        return self.annotate(movie_count=Count('movies')).order_by('-movie_count', 'full_name')
