import random

user_action = input("Ingrese la opcion (piedra, papel, tijera): ")
possible_actions = ["piedra", "papel", "tijera"]
computer_action = random.choice(possible_actions)
print(f"\nTu eleccion {user_action}, eleccion de la computadora {computer_action}.\n")

if user_action == computer_action:
    print(f"Los dos jugadores eligieron {user_action}. Empate!")
elif user_action == "piedra":
    if computer_action == "tijera":
        print("Piedra vence tijeras! Ganaste!")
    else:
        print("Papel vence piedra! Perdiste.")
elif user_action == "papel":
    if computer_action == "piedra":
        print("Papel vence piedra! Ganaste!")
    else:
        print("Tijeras vence papel! Perdiste.")
elif user_action == "tijera":
    if computer_action == "papel":
        print("Tijeras vence papel! Ganaste!")
    else:
        print("Piedra vence tijeras! Perdiste.")
