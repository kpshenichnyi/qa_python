import pytest
from main import BooksCollector

# # ФИКСТУРЫ
# фикстура с созданием объекта класса BooksCollector
@pytest.fixture()
def collector_books():
    return BooksCollector()

# фикстура добавления одной книги в список
@pytest.fixture()
def add_one_book_collector_books(collector_books):
    return collector_books.add_new_book("Преступление и наказание")


# фикстура со списком книг по каждому жанру
@pytest.fixture()
def collector_list_books_all_genre():
    list_books_all_genre = [['Дюна', 'Фантастика'], ['Мгла', 'Ужасы'], ['Собака Баскервилей', 'Детективы'], ['Путешествие Нильса с дикими гусями', 'Мультфильмы'], ['Золотой теленок', 'Комедии']]
    return list_books_all_genre
