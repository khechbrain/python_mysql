import mysql.connector

connexion = mysql.connector.connect(
    host='localhost',
    user='khech',
    password='Mcn962016',
    database='online_moovies_ratings',
    port = 3307
)
cursor = connexion.cursor()


def createTableMovies():
    cursor.execute(
        """
        CREATE TABLE movies(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            release_year YEAR(4),
            genre VARCHAR(100),
            collection_in_mil INT
        )
        """
    )
    print('Le tableau "movies" a été créé')


def createTableRatings():
    cursor.execute(
        """
        CREATE TABLE ratings(
            movie_id INT,
            user_id INT,
            rating DECIMAL(2,1),
            FOREIGN KEY(movie_id) REFERENCES movies(id),
            FOREIGN KEY(user_id) REFERENCES users(id),
            PRIMARY KEY(movie_id, user_id)
        )
        """
    )
    print('Le tableau "ratings" a été créé')


def createTableUsers():
    cursor.execute(
        """
        CREATE TABLE users(
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            email VARCHAR(100),
            password VARCHAR(100)
        )
        """
    )
    print('Le tableau "users" a été créé')