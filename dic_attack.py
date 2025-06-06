import hashlib
import tqdm
import time
import requests



def load_dictionary(file_path = 'dics/rockyou.txt'):
    with open(file_path,'r', errors='ignore') as f:
        return [line.strip() for line in f]
    
def dictionay_attack(password, dictionary):
    return  password in dictionary

def slow_hash(password, salt='', iterations=100000):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), iterations).hex()

def is_vulnerable_to_common(password, dictionary):
    variants = [
        password,
        password.lower(),
        password + '123',
        password + '!',
        password + '_',
        password + time.strftime('%Y'),
        password.replace('a', '@').replace('s', '$').replace('o', '0'),
        password.replace('e', '3').replace('i', '1').replace('l', '1'),
        
    ]
    return any(variant in dictionary for variant in variants)

def check_hibp_password(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    try:
        response = requests.get(
            f"https://api.pwnedpasswords.com/range/{prefix}",
            headers={"Add-Padding": "true"},
            timeout=3
        )
        hashes = (line.split(':') for line in response.text.splitlines())
        return any(h[0] == suffix for h in hashes)
    except requests.RequestException:
        return False
    
    
