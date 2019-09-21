# print("Hello")
#
#
# def user_info(name, age, city):
#     return name + ' ' + age + ', ' + city
#
#
# print(user_info('Ivan', '28', 'Tomsk'))


from math import *


class Point:

    def __init__(self, x, y, z=0):
        self.x: float = x
        self.y: float = y

    def to_vector(self) -> tuple:
        return self.x, self.y

    def to_json(self) -> str:
        import json
        return json.dumps({
            'x': self.x,
            'y': self.y,
        })

    def distance_to(self, other) -> float:
        return sqrt((other.x - self.x) ** 2 + ((other.y - self.y) ** 2))


p = Point(3, 4)
print(p.distance_to(Point(-98.8, 7)))
print(p.to_vector())
print(p.to_json())
