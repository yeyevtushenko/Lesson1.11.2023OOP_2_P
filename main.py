class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_info(self):
        print(f"Назва: {self.title}, Автор: {self.author}, Жанр: {self.genre}")

    def __str__(self):
        return f"{self.title} - {self.author}"

    def __eq__(self, other):
        return (
            self.title == other.title
            and self.author == other.author
            and self.genre == other.genre
        )

    def __ne__(self, other):
        return not self.__eq__(other)


title = input("Введіть назву книги: ")
author = input("Введіть автора книги: ")
genre = input("Введіть жанр книги: ")

book1 = Book(title, author, genre)
book2 = Book("Inferno", "Dan Brown", "Mystery")

print("\nІнформація про вашу книгу:")
book1.display_info()

print("\nІнформація про книгу 'Inferno':")
print(book2)

if book1 == book2:
    print("\nКниги однакові.")
else:
    print("\nКниги різні.")
