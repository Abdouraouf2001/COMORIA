from database.operations import definir_administrateur

nom = input("Entre ton nom d'utilisateur:")
if definir_administrateur(nom):
    print("tu admin")

else:print("aucun utilisateur")