import movies
import myDB
import ratings
import users

def demandeConnexion():
    print('\nConnexion \nSi vous n\'avez pas compte inscrivez vous')
    print('(1) Me connecter \n(2) M\'iscrire')
    response = input('Votre réponse:')
    if response == '1':
        users.connectUser()
    elif response == '2':
        users.registerUser()
    else:
        print('Réponse invalide!')

    return defaulFunction()


def defaulFunction():
    if users.getCurrentUser():
        print('\nQuelle autre actoin voulez vous faire?')
        print("(1) Ajouter un film \n(2) Afficher la list des filmes\n(3) Noter un film\n(4) Voir toutes les notes")
        result = str(input('Votre réponse:'))
        if result == '1':
            movies.addMovie()
        elif result == '2':
            movies.showMoviesList()
        elif result == '3':
            ratings.addRating()
        elif result == '4':
            ratings.showRatingsList()
        else:
            print('réponse invalid')

        return defaulFunction()
    else:
        demandeConnexion()


defaulFunction()