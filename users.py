import myDB

cursor = myDB.cursor
currentUser = None


def getCurrentUser():
    return currentUser


def setCurrentUser(user):
    global currentUser
    currentUser = user


def disconnect():
    setCurrentUser(None)


def isUserExist(email):
    cursor.execute("""SELECT * FROM users WHERE email = "%s" """ % (email))
    result = cursor.fetchall()
    if result:
        return result
    else:
        return False


def findUserByEmail(email):
    result = isUserExist(email)
    if result:
        return result[0]
    else:
        return False


def connectUser(email = None,password = None):
    print('\nPour vous connecter veulliez remplir les champs suivants:')
    email = email if email != None else str(input('Email:'))
    password = password if password != None else str(input('Mot de passe:'))

    user = findUserByEmail(email)
    if user:
        [*rest,user_password] = user
        if password == user_password:
            print('Connexion réuissi')
            setCurrentUser(user)
            return True
        else:
            print('Mot de passe incorrece!, veuillez saisir a nouveau')
            password = str(input('Mot de passe:'))
            return connectUser(email,password)
    else:
        print('Utlisateur introuvable!')
        return False


def registerUser():
    print('Pour vous inscrire veulliez remplir les champs suivants:')
    first_name = str(input('prénom:'))
    last_name = str(input('nom:'))
    email = str(input('email:'))
    password = str(input('mot de passe:'))

    if isUserExist(email):
        print('Erreur: l\'utilisateur ' + email + ' existet déja')
        return False
    else:
        cursor.execute(
            """
            INSERT INTO users (first_name, last_name, email, password)
            VALUES
            ("%s","%s","%s","%s")
            """ % (
                first_name,
                last_name,
                email,
                password
            )
        )
        myDB.connexion.commit()
        if isUserExist(email):
            print('L\'inscription a bien réussi')
            return True
        else:
            return False
