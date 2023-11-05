import os
import django
from django.db.models import QuerySet, Avg, Sum, Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Book, Artist, Song, Product, Review


#
# Exam: 01. Library
#
def show_all_authors_with_their_books() -> str:
    all_authors = Author.objects.all().order_by('id')

    result = []
    for author in all_authors:
        books = author.books.all()

        if not books:
            continue

        result.append(
            f'{author.name} has written - {", ".join(b.title for b in books)}'
        )

    return '\n'.join(result)


def delete_all_authors_without_books() -> None:
    Author.objects.filter(books__isnull=True).delete()


# Test Code
# # Create authors
# author1 = Author.objects.create(name="J.K. Rowling")
# author2 = Author.objects.create(name="George Orwell")
# author3 = Author.objects.create(name="Harper Lee")
# author4 = Author.objects.create(name="Mark Twain")
#
# # Create books associated with the authors
# book1 = Book.objects.create(
#     title="Harry Potter and the Philosopher's Stone",
#     price=19.99,
#     author=author1
# )
# book2 = Book.objects.create(
#     title="1984",
#     price=14.99,
#     author=author2
# )
#
# book3 = Book.objects.create(
#     title="To Kill a Mockingbird",
#     price=12.99,
#     author=author3
# )
#
# # Display authors and their books
# authors_with_books = show_all_authors_with_their_books()
# print(authors_with_books)

# # Delete authors without books
# delete_all_authors_without_books()
# print(Author.objects.count())


#
# Exam: 02. Music App
#
def add_song_to_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str) -> QuerySet:
    artist = Artist.objects.get(name=artist_name)

    return artist.songs.all().order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)

    # One row code
    # Artist.objects.get(name=artist_name).songs.remove(Song.objects.get(title=song_title))


# Test Code
# # Create artists
# artist1 = Artist.objects.create(name="Daniel Di Angelo")
# artist2 = Artist.objects.create(name="Indila")
#
# # Create songs
# song1 = Song.objects.create(title="Lose Face")
# song2 = Song.objects.create(title="Tourner Dans Le Vide")
# song3 = Song.objects.create(title="Loyalty")

# # Add a song to an artist
# add_song_to_artist("Daniel Di Angelo", "Lose Face")
# add_song_to_artist("Daniel Di Angelo", "Loyalty")
# add_song_to_artist("Indila", "Tourner Dans Le Vide")

# # Get all songs by a specific artist
# songs = get_songs_by_artist("Daniel Di Angelo")
# for song in songs:
#     print(f"Daniel Di Angelo: {song.title}")

# # Get all songs by a specific artist
# songs = get_songs_by_artist("Indila")
# for song in songs:
#     print(f"Indila: {song.title}")

# # Remove a song from an artist
# remove_song_from_artist("Daniel Di Angelo", "Lose Face")
#
# # Check if the song is removed
# songs = get_songs_by_artist("Daniel Di Angelo")
#
# for song in songs:
#     print(f"Songs by Daniel Di Angelo after removal: {song.title}")

#
# # Exam: 03. Shop
#
def calculate_average_rating_for_product_by_name(product_name: str) -> float:
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()

    total_rating = sum(r.rating for r in reviews)
    avg_rating = total_rating / reviews.count()

    return avg_rating

    # # result using aggregation and Avg form Django
    # product = Product.objects.get(name=product_name)
    # return product.reviews.aggregate(average=Avg('rating'))['average']

    # # result using annotate, Sum and Count form Django
    # product = Product.objects.annotate(
    #     total_rating=Sum('reviews__rating'),
    #     reviews_count=Count('reviews')
    # ).get(name=product_name)
    #
    # avg_rating = product.total_rating / product.reviews_count
    #
    # return avg_rating


def get_reviews_with_high_ratings(threshold: int) -> QuerySet[Review]:
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews() -> QuerySet[Product]:
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews() -> None:
    Product.objects.filter(reviews__isnull=True).delete()

# Test Code
# # Create some products
# product1 = Product.objects.create(name="Laptop")
# product2 = Product.objects.create(name="Smartphone")
# product3 = Product.objects.create(name="Headphones")
# product4 = Product.objects.create(name="PlayStation 5")
#
# # Create some reviews for products
# review1 = Review.objects.create(description="Great laptop!", rating=5, product=product1)
# review2 = Review.objects.create(description="The laptop is slow!", rating=2, product=product1)
# review3 = Review.objects.create(description="Awesome smartphone!", rating=5, product=product2)

# Run the function to get products without reviews
# products_without_reviews = get_products_with_no_reviews()
# print(f"Products without reviews: {', '.join([p.name for p in products_without_reviews])}")
# # Run the function to delete products without reviews
# delete_products_without_reviews()
# print(f"Products left: {Product.objects.count()}")

# # Calculate and print the average rating
# print(calculate_average_rating_for_product_by_name("Laptop"))
