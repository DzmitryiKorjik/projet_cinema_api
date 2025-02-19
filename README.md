# Projet Cinema API

## Description

Cette application est une API pour gérer une base de données de films. Elle permet d'ajouter, de supprimer, de mettre à jour et de récupérer des informations sur les films.

## Fichiers

### app.py

Ce fichier contient le code principal de l'application. Il configure et lance le serveur web, définit les routes de l'API et gère les requêtes HTTP.

#### Fonctionnalités principales :

-   Configuration du serveur web
-   Définition des routes de l'API
-   Gestion des requêtes HTTP

### movie.py

Ce fichier contient la définition du modèle de données pour les films. Il gère la structure des données et les interactions avec la base de données.

#### Fonctionnalités principales :

-   Définition du modèle de données pour les films
-   Gestion des interactions avec la base de données

## Fonctionnement

### Installation

1. Clonez ce dépôt :
    ```bash
    git clone https://github.com/DzmitryiKorjik/projet_cinema_api.git
    ```
2. Accédez au répertoire du projet :
    ```bash
    cd projet_cinema_api
    ```
3. Pour lancer l'application avec `uvicorn`, exécutez la commande suivante :

```bash
uv run app.py
```

Cette commande démarre le serveur avec `uvicorn` et active le rechargement automatique pour le développement.

4. Pour lancer l'application ouvrir le dossier listeApp et et exécutez la fichier de l'application ListeApp.exe

## Auteur

-   **Nom :** Mardovitch Dzmitryi
-   **Formation :** Développement Web et Web Mobile.
-   **Objectif :** Validation des compétences en création et déploiement d'applications web.
