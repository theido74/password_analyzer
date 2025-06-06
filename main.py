from password_checker import check_password_strength
from dic_attack import load_dictionary, is_vulnerable_to_common
from dic_attack import check_hibp_password

def main():
    password = input("Entrez le mot de passe à analyser: ")
   
    # Analyse basique
    strength = check_password_strength(password)
    print("\n=== Analyse Basique ===")
    print(f"Longueur: {'✅' if strength['length'] else '❌'} ({len(password)} caractères)")
    print(f"Complexité: Entropie = {strength['entropy']:.1f} bits")  # Affichez l'entropie
    print(f"Score: {strength['score']}/6")
   
    # Attaque dictionnaire
    dictionary = load_dictionary()
    if dictionary:
        print("\n=== Test Dictionnaire ===")
        if is_vulnerable_to_common(password, dictionary):
            print("❌ Vulnérable aux attaques par dictionnaire (variantes courantes)")
        else:
            print("✅ Résistant aux variantes courantes")
   
    # Vérification HIBP
    print("\n=== Base de Données Compromis ===")
    if check_hibp_password(password):
        print("❌ MOT DE PASSE COMPROMIS (trouvé dans des fuites de données)")
    else:
        print("✅ Non trouvé dans les bases de données connues")

if __name__ == "__main__":
    main()
