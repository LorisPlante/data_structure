import random


def deviner_nombre(nombre_tentatives=5):
    nombre_mystere = random.randint(1, 100)
    print("Devinez le nombre mystère entre 1 et 100. Vous avez {} tentatives.".format(nombre_tentatives))

    for _ in range(nombre_tentatives):
        guess = int(input("Entrez votre choix : "))
        if guess < nombre_mystere:
            print("Le nombre mystère est plus grand.")
        elif guess > nombre_mystere:
            print("Le nombre mystère est plus petit.")
        else:
            print("Bravo ! Vous avez deviné le nombre mystère, c'était {}.".format(nombre_mystere))
            return

    print("Désolé, vous avez épuisé vos tentatives. Le nombre mystère était {}.".format(nombre_mystere))
