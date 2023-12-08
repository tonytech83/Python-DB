## Django Models

```
ORM - Object Relational Mapping
```

### 1. Django models

- Each model is a separate table.
- Each variable that uses a field from `models` is a column in that table.
- Models allow us to avoid writing low-level SQL.

### 2. Model creation

- Inheritance `models.Model`

### 3. Migrations

- `makemigrations` - Create migration file
- `migrate` - Applies migrations files to database

### 4. Other commands

- `dbshell` - console where can use SQL directly
- `CTRL + ALT + R` - django console in PyCharm

---

## Migrations and Admin

### 1. Django Migrations Advanced

- Migrations help us to keep our models up-to-date.
- They also allow us to save previous states of our database.
- Commands:
  - `makemigrations` - creates a new migration file.
  - `migrate` - applies all migrations to the database.
  - `migrate main_app 0001` - rolls back to a specific migration.
  - `migrate main_app zero` - rolls back all migrations.
  - `showmigrations` - shows all apps and their migrations.
  - `showmigrations app_name` - shows the migrations for a specific app.
  - `showmigrations --list` - same as `howmigrations -l`
  - `squashmigrations app_name migration_to_which_you_want_to_sqash` - merges migrations up to a specific migration into one migration.
  - `sqlmigrate app_name migration_name` - shows the SQL for the current migration. This can be used to check if the migration is valid.
  - `makemigrations --empty main_app` - creates an empty migration in a specified app.

### 2. Custom/Data migrations

- When we add a new field, for example, and we want to populate it with data based on existing fields, we use data migrations.
- RunPython
- Calling a function through it gives us access to all apps and their models (first parameter), Scheme Editor (second parameter).
- It is a good practice to pass a function and a reverse function, so that we can roll back migrations without problems.
- Scheme Editor is a class that converts our Python code into SQL. We use it when we create, alter, or delete a table.
  - Using RunPython in 95% of cases, we will not need to use Scheme Editor, except if we are creating a temporary table, indexes, or changing the table schema.
- Steps:

  2.1. Create an empty migration file: `makemigrations --empty main_app` - creates an empty migration in a specified app.

  2.2. Define operations - We use RunPython to execute data migrations.

  2.3. Apply the changes: migrate.

Example with a temporary table:

Assume you have a model named "Person" in your Django application and you want to create a temporary table to store some calculated data based on the existing data in the "Person" table. In this case, you can use a data migration to perform this operation:

1. **Create the Data Migration:**

Run the following command to create a data migration:

```bash
python manage.py makemigrations your_app_name --empty
```

This will create an empty data migration file.

2. **Edit the Data Migration:**

Open the generated data migration file and modify it to use `RunPython` with a custom Python function that utilizes the `SchemaEditor` to create a temporary table. Here's an example:

```python
from django.db import migrations, models

def create_temporary_table(apps, schema_editor):
    # Get the model class
    Person = apps.get_model('your_app_name', 'Person')

    # Access the SchemaEditor to create a temporary table
    schema_editor.execute(
        "CREATE TEMPORARY TABLE temp_person_data AS SELECT id, first_name, last_name FROM your_app_name_person"
    )

def reverse_create_temporary_table(apps, schema_editor):
    schema_editor.execute("DROP TABLE temp_person_data")

class Migration(migrations.Migration):

    dependencies = [
        ('your_app_name', 'previous_migration'),
    ]

    operations = [
        migrations.RunPython(create_temporary_table, reverse_create_temporary_table),
    ]
```

### 3. Django admin

- createsuperuser
- Register model, example:

```python
   @admin.register(OurModelName)
   class OurModelNameAdmin(admin.ModelAdmin):
	pass
```

### 4. Admin site customizations

- **str** - method into model for better visualization in Admin portal.

- `list_display` - List of fields names which we want to display into Admin portal.

  Example:

  ```python
  class EmployeeAdmin(admin.ModelAdmin):
  	list_display = ['job_title', 'first_name', 'email_address']
  ```

- `list_filter` - adds side panel with predefine fields for filtering

  Example:

  ```python
   class EmployeeAdmin(admin.ModelAdmin):
   	list_filter = ['job_level']
  ```

- `search_fields`- which fields we allow to search, by default they are all

  Example:

  ```python
  class EmployeeAdmin(admin.ModelAdmin):
      search_fields = ['email_address']
  ```

- `Layout changes` - choose which fields how and whether to appear when adding or changing a record

  Example:

  ```python
  class EmployeeAdmin(admin.ModelAdmin):
      fields = [('first_name', 'last_name'), 'email_address']
  ```

- `list_per_page` - control how many items appear on each paginated admin change list page. By default, this is set to 100.

- `fieldsets` - make simple layout changes in the forms on the “add” and “change” pages

  Example:

  ```python
    fieldsets = (
         ('Personal info',
            {'fields': (...)}),
         ('Advanced options',
            {'classes': ('collapse',),
         'fields': (...),}),
    )
  ```

---

## Data Operations in Django with queries

### 1. CRUD overview

- CRUD - Create, Read, Update, Delete
- Use it for:
  - Web Development
  - Database Management
- It gives us a consistent way to create CRUD functionality.
- We can do it through Django's ORM

### 2. Django Manager:

- A class-level attribute of a model for database interactions.
- Responsible for CRUD.
- Custom Manager: models.Model sub-class.
  - Why custom managers:
    - Encapsulation of common or complex queries.
    - Improved code readability.
    - Avoid repetition and improve reusability.
    - Change request sets as needed.

### 3. Django QuerySet

- QuerySet - a python class that we use to hold the data from a given query.
- Data is not collected until requested by us
  ```python
  cars = Cars.objects.all() # <QuerySet []>
  print(cars)  # <QuerySet [Car object(1)]>
  ```
- QuerySet Features:

  - Lazy Evaluation - the query is not called until the data is needed
  - Retrieving objects - we can take all objects or according to a given criteria
  - Chaining filters
    ```python
    MyModel.objects.filter(category='electronics').filter(price__lt=1000)
    ```
  - Query related objects - allows us to search in tables with which we have relations through the model: # Query related objects using double underscores

    ```python
    related_objects = Order.objects.filter(customer__age__gte=18)
    ```

  - Ordering
    ```python
    ordered_objects = Product.objects.order_by('-price')
    ```
  - Pagination

    ```python
    from django.core.paginator import Paginator

    # Paginate queryset with 10 objects per page
    paginator = Paginator(queryset, per_page=10)
    page_number = 2
    print([x for x in paginator.get_page(2)])
    ```

### 4. Django Simple Queries

- Object Manager - default Objects
- Methods:
  - `all()` - returns all objects in QuerySet
  - `first()` - returns first object
  - `get(**kwargs)` - get instance by `**kwargs`
  - `create(**kwargs)`
  - `filter(**kwargs)` - filter QuerySet by `**kwarks`
  - `order_by(*fields)` - order QuerySet by `*fields`
  - `delete()` - delete

### 5. Django Shell and SQL Logging

- Django Shell
  - It gives us access to the whole project
  - python manage.py shell
- SQL logging

  - Enable SQL logging

    ```python
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG',  # Other levels CRITICAL, ERROR, WARNING, INFO, DEBUG
        },
        'loggers': {
            'django.db.backends': {  # responsible for the sql logs
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False,
            },
        },
    }
    ```

---

## Working with queries

Working with Queries

### 1. Useful Methods

- `filter()` - returns a subset of objects; accepts kwargs; return QuerySet;
- `exclude()` - returns a subset of objects; accepts kwargs; return QuerySet;
- `order_by()` - returns the sorted objects; - for desc;
- `count()` - like len, but faster; count returns only the count without needing the actual objects;
- `get()` - takes an object according to given criteria;

### 2. Chaning methods

- each method works with the result returned by the previous one

### 3. Lookup keys

- They are used in filter, exclude, get;
- `__exact`, `__iexact` - exact match;
- `__contains`, `__icontains` - checks if it is contained;
- `__startswith`, `__endswith`
- `__gt`, `__gte`
- `__lt`, `__lte`
- `__range=(2, 5)` - both inclusive

### 4. Bulk methods - are used to perform operations on many objects simultaneously

- `bulk_create` - creates multiple objects at once;
- `filter().update()`
- `filter().delete()`

---

## Django Relations

Django Models Relations

### 1. Database Normalization

- Efficient Database Organization

  - Data normalization - breaks large tables into smaller ones, making data more organized
  - Example: It's as if we have an online store and instead of keeping name, address and order in one table, we can break it into 3 tables and so we don't repeat records.

- Guidelines and Rules

  - First Normal Form - First Normal Form (1NF): we eliminate corrupt records, each table keeps unique values.

- Second Normal Form (2NF): we do the former by making it dependent on `pk`. - Example: Online store with data and purchases Customers and Orders are linked to `pk` instead of everything being in one table.

- Third Normal Form (3NF):
  - remove transient dependencies.
  - Employees table keeps `id`, `employee`, `city`, `address` => we divide them into 3 tables and connect them, not necessarily by `pk`, maybe by `city_id`, employee is now independent.
- Boyce-Codd Normal Form (BCNF):

  - A stricter version of 3NF.
  - Here we make them bind on `pk`.

- Fourth Normal Form (4NF):
  - If data from one table is used in two others, this is not good.
  - Example: We have Course X and Course Y, X needs books A and B, Y needs A and C, what we do is make a table of books A and a table of Books B.
- Fifth Normal Form (5NF) - Project-Join Normal Form or PJ/NF:

  - In short so we don't have to go through tables of data we don't need to get to a table of data we do need.

- Database Schema Design

  - Creating various keys and relationships between tables.

- Minimizing Data Redundancy

  - By breaking tables we would again have reduced repetition of information
  - We have a book and copies, the copies are in a separate table, and are linked to the original.

- Ensuring Data Integrity & Eliminating Data Anomalies

  - This helps us update and delete data everywhere equally.
  - again thanks to some constraints we can change one value in one table and it is reflected in all.

- Efficiency and Maintainability
  - Thanks to the smaller tables, we query and update them faster.

### 2. Relations in Django Models

- Obtained using ForeignKey fields
- `related_name` - we can make a reverse link

  - By default it is the name + `_set`

- Example:

  ```python
  class Author(models.Model):
      name = models.CharField(max_length=100)

  class Post(models.Model):
      title = models.CharField(max_length=200)
      content = models.TextField()
      author = models.ForeignKey(Author, on_delete=models.CASCADE)
  ```

- Access all posts written by an author
  ```python
  author = Author.objects.get(id=1)
  author_posts = author.post_set.all()
  ```

### 3. Types of relationships

- Many-To-One (One-To-Many)
- Many-To-Many

  - It doesn't matter in which model it goes
  - Django automatically creates a join table or also called a junction
  - But, if we want, we can also create:

  ```python
  class Author(models.Model):
      name = models.CharField(max_length=100)

  class Book(models.Model):
      title = models.CharField(max_length=200)
      authors = models.ManyToManyField(Author, through='AuthorBook')

  class AuthorBook(models.Model):
      author = models.ForeignKey(Author, on_delete=models.CASCADE)
      book = models.ForeignKey(Book, on_delete=models.CASCADE)
      publication_date = models.DateField()
  ```

- OneToOne - mostly using `pk`
- Self-referential Foreign Key

  - Example we have workers and they can be managers of other workers

    ```python
    class Employee(models.Model):
        name = models.CharField(max_length=100)
        supervisor = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    ```

- Lazy Relationships - the object from the relation is retrieved, by request, only when it is called.

---

## Models Inheritance and Customization

### 1. Types of Inheritance

- Multi-table

  - We extend a model with the fields from another model, not copying the fields themselves, but using the pointer created by django, which makes a One-To-One Relationship
  - Example:

    ```python
    class Person(models.Model):
        name = models.CharField(max_length=100)
        date_of_birth = models.DateField()

        def is_student(self):
            """Check if this person is also a student."""
            return hasattr(self, 'student')

    class Student(Person):
        student_id = models.CharField(max_length=15)
        major = models.CharField(max_length=50)
    ```

- Abstract Base Classes

  - In this inheritance, two new tables are not created, but only one, and it belongs to the inheriting class (Child), and the abstract class (Parent) is only a template
  - We achieve it by changing the Meta class:

    ```python
    class AbstractBaseModel(models.Model):
        common_field1 = models.CharField(max_length=100)
        common_field2 = models.DateField()

        def common_method(self):
            return "This is a common method"

        class Meta:
            abstract = True
    ```

- Proxy Models

  - We use them to add functionality to a model that we cannot access
  - We can add methods but not new fields
  - Example:

    ```python
    class Article(models.Model):
        title = models.CharField(max_length=200)
        content = models.TextField()
        published_date = models.DateField()

    class RecentArticle(Article):
        class Meta:
            proxy = True

        def is_new(self):
            return self.published_date >= date.today() - timedelta(days=7)

        @classmethod
        def get_recent_articles(cls):
            return cls.objects.filter(published_date__gte=date.today() - timedelta(days=7))
    ```

### 2. Basic Built-In Methods

- `save()` - used to save records

```py
    def save(self, *args, **kwargs):
        # Check the price and set the is_discounted field
        if self.price < 5:
            self.is_discounted = True
        else:
            self.is_discounted = False

        # Call the "real" save() method
        super().save(*args, **kwargs)
```

- `clean()` - is used when we want to logically validate several fields, for example we have a t-shirt in 3 colors but if XXL is selected the colors are only 2.

### 3. Custom Model Properties

- As in OOP, we can use the @property decorator to create new attributes, which in this case are not saved in the database
- We use them for dynamic value calculations

### 4. Custom Model Fields

- We use them when Django doesn't have fields that work for us
- We have methods like:

  - `from_db_value` - called when we want to get the value from the python database
  - `to_python` - called when we do deserialization or clean
  - `get_prep_value` - the opposite of from_db_value, from Python to the base, we mainly use for serializations
  - `pre_save` - used for last minute changes, just before we save the result to the database

  ```python
  class RGBColorField(models.TextField):
      # Convert the database format "R,G,B" to a Python tuple (R, G, B)
      def from_db_value(self, value, expression, connection):
          if value is None:
              return value
          return tuple(map(int, value.split(',')))

      # Convert any Python value to our desired format (tuple)
      def to_python(self, value):
          if isinstance(value, tuple) and len(value) == 3:
              return value
          if isinstance(value, str):
              return tuple(map(int, value.split(',')))
          raise ValidationError("Invalid RGB color format.")

      # Prepare the tuple format for database insertion
      def get_prep_value(self, value):
          # Convert tuple (R, G, B) to "R,G,B" for database storage
          return ','.join(map(str, value))
  ```

---

## Advanced Django Models Techniques

### 1. Validation in Models

- Built-in Validators

  - `MaxValueValidator`, `MinValueValidator` - accepts two arguments (limit, message)
  - `MaxLengthValidator`, `MinLengthValidator` - accepts two arguments (limit, message)
  - `RegexValidator` - accepts two arguments (regex, message)

    ```python
    class SampleModel(models.Model):
        name = models.CharField(
            max_length=50,
            validators=[MinLengthValidator(5)]  # Name should have a minimum length of 5 characters
        )

        age = models.IntegerField(
            validators=[MaxValueValidator(120)]  # Assuming age shouldn't exceed 120 years
        )

        phone = models.CharField(
            max_length=15,
            validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )]  # A simple regex for validating phone numbers
        )
    ```

- Custom Validators - functions that we often write in a separate file. In case of an error, we raise `ValidationError`

### 2. Meta Options and Meta Inheritance

- In the meta class we can change:

  - The name of the table
  - The arrangement of the data
  - We can set constraints
  - We can set the class type (proxy, abstract)

    ```python
    class SampleModel(models.Model):
        name = models.CharField(max_length=50)
        age = models.IntegerField()
        email = models.EmailField()

        class Meta:
            # Database table name
            db_table = 'custom_sample_model_table'

            # Default ordering (ascending by name)
            ordering = ['name'] # Happens on SELECT, not INSERT

            # Unique constraint (unique combination of name and email)
            unique_together = ['name', 'email']
    ```

- Meta inheritance:

  - If we inherit an abstract class and do not override the meta class, we inherit the meta class of the abstract class

    ```python
    class BaseModel(models.Model):
        name = models.CharField(max_length=100)

        class Meta:
            abstract = True
            ordering = ['name']

    class ChildModel(BaseModel):
        description = models.TextField()
        # ChildModel inherits the Meta options
    ```

### 3. Indexing

- Indexing helps us by arranging items in a certain order or creating another structure through which to search faster.
- We take records quickly, but save them more slowly.
- In Django we can put an index on a field by adding the key-word argument `db_index=True`.
- We can also make an index, through the meta class, and we can also make a composite index.

  ```python
  class Meta:
      indexes = [
          models.Index(
              fields=["title", "author"]
          ),  # makes searching by two criteria faster
          models.Index(fields=["publication_date"]),
      ]
  ```

### 4. Django Model Mixins

- As we know, `Mixins` are classes that we use to separate common functionality

```python
class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
```

---

## Advanced Django Queries

### 1. Custom Managers

- We use them to export business logic for frequently used queries in one place
- We do it by inheriting the default manager.

  ```python
  class BookManager(models.Manager):
      def average_rating(self):
          # Calculate the average rating of all books
          return self.aggregate(avg_rating=models.Avg('rating'))['avg_rating']

      def highest_rated_book(self):
          # Get the highest-rated book
          return self.order_by('-rating').first()
  ```

### 2. Annotations and Aggregations

- Annotations - we use these to add new fields to the returned result, often based on some calculations. Returns an QuerySet.
- Example:

  ```python
  # Annotating the queryset to get the count of books for each author
  authors_with_book_count = Book.objects.values('author').annotate(book_count=Count('id'))
  ```

- Aggregations - return one field (one value), often the result of aggregation functions. Returns `dict`.

  ```python
  # Annotating the queryset to get the average rating of all books
  average_rating = Book.objects.aggregate(avg_rating=Avg('rating'))
  ```

### 3. select_related & prefetch_related

- `select_related` - reduces the number of requests in One-To-One and Many-To-One requests

  - instead of lazily fetching the connected objects, we do JOIN on the first request
  - Example:

  ```python
  from django.db import models

  class Author(models.Model):
      name = models.CharField(max_length=100)

  class Book(models.Model):
      title = models.CharField(max_length=100)
      author = models.OneToOneField(Author, on_delete=models.CASCADE)

  books_with_authors = Book.objects.select_related('author')
  ```

  ```sql
  SELECT * FROM "myapp_book" JOIN "myapp_author" ON ("myapp_book"."author_id" = "myapp_author"."id")
  ```

- `prefetch_related` - reduces the number of Many-To-Many requests (not only) to the number of relations + 1
- Example:

  ```python
  class Author(models.Model):
      name = models.CharField(max_length=100)

  class Book(models.Model):
      title = models.CharField(max_length=100)
      authors = models.ManyToManyField(Author)

  authors_with_books = Author.objects.prefetch_related('book_set')
  ```

  ```sql
  SELECT * FROM "myapp_author"
  SELECT * FROM "myapp_book" INNER JOIN "myapp_book_authors" ON ("myapp_book"."id" = "myapp_book_authors"."book_id")
  ```

### 4. Q and F

- We use the `Q` object to make queries requiring more complex conditions.
- Example:

  ```python
  q = Q(title__icontains='Django') & (Q(pub_year__gt=2010) | Q(author='John Doe'))

  books = Book.objects.filter(q)
  ```

- We use the `F` object to access the values through which we iterate at the SQL level.

  ```python
  from django.db.models import F

  Book.objects.update(rating=F('rating') + 1)
  ```

---

## SQL Alchemy

### 1. SQL Alchemy - ORM - Object Relational Mapper

- ORM - an abstraction allowing us to write SQL, through Python
- Core - takes care of transactions, sending requests, sessions and database pooling

### 2. SetUp:

1.  `pip install sqlalchemy`
2.  `pip install psycopg2`

### 3. Models

- Like Django we inherit a base class, `Base`, which we take as the result of calling `declarative_base()`

  ```python
  from sqlalchemy.ext.declarative import declarative_base

  Base = declarative_base()

  class User(Base):
      __tablename__ = 'users'

      id = Column(Integer, primary_key=True)
      name = Column(String)
  ```

### 4. Migrations

- SetUp: - They are not included in SQLAlchemy, for them we can use Alembic.

  - `pip install alembic`
  - `alembic init alembic` - creates the file structure for us for the migrations
  - `sqlalchemy.url = postgresql+psycopg2://username:password@localhost/db_name` - in the `alembic.ini` file

  - `py target_metadata = Base.metadata` - in the `env.py` file so we can support autogenerate

- Commands: - `alembic revision --autogenerate -m "Add User Table"` - creates migration with reported as `makemigrations`

  - `alembic upgrade head` - applies migrations like `migrate` in Django
  - `alembic downgrade -1` - reverse migration

### 5. CRUD

- We open a connection to the base, launching a new session
- We always close the session after finishing work
- We need to commit the result, similar to Django where we used `save()`

    ```python
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('sqlite:///example.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    with Session() as session: # a good practice
    ...
    ```

  - Add:

      ```python
      new_user = User(username='john_doe', email='john@example.com')
      session.add(new_user)
      ```

  - Query:

      ```python
      users = session.query(User).all()
      ```

  - Update:

    ```python
    with engine.connect() as connection:
      # Create an update object
      upd = update(User).where(User.name == 'John').values(nickname='new_nickname')

    # Execute the update
    connection.execute(upd)
    ```

    or

    ```python
    session.query(User).filter(User.name == 'John').update({"nickname": "new_nickname"}, synchronize_session=False)

    session.commit()
    ```

  - Delete:

    ```python
    del_stmt = delete(User).where(User.name == 'John')
    ```

### 6. Transactions

- `session.begin()`

- `session.commit()`

- `session.rollback()`

### 7. Relationships

1.  Many to One
    ```py
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')
    ```
2.  One to One

- `uselist=false`

```py
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    profile = relationship("UserProfile", back_populates="user", uselist=False)

class UserProfile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="profile")
```

3.  Many to many

```py

user_group_association = Table('user_group', Base.metadata,
  Column('user_id', Integer, ForeignKey('users.id')),
  Column('group_id', Integer, ForeignKey('groups.id'))
)

class Group(Base):
  __tablename__ = 'groups'

  id = Column(Integer, primary_key=True)
  users = relationship("User", secondary=user_group_association, back_populates="groups")

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  groups = relationship("Group", secondary=user_group_association, back_populates="users")

```

### 8. Database pooling

`py engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)` - sets initial connections and maximum created
