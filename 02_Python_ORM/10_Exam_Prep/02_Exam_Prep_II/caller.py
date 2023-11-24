import os
import django
from django.db.models import Count, F, Q

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Profile, Product, Order


def insert_into_db():
    profile1 = Profile.objects.get(
        full_name='Adam Smith',
        email='as@test.com',
        phone_number='001 555 555'
    )
    profile2 = Profile.objects.get(
        full_name='Susan James',
        email='sj@test.co.uk',
        phone_number='0044 333 222'
    )

    product1 = Product.objects.get(
        name='Display DL',
        price=10.99,
        in_stock=10,
    )
    product2 = Product.objects.get(
        name='Desk M',
        price=11.22,
        in_stock=11,
    )
    product3 = Product.objects.get(
        name='Printer Br PM',
        price=22.33,
        in_stock=13,
    )

    # o1 = Order.objects.get(
    #     profile=profile1,
    #     total_price=44.54
    # )

    # o1.products.add(product1)
    # o1.products.add(product2)
    # o1.products.add(product3)
    #
    # o2 = Order.objects.create(
    #     profile=profile1,
    #     total_price=44.54
    # )
    # o2.products.add(product2)
    # o2.products.add(product3)
    #
    # o3 = Order.objects.create(
    #     profile=profile2,
    #     total_price=11.22
    # )
    # o3.products.add(product1)
    #
    # o4 = Order.objects.create(
    #     profile=profile2,
    #     total_price=11.22
    # )
    # o4.products.add(product1)

    o5 = Order.objects.create(
        profile=profile1,
        total_price=22.33
    )
    o5.products.add(product1)


# insert_into_db()


def get_profiles(search_string=None) -> str:
    if search_string is None:
        return ''

    query = Q(full_name__icontains=search_string) | Q(email__icontains=search_string) | Q(
        phone_number__icontains=search_string)

    profiles = Profile.objects.filter(query).order_by('full_name')

    if not profiles:
        return ''

    return '\n'.join(
        f'Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.orders.count()}'
        for p in profiles
    )


def get_loyal_profiles() -> str:
    profiles = Profile.objects.get_regular_customers()

    if not profiles:
        return ''

    return '\n'.join(
        f'Profile: {p.full_name}, orders: {p.orders_count}'
        for p in profiles
    )


def get_last_sold_products() -> str:
    last_order = Order.objects.prefetch_related('products').last()

    if last_order is None or not last_order.products.exists():
        return ''

    products = [p.name for p in last_order.products.all()]

    return f'Last sold products: {", ".join(products)}'


# print(Profile.objects.get_regular_customers())
# print(get_profiles('Co'))
# print(get_profiles('9zz'))
# print(get_loyal_profiles())
# print(get_last_sold_products())


def get_top_products() -> str:
    top_products = (Product.objects
                    .annotate(orders_count=Count('products_orders'))
                    .filter(orders_count__gt=0)
                    .order_by('-orders_count', 'name')[:5])

    if not top_products:
        return ''

    products_rows = [f'{p.name}, sold {p.orders_count} times' for p in top_products]

    return 'Top products:\n' + '\n'.join(products_rows)


def apply_discounts() -> str:
    updated_orders = (Order.objects
                      .annotate(sell_count=Count('products'))
                      .filter(is_completed=False, sell_count__gt=2)
                      .update(total_price=F('total_price') * 0.9))

    return f'Discount applied to {updated_orders} orders.'


def complete_order() -> str:
    order = (Order.objects
             .prefetch_related('products')
             .filter(is_completed=False)
             .first())

    if order is None:
        return ''

    Order.objects.filter(pk=order.pk).update(is_completed=True)
    order.products.update(in_stock=F('in_stock') - 1)
    order.products.filter(in_stock=0).update(is_available=False)

    return "Order has been completed!"


print(get_top_products())
# print(apply_discounts())
# print(complete_order())
