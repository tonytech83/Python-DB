import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import RealEstateListing, VideoGame, BillingInfo, Invoice

#
# Exam: 01. Real Estate Listing
# Test Code
#
# Create instances of RealEstateListing with locations
# RealEstateListing.objects.create(
#     property_type='House',
#     price=100000.00,
#     bedrooms=3,
#     location='Los Angeles'
# )
# RealEstateListing.objects.create(
#     property_type='Flat',
#     price=75000.00,
#     bedrooms=2,
#     location='New York City'
# )
#
# RealEstateListing.objects.create(
#     property_type='Villa',
#     price=250000.00,
#     bedrooms=4,
#     location='Los Angeles'  # Same location as the first instance
# )
#
# RealEstateListing.objects.create(
#     property_type='House',
#     price=120000.00,
#     bedrooms=3,
#     location='San Francisco'
# )

# Run the 'by_property_type' method
# house_listings = RealEstateListing.objects.by_property_type('House')
# print("House listings:")
# for listing in house_listings:
#     print(f"- {listing.property_type} in {listing.location}")
#
# # Run the 'in_price_range' method
# affordable_listings = RealEstateListing.objects.in_price_range(75000.00, 120000.00)
# print("Price in range listings:")
# for listing in affordable_listings:
#     print(f"- {listing.property_type} in {listing.location}")
#
# # Run the 'with_bedrooms' method
# two_bedroom_listings = RealEstateListing.objects.with_bedrooms(2)
# print("Two-bedroom listings:")
# for listing in two_bedroom_listings:
#     print(f"- {listing.property_type} in {listing.location}")
#
# # Run the 'popular_locations' method
# popular_locations = RealEstateListing.objects.popular_locations()
# print("Popular locations:")
# for location in popular_locations:
#     print(f"- {location['location']}")


#
# Exam: 02. Video Games Library
# Test Code
#
# # Create instances of VideoGame with real data
# game1 = VideoGame.objects.create(title="The Last of Us Part II", genre="Action", release_year=2020, rating=9.0)
#
# game2 = VideoGame.objects.create(title="Cyberpunk 2077", genre="RPG", release_year=2020, rating=7.2)
#
# game3 = VideoGame.objects.create(title="Red Dead Redemption 2", genre="Adventure", release_year=2018, rating=9.7)
#
# game4 = VideoGame.objects.create(title="FIFA 22", genre="Sports", release_year=2021, rating=8.5)
#
# game5 = VideoGame.objects.create(title="Civilization VI", genre="Strategy", release_year=2016, rating=8.8)

# # Run the custom manager methods
# action_games = VideoGame.objects.games_by_genre('Action')
# recent_games = VideoGame.objects.recently_released_games(2019)
# average_rating = VideoGame.objects.average_rating()
# highest_rated = VideoGame.objects.highest_rated_game()
# lowest_rated = VideoGame.objects.lowest_rated_game()
#
# # Print the results
# print(action_games)
# print(recent_games)
# print(average_rating)
# print(highest_rated)
# print(lowest_rated)


#
# Exam: 03. Shopaholic Haven
# Test Code
#
# # Create BillingInfo instances with real addresses
# billing_info_1 = BillingInfo.objects.create(address="456 Oak Lane, Boston, MA 02108")
#
# billing_info_2 = BillingInfo.objects.create(address="789 Maple Avenue, San Francisco, CA 94101")
#
# billing_info_3 = BillingInfo.objects.create(address="101 Pine Street, New York, NY 10001")
#
# # Create Invoice instances with related BillingInfo
# invoice_1 = Invoice.objects.create(invoice_number="INV007", billing_info=billing_info_1)
# invoice_2 = Invoice.objects.create(invoice_number="INV002", billing_info=billing_info_2)
# invoice_3 = Invoice.objects.create(invoice_number="INV004", billing_info=billing_info_3)

# # Get invoices starting with a specific prefix
# invoices_with_prefix = Invoice.get_invoices_with_prefix("INV")
# for invoice in invoices_with_prefix:
#     print(f"Invoice Number with prefix INV: {invoice.invoice_number}")

# # Get invoices sorted by invoice number
# invoices_sorted = Invoice.get_invoices_sorted_by_number()
# for invoice in invoices_sorted:
#     print(f"Invoice Number: {invoice.invoice_number}")

# # Get an invoice by a specific invoice number along with its related billing info
# invoice = Invoice.get_invoice_with_billing_info("INV002")
# print(f"Invoice Number: {invoice.invoice_number}")
# print(f"Billing Info: {invoice.billing_info.address}")
