from datetime import timedelta

from django.db import models
from django.db.models import QuerySet, Q, F

from main_app.managers import RealEstateListingManager, VideoGameManager
from main_app.validations import validate_rating, validate_release_year


class RealEstateListing(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('House', 'House'),
        ('Flat', 'Flat'),
        ('Villa', 'Villa'),
        ('Cottage', 'Cottage'),
        ('Studio', 'Studio'),
    ]

    property_type = models.CharField(max_length=100, choices=PROPERTY_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    location = models.CharField(max_length=100)

    objects = RealEstateListingManager()


class VideoGame(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('RPG', 'RPG'),
        ('Adventure', 'Adventure'),
        ('Sports', 'Sports'),
        ('Strategy', 'Strategy'),
    ]

    title = models.CharField(max_length=100, )
    genre = models.CharField(
        max_length=100,
        choices=GENRE_CHOICES
    )
    release_year = models.PositiveIntegerField(
        validators=[validate_release_year]
    )
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[validate_rating],
    )

    objects = VideoGameManager()

    def __str__(self):
        return self.title


class BillingInfo(models.Model):
    address = models.CharField(max_length=200)


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    billing_info = models.OneToOneField(BillingInfo, on_delete=models.CASCADE)

    # Exam: 03. Shopaholic Haven
    @classmethod
    def get_invoices_with_prefix(cls, prefix: str) -> QuerySet:
        return (cls.objects
                .filter(invoice_number__contains=prefix)
                .select_related('billing_info'))

    @classmethod
    def get_invoices_sorted_by_number(cls) -> QuerySet:
        return cls.objects.order_by('invoice_number')

    @classmethod
    def get_invoice_with_billing_info(cls, invoice_number: str) -> object:
        return (cls.objects
        .filter(invoice_number=invoice_number)
        .select_related('billing_info')[0])


class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.ManyToManyField(Technology, related_name='projects')

    # Exam: 04. IT Sector
    def get_programmers_with_technologies(self) -> QuerySet:
        return Programmer.objects.filter(projects=self).prefetch_related('projects__technologies_used')


class Programmer(models.Model):
    name = models.CharField(max_length=100)
    projects = models.ManyToManyField(Project, related_name='programmers')

    def get_projects_with_technologies(self) -> QuerySet:
        return Project.objects.filter(programmers=self).prefetch_related('programmers__projects__technologies_used')


class Task(models.Model):
    PRIORITIES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITIES)
    is_completed = models.BooleanField(default=False)
    creation_date = models.DateField()
    completion_date = models.DateField()

    # Exam: 05. Taskify
    @classmethod
    def overdue_high_priority_tasks(cls) -> QuerySet:
        query = Q(priority='High') & Q(is_completed=False) & Q(completion_date__gt=F('creation_date'))

        return cls.objects.filter(query)

    @classmethod
    def completed_mid_priority_tasks(cls) -> QuerySet:
        query = Q(priority='Medium') & Q(is_completed=True)

        return cls.objects.filter(query)

    @classmethod
    def search_tasks(cls, query: str) -> QuerySet:
        search_query = Q(title__contains=query) | Q(description__contains=query)

        return cls.objects.filter(search_query)

    @classmethod
    def recent_completed_tasks(cls, days: int) -> QuerySet:
        query = Q(is_completed=True) & Q(completion_date__gte=(F('creation_date')) - timedelta(days=days))

        return cls.objects.filter(query)


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    difficulty_level = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()
