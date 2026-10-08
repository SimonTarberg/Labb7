import csv                       
from hashtable import Hashtable  

class DictHash:
    def __init__(self):
        self._dict = {}

    def store(self, key, data): #dict innehåller data och key som nyckel.
        self._dict[key] = data

    def search(self, key):

        if key not in self._dict:
            raise KeyError(key)
        return self._dict[key]

    #Extra frivilliga metoder

    def  __getitem__(self, key):
        return self.search(key)

    def __contains__(self, key):
        return key in self._dict

    #Testkörning___
class Drama:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def __str__(self):
        return f"{self.name} (Betyg: {self.rating})"

# 
def las_in_dramer(filnamn):
    """Läser kdrama.csv och returnerar en lista med Drama-objekt.
    csv-modulen behövs eftersom t.ex. Actors innehåller kommatecken."""
    dramer = []
    with open(filnamn, encoding="utf-8") as fil:
        lasare = csv.reader(fil)
        next(lasare)                      # hoppa över rubrikraden
        for rad in lasare:
            namn = rad[0]                 # kolumn "Drama Name"
            betyg = float(rad[1])         # kolumn "Rating(Out of 10)"
            dramer.append(Drama(namn, betyg))
    return dramer

if __name__ == "__main__":
    d_hash = DictHash()

    #lägg in alla dramer från filen, med namnet som nyckel 
    dramer = las_in_dramer("kdrama.csv")
    for drama in dramer:
        d_hash.store(drama.name, drama)
    print(f"La in {len(dramer)} dramer i DictHash")
  

    #Sök efter ett drama som finns
    print("Söker efter squid game")
    print(d_hash.search("Squid Games"))              

    if "Crash Landing on you" in d_hash:              
        print("Crash Landing on You finns i tabellen!!!")
        print(d_hash["Crash Landing on you"])         
    try: #det finns inte
        d_hash.search("Game of Thrones")
    except KeyError:
        print("Game of thrones finns inte i tabellen")


    h = Hashtable(541)
    for drama in dramer:
        h.store(drama.name, drama)

    print("\nSöker i Hashtable efter squid game")
    print(h.search("Squid Games"))

    if "Crash Landing on you" in h:
        print("Crash Landing on You finns i Hashtable!!!")
        print(h["Crash Landing on you"])
    try:
        h.search("Game of Thrones")
    except KeyError:
        print("Game of thrones finns inte i Hashtable")

    print("Längsta krocklista:", h.max_krock())



