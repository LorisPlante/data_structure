import random

def guess_number_game(max_attempts=10):
    number_to_guess = random.randint(1, 100)
    print("J'ai choisi un nombre entre 1 et 100. Pouvez-vous le deviner?")

    for attempt in range(max_attempts):
        try:
            guess = int(input(f"Tentative {attempt + 1}/{max_attempts} - Devinez le nombre : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if guess == number_to_guess:
            print(f"Bravo! Vous avez trouvé le nombre mystère en {attempt + 1} tentatives.")
            return
        print("Le nombre mystère est plus grand." if guess < number_to_guess else "Le nombre mystère est plus petit.")

    print(f"Désolé, vous avez utilisé toutes vos tentatives. Le nombre était : {number_to_guess}")
