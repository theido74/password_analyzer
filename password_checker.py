import re
from math import log

def entropy(password):
    char_class = 0
    if re.search(r'[a-z]', password): char_class += 1  # Classe pour les minuscules
    if re.search(r'[A-Z]', password): char_class += 1  # Classe pour les majuscules
    if re.search(r'[0-9]', password): char_class += 1  # Classe pour les chiffres
    if re.search(r'[\W]', password): char_class += 1   # Classe pour les caractères spéciaux
    
    # Calcul de l'entropie
    return len(password) * log(char_class or 1, 2)

def check_password_strength(password):
    entropy_value = entropy(password)  # Calculez l'entropie
    results = {
        'length': len(password) >= 12,
        'lower': bool(re.search(r'[a-z]', password)),
        'upper': bool(re.search(r'[A-Z]', password)),
        'digit': bool(re.search(r'[0-9]', password)),
        'special': bool(re.search(r'[\W]', password)),
        'entropy': entropy_value,  # Stockez la valeur d'entropie
        'common_pattern': not (
            re.search(r'password|123|admin|qwerty', password, re.IGNORECASE) or password.isnumeric()
        )
    }
    results['score'] = sum(v for k, v in results.items() if isinstance(v, bool))
    return results