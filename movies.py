import myDB

cursor = myDB.cursor


def isMovieExist(title):
    cursor.execute("""SELECT * FROM movies WHERE title = "%s" """ % (title))
    result = cursor.fetchall()
    if result:
        return result[0]
    else:
        return False


def addMovie():
    print('\nPour ajouter un milf veuillez remplir les champs suivants')
    title = str(input('Titre:'))
    release_year = str(input('Année de sortie:'))
    genre = str(input('Genre:'))
    collection_in_mil = int(input('collecte en millions'))

    if isMovieExist(title):
        print('Un film du meme nom ('+title+') existe dèja')
        return False
    else:
        cursor.execute(
            """
            INSERT INTO movies (title,release_year,genre,collection_in_mil)
            VALUES ("%s","%s","%s","%s")
            """ % (
                title,
                release_year,
                genre,
                collection_in_mil
            )
        )
        myDB.connexion.commit();
        if isMovieExist(title):
            print('Le film a bien été ajouté')
            return True
        else:
            print('L\'ajout du film n\'a pas réuissi')
            return False


def getMoviesList():
    cursor.execute(
        """
        SELECT * FROM movies
        """
    )
    result = cursor.fetchall()
    return result


def showMoviesList():
    result = getMoviesList()
    if result:
        print('Liste des films:\n', result)
    else:
        print('Erreur on n\'arrive pas a afficher la liste des films')