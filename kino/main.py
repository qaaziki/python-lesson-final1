import os
import random


class Film:
    def __init__(self, params):
        self.title = params[0]
        self.year = params[1]
        self.producer = params[2]

    def print_info (self):
        print(f'{self.title} ({self.year})')

class Advice:
    @staticmethod
    def read_from_files(path,files):
        films=[]
        for file_name in files:
            file=open(f'{path}/{file_name}','r',encoding="utf=8")
            lines = file.readlines()
            file.close()

            lines=[ line.rstrip() for line in lines ]

            films.append(Film(lines))
        return films

    def __init__(self, films):
        self.films = films
        self.producer = self.__uniq_producers(films)

    def produser_to_choce(self):
        for num, name in enumerate(self.producer,start=1):
            print(f'{num} {name}')

    def get_advice(self,user_choce):
        producers_films = []
        for film in self.films:
            if film.producer == self.producer[user_choce -1]:
                producers_films.append(film)
        return random.choice(producers_films)

    def __uniq_producers(self,films):
        producers = []
        for film in films:
            producer = film.producer
            if producer not in producers: producers.append(producer)
        return producers

current_path = os.getcwd()+'/kino/'
films = Advice.read_from_files(current_path, os.listdir(current_path))
advice = Advice(films)
advice.produser_to_choce()
user_choce = input('Введите число')