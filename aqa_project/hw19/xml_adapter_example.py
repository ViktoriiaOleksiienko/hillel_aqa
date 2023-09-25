from xml.etree import ElementTree as ET
import json


class Movie:
    def __init__(self,
                 title,
                 format,
                 year,
                 rating,
                 description,
                 category):
        self.title = title
        self.format = format
        self.year = year
        self.rating = rating
        self.description = description
        self.category = category

    def to_dict(self):
        return {
            'title': self.title,
            'format': self.format,
            'year': self.year,
            'rating': self.rating,
            'description': self.description,
            'category': self.category
        }

    def to_xml_element(self):
        movie = ET.Element("movie", attrib={'title': self.title})
        ET.SubElement(movie, "format").text = self.format
        ET.SubElement(movie, "year").text = self.year
        ET.SubElement(movie, "rating").text = self.rating
        ET.SubElement(movie, "description").text = self.description
        return movie


class Movies:
    def __init__(self, movies):
        self.movies = movies

    def to_xml_string(self):
        collection = ET.Element("collection")
        for movie in self.movies:
            collection.append(movie.to_xml_element())
        return ET.tostring(collection).decode('utf-8')

    @classmethod
    def from_xml(cls, path):
        try:
            tree = ET.parse(path)
            collection = tree.getroot()
            movies = []
            for genre in collection:
                for decade in genre:
                    for movie in decade:
                        movies.append(Movie(
                            movie.attrib.get('title', ''),
                            movie.find('format').text or '',
                            movie.find('year').text or '',
                            movie.find('rating').text or '',
                            movie.find('description').text or '',
                            genre.attrib.get('category', '')
                        ))
            return cls(movies)
        except ET.ParseError as e:
            print(f"Failed when parsing xml: {e}")
            return cls([])

    def to_json(self, file_path):
        movies_list = [movie.to_dict() for movie in self.movies]
        with open(file_path, 'w') as json_file:
            json.dump(movies_list, json_file, indent=4)

    @classmethod
    def from_json(cls, file_path):
        with open(file_path, 'r') as json_file:
            movies_list = json.load(json_file)
            movies = [Movie(movie['title'], movie['format'], movie['year'],
                             movie['rating'], movie['description'], movie['category']) for movie in movies_list]
            return cls(movies)

movies = Movies.from_xml("film.xml")
xml_string = movies.to_xml_string()
print(xml_string)

movies.to_json("movies.json")

loaded_movies = Movies.from_json("movies.json")
for movie in loaded_movies.movies:
    print(f"Title: {movie.title}, Format: {movie.format}, Year: {movie.year}")