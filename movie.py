import os
import json
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, 'data', 'movies.json')

def get_movies():

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding="utf-8") as f:
            movies_title = json.load(f)
        movies = [Movie(title) for title in movies_title]
        return movies




class Movie:
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title
    
    def _get_movies(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding="utf-8") as f:
                return json.load(f)

    def _write_movies(self, movies):
        with open(DATA_FILE, 'w', encoding="utf-8") as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        movies = self._get_movies()

        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"{self.title} already exists in the movies list.")
            return False
        

    def remove_from_movies(self):
        movies = self._get_movies()

        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"{self.title} does not exist in the movies list.")
            return False

if __name__ == '__main__':
    movies = get_movies()
    print(movies)
    
# movie = Movie('the matrix')
# movie._write_movies(["harry poter", "barry lyndon"])
