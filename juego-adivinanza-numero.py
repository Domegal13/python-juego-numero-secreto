import random
from colorama import init, Fore, Back, Style
init()

def juego_adivinanza():
    # Generar un número del 1 al 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print(Fore.GREEN + f'¡Bienvenido al juego para adivinar un número entre el 1 y el 100')
    print(Fore.YELLOW + '!Intenta adivinarlo!' + Style.RESET_ALL)

    while not adivinado:
        try:
            intentos += 1
            print()
            numero_ingresado = int(input('Introduzca el número entre 1 y 100: '))
            if numero_ingresado == numero_secreto:
                adivinado = True
            elif numero_ingresado > numero_secreto:
                print(Fore.CYAN + 'El número es menor...' + Style.RESET_ALL)
            else:
                print(Fore.CYAN + 'El número es mayor...' + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + Style.BRIGHT + 'Debe ingresar un número válido' + Style.RESET_ALL)
            intentos -= 1
       
            
    print(Fore.LIGHTGREEN_EX + 'Felicidades has adivinado el número secreto en ' + Fore.LIGHTYELLOW_EX + f'{intentos}' + Fore.LIGHTGREEN_EX + ' intentos' + Style.RESET_ALL)


if __name__ == "__main__":
    juego_adivinanza()
    
    