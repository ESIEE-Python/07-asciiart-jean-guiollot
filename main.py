"""
Module pour construire une liste de tuple qui se base sur une chaine de caractere.
"""
#### Imports et définition des variables globales
import sys

# Augmente la limite de récursion
sys.setrecursionlimit(1500)  # Ajuste cette valeur selon tes besoins

#### Fonctions secondaires


#### Fonction itérative
def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []

    caractere = [s[0]]  # Liste des caractères rencontrés
    occurence = [1]     # Liste des occurrences

    for k in range(1, len(s)):
        if s[k] == s[k - 1]:
            occurence[-1] += 1  # Augmenter le nombre d'occurrences du dernier caractère
        else:
            caractere.append(s[k])  # Ajouter un nouveau caractère
            occurence.append(1)     # Ajouter 1 pour sa première occurrence

    return list(zip(caractere, occurence))  # Transformer en tuples


#### Fonction récursive
def artcode_r(s, index=0):
    """Retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme récursif.

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurrences)
    """
    # Cas de base : si on a atteint la fin de la chaîne
    if index >= len(s):
        return []

    current_char = s[index]
    count = 1
    # Compte les occurrences du caractère actuel
    while index + 1 < len(s) and s[index + 1] == current_char:
        count += 1
        index += 1

    # Appelle récursivement pour le reste de la chaîne
    return [(current_char, count)] + artcode_r(s, index + 1)


#### Fonction principale


def main():
    """
    Fonction principale.
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
