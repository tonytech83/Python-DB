from django.db import models
from django.db.models import QuerySet, Count, Max, Min, Avg
from decimal import Decimal


# Exam: 01. Real Estate Listing
class RealEstateListingManager(models.Manager):

    def by_property_type(self, property_type: str) -> QuerySet:
        return self.filter(property_type=property_type)

    def in_price_range(self, min_price: Decimal, max_price: Decimal) -> QuerySet:
        return self.filter(price__range=(min_price, max_price))

    def with_bedrooms(self, bedrooms_count: int) -> QuerySet:
        return self.filter(bedrooms=bedrooms_count)

    def popular_locations(self) -> QuerySet:
        return (self
                .values('location')
                .annotate(location_count=Count('location'))
                .order_by('-location_count', 'id')[:2])


# Exam: 02. Video Games Library
class VideoGameManager(models.Manager):

    def games_by_genre(self, genre: str) -> QuerySet:
        return self.filter(genre=genre)

    def recently_released_games(self, year: int) -> QuerySet:
        return self.filter(release_year__gte=year)

    def highest_rated_game(self) -> QuerySet:
        # two queries with aggregation
        # return self.filter(rating=self.aggregate(Max('rating'))['rating__max']).first()

        # one query with annotation
        return self.annotate(max_rating=Max('rating')).order_by('-max_rating').first()

    def lowest_rated_game(self) -> QuerySet:
        # two queries with aggregation
        # return self.filter(rating=self.aggregate(Min('rating'))['rating__min']).first()

        # one query with annotation
        return self.annotate(min_rating=Max('rating')).order_by('min_rating').first()

    def average_rating(self):
        return round(self.aggregate(avg_rating=Avg('rating'))['avg_rating'], 1)
