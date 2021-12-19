from case3_1.models import Book
from django.http import JsonResponse, HttpResponse
from django.db import connection


def create_books_orm(request):
    author = request.POST.get("author")
    name = request.POST.get("name")

    Book.objects.create(name=name, author=author)

    print(connection.queries)
    return HttpResponse(status=201)


def get_books_orm(request):
    author = request.POST.get("author")
    books = Book.objects.filter(author=author)

    result = []
    for book in books:
        result.append({
            "name": book.name,
            "author": book.author
        })

    print(connection.queries)
    return JsonResponse({"data": result}, status=201)


def get_books_raw(request):
    author = request.POST.get("author")

    sql_query = '''SELECT "case2_book"."id", "case2_book"."name", "case2_book"."author" FROM "case2_book" WHERE "case2_book"."author" = '{}' '''.format(author)

    books = Book.objects.raw(sql_query)

    result = []
    for book in books:
        result.append({
            "name": book.name,
            "author": book.author
        })

    print(connection.queries)
    return JsonResponse({"data": result}, status=201)
