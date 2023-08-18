'''Опишіть 1 будь-який клас, за умови що буде існувати тільки один інстанс цього класу'''


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


instance1 = Singleton()
instance2 = Singleton()

print(instance1 is instance2)