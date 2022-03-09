#Задача 1: Построить три класса (базовый и 3 потомка),
# описывающих некоторых хищных животных (один из потомков),
# всеядных(второй потомок) и травоядных (третий потомок).
# Описать в базовом классе абстрактный метод для
# расчета количества и типа пищи,
# необходимого для пропитания животного в зоопарке.

from abc import ABC


class Perent(ABC):
    def __init__(self, colvo, tip_pit):
        self.colvo = colvo
        self.tip_pit = tip_pit
    def C(self):
        print(f'Количество еды', self.colvo)
    def T(self):
        print(f'Вид еды', self.tip_pit)


class Xichnic (Perent):
    def __init__(self, colvo, tip_pit):
        super().__init__(colvo, tip_pit)

class Vseyad (Perent):
    def __init__(self, colvo, tip_pit):
        super().__init__(colvo, tip_pit)

class Travayad (Perent):
    def __init__(self, colvo, tip_pit):
        super().__init__(colvo, tip_pit)

x= Xichnic('1500', 'мясо')
v= Vseyad('1000', 'мясо и трава')
t=Travayad('500', 'трава')
x.C()
x.T()
v.C()
v.T()
t.C()
t.T()
