'''Опишіть об'єкти мистецтва для музею. скористайтесь всіма 5 принципами: абстракція, наслідування, поліморфізм,
скриття, інкапсуляція. додайте property, setter. Створіть хоча-б по одному інстансу кожного класу і викличте методи'''


class ArtPiece:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def display_info(self):
        return f"{self.title} by {self.artist}, {self.year}"


class Painting(ArtPiece):
    def __init__(self, title, artist, year, medium):
        super().__init__(title, artist, year)
        self.medium = medium

    def display_info(self):
        return f"Painting: {super().display_info()}, Medium: {self.medium}"


class Sculpture(ArtPiece):
    def __init__(self, title, artist, year, material):
        super().__init__(title, artist, year)
        self.material = material

    def display_info(self):
        return f"Sculpture: {super().display_info()}, Material: {self.material}"


class Photography(ArtPiece):
    def __init__(self, title, artist, year, technique):
        super().__init__(title, artist, year)
        self.technique = technique

    def display_info(self):
        return f"Photography: {super().display_info()}, Technique: {self.technique}"


class Music(ArtPiece):
    def __init__(self, title, artist, year, genre):
        super().__init__(title, artist, year)
        self.genre = genre

    def display_info(self):
        return f"Music: {super().display_info()}, Genre: {self.genre}"


starry_night = Painting("Starry Night", "Van Gogh", 1889, "Oil")
kiss = Sculpture("Kiss", "Auguste Rodin", 1882 , "Marble")
moonlight_sonata = Music("Moonlight Sonata", "Ludwig van Beethoven", 1801, "Classical")
moon_landing = Photography("Moon Landing", "Neil Armstrong", 1969, "B/W")

print(starry_night.display_info())
print(kiss.display_info())
print(moonlight_sonata.display_info())
print(moon_landing.display_info())


class Film(ArtPiece):
    def __init__(self, title, artist, year, duration):
        super().__init__(title, artist, year)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if value > 0:
            self._duration = value
        else:
            print("Duration must be a positive value.")

    def display_info(self):
        return f"Film: {super().display_info()}, Duration: {self.duration} minutes"


avatar = Film("Avatar", "James Cameron", 2009, 162 )
print(avatar.display_info())

avatar.duration = -100