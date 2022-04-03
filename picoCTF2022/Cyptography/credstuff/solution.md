< noms des utilisateurs dans le fichier usernames.txt dans le même ordre.

Allons donc à la recherche de la position de **cultiris** dans le fichier usernames.txt.

Utilisons la commande grep:

grep -n cultiris leak/usernames.txt 

Celle-ci donne la ligne 378

Allons à la recherche du mot de passe correspondant:

head -n378 leak/passwords.txt | tail -n1 

cvpbPGS{P7e1S_54I35_71Z3}


