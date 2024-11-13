import random
import string

def generate_password(length=16, use_special_chars=True):
    
    characters = string.ascii_letters + string.digits  
    if use_special_chars:
        characters += string.punctuation  

    password = ''.join(random.choices(characters, k=length))
    return password

password = generate_password(length=16, use_special_chars=True)
print("Generated Password:", password)
