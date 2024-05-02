# qa_python

# ФИКСТУРЫ
    # collector_books: фикстура с созданием объекта класса BooksCollector

    # add_one_book_collector_books: фикстура добавления одной книги
    # 'Преступление и наказание'

    # collector_list_books_all_genre: фикстура со списком книг по каждому жанру
    # ['Дюна', 'Фантастика'], ['Мгла', 'Ужасы'], ['Собака Баскервилей', 'Детективы'], ['Путешествие Нильса с дикими гусями', 'Мультфильмы'], ['Золотой теленок', 'Комедии']

# ТЕСТЫ
    # test_add_new_book_add_two_books: тест для метода "add_new_book",
    # на добавление книги с названием удовлетворяющим ограничению по кол-ву символов 0 < x < 41

    # test_add_new_book_with_long_name_not_add: параметризованный тест,для метода "add_new_book",
    # невозможности добавить в словарь книгу, если у названия кол-во символов равно или больше 41

    # test_set_book_genre_set_default_genre: параметризованный тест метода "set_book_genre",
    # на возможность установить значения любого жанра из списка жанров по умолчанию, 
    # для книги содержащейся в словаре

    # test_set_book_genre_set_unknown_genre: параметризованный тест метода "set_book_genre",
    # на невозможность установить жанр книги не из списка жанров по умолчанию

    # test_set_book_genre_for_unknown_book: параметризованный тест метода "set_book_genre",
    # на невозможность установить жанр, для книги отсутствующей в словаре

    # test_get_book_genre_get_genre_to_list_books: параметризованный тест метода "get_book_genre",
    # на соответсвие названия книги и присвоенного жанра
  
    # test_get_books_with_specific_genre_get_books_selected_genre: параметризованный тест метода "get_books_with_specific_genre",
    # c возвратом списка книг только указанного в параметрах жанра

    # test_get_books_genre_get_dictionary_without_books: тест метода "get_books_genre",
    # на возврат словаря без единой книги

    # test_get_books_genre_get_dictionary_one_book: тест метода "get_books_genre",
    # на возврат словаря из одной книги без жанра

    # test_get_books_genre_get_dictionary_all_books_all_genre: тест метода "get_books_genre",
    # возврата сформированного словаря со множеством книг и перечислением всех доступных жанров

    # test_get_books_for_children_get_books_only_for_children: тест метода "get_books_for_children",
    # на вовращение списка книг для детей состоящего только из НЕ запрещенных жанров

    # test_get_books_for_children_get_zero_list_books: параметризованный тест метода "get_books_for_children",
    # на отсутствие в списке книг для детей, книг из запрещенных жанров 'Ужасы', 'Детективы'

    # test_add_book_in_favorites_add_one_book: тест метода "add_book_in_favorites",
    # на добавление книги в список Избранное

    # test_delete_book_from_favorites_get_zero_list_favorites_book: тест метода "delete_book_from_favorites",
    # на удаление книги из списка Избранное

    # test_get_list_of_favorites_books_get_list_with_two_book: тест метода "get_list_of_favorites_books",
    # получения текущего списка Избранных книг
