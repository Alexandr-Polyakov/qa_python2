import pytest
from main import BooksCollector  # Укажите правильный путь к вашему классу BooksCollector

class TestBooksCollector:

    def test_add_new_book_one_book(self):
        # Создаем экземпляр класса BooksCollector
        collector = BooksCollector()
        # Добавляем новую книгу
        collector.add_new_book('Ромео и Джульетта')
        # Проверяем, что книга добавлена в коллекцию
        assert 'Ромео и Джульетта' in collector.get_books_genre()

    def test_add_new_book_default_genre_is_empty(self):
        # Создаем экземпляр класса BooksCollector
        collector = BooksCollector()
        # Добавляем новую книгу
        collector.add_new_book('Ромео и Джульетта')
        # Проверяем, что жанр новой книги по умолчанию - пустая строка
        assert collector.get_book_genre('Ромео и Джульетта') == ''

    @pytest.mark.parametrize("book_name", [
        "Ромео и Джульетта",
        "Мастер и Маргарита",
        "Король Лев"
    ])
    def test_add_new_book_multiple_books(self, book_name):
        # Создаем экземпляр класса BooksCollector
        collector = BooksCollector()
        # Добавляем новую книгу
        collector.add_new_book(book_name)
        # Проверяем, что книга добавлена в коллекцию
        assert book_name in collector.get_books_genre()

    def test_add_book_already_in_list(self):
        collector = BooksCollector()
        book_name = 'Ромео и Джульетта'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert list(collector.books_genre.keys()).count(book_name) == 1


    import pytest
from main import BooksCollector  # Укажите правильный путь к вашему классу BooksCollector

class TestBooksCollector:

    def test_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2  # Проверяем, что добавилось именно две книги

    def test_set_book_genre(self):
        collector = BooksCollector()
        book = "Книга"
        collector.add_new_book(book)
        collector.set_book_genre(book, "Фантастика") #Устанавливаем жанр для книги
        assert collector.get_book_genre(book) == "Фантастика" #Проверяем, что жанр установился корректно

    def test_get_book_genre_returns_empty_for_new_book(self):
        collector = BooksCollector()
        book = "Книга"
        collector.add_new_book(book)
        assert collector.get_book_genre(book) == '' #Добавлена проверка на пустую строку

    def test_get_book_genre_returns_correct_genre_from_dict(self):
        collector = BooksCollector()
        book = "Книга"
        genre = "Детективы"
        collector.add_new_book(book)
        collector.set_book_genre(book, genre) #Теперь используем set_book_genre
        assert collector.get_book_genre(book) == genre #Проверяем, что get_book_genre возвращает правильный жанр


    def test_set_genre_for_nonexistent_book_does_nothing(self, collection):
        collection.set_book_genre("Неизвестная книга", "Фантастика")
        assert collection.get_book_genre("Неизвестная книга") is None

    def test_get_books_with_specific_genre(self, collection_five_books):
        result = collection_five_books.get_books_with_specific_genre("Ужасы")
        assert "Чужой" in result

    def test_get_books_genre_returns_dict(self, collection):
        collection.add_new_book("1984")
        genres = collection.get_books_genre()
        assert isinstance(genres, dict)
        assert "1984" in genres

    def test_get_books_for_children_excludes_age_rated(self, collection_five_books):
        kids_books = collection_five_books.get_books_for_children()
        expected = {'Властелин колец', 'Король лев', 'Сон в летнюю ночь'}
        assert set(kids_books) == expected

    def test_add_book_in_favorites(self, collection):
        book = "Хоббит"
        collection.add_new_book(book)
        collection.add_book_in_favorites(book)
        assert book in collection.get_list_of_favorites_books()

    def test_add_book_in_favorites_for_nonexistent_book_does_nothing(self, collection):
        collection.add_book_in_favorites("Неизвестная книга")
        assert collection.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites(self, collection):
        book = "1984"
        collection.add_new_book(book)
        collection.add_book_in_favorites(book)
        collection.delete_book_from_favorites(book)
        assert book not in collection.get_list_of_favorites_books()

    def test_delete_nonexistent_book_from_favorites_does_nothing(self, collection):
        book = "1984"
        collection.add_new_book(book)
        collection.add_book_in_favorites(book)
        collection.delete_book_from_favorites("Неизвестная книга")
        assert book in collection.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_returns_correct_list(self, collection):
        book1 = "Хоббит"
        book2 = "1984"
        collection.add_new_book(book1)
        collection.add_new_book(book2)
        collection.add_book_in_favorites(book1)
        collection.add_book_in_favorites(book2)
        favorites = collection.get_list_of_favorites_books()
        assert isinstance(favorites, list)
        assert set(favorites) == {book1, book2}
