from typing import List

from django.db import models
from django.db.models import QuerySet, Count
from decimal import Decimal


# Exam: 01. Real Estate Listing
class RealEstateListingManager(models.Manager):

    def by_property_type(self, property_type: str) -> QuerySet:
        return self.filter(property_type=property_type)

    def in_price_range(self, min_price: Decimal, max_price: Decimal) -> QuerySet:
        return self.filter(price__range=(min_price, max_price))

    def with_bedrooms(self, bedrooms_count: int) -> QuerySet:
        return self.filter(bedrooms=bedrooms_count)

    def popular_locations(self) -> List:
        most_visited_locations = (self.annotate(visits=Count('location')).order_by('-visits', 'id')[:2])

        result = []
        for location in most_visited_locations:
            result.append({'location': location.location})

        return result
