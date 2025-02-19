# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "PySide6"
# ]
# ///

import sys
import PySide6
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox

class MovieApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Movie List App")
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

    def add_movie(self):
        """Ajoute un film à la liste"""
        movie_name = self.movie_input.text().strip()
        if movie_name:
            self.movie_list.addItem(movie_name)
            self.movie_input.clear()
        else:
            QMessageBox.warning(self, "Erreur", "Saisir le titre du film!")

    def remove_movie(self):
        """Supprime le film sélectionné"""
        selected_item = self.movie_list.currentItem()
        if selected_item:
            self.movie_list.takeItem(self.movie_list.row(selected_item))
        else:
            QMessageBox.warning(self, "Erreur", "Sélectionner un film à supprimer!")

# Lancement de l'application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MovieApp()
    window.show()
    sys.exit(app.exec())
