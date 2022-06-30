#zadanie 1
from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    weight: int
    
def task_1():
    person_1 = Person('Henry', 21, 200)
    person_2 = Person('Phil', 20, 80)
    print(person_1)
    print(person_2)
    print(person_1 == person_2)

#zadanie 2
from dataclasses import dataclass
@dataclass(frozen=True)
class Person:
    name: str
    age: int
    weight: int
    def with_name(self, new_name: str):
        return Person(new_name, self.age, self.weight)
    def with_age(self, new_age: int):
        return Person(self.name, new_age, self.weight)
    def with_weight(self, new_weight: int):
        return Person(self.name, self.age, new_weight)
    
def task_2():
    person_1 = Person('Bob', 18, 64)
    person_2 = person_1.with_name('Carl').with_age(20).with_weight(99)
    person_3 = person_2.with_name('Mattew').with_age(11)
    print(person_2)
    print(person_3)

#zadanie 3
from dataclasses import dataclass
import json

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    weight: int
    
    def with_name(self, new_name: str):
        return Person(new_name, self.age, self.weight)
    def with_age(self, new_age: int):
        return Person(self.name, new_age, self.weight)
    def with_weight(self, new_weight: int):
        return Person(self.name, self.age, new_weight)
    def serialize_object(self):
        data_to_serialize = {'name': self.name, 'age': self.age, 'weight': self.weight}
        return json.dumps(data_to_serialize)
    
def task_3():
    person_1 = Person('Billy', 20, 300)
    print(person_1.serialize_object())

