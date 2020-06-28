"""An example of a very simple Singleton design pattern."""

class _Tigger:
    """A class meant to be a singleton."""

    def roar(self):
        print('roooooaaaar!')


_instance = None


def Tigger():
    """Ensure Tigger is a singleton."""
    global _instance
    if _instance is None:
        _instance = _Tigger()
    return _instance


if __name__ == '__main__':
    tigger1 = Tigger()
    tigger2 = Tigger()

    print(f'Tigger1 ID={id(tigger1)}')
    print(f'Tigger2 ID={id(tigger2)}')
    print(f'Is there only one Tigger? {tigger1 is tigger2}')