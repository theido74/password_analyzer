# Password Analyzer

Ce projet est un analyseur de mots de passe qui évalue la force d'un mot de passe en fonction de plusieurs critères, notamment la longueur, la complexité, et la résistance aux attaques par dictionnaire. Il vérifie également si le mot de passe a été compromis dans des bases de données connues.

## Fonctionnalités

- Analyse de la longueur et de la complexité du mot de passe.
- Calcul de l'entropie du mot de passe.
- Vérification de la résistance aux attaques par dictionnaire.
- Vérification de la présence du mot de passe dans des bases de données compromises.

## Prérequis

- Python 3.x
- Bibliothèques Python nécessaires (voir ci-dessous)

## Installation

1. Clonez ce dépôt sur votre machine locale :

       ```bash
       git clone <URL_DU_DEPOT>
       cd password_analyzer
       mkdir dics
2. Télécharger rockyou.txt

       source : https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
       enregistrer dans dics

3.Lancer le script:

      python3 main.py
