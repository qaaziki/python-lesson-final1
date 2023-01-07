import os


class Nema():

    @staticmethod
    def nem_books():
        """

        """
        all_name_books = os.listdir('Books/')
        return all_name_books

    @staticmethod
    def get_all_id(user_id, nem_books):
        for key in nem_books:
            file = open (f'Books/{key}/info.txt', 'r', encoding="utf-8")
            regl = file.read()
            if user_id == regl[0]:
                raise ValueError("Id должен быть уникален")
            file.close()

    @staticmethod
    def getting_data(nem_books):
        for key in nem_books:
            file = open(f'Books/{key}/info.txt', 'r', encoding="utf-8")
            regl = file.readline().strip()
            regl_2 = file.readline()
            print(f'Название книги {key}')
            print(f'id книги {regl}')
            print(f'Количество {regl_2}\n')
            file.close()