import os
from file_worker import Nema
import shutil

class Book(Nema):
    def __init__(self, name_boook, ):
        self.name_book = name_boook
        self.book_id = id(self)


    def creating_a_book(self,nambr_capters):
        os.mkdir(f'Books/{self.name_book}')
        file = open(f'Books/{self.name_book}/info.txt', 'a', encoding="utf-8")
        file.write(f'{self.book_id}\n')
        file.write(f'{nambr_capters}')
        file.close()
        return self.name_book


    def delet(self):
        os.remove(f'Books/{self.name_book}/info.txt')
        os.rmdir(f'Books/{self.name_book}')
        return 'книга удалена'

    def changing_the_book(self,new_book):
        os.rename(f'Books/{self.name_book}', f'{new_book}',)
        return 'книга изменина'


    def add_a_chapter(self, new_chapter):
        file = open(f'Books/{self.name_book}/{new_chapter}.txt','w+', encoding="utf-8" )
        file.close()


    def chapter_change(self, old_chapter, new_changing):
        os.rename(f'Books/{self.name_book}/{old_chapter}.txt', f'Books/{self.name_book}/{new_changing}.txt')
        return 'изменение файла'



    def del_change(self, chapter_del):
        os.remove(f'Books/{self.name_book}/{chapter_del}.txt')
        return'файл удален'




