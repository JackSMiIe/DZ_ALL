import json
import pprint
import os

"""Создание файла .json"""

countries = {'Аргентина':'Буэнос-Айрес',
             'Армения':'Ереван',
             'Бельгия':'Брюссель',
             'Боливия':'Ла-Пас',
             'Ботсвана':'Габороне'}

with open('countries.json','w',encoding='utf-8') as file:
    json.dump(countries,file,ensure_ascii=False)

class List:
    """Класс Лист"""
    def __init__(self):
        self.change_file = dict()
        self.new_file = dict()

    def download_file(self,filename):
        """Загрузка из файла"""
        with open(filename,'r',encoding='utf-8') as f:
            self.new_file = json.load(f)
            self.change_file = {**self.change_file, **self.new_file}


    def print_all(self):
        """Создержимое файла"""
        return pprint.pp(self.change_file)

    def find_key(self,key_name):
        """Поиск по ключу"""
        if key_name in self.change_file:
            return self.change_file.get(key_name)
        else:
            return None

    def save(self):
        """Сохраниние файла"""
        with open('save.json','w',encoding='utf-8') as f:
            json.dump(self.change_file,f,ensure_ascii=False)

    def аddition(self,country,сapital=None):
        """Добавление"""
        if country in self.change_file:
            return None
        self.change_file.setdefault(country,сapital)

    def dell_key(self,key):
        """Удаление по ключу"""
        if key in self.change_file:
            try:
                self.change_file.pop(key, None)
            except:
                KeyError
        else:
            return None
    def dell_value(self,value):
        pass
    def redactor(self):
        """Редактирование файла"""
        self.save()
        os.startfile(r'C:\Users\Python32\PycharmProjects\execrcise 1\.venv\save.json')



d = List()
d.аddition('Нидерланды','Амстердам')
d.аddition('Греция','Афины')
d.download_file('countries.json')
d.print_all()
print(d.find_key('Аргентина'))
d.аddition('Россия','Москва')
d.save()
d.print_all()
print(d.find_key('Россия'))
d.dell_key('Греция')
d.save()

d.dell_value('Габороне')
d.аddition('USA',)
d.print_all()
d.redactor()