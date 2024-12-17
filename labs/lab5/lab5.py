class Book:
    def __init__(self, title, author, year, genre):

        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __repr__(self):

        return f"'{self.title}' by {self.author} ({self.year}, {self.genre})"

class HomeLibrary:
    def __init__(self):

        self.books = []

    def add_book(self, book):

        self.books.append(book)
        print(f"Книга '{book.title}' додана до бібліотеки.")

    def remove_book(self, index):

        if 0 <= index < len(self.books):
            removed_book = self.books.pop(index)
            print(f"Книга '{removed_book.title}' видалена з бібліотеки.")
        else:
            print("Неправильний індекс книги.")

    def search_books(self, **kwargs):

        results = self.books
        for key, value in kwargs.items():
            results = [book for book in results if getattr(book, key) == value]
        return results

    def get_book(self, index):

        if 0 <= index < len(self.books):
            return self.books[index]
        else:
            print("Неправильний індекс книги.")
            return None

    def list_books(self):

        return self.books

library = HomeLibrary()

library.add_book(Book("Війна і мир", "Лев Толстой", 1869, "Роман"))
library.add_book(Book("Гаррі Поттер і філософський камінь", "Джоан Роулінг", 1997, "Фентезі"))
library.add_book(Book("1984", "Джордж Орвелл", 1949, "Антиутопія"))

print("\nСписок книг у бібліотеці:")
print(library.list_books())

print("\nПошук книг за автором 'Джордж Орвелл':")
print(library.search_books(author="Джордж Орвелл"))

print("\nПошук книг за жанром 'Фентезі':")
print(library.search_books(genre="Фентезі"))

print("\nКнига за індексом 1:")
print(library.get_book(1))

library.remove_book(1)

print("\nСписок книг після видалення:")
print(library.list_books())