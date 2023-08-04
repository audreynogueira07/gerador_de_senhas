import random
import string

def generate_password():
    while True:
        try:
            length = int(input("Insira o tamanho da senha (mínimo de 4): "))
            if length < 4:
                print("O tamanho mínimo para a senha é 4. Por favor, insira um número válido.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido.")
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    # Initialize password
    password = []

    print("Quer incluir letras minúsculas na sua senha? (s/n)")
    if input().lower() == "s":
        password.append(random.choice(lower))

    print("Quer incluir letras maiúsculas na sua senha? (s/n)")
    if input().lower() == "s":
        password.append(random.choice(upper))

    print("Quer incluir números na sua senha? (s/n)")
    if input().lower() == "s":
        password.append(random.choice(num))

    print("Quer incluir símbolos na sua senha? (s/n)")
    if input().lower() == "s":
        password.append(random.choice(symbols))
    
    if len(password) > length:
        print("O número de tipos de caracteres escolhidos é maior que o tamanho da senha desejada. Tente novamente.")
        return generate_password()

    while len(password) < length:
        password.append(random.choice(lower + upper + num + symbols))

    random.shuffle(password)

    return "".join(password)

generate_password()