import re
from math import log

def entropy(password):
    
    total_symbols = 0
    if re.search(r'[a-z]', password): total_symbols += 26  
    if re.search(r'[A-Z]', password): total_symbols += 26  
    if re.search(r'[0-9]', password): total_symbols += 10  
    if re.search(r'[\W]', password): total_symbols += 32   
    if total_symbols == 0:
        return 0

    return len(password) * log(total_symbols, 2)


def check_password_strength(password):
    entropy_value = entropy(password)
    results = {
        'length': len(password) >= 12,
        'lower': bool(re.search(r'[a-z]', password)),
        'upper': bool(re.search(r'[A-Z]', password)),
        'digit': bool(re.search(r'[0-9]', password)),
        'special': bool(re.search(r'[\W]', password)),
        'entropy': entropy_value,  
        'common_pattern': not (
            re.search(r'password|123|admin|qwerty', password, re.IGNORECASE) or password.isnumeric()
        )
    }
    results['score'] = sum(v for k, v in results.items() if isinstance(v, bool))
    return results