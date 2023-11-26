from django.db import models
from django.db.models import QuerySet, Count


class AuthorManager(models.Manager):
    def get_authors_by_article_count(self) -> QuerySet:
        return (self
                .annotate(article_count=Count('article'))
                .order_by('-article_count', 'email'))
