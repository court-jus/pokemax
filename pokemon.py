class Pokemon:
    nom = ""
    types = []
    taille = 0

    def __init__(self, nom, types, taille):
        self.nom = nom
        self.types = types
        self.taille = taille

    def sais_nager(self):
        return "eau" in self.types

    def dangereux(self):
        return "poison" in self.types or "feu" in self.types

    def decris_toi(self):
        separateur = " et "

        # Je suis Florizzare, je mesure 150cm et je suis de type plante et poison.
        type_ou_types = "type"
        if len(self.types) > 1:
            type_ou_types = type_ou_types + "s"

        return f"Je suis {self.nom}, je mesure {self.taille} cm et je suis de {type_ou_types} {separateur.join(self.types)}."
