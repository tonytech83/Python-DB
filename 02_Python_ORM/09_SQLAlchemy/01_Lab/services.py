from models import User, Order
from main import Session

# Perform Database Operations

# create a new session, create a new user object, add it to that session,
# and then commit the changes to the database
with Session() as session:
    new_user = User(username='john_doe', email='john@example.com')
    session.add(new_user)
    session.commit()

# retrieve all data from a table
with Session() as session:
    users = session.query(User).all()
    for user in users:
        print(user.username, user.email)

# update a record from the database
with Session() as session:
    user_to_update = session.query(User).filter_by(username='john_doe').first()

    if user_to_update:
        user_to_update.email = 'new_email@example.com'
        session.commit()
        print('User updated successfully')
    else:
        print('User not found')

# delete a record from the database
with Session() as session:
    user_to_delete = session.query(User).filter_by(username='john_doe').first()

    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()
        print('User deleted successfully')
    else:
        print('User not found')

# create multiple users in the database
users = [
    ('john_doe', 'john.doe@example.com'),
    ('sarah_smith', 'sarah.smith@gmail.com'),
    ('mike_jones', 'mike.jones@company.com'),
    ('emma_wilson', 'emma.wilson@domain.net'),
    ('david_brown', 'david.brown@email.org'),
]

with Session() as session:
    users_to_add = []
    for user in users:
        users_to_add.append(User(username=user[0], email=user[1]))

    session.add_all(users_to_add)
    session.commit()
    print('All users added successfully')

# Populate Order Table
with Session() as session:
    session.add_all((Order(user_id=7), Order(user_id=9)))
    session.commit()

# Queries for Relationships
with Session() as session:
    orders = session.query(Order).order_by(Order.user_id.desc()).all()

    if not orders:
        print('No orders yet.')
    else:
        for order in orders:
            user = order.user
            print(f'Order number {order.id}, Is completed: {order.is_completed}, Username: {user.username}')
