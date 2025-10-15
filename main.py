#### Fonction secondaire
import string
import unicodedata

def ispalindrome(p):

    p = unicodedata.normalize("NFD", p)
    p = "".join(ch for ch in p if unicodedata.category(ch) != "Mn")
    p = p.lower()

    table = str.maketrans("", "", string.punctuation + " " + "’")

    p = p.translate(table)

    return p == p[::-1]


#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))
    print(ispalindrome("Esope reste ici et se repose")) 
    print(ispalindrome("Tu l’as trop écrasé César, ce port salut"))
    print(ispalindrome("Bonjour"))

if __name__ == "__main__":
    main()