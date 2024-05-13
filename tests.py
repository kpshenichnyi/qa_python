import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # тест на добавление книги с названием удовлетворяющим ограничению по кол-ву символов 0 < x < 41
    def test_add_new_book_add_two_books(self, collector_books):
        collector_books.add_new_book("Что делать, если ваш кот хочет вас убить")

        assert len(collector_books.get_books_genre()) == 1

    # тест невозможности добавить в словарь книгу с названием равным или больше 41 символа
    @pytest.mark.parametrize('name', ["Что делать если ваш кот хочет вас убить 2", "Что НЕ делать если ваш кот хочет вас убить"])
    def test_add_new_book_with_long_name_not_add(self, collector_books, name):
        collector_books.add_new_book(name)

        assert len(collector_books.get_books_genre()) == 0

    # тест установки для книги из словаря, значения жанра из списка жанров по умолчанию
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_set_default_genre(self, collector_books, add_one_book_collector_books, genre):
        collector_books.set_book_genre('Преступление и наказание', genre)

        assert collector_books.get_book_genre('Преступление и наказание') == genre

    # тест невозможность установить жанр книги не из списка жанров по умолчанию
    @pytest.mark.parametrize('genre', ['Сказки', 'Поэзия'])
    def test_set_book_genre_set_unknown_genre(self, collector_books, add_one_book_collector_books, genre):
        collector_books.set_book_genre("Преступление и наказание", genre)

        assert not collector_books.get_book_genre("Преступление и наказание") == genre

    # тест невозможности установить жанр(перебор значений и списка жанров по умолчанию) для книги отсутствующей в словаре
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_for_unknown_book(self, collector_books, genre):
        collector_books.set_book_genre("Преступление и наказание", genre)

        assert not collector_books.get_book_genre("Преступление и наказание") == genre

    # тест соответсвия названия книги и присвоенного жанра с параметрами
    @pytest.mark.parametrize('name, genre', [['Дюна', 'Фантастика'], ['Мгла', 'Ужасы'], ['Собака Баскервилей', 'Детективы'], ['Путешествие Нильса с дикими гусями', 'Мультфильмы'], ['Золотой теленок', 'Комедии']])
    def test_get_book_genre_get_genre_to_list_books(self, collector_books, name, genre):
        collector_books.add_new_book(name)
        collector_books.set_book_genre(name, genre)
        book_genre = collector_books.get_book_genre(name)

        assert book_genre == genre

    # тест возврата списка книг только указанного в параметрах жанра
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre_get_books_selected_genre(self, collector_books, genre):
        collector_books.add_new_book("Поднятая целина")
        collector_books.add_new_book("Дом который построил Свифт")
        collector_books.set_book_genre("Дом который построил Свифт", genre)
        collector_books.add_new_book("Там, на невиданных дорожках...")
        collector_books.set_book_genre("Там, на невиданных дорожках...", genre)

        assert collector_books.get_books_with_specific_genre(genre) == ["Дом который построил Свифт", "Там, на невиданных дорожках..."]

    # тест на возврат словаря без единой книги
    def test_get_books_genre_get_dictionary_without_books(self, collector_books):
        dic_book_genre = collector_books.get_books_genre()
        assert dic_book_genre == {}

    # тест на возврат словаря из одной книги без жанра
    def test_get_books_genre_get_dictionary_one_book(self, collector_books, add_one_book_collector_books):
        dic_book_genre = collector_books.get_books_genre()
        assert dic_book_genre == {"Преступление и наказание": ''}

    # тест возврата сформированного словаря со множеством книг и жанров
    def test_get_books_genre_get_dictionary_all_books_all_genre(self, collector_books, collector_list_books_all_genre):
        for i in collector_list_books_all_genre:
            collector_books.add_new_book(i[0])
            collector_books.set_book_genre(i[0], i[1])

        assert collector_books.get_books_genre() == {"Дюна": "Фантастика",
                                                    "Мгла": "Ужасы",
                                                    "Собака Баскервилей": "Детективы",
                                                    "Путешествие Нильса с дикими гусями": "Мультфильмы",
                                                    "Золотой теленок": "Комедии"}

    # тест содержания списка книг для детей без запрещенных жанров
    def test_get_books_for_children_get_books_only_for_children(self, collector_books, collector_list_books_all_genre):
        for i in collector_list_books_all_genre:
            collector_books.add_new_book(i[0])
            collector_books.set_book_genre(i[0], i[1])

        assert collector_books.get_books_for_children() == ["Дюна", "Путешествие Нильса с дикими гусями", "Золотой теленок"]

    # тест на отсутствие в списке книг для детей, книг из жанров 'Ужасы', 'Детективы'
    @pytest.mark.parametrize('genre', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_get_zero_list_books(self, collector_books, add_one_book_collector_books, genre):
        collector_books.set_book_genre("Преступление и наказание", genre)

        assert collector_books.get_books_for_children() == []

    # тест добавления книги в список Избранное
    def test_add_book_in_favorites_add_one_book(self, collector_books, add_one_book_collector_books):
        collector_books.add_book_in_favorites("Преступление и наказание")

        assert "Преступление и наказание" in collector_books.get_list_of_favorites_books()

    # тест на удаление книги из списка Избранное
    def test_delete_book_from_favorites_get_zero_list_favorites_book(self, collector_books, add_one_book_collector_books):
        collector_books.add_book_in_favorites("Преступление и наказание")
        collector_books.delete_book_from_favorites("Преступление и наказание")

        assert "Преступление и наказание" not in collector_books.get_list_of_favorites_books()

    # тест получения списка Избранных книг
    def test_get_list_of_favorites_books_get_list_with_two_book(self, collector_books, add_one_book_collector_books):
        collector_books.add_book_in_favorites("Преступление и наказание")
        collector_books.add_new_book("Мастер и Маргарита")
        collector_books.add_book_in_favorites("Мастер и Маргарита")

        assert collector_books.get_list_of_favorites_books() == ["Преступление и наказание", "Мастер и Маргарита"]
