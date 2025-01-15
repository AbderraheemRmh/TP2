nom = input("veuillez saisir votre nom svp : ")
prenom = input ("veuillez saisir votre prenom svp : ")
if nom == "" or prenom == "" : # if not nom or not prenom :
    print ("erreur : le nom et le prenom doivent etre indiques")
else :
    print ("bienvenue," + nom + " " + prenom + "!")
user = "admin"
login = "password123"
nom_utilisateur = input("veuillez saisir votre nom d'utilisateur svp : ")
mot_de_passe = input("veuillez saisir vote mot de passe svp : ")
if nom_utilisateur == user and mot_de_passe == login :
    print ("connexion reussie")
elif nom_utilisateur != "admin" :
    print ("votre nom d'utilisateur est incorrecte")
else :
    print ("votre mot de passe est incorrecte")