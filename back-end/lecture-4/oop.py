# OOP, PEP-8

# Animal -> FourLeggedAnimal

# class-variables
# object-variable

class Animal(object):
    creator = 'Graey'

    def __init__(self, kind, speed):
        self.kind: str = kind
        self._speed: int = speed

    def run(self):
        self.speed -= 1

    @classmethod
    def get_creator(cls):
        return cls.creator

    @staticmethod
    def convert_to_km_h(speed: int):
        return speed * 5 / 18

    @property
    def speed(self):
        # სანამ დაბრუნდება მონაცემი
        return self._speed

    @speed.setter
    def speed(self, value):
        # მინიჭების მერე რა მოხდეს
        self._speed = self.convert_to_km_h(value)

    @speed.deleter
    def speed(self):
        # სანამ წაიშლება
        print('logic when speed will be deleted')

    def __add__(self, other: 'Animal'):
        return Animal(
            kind=f'{self.kind} {other.kind}',
            speed=max(self.speed, other.speed)
        )

    def __str__(self, ):
        return f'Kind: {self.kind} da Movement Speed: {self.speed}'


class Dog(Animal):
    def __init__(self, owners: list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.owners = owners

    def run(self):
        self.speed += 1


class TwoLeggedAnimal(Animal):
    pass


class NewMeta(type):
    def __new__(mcs, class_name, parents, properties):
        _private = properties.pop('_private', None)
        sub_meta = properties.pop('Meta', None)
        fields = getattr(sub_meta, 'fields', None)
        print(fields)
        if _private:
            properties['_Staff_private'] = _private

            return type(
                class_name, parents, properties
            )

        return super().__new__(mcs, class_name, parents, properties)


class Staff(object, metaclass=NewMeta):
    class Meta:
        fields = ('name', 'last_name')

    counter = 0
    _private = 'Private'
    __protected = 'Protected'

    def __init__(self, name):
        self.name = name
        self.change_counter(1)

    def __del__(self):
        self.change_counter(-1)

    def __str__(self):
        return str(self.counter)

    @classmethod
    def change_counter(cls, val):
        cls.counter += val


class Factory:
    def __init__(self):
        self.staff = [
            Staff('a'), Staff('b'), Staff('c')
        ]

    def __len__(self):
        return len(self.staff)


factory = Factory()

print(len(factory))

# Creating Objects
tiger = Animal(kind='Sponge', speed=100)  # or Animal('Sponge', 100)
lion = Animal(kind='Nomad', speed=90)

if __name__ == '__main__':
    animal = Animal('s', 100)
    print(animal.speed)
    animal.speed = 14.4
    print(animal.speed)

    a = Staff(name='a')
    print(
        a, a._Staff_private
    )

    my_dog = Dog(['Owner_A', 'Owner_B'], 'Sponge', 0.2, )
    print(my_dog.owners)

    def dog__init__(self, x):
        self.x = x


    A = type(
        'Class_Name', (), {'x': 1, '__init__': dog__init__, }
    )

    print(tiger)

    print(tiger + lion)
