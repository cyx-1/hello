# SQLAlchemy ORM with SQLite Database Demo

This example demonstrates how to use SQLAlchemy as an Object-Relational Mapping (ORM) layer for a SQLite database in Python. It covers model definitions, relationships, and all CRUD (Create, Read, Update, Delete) operations.

## Requirements

- Python 3.10+
- SQLAlchemy 2.0+

## Running the Demo

```bash
uv run --script main_sqlalchemy_sqlite.py
```

## Key Source Code

### Model Definitions with Relationships

**Lines 21-23: Base Class Declaration**
```python
class Base(DeclarativeBase):
    pass
```
This establishes the declarative base that all ORM models inherit from.

**Lines 27-38: Author Model (One-to-Many Parent)**
```python
class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Relationship: one author has many books
    books: Mapped[list["Book"]] = relationship(back_populates="author", cascade="all, delete-orphan")
```
The `Author` model uses typed mappings (`Mapped[type]`) for type safety. The relationship to books includes cascade delete, meaning when an author is deleted, all their books are automatically deleted.

**Lines 42-54: Book Model (One-to-Many Child)**
```python
class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    isbn: Mapped[str] = mapped_column(String(13), unique=True)
    published_year: Mapped[int] = mapped_column(Integer)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))

    # Relationship: many books belong to one author
    author: Mapped["Author"] = relationship(back_populates="books")
```
The `Book` model has a foreign key relationship to `Author` through `author_id`.

### Database Setup

**Lines 64-68: Engine and Schema Creation**
```python
engine = create_engine("sqlite:///:memory:", echo=False)
Base.metadata.create_all(engine)
```
Creates an in-memory SQLite database and generates all tables based on the model definitions.

**Output:**
```
[Step 1] Creating SQLite engine and database schema...
✓ Tables created: authors, books
```

### CREATE Operations

**Lines 76-83: Inserting Authors**
```python
author1 = Author(name="Brandon Sanderson", email="brandon@cosmere.com")
author2 = Author(name="Patrick Rothfuss", email="patrick@kingkiller.com")
author3 = Author(name="N.K. Jemisin", email="nk@brokenearth.com")

session.add_all([author1, author2, author3])
session.commit()
```

**Output:**
```
[Step 3] Inserting authors into database...
✓ Inserted 3 authors
```

**Lines 87-99: Inserting Books with Relationships**
```python
books = [
    Book(title="The Way of Kings", isbn="9780765326355", published_year=2010, author=author1),
    Book(title="Words of Radiance", isbn="9780765326362", published_year=2014, author=author1),
    Book(title="Oathbringer", isbn="9780765326379", published_year=2017, author=author1),
    Book(title="The Name of the Wind", isbn="9780756404079", published_year=2007, author=author2),
    # ... more books
]
session.add_all(books)
session.commit()
```
Notice how relationships are set using the `author=author1` syntax, not by manually setting `author_id`.

**Output:**
```
[Step 4] Inserting books with author relationships...
✓ Inserted 7 books
```

### READ Operations

**Lines 103-107: Query All Records**
```python
stmt = select(Author).order_by(Author.name)
all_authors = session.scalars(stmt).all()
for author in all_authors:
    print(f"  {author}")
```
SQLAlchemy 2.0 uses the `select()` function for queries, not the legacy `session.query()`.

**Output:**
```
[Step 5] Querying all authors...
  Author(id=1, name='Brandon Sanderson', email='brandon@cosmere.com')
  Author(id=3, name='N.K. Jemisin', email='nk@brokenearth.com')
  Author(id=2, name='Patrick Rothfuss', email='patrick@kingkiller.com')
```

**Lines 110-115: Filtered Query**
```python
stmt = select(Book).where(Book.published_year > 2014).order_by(Book.published_year)
recent_books = session.scalars(stmt).all()
```
The `where()` clause filters results using SQL-like expressions.

**Output:**
```
[Step 6] Querying books published after 2014...
  2015: The Fifth Season
  2016: The Obelisk Gate
  2017: Oathbringer
```

**Lines 118-124: Relationship Navigation (Lazy Loading)**
```python
stmt = select(Author).where(Author.name == "Brandon Sanderson")
brandon = session.scalar(stmt)
if brandon:
    print(f"  Books written:")
    for book in brandon.books:
        print(f"    - {book.title} ({book.published_year})")
```
Once an author is loaded, accessing `brandon.books` triggers a lazy query to load related books.

**Output:**
```
[Step 7] Accessing author's books through relationship...
  Author: Brandon Sanderson
  Books written:
    - The Way of Kings (2010)
    - Words of Radiance (2014)
    - Oathbringer (2017)
```

**Lines 128-134: Join Query**
```python
stmt = select(Book, Author).join(Book.author).where(Author.email.like("%cosmere%"))
results = session.execute(stmt).all()
for book, author in results:
    print(f"  '{book.title}' by {author.name}")
```
Explicit joins allow filtering across relationships efficiently.

**Output:**
```
[Step 8] Querying books with author information (using join)...
  'The Way of Kings' by Brandon Sanderson
  'Words of Radiance' by Brandon Sanderson
  'Oathbringer' by Brandon Sanderson
```

### UPDATE Operations

**Lines 137-142: Modifying Records**
```python
stmt = select(Book).where(Book.isbn == "9780765326355")
book_to_update = session.scalar(stmt)
if book_to_update:
    book_to_update.published_year = 2011  # Update the field
    session.commit()  # Persist the change
```
Updates are performed by modifying object attributes and calling `commit()`.

**Output:**
```
[Step 9] Updating a book's publication year...
  Before: The Way of Kings - Year: 2010
  After:  The Way of Kings - Year: 2011
```

**Lines 146-150: Aggregate Query Using Relationships**
```python
stmt = select(Author).order_by(Author.name)
authors = session.scalars(stmt).all()
for author in authors:
    print(f"  {author.name}: {len(author.books)} books")
```

**Output:**
```
[Step 10] Counting books per author...
  Brandon Sanderson: 3 books
  N.K. Jemisin: 2 books
  Patrick Rothfuss: 2 books
```

### DELETE Operations

**Lines 153-159: Deleting a Single Record**
```python
stmt = select(Book).where(Book.isbn == "9780756407919")
book_to_delete = session.scalar(stmt)
if book_to_delete:
    session.delete(book_to_delete)
    session.commit()
```

**Output:**
```
[Step 11] Deleting a book...
  Deleting: The Wise Man's Fear
✓ Book deleted
```

**Lines 162-169: Verifying Deletion**
```python
stmt = select(Author).where(Author.name == "Patrick Rothfuss")
patrick = session.scalar(stmt)
if patrick:
    print(f"  Remaining books: {len(patrick.books)}")
```

**Output:**
```
[Step 12] Verifying deletion - Patrick Rothfuss's remaining books...
  Remaining books: 1
    - The Name of the Wind
```
Patrick Rothfuss had 2 books; after deleting one, only 1 remains.

**Lines 171-182: Cascade Delete**
```python
stmt = select(Author).where(Author.name == "N.K. Jemisin")
author_to_delete = session.scalar(stmt)
if author_to_delete:
    book_count = len(author_to_delete.books)
    session.delete(author_to_delete)
    session.commit()
```
Because the `Author.books` relationship has `cascade="all, delete-orphan"` (line 36), deleting an author automatically deletes all their books.

**Output:**
```
[Step 13] Cascade delete - Removing author and all their books...
  Deleting author: N.K. Jemisin
  This will cascade delete 2 books
✓ Author and 2 books deleted
```

**Lines 184-189: Counting Records with func.count()**
```python
author_count = session.scalar(select(func.count()).select_from(Author))
book_count = session.scalar(select(func.count()).select_from(Book))
```

**Output:**
```
[Step 14] Final database statistics...
  Total authors: 2
  Total books: 4
```
Final tally: Started with 3 authors and 7 books, ended with 2 authors and 4 books after deletions.

## Full Program Output

```
================================================================================
SQLAlchemy ORM with SQLite Database Demo
================================================================================

[Step 1] Creating SQLite engine and database schema...
✓ Tables created: authors, books

[Step 2] Creating database session...

[Step 3] Inserting authors into database...
✓ Inserted 3 authors

[Step 4] Inserting books with author relationships...
✓ Inserted 7 books

[Step 5] Querying all authors...
  Author(id=1, name='Brandon Sanderson', email='brandon@cosmere.com')
  Author(id=3, name='N.K. Jemisin', email='nk@brokenearth.com')
  Author(id=2, name='Patrick Rothfuss', email='patrick@kingkiller.com')

[Step 6] Querying books published after 2014...
  2015: The Fifth Season
  2016: The Obelisk Gate
  2017: Oathbringer

[Step 7] Accessing author's books through relationship...
  Author: Brandon Sanderson
  Books written:
    - The Way of Kings (2010)
    - Words of Radiance (2014)
    - Oathbringer (2017)

[Step 8] Querying books with author information (using join)...
  'The Way of Kings' by Brandon Sanderson
  'Words of Radiance' by Brandon Sanderson
  'Oathbringer' by Brandon Sanderson

[Step 9] Updating a book's publication year...
  Before: The Way of Kings - Year: 2010
  After:  The Way of Kings - Year: 2011

[Step 10] Counting books per author...
  Brandon Sanderson: 3 books
  N.K. Jemisin: 2 books
  Patrick Rothfuss: 2 books

[Step 11] Deleting a book...
  Deleting: The Wise Man's Fear
✓ Book deleted

[Step 12] Verifying deletion - Patrick Rothfuss's remaining books...
  Remaining books: 1
    - The Name of the Wind

[Step 13] Cascade delete - Removing author and all their books...
  Deleting author: N.K. Jemisin
  This will cascade delete 2 books
✓ Author and 2 books deleted

[Step 14] Final database statistics...
  Total authors: 2
  Total books: 4

✓ Session closed

================================================================================
Demo completed successfully!
================================================================================
```

## Key SQLAlchemy Concepts Demonstrated

1. **Declarative Models**: Using `DeclarativeBase` and `Mapped[]` type hints for type-safe model definitions
2. **Relationships**: One-to-many relationships with `relationship()` and `ForeignKey`
3. **Cascade Operations**: Automatic deletion of child records using `cascade="all, delete-orphan"`
4. **Session Management**: Using `Session` for transaction management
5. **Modern Query API**: SQLAlchemy 2.0's `select()` syntax instead of legacy `query()`
6. **CRUD Operations**: Complete examples of Create, Read, Update, and Delete
7. **Filtering**: Using `where()` clauses for conditional queries
8. **Joins**: Explicit joins across relationships
9. **Aggregation**: Using `func.count()` for aggregate queries
10. **Lazy Loading**: Accessing related objects through relationship attributes

## Version Requirements

This code requires **SQLAlchemy 2.0 or higher** due to:
- Use of `select()` function instead of `session.query()`
- `Mapped[]` type hints with `mapped_column()`
- Modern query execution patterns with `scalars()` and `scalar()`
