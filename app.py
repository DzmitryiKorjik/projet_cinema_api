# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "PySide6"
# ]
# ///

import sys
import PySide6
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox, QListWidgetItem
from PySide6 import QtCore
from movie import get_movies
from movie import Movie

class MovieApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Movie List")
        self.setGeometry(100, 100, 400, 300)

        # Champ d'entrée du film
        self.movie_input = QLineEdit(self)
        self.movie_input.setPlaceholderText("Saisir le titre du film")

        # Bouton d'ajout de film
        self.add_button = QPushButton("Ajouter un film")
        self.add_button.clicked.connect(self.add_movie)

        # Liste de films
        self.movie_list = QListWidget(self)

        # Bouton de suppression de film
        self.remove_button = QPushButton("Supprimer le film sélectionné")
        self.remove_button.clicked.connect(self.remove_movie)

        # Disposition des widgets
        layout = QVBoxLayout()
        layout.addWidget(self.movie_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.movie_list)
        layout.addWidget(self.remove_button)

        self.setLayout(layout)
        self.load_movies()

    def load_movies(self):
        """Charge les films d'un fichier JSON dans la liste au démarrage"""
        movies = get_movies()
        for movie in movies:
            lw_item = QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.movie_list.addItem(lw_item)

    def add_movie(self):
        """Ajoute un film à la liste"""
        movie_title = self.movie_input.text()
        if movie_title:
            movie = Movie(movie_title)
            if movie.add_to_movies():
                lw_item = QListWidgetItem(movie.title)
                lw_item.setData(QtCore.Qt.UserRole, movie)
                self.movie_list.addItem(lw_item)
                self.movie_input.setText("")
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez saisir un titre de film!")

    def remove_movie(self):
        """Supprime le film sélectionné"""
        selected_item = self.movie_list.currentItem()
        if selected_item:
            movie = selected_item.data(QtCore.Qt.UserRole)
            if movie.remove_from_movies():
                self.movie_list.takeItem(self.movie_list.row(selected_item))
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un film!")

# Lancement de l'application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MovieApp()
    window.show()
    sys.exit(app.exec())
