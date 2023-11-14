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
                .select_related('billing_info')
                .filter(invoice_number__contains=prefix))

    @classmethod
    def get_invoices_sorted_by_number(cls) -> QuerySet:
        return (cls.objects
                .select_related('billing_info')
                .order_by('invoice_number'))

    @classmethod
    def get_invoice_with_billing_info(cls, invoice_number: str) -> object:
        return (cls.objects
                .select_related('billing_info')
                .get(invoice_number=invoice_number))


class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.ManyToManyField(Technology, related_name='projects')

    # Exam: 04. IT Sector
    def get_programmers_with_technologies(self) -> QuerySet:
        return self.programmers.prefetch_related('projects__technologies_used')

        # return (Programmer.objects
        #         .prefetch_related('projects__technologies_used')
        #         .filter(projects=self))


class Programmer(models.Model):
    name = models.CharField(max_length=100)
    projects = models.ManyToManyField(Project, related_name='programmers')

    # Exam: 04. IT Sector
    def get_projects_with_technologies(self) -> QuerySet:
        return self.projects.prefetch_related('technologies_used')

        # return (Project.objects
        #         .prefetch_related('programmers__projects__technologies_used')
        #         .filter(programmers=self))


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
        search_query = Q(title__icontains=query) | Q(description__icontains=query)

        return cls.objects.filter(search_query)

    def recent_completed_tasks(self, days: int) -> QuerySet:
        query = Q(is_completed=True) & Q(completion_date__gte=self.creation_date - timedelta(days))

        return Task.objects.filter(query)


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    difficulty_level = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()

    # Exam: 06. Gym Session
    @classmethod
    def get_long_and_hard_exercises(cls) -> QuerySet:
        query = Q(duration_minutes__gt=30) & Q(difficulty_level__gte=10)

        return cls.objects.filter(query)

    @classmethod
    def get_short_and_easy_exercises(cls) -> QuerySet:
        queue = Q(duration_minutes__lt=15) & Q(difficulty_level__lt=5)

        return cls.objects.filter(queue)

    @classmethod
    def get_exercises_within_duration(cls, min_duration: int, max_duration: int) -> QuerySet:
        return cls.objects.filter(duration_minutes__range=(min_duration, max_duration))

    @classmethod
    def get_exercises_with_difficulty_and_repetitions(cls, min_difficulty: int, min_repetitions: int) -> QuerySet:
        query = Q(difficulty_level__gte=min_difficulty) & Q(repetitions__gte=min_repetitions)

        return cls.objects.filter(query)
