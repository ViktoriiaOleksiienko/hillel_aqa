'''Створіть клас з описом будь-якої компанії чи організації. Додайте 1 classmethod, 3 звичайних методи'''


class Apple:
    def __init__(self, name, founded_year, headquarters):
        self.name = name
        self.founded_year = founded_year
        self.headquarters = headquarters

    def display_info(self):
        print(f"Company: {self.name}")
        print(f"Founded: {self.founded_year}")
        print(f"Headquarters: {self.headquarters}")

    def products(self):
        print(f"{self.name} is known for its innovative products like iPhone and Mac.")

    def revenue(self, year, amount):
        print(f"In {year}, {self.name} generated ${amount} billion in revenue.")

    @classmethod
    def industry(cls):
        print(f"{cls.__name__} operates in the technology industry, specializing in consumer electronics and software.")


apple_inc = Apple("Apple Inc.", 1976, "Cupertino, California")

apple_inc.display_info()
apple_inc.products()
apple_inc.revenue(2022, 370)
Apple.industry()