import datetime, pprint
import json

rock = {
    "Led Zeppelin": ["Led Zeppelin IV", "Houses of the Holy", "Physical Graffiti"],
    "The Beatles": ["Abbey Road", "Sgt. Pepper's Lonely Hearts Club Band", "Revolver"],
    "Pink Floyd": ["The Dark Side of the Moon", "Wish You Were Here", "The Wall"],
    "Queen": ["A Night at the Opera", "News of the World", "Innuendo"],
    "AC/DC": ["Back in Black", "Highway to Hell", "The Razors Edge"],
    "Nirvana": ["Nevermind", "In Utero", "Bleach"],
    "Metallica": ["Master of Puppets", "Ride the Lightning", "The Black Album"],
    "The Rolling Stones": ["Exile on Main St.", "Let It Bleed", "Sticky Fingers"],
    "Guns N' Roses": ["Appetite for Destruction", "Use Your Illusion I", "Use Your Illusion II"],
    "Radiohead": ["OK Computer", "Kid A", "In Rainbows"]
}

# Создаем json файл
with open('rock_bands.json', 'w') as json_file:
    json.dump(rock, json_file, ensure_ascii=False, indent=4)


class MyPlaylist:
    """класс MyPlaylist"""

    def __init__(self, name):
        self.name = name
        self.date = datetime.datetime.now()
        self.play_list = dict()

    def add_download(self, playlist_file):
        """Загрузка из файла json"""
        with open(playlist_file, 'r') as file:
            new_playlist = json.load(file)
        self.play_list = {**self.play_list, **new_playlist}
        return self.play_list

    def save_soon(self):
        """Сохранение в файл json"""
        with open('my_save.json', 'w') as file:
            json.dump(self.play_list, file, ensure_ascii=False, indent=4)
            return f'Saved to: my_save.json'

    def print_all_artists(self):
        """Вывести всех артистов"""
        for artist in self.play_list.keys():
            print(artist)

    def add_artist(self, name_gr, name_al):
        """Добавить нового артиста и альбомы"""
        if name_gr not in self.play_list:
            self.play_list[name_gr] = name_al
        else:
            self.play_list[name_gr].extend(name_al)
        return self.play_list

    def del_artist(self, name):
        """Удалить артиста из плейлиста"""
        if name in self.play_list:
            del self.play_list[name]
            return f'Delete {name}'
        else:
            return None

    def find_artist(self, name):
        """Поиск артиста"""
        if name in self.play_list:
            return self.play_list[name]
        else:
            return None

    def edit_artist(self, name, new_albums):
        """Редактировать альбомы артиста"""
        if name in self.play_list:
            self.play_list[name] = new_albums
            return f'Updated'
        return None


# Пример использования
Cool = MyPlaylist('good')
print(Cool.date)
pprint.pprint(Cool.add_download('rock_bands.json'))
print(Cool.save_soon())
Cool.print_all_artists()
Cool.add_artist('Sasha', 'Proshkin')
Cool.print_all_artists()
Cool.save_soon()
Cool.del_artist('Sasha')
Cool.print_all_artists()
print()
print()
print(Cool.find_artist("Led Zeppelin"))
print(Cool.edit_artist('Nirvana', 'WTF'))
Cool.save_soon()
