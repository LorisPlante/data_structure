class ExoString:
    def __init__(self):
        pass

    s = "Python est un langage de programmation puissant et facile à apprendre"

    def extract_python(self):
        mot_pyhton = self.chaine_donnee.split()[0]
        return mot_pyhton 

    def extract_apprendre(self):
        mot_apprendre = self.chaine_donnee[-9:]
        return mot_apprendre

    def extract_phrase(self):
        phrase = self.chaine_donnee[14:38]
        return phrase

    def extract_inverse(self):
        chaine_inverse = self.chaine_donnee[::-1]
        return chaine_inverse