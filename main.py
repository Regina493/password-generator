import random
import string

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

new_password = generate_password(16)
print(f"Ваш новый пароль: {new_password}")

with open("password.txt", "w") as f:
    f.write(new_password)