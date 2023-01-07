# class Greeg():
#     def __init__(self, size, nam, cellar, pit):
#         self.size = size
#         self.nam = nam
#         self.cellar = cellar
#         self.pit = pit
#
#     def hranit(self):
#         print('хранить')
#
#     def hcinit(self):
#         print('ремонт')
#
#     def master(self):
#         print('мастерская')
#
# g_1 = Greeg('200х200', 1, 'да', 'нет')
# g_2 = Greeg('350х350', 2, 'нет', 'да')
# g_3 = Greeg('100х100', 3, 'да', 'да')


# class Kino():
#     def __init__(self,genere, erei_ater, stil, nem, language, aftor):
#         self.genere = genere
#         self.erei_ater = erei_ater
#         self.stil = stil
#         self.nem = nem
#         self.language = language
#         self.aftor = aftor
#
#     def get_list(self):
#         for i in self.erei_ater:
#             print(i)
#
#     def gan(self):
#         print(self.genere)
#
#     def admin(self,new_nem):
#         self.nem = new_nem
#         print(self.nem)
#
#
# k_1 = Kino('Комедия', ['a', 's', 'd', 'f'], 'космос', 'Масяня', 'Русский', 'Джон')
# k_1.get_list()
# k_2 = Kino('Мелодрамма', ['a', 'ав', 'd', 'f'], 'лес', 'избушка', 'англиский', 'Петор1')

# b = []
# n = int(input('введите число'))
# for i in range(1,n):
#     b.append(i)
# print(sum(b))


def fio(a,b,s):
    print(f'{a[0]}.{b[0]}.{s}')
fio('Sergei','Sergeevihc','Ermacov')