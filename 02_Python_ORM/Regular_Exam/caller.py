import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Article, Review
from django.db.models import Q, Count, Avg


def insert_into_db():
    author1 = Author.objects.create(
        full_name='Anna Williams',
        email='aw@test.com',
        birth_year=1901
    )
    author2 = Author.objects.create(
        full_name='Adam Smith',
        email='as@dev.com',
        birth_year=1902
    )
    article1 = Article.objects.create(
        title='Title1',
        category='Science',
    )
    article1.authors.add(author1)
    article2 = Article.objects.create(
        title='Title2',
        category='Education',
    )
    article2.authors.add(author2)
    article3 = Article.objects.create(
        title='Title3',
        category='Technology',
    )
    article3.authors.add(author1)
    article3.authors.add(author2)

    r1 = Review.objects.create(
        rating=2,
        author=author1,
        article=article1
    )

    r2 = Review.objects.create(
        rating=3,
        author=author2,
        article=article1,
    )

    r3 = Review.objects.create(
        rating=4,
        author=author1,
        article=article2
    )

    r4 = Review.objects.create(
        rating=5,
        author=author1,
        article=article3
    )

    article4 = Article.objects.create(
        title='Article4',
        category='Technology',
    )
    article4.authors.add(author1)


# insert_into_db()


def get_authors(search_name=None, search_email=None) -> str:
    if search_name is None and search_email is None:
        return ''

    query = Q()
    query_by_name = Q(full_name__icontains=search_name)
    query_by_email = Q(email__icontains=search_email)

    if search_name is not None and search_email is not None:
        query = query_by_name & query_by_email
    else:
        query = query_by_email if search_name is None else query_by_name

    authors = Author.objects.filter(query).order_by('-full_name')

    if not authors:
        return ''

    return '\n'.join([
        f'Author: {a.full_name}, email: {a.email}, status: {"Banned" if a.is_banned else "Not Banned"}'
        for a in authors
    ])


def get_top_publisher() -> str:
    top_publisher = Author.objects.get_authors_by_article_count().first()

    if not top_publisher or not Article.objects.all():
        return ''

    return f'Top Author: {top_publisher.full_name} with {top_publisher.article_count} published articles.'


def get_top_reviewer() -> str:
    top_reviewer = (Author.objects
                    .annotate(review_count=Count('author_reviews'))
                    .order_by('-review_count', 'email')
                    .first())

    if not top_reviewer or not Review.objects.all():
        return ''

    return f'Top Reviewer: {top_reviewer.full_name} with {top_reviewer.review_count} published reviews.'


# print(Author.objects.get_authors_by_article_count())
# print(get_authors(search_name='I', search_email=None))
# print(get_authors(search_name='z', search_email='com'))
# print(get_top_publisher())
# print(get_top_reviewer())


def get_latest_article() -> str:
    if not Article.objects.exists():
        return ''

    last_article = (Article.objects
                    .prefetch_related('authors')
                    .annotate(review_count=Count('article_reviews'),
                              avg_rating=Avg('article_reviews__rating'))
                    .order_by('-published_on')
                    .first())

    authors = [a.full_name for a in last_article.authors.all().order_by('full_name')]
    avg_rating = '0.00' if last_article.avg_rating is None else f'{last_article.avg_rating:.2f}'

    return (f'The latest article is: {last_article.title}. Authors: {", ".join(authors)}.'
            f' Reviewed: {last_article.review_count} times. Average Rating: {avg_rating}.')


def get_top_rated_article() -> str:
    top_rated_article = (Article.objects
                         .prefetch_related('article_reviews')
                         .annotate(avg_rating=Avg('article_reviews__rating'), review_count=Count('article_reviews'))
                         .order_by('-avg_rating', 'title')
                         .first())

    if not top_rated_article or top_rated_article.review_count == 0:
        return ''

    return (f'The top-rated article is: {top_rated_article.title},'
            f' with an average rating of {top_rated_article.avg_rating:.2f},'
            f' reviewed {top_rated_article.review_count} times.')


def ban_author(email=None) -> str:
    message = 'No authors banned.'

    if email is None:
        return message

    try:
        author = Author.objects.get(email=email)
    except Exception:
        return message

    author_reviews_num = author.author_reviews.count()
    author.author_reviews.all().delete()
    author.is_banned = True
    author.save()

    return f'Author: {author.full_name} is banned! {author_reviews_num} reviews deleted.'


# print(get_latest_article())
# print(get_top_rated_article())
# print(ban_author('as@dev.com'))
# print(ban_author('aw@test.co'))
