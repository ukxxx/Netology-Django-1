from django.shortcuts import render
from books.models import Book
from datetime import datetime


def books_view(request):
    template = "books/books_list.html"
    books = Book.objects.all()
    book_list = []
    for book in books:
        book_list.append(
            {"name": book.name, "author": book.author, "pub_date": book.pub_date}
        )
    context = {"books": book_list}
    return render(request, template, context)


def books_date_view(request, pub_date):
    template = "books/books_list.html"
    books_all = Book.objects.all()
    books = Book.objects.filter(pub_date=datetime.strptime(pub_date, "%Y-%m-%d").date())
    books = books.order_by("pub_date")

    pub_dates = ()
    for book in books_all:
        pub_dates = pub_dates + (book.pub_date,)
    pub_dates = sorted(list(pub_dates))
    previous_date = None
    next_date = None
    for dt in sorted(pub_dates):
        if dt < datetime.strptime(pub_date, "%Y-%m-%d").date():
            previous_date = dt.strftime("%Y-%m-%d")
        elif dt > datetime.strptime(pub_date, "%Y-%m-%d").date():
            next_date = dt.strftime("%Y-%m-%d")
            break

    context = {
        "books": books,
        "pub_date": datetime.strptime(pub_date, "%Y-%m-%d"),
        "next_page": next_date,
        "previous_page": previous_date,
    }
    return render(request, template, context)
