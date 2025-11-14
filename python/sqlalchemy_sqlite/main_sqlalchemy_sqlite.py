#!/usr/bin/env python3
# /// script
# dependencies = [
#   "sqlalchemy>=2.0.0",
# ]
# ///

"""
SQLAlchemy ORM Demo with SQLite Database

This script demonstrates:
- Setting up SQLAlchemy with SQLite
- Defining models with relationships
- CRUD operations
- Querying and filtering
- One-to-many relationships
"""

from datetime import datetime
from sqlalchemy import create_engine, String, Integer, DateTime, ForeignKey, select, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session


# Line 21-23: Define base class for declarative models
class Base(DeclarativeBase):
    pass


# Line 27-38: Define Author model (one side of one-to-many relationship)
class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Relationship: one author has many books
    books: Mapped[list["Book"]] = relationship(back_populates="author", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Author(id={self.id}, name='{self.name}', email='{self.email}')"


# Line 42-54: Define Book model (many side of one-to-many relationship)
class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    isbn: Mapped[str] = mapped_column(String(13), unique=True)
    published_year: Mapped[int] = mapped_column(Integer)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))

    # Relationship: many books belong to one author
    author: Mapped["Author"] = relationship(back_populates="books")

    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}', isbn='{self.isbn}')"


def main():
    print("=" * 80)
    print("SQLAlchemy ORM with SQLite Database Demo")
    print("=" * 80)

    # Line 64-65: Create SQLite engine (in-memory database)
    print("\n[Step 1] Creating SQLite engine and database schema...")
    engine = create_engine("sqlite:///:memory:", echo=False)

    # Line 68: Create all tables
    Base.metadata.create_all(engine)
    print("✓ Tables created: authors, books")

    # Line 72-73: Create a session for database operations
    print("\n[Step 2] Creating database session...")
    session = Session(engine)

    # Line 76-83: CREATE - Insert authors
    print("\n[Step 3] Inserting authors into database...")
    author1 = Author(name="Brandon Sanderson", email="brandon@cosmere.com")
    author2 = Author(name="Patrick Rothfuss", email="patrick@kingkiller.com")
    author3 = Author(name="N.K. Jemisin", email="nk@brokenearth.com")

    session.add_all([author1, author2, author3])
    session.commit()
    print("✓ Inserted 3 authors")

    # Line 87-99: CREATE - Insert books with relationships
    print("\n[Step 4] Inserting books with author relationships...")
    books = [
        Book(title="The Way of Kings", isbn="9780765326355", published_year=2010, author=author1),
        Book(title="Words of Radiance", isbn="9780765326362", published_year=2014, author=author1),
        Book(title="Oathbringer", isbn="9780765326379", published_year=2017, author=author1),
        Book(title="The Name of the Wind", isbn="9780756404079", published_year=2007, author=author2),
        Book(title="The Wise Man's Fear", isbn="9780756407919", published_year=2011, author=author2),
        Book(title="The Fifth Season", isbn="9780316229296", published_year=2015, author=author3),
        Book(title="The Obelisk Gate", isbn="9780316229265", published_year=2016, author=author3),
    ]

    session.add_all(books)
    session.commit()
    print(f"✓ Inserted {len(books)} books")

    # Line 103-107: READ - Query all authors
    print("\n[Step 5] Querying all authors...")
    stmt = select(Author).order_by(Author.name)
    all_authors = session.scalars(stmt).all()
    for author in all_authors:
        print(f"  {author}")

    # Line 110-115: READ - Query with filter
    print("\n[Step 6] Querying books published after 2014...")
    stmt = select(Book).where(Book.published_year > 2014).order_by(Book.published_year)
    recent_books = session.scalars(stmt).all()
    for book in recent_books:
        print(f"  {book.published_year}: {book.title}")

    # Line 118-124: READ - Query with relationship (lazy loading)
    print("\n[Step 7] Accessing author's books through relationship...")
    stmt = select(Author).where(Author.name == "Brandon Sanderson")
    brandon = session.scalar(stmt)
    if brandon:
        print(f"  Author: {brandon.name}")
        print("  Books written:")
        for book in brandon.books:
            print(f"    - {book.title} ({book.published_year})")

    # Line 128-134: READ - Query with join
    print("\n[Step 8] Querying books with author information (using join)...")
    stmt = select(Book, Author).join(Book.author).where(Author.email.like("%cosmere%"))
    results = session.execute(stmt).all()
    for book, author in results:
        print(f"  '{book.title}' by {author.name}")

    # Line 137-142: UPDATE - Modify a book
    print("\n[Step 9] Updating a book's publication year...")
    stmt = select(Book).where(Book.isbn == "9780765326355")
    book_to_update = session.scalar(stmt)
    if book_to_update:
        print(f"  Before: {book_to_update.title} - Year: {book_to_update.published_year}")
        book_to_update.published_year = 2011  # Fictional update
        session.commit()
        print(f"  After:  {book_to_update.title} - Year: {book_to_update.published_year}")

    # Line 146-150: Aggregate query - Count books per author
    print("\n[Step 10] Counting books per author...")
    stmt = select(Author).order_by(Author.name)
    authors = session.scalars(stmt).all()
    for author in authors:
        print(f"  {author.name}: {len(author.books)} books")

    # Line 153-159: DELETE - Remove a book
    print("\n[Step 11] Deleting a book...")
    stmt = select(Book).where(Book.isbn == "9780756407919")
    book_to_delete = session.scalar(stmt)
    if book_to_delete:
        print(f"  Deleting: {book_to_delete.title}")
        session.delete(book_to_delete)
        session.commit()
        print("✓ Book deleted")

    # Line 162-165: Verify deletion
    print("\n[Step 12] Verifying deletion - Patrick Rothfuss's remaining books...")
    stmt = select(Author).where(Author.name == "Patrick Rothfuss")
    patrick = session.scalar(stmt)
    if patrick:
        print(f"  Remaining books: {len(patrick.books)}")
        for book in patrick.books:
            print(f"    - {book.title}")

    # Line 171-177: DELETE - Cascade delete (delete author and all their books)
    print("\n[Step 13] Cascade delete - Removing author and all their books...")
    stmt = select(Author).where(Author.name == "N.K. Jemisin")
    author_to_delete = session.scalar(stmt)
    if author_to_delete:
        book_count = len(author_to_delete.books)
        print(f"  Deleting author: {author_to_delete.name}")
        print(f"  This will cascade delete {book_count} books")
        session.delete(author_to_delete)
        session.commit()
        print(f"✓ Author and {book_count} books deleted")

    # Line 181-186: Final count
    print("\n[Step 14] Final database statistics...")
    author_count = session.scalar(select(func.count()).select_from(Author))
    book_count = session.scalar(select(func.count()).select_from(Book))
    print(f"  Total authors: {author_count}")
    print(f"  Total books: {book_count}")

    # Line 189-190: Cleanup
    session.close()
    print("\n✓ Session closed")

    print("\n" + "=" * 80)
    print("Demo completed successfully!")
    print("=" * 80)


if __name__ == "__main__":
    main()
