from book import Book
from  file_worker import Nema
import os

name = input("кто вы ")
if name == "admin":
    choice = int(input("Что вы хотите сделать?\n1.Добавить книгу\n2.Удалить книгу\n\
3.Изменение книгу\n4.Изменить главу \n5.Удаление главы \n6.Добавить главу"))

    if choice == 1:
        nam_book = input("Введите название книги")
        nambr_capters = input('Введите главу')
        book=Book(nam_book)
        book.creating_a_book(nambr_capters)

    if choice == 2:
        del_book = input("Введите название книги которую хотите удалить")
        book = Book(del_book)
        book.delet()

    if choice == 3:
        booc = input("Введите книгу которую хотите изменить")
        new_book = input('Введите новое название книги')
        book = Book(booc)
        book.changing_the_book(new_book)

    if choice == 4:
        book_changing = input('Введите название книге в которой хотите изменить главу')
        old_chapter = input('Введите название существуещей главы')
        new_changing = input('Введите новую главу')
        book = Book(book_changing)
        book.chapter_change(old_chapter,new_changing)

    if choice == 5:
        book_dell = input('Введите название книге в которой хотите удалить главу')
        chapter_del = input('Введите файл который хотите удалить')
        book = Book(book_dell)
        book.del_change(chapter_del)

    if choice == 6:
        book_selection = input('Введите название книги в которую хотите добавить главу')
        chapter_new = input('Введите название новой главы')
        book = Book(book_selection)
        book.add_a_chapter(chapter_new)
else:
    choice = int(input("Что вы хотите сделать?\n1.Посмотреть все книги\n2.Посмотреть инфу про книги"))
    if choice == 1:
        for i in Nema.nem_books():
            print(i)

    if choice == 2:
        Nema.getting_data(Nema.nem_books())


print('Привет это тест из гита')



# Nema.getting_data(Nema.nem_books())
