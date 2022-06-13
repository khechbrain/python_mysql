from decimal import Decimal

import myDB
import users

cursor = myDB.cursor


def isRatingExist(user_id,movie_id):
    cursor.execute(
        """
        SELECT * from ratings WHERE user_id = "%s" AND movie_id = "%s"
        """ % (
            user_id,
            movie_id
        )
    )
    result = cursor.fetchall()
    return result


def getRatingsList():
    cursor.execute("""
        SELECT title, AVG(rating) as average_rating
        FROM ratings
        INNER JOIN movies
            ON movies.id = ratings.movie_id
        GROUP BY movie_id
        ORDER BY average_rating DESC
        LIMIT 5
    """)
    return cursor.fetchall()


def showRatingsList():
    result = getRatingsList()
    if result:
        print("\n Voici la liste des notes:\n",result)
    else:
        print('La liste est vide!')


def addRating():
    print('\nPour notter un film veuillez remplir les champs suivant')
    movie_id = str(input('L\'ID du film:'))
    rating = str(input('Note de 1 a 5:'))
    [user_id, *rest] = users.getCurrentUser()

    if int(rating) > 5 or int(rating) < 1:
        print('Erreur: La note dois être entre 1 et 5')
        return addRating()

    if isRatingExist(user_id,movie_id):
        cursor.execute(
            """
            UPDATE ratings
            SET rating = "%s"
            WHERE user_id = "%s" AND movie_id = "%s"
            """ % (
                rating,
                user_id,
                movie_id
            )
        )
        myDB.connexion.commit()

        result = isRatingExist(user_id,movie_id)
        if result and result[0][2] == Decimal(rating):
            print('La note a été mise a jour')
        else:
            print('La mise a jour de la note n\'a pas réuissi!')
    else:
        cursor.execute(
            """
            INSERT INTO ratings(movie_id,user_id,rating)
            VALUES ("%s","%s","%s")
            """ % (
                movie_id,
                user_id,
                rating
            )
        )
        myDB.connexion.commit()

        if isRatingExist(user_id,movie_id):
            print('Le film a bien été noté')
            return True
        else:
            print("La notation du film n'a pas réuissi")
            return False