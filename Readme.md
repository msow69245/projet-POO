# Lancement du programme
```
python Etudiant.py
```

#Fonctionnalités disponibles
1. Lister les étudiants
2. Saluer un étudiant
3. Modifier l'âge d'un étudiant
4. Ajouter un étudiant
5. Supprimer un étudiant
6. Afficher le nombre total d'étudiants
7. Quitter

# Exemple de sortie
```
==============================
   GESTION DES ETUDIANTS
==============================
1. Lister les étudiants
2. Saluer un étudiant
3. Modifier l'âge d'un étudiant
4. Ajouter un étudiant
5. Supprimer un étudiant
6. Afficher le nombre total d'étudiants
7. Quitter
===================================
Votre choix : 1
--- Liste des étudiants ---
-> MBACKE - 22
-> SOW - 16
-> NDIAYE - 23

Votre choix : 2
Choisir l'étudiant à saluer :
  1. MBACKE
  2. SOW
  3. NDIAYE
Numéro de l'étudiant : 1
Bonjour MBACKE !

Votre choix : 3
Choisir l'étudiant dont vous voulez modifier l'âge :
  1. MBACKE
  2. SOW
  3. NDIAYE
Numéro de l'étudiant : 2
Nouvel âge : 17
Âge mis à jour.
-> SOW - 17

Votre choix : 4
Nom du nouvel étudiant : DIALLO
Âge : 20
Étudiant DIALLO ajouté avec succès.

Votre choix : 6
NB Etudiants : 4

Votre choix : 7
Au revoir !
```

# Contenu du dépôt
-`Etudiants.py` : solution complète du TP
-`cours1105.py` : fichier de cours de référence (classe `Etudiant`)
-`TP_Gestion_Etudiants.md` : énoncé du TP
-`README.md` : ce fichier


# Choix technique
La classe `Etudiant` est recopiée directement dans `Etudiants.py` plutôt qu'importée depuis `cours1105.py`, car ce fichier exécute du code au chargement ce qui fausserait le compteur `nb_etudiants`.
