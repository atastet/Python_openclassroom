# -*-coding:Utf-8

class RevStr(str):
    """Classe reprenant methodes et attributs de str mais qui la parcours a l'envers"""

    def __iter__(self):
        """Revoie a um iterateur qui parcours a l'envers"""

        return ItRevStr(self)

class ItRevStr:

    def __init__(self, chaine_a_parcourir):
        """On se positionne a la fin de la chaine"""

        self.chaine_a_parcourir = chaine_a_parcourir
        self.position = len(chaine_a_parcourir)

    def __next__(self):

        if self.position == 0:
            raise StopIteration
        self.position -= 1
        return self.chaine_a_parcourir[self.position]


my_string = RevStr("""Hello world @""")  # type: RevStr
for letter in my_string:
    print(letter)