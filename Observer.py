from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint as r
from typing import List


class Subject(ABC):
    """
    Интерфейс издателя объявляет набор методов для управления подписчиками.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Присоединяет наблюдателя к издателю.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Отсоединяет наблюдателя от издателя.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Уведомляет всех наблюдателей о событии.
        """
        pass


class ConcreteSubject(Subject):
    """
    Издатель владеет некоторым важным состоянием и оповещает наблюдателей о его
    изменениях.
    """

    def __init__(self):
        self._state: int = None
        self._old_state: int = self._state
        self._video_menu: List[str] = ['Фильмы', 'Музыка', 'Развлекательные каналы']
        self._old_video_menu: List[str] = self._video_menu.copy()
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)
        print("Добавлен наблюдатель")
        print(f'Текущее состояние меню: {self._video_menu}')

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
        print("Наблюдатель удален!")
        print(f'Текущее состояние меню: {self._video_menu}')

    def add_video(self) -> None:
        print("Добавление!")
        """Добавить видео"""
        old_video_menu = self._video_menu.copy()
        arr: list = ['Подписки', 'Новинки недели', 'Подборка', 'Ужасы']
        self._video_menu.append(arr[r(0, 3)])
        print(f'Старое меню: {old_video_menu}')
        print(f'Новое меню: {self._video_menu}')
        if self._video_menu != old_video_menu:
            self.notify()
            self._old_video_menu = old_video_menu

    def remove_video(self, video: str) -> None:
        """Удалить видео"""
        if video in self._video_menu:
            print(f'Удаление! {video}')
            old_video_menu = self._video_menu.copy()  # Сохраняем текущее состояние
            self._video_menu.remove(video)  # Удаляем
            print(f'Старое меню: {old_video_menu}')
            print(f'Новое меню: {self._video_menu}')
            self.notify()

    def notify(self) -> None:
        """
        Запуск обновления в каждом подписчике.
        """
        print("Отправка уведомления")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Изменяет состояние и уведомляет наблюдателей, если состояние изменилось.
        """
        print("Изменения состояния")
        self._state = r(0, 3)
        if self._state != self._old_state:
            print("Состояние изменилось!")
            print(f'Старое меню: {self._old_video_menu}')
            print(f'Новое меню: {self._video_menu}')
            self.notify()


class Observer(ABC):
    """
    Интерфейс Наблюдателя объявляет метод уведомления, который издатели
    используют для оповещения своих подписчиков.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Получить обновление от субъекта.
        """
        pass


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._old_video_menu != subject._video_menu:
            print("Уведомлен! ConcreteObserverA")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._old_video_menu != subject._video_menu:
            print("Уведомлен! ConcreteObserverB")


# Пример
subject = ConcreteSubject()
observer_a = ConcreteObserverA()
observer_b = ConcreteObserverB()
print('-'*100)
# Добавление наблюдателей
subject.attach(observer_a)
subject.attach(observer_b)
print('-'*100)
# Изменение
subject.add_video()
print('-'*100)
subject.some_business_logic()
print('-'*100)
# Добавление
subject.add_video()
print('-'*100)
# Удаление
subject.remove_video('Музыка')
print('-'*100)
