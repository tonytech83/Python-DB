import os
from decimal import Decimal

import django
from django.core.exceptions import ValidationError

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Customer, Book, Product, DiscountedProduct

#
# Exam: 01. Customer
# Test Code
#
# customer = Customer(
#     name="Svetlin Nakov1",
#     age=1,
#     email="nakov@example",
#     phone_number="+35912345678",
#     website_url="htsatps://nakov.com/"
# )
#
# try:
#     customer.full_clean()
#     customer.save()
# except ValidationError as e:
#     print('\n'.join(e.messages))


#
# Exam: 02. Media
# Test Code
#
# book = Book(
#     title="Short Title",
#     description="A book with a short title.",
#     genre="Fiction",
#     author="A",
#     isbn="1234"
# )
#
# try:
#     book.full_clean()
#     book.save()
#
# except ValidationError as e:
#     print("Validation Error for Book:")
#     for field, errors in e.message_dict.items():
#         print(f"{field}: {', '.join(errors)}")


#
# Exam: 03. Tax-Inclusive Pricing
# Test Code
#
# # Create a Product instance
# product = Product.objects.create(name="Gaming Keyboard", price=Decimal(100.00))
#
# # Calculate and print the tax
# tax_price = product.calculate_tax()
# print(f"Tax for {product.name}: ${tax_price:.2f}")
#
# # Calculate and print the shipping cost
# shipping_cost = product.calculate_shipping_cost(Decimal(2.50))
# print(f"Shipping Cost for {product.name}: ${shipping_cost:.2f}")
#
# # Format and print the product name
# formatted_name = product.format_product_name()
# print(f"Formatted Product Name: {formatted_name}")
#
# # Create a DiscountedProduct instance
# discounted_product = DiscountedProduct.objects.create(name="Gaming Mouse", price=Decimal(120.00))
#
# # Calculate and print the price without discount (DiscountedProduct)
# discounted_price = discounted_product.calculate_price_without_discount()
# print(f"Price Without Discount for {discounted_product.name}: ${discounted_price:.2f}")
#
# # Calculate and print the tax (DiscountedProduct)
# tax_price = discounted_product.calculate_tax()
# print(f"Tax for {discounted_product.name}: ${tax_price:.2f}")
#
# # Calculate and print the shipping cost (DiscountedProduct)
# shipping_cost = discounted_product.calculate_shipping_cost(Decimal(2.50))
# print(f"Shipping Cost for {discounted_product.name}: ${shipping_cost:.2f}")
#
# # Format and print the product name (DiscountedProduct)
# formatted_name = discounted_product.format_product_name()
# print(f"Formatted Product Name: {formatted_name}")

