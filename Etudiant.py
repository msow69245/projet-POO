# Question 1 : Quel est le rôle de __age ?
# __age est un attribut privé. Le double underscore (__) signifie qu'il
# ne peut pas être accédé directement depuis l'extérieur de la classe.
# Cela protège la valeur de l'âge contre toute modification non contrôlée.
 
# Question 2 : Pourquoi utilise-t-on get_age() et set_age() ?
# Parce que __age est privé, on ne peut pas écrire etu.__age directement.
# get_age() permet de lire la valeur de __age.
# set_age() permet de la modifier de façon contrôlée.
 
# Question 3 : Que représente nb_etudiants ?
# nb_etudiants est un attribut de classe.
# Il compte le nombre total d'objets Etudiant créés depuis le début
# du programme. Il s'incrémente automatiquement à chaque __init__.
 
# Question 4 : Quelle est la différence entre nom, _genre et __age ?
# nom : attribut public → accessible librement depuis n'importe où
# _genre : attribut protégé → accessible dans la classe et ses sous-classes
# __age : attribut privé → accessible uniquement à l'intérieur de la classe
 
# Checkpoint 1 : sortie de python cours1105.py
# -> MBACKE - 22
# -> MBACKE - 24  (après set_age(24))

class Etudiant:
    nb_etudiants = 0

    def __init__(self, nom: str, age: int = 18, genre: str = None) -> None:
        self.nom = nom
        self.__age = age      # attribut privé
        self._genre = genre   # attribut protégé
        Etudiant.nb_etudiants += 1

    def get_age(self):
        return self.__age

    def set_age(self, new_age: int):
        self.__age = new_age

    @classmethod
    def nb_etudiant(cls):
        print(f"NB Etudiants : {cls.nb_etudiants}")

    def infos(self):
        print(f"-> {self.nom} - {self.get_age()}")

    def __str__(self) -> str:
        return f"Etudiant(nom={self.nom}, age={self.get_age()})"

    def saluer(self):
        print(f"Bonjour {self.nom} !")

    def est_majeur(self):
        statut = "Vous etes Majeur" if self.get_age() >= 18 else "Vous etes Mineur"
        print(statut)


# Fonctions pour le menu

def afficher_menu():
    print("\n" + "=" * 20)
    print(" gestion de etudiants")
    print("=" * 20)
    print("1. Lister les etudiants")
    print("2. Saluer un etudiant")
    print("3. Modifier l'age d'un etudiant")
    print("4. Ajouter un etudiant")
    print("5. Supprimer un etudiant")
    print("6. Afficher le nombre d'etudiants")
    print("7. Quitter")
    print("=" * 20)


def choisir_index(etudiants):
    for i, etu in enumerate(etudiants):
        print(f"{i + 1}. {etu.nom}")
    try:
        choix = int(input("Numero de l'etudiant : "))
        if 1 <= choix <= len(etudiants):
            return choix - 1
        else:
            print("Index invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
    return None


def lister_etudiants(etudiants):
    if not etudiants:
        print("Aucun etudiant dans la liste.")
        return
    print("\nListe des etudiants :")
    for etu in etudiants:
        etu.infos()


def saluer_etudiant(etudiants):
    if not etudiants:
        print("Aucun etudiant dans la liste.")
        return
    print("\nchoisir l'etudiant a saluer :")
    index = choisir_index(etudiants)
    if index is not None:
        etudiants[index].saluer()


def modifier_age(etudiants):
    if not etudiants:
        print("Aucun etudiant dans la liste.")
        return
    print("\nchoisir l'etudiant pour modifier l'age :")
    index = choisir_index(etudiants)
    if index is not None:
        try:
            new_age = int(input("Nouvel age : "))
            etudiants[index].set_age(new_age)
            print("Age mis a jour.")
            etudiants[index].infos()
        except ValueError:
            print("Age invalide.")


def ajouter_etudiant(etudiants):
    nom = input("Nom de l'etudiant : ")
    if not nom:
        print("Le nom ne peut pas etre vide.")
        return
    try:
        age = int(input("Age"))
    except ValueError:
        print("Age invalide.")
        return
    new_etudiant = Etudiant(nom=nom,age=age)
    etudiants.append(new_etudiant)
    print(f"Etudiant {nom} ajouté avec succès.")

def supprimer_etudiant(etudiants):
    if not etudiants:
        print("Aucun etudiant a supprimer.")
        return
    print("\nchoisir l'etudiant a supprimer :")
    index = choisir_index(etudiants)
    if index is not None:
        supprime = etudiants.pop(index)
        print(f"Etudiant {supprime.nom} supprimé avec succès.")


def afficher_compteur():
    Etudiant.nb_etudiant()

#fonction principale
def main():
    etu_01 = Etudiant(nom="MBACKE", age=22)
    etu_02 = Etudiant(nom="SOW", age=16)
    etu_03 = Etudiant(nom="NDIAYE", age=23)

    etudiants = [etu_01, etu_02, etu_03]

    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()

        if choix == "1":
            lister_etudiants(etudiants)
        elif choix == "2":
            saluer_etudiant(etudiants)
        elif choix == "3":
            modifier_age(etudiants)
        elif choix == "4":
            ajouter_etudiant(etudiants)
        elif choix == "5":
            supprimer_etudiant(etudiants)
        elif choix == "6":
            afficher_compteur()
        elif choix == "7":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 7.")

if __name__ == "__main__":
    main()