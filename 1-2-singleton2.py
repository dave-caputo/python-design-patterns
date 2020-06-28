"""
An example of a singleton using a Metaclass.

https://refactoring.guru/design-patterns/singleton/python/example
"""

class SingletonMeta(type):  # https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/

    _instance = None

    def __call__(self):
        """
        Return a single instance.

        How this works? When a new instance of a class is created, the first method called is this one
        i.e. from the Metaclass which will call the  __new__ constructor from the Class'.

        https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/#putting-it-all-together
        """
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class Tigger(metaclass=SingletonMeta):

    def roar(self):
        print('roooooaaar!')


if __name__ == '__main__':
    tigger1 = Tigger()
    tigger2 = Tigger()

    print(f'Tigger1 ID={id(tigger1)}')
    print(f'Tigger2 ID={id(tigger2)}')
    print(f'Is there only one Tigger? {tigger1 is tigger2}')